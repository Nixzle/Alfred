import datetime as dt
import json
import os
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ledger import Ledger, Conflict
from bounded_worker import Broker, run, digest


class FoundationsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.workspace = self.root/'worker'; self.workspace.mkdir()
        self.db = self.root/'control.sqlite'
        self.ledger = Ledger(self.db)
        self.ledger.create('t', 'Create report', 'prime', ['Report reviewed'])
        self.cap = dict(task_id='t', worker_id='image-1', owner='prime',
                        expires_at=(dt.datetime.now(dt.timezone.utc)+dt.timedelta(minutes=10)).isoformat(),
                        allowed_actions=['read','create'], allowed_targets=['*.txt'])
        self.op = dict(id='op-1', action='create', target='report.txt', text='approved content')

    def tearDown(self):
        self.ledger.close(); self.tmp.cleanup()

    def activate(self):
        self.ledger.update('t', 1, 'prime', status='active', worker='image-1')
        return Broker(self.ledger, self.cap, self.workspace)

    def test_fresh_session_and_stale_writer(self):
        other = Ledger(self.db)
        try:
            self.ledger.update('t', 1, 'prime', next_action='Inspect inputs')
            self.assertEqual(other.get('t')['next_action'], 'Inspect inputs')
            with self.assertRaises(Conflict): other.update('t', 1, 'prime', status='active')
            self.assertEqual(other.get('t')['revision'], 2)
        finally: other.close()

    def test_dependency_and_completion_evidence(self):
        self.ledger.create('child', 'Review', 'prime', ['Reviewed'], ['t'])
        with self.assertRaises(ValueError): self.ledger.update('child', 1, 'prime', status='active')
        with self.assertRaises(ValueError): self.ledger.update('t', 1, 'prime', status='complete')
        with self.assertRaises(PermissionError): self.ledger.update('t', 1, 'worker', status='active')

    def test_restart_does_not_repeat_committed_create(self):
        first = run(self.ledger, self.cap, self.workspace, [self.op])
        stamp = (self.workspace/'report.txt').stat().st_mtime_ns
        second = run(self.ledger, self.cap, self.workspace, [self.op])
        self.assertEqual(first['evidence'], second['evidence'])
        self.assertEqual((self.workspace/'report.txt').stat().st_mtime_ns, stamp)
        self.assertEqual(second['blocker'], 'Acceptance review required')

    def test_unknown_create_reconciles_without_replay(self):
        broker = self.activate()
        fp = digest(json.dumps(self.op, sort_keys=True).encode())
        self.ledger.db.execute('INSERT INTO effects VALUES(?,?,?,?,?)', ('t','op-1',fp,'intent','{}'))
        (self.workspace/'report.txt').write_text(self.op['text'])
        self.assertTrue(broker.execute(self.op)['reconciled'])

    def test_unknown_outcome_missing_target_blocks(self):
        broker = self.activate()
        fp = digest(json.dumps(self.op, sort_keys=True).encode())
        self.ledger.db.execute('INSERT INTO effects VALUES(?,?,?,?,?)', ('t','op-1',fp,'intent','{}'))
        with self.assertRaises(Conflict): broker.execute(self.op)
        self.assertFalse((self.workspace/'report.txt').exists())

    def test_denied_effects_never_dispatch(self):
        broker = self.activate()
        for action, target in [('create','../escape.txt'),('create','/escape.txt'),
                               ('create','file.txt:stream'),('create','.env'),
                               ('delete','report.txt'),('install','report.txt'),('network','report.txt')]:
            with self.subTest(action=action,target=target):
                with self.assertRaises(PermissionError): broker.execute(self.op|{'action':action,'target':target})
        self.assertEqual(list(self.workspace.iterdir()), [])

    def test_approval_and_expiry_cannot_be_bypassed_by_plan(self):
        self.ledger.update('t', 1, 'prime', status='active', worker='image-1')
        cap = self.cap|{'approval_required_actions':['create']}
        with self.assertRaises(PermissionError): Broker(self.ledger,cap,self.workspace).execute(self.op|{'approved':True})
        self.ledger.db.execute('DELETE FROM workers')
        cap = self.cap|{'expires_at':'2000-01-01T00:00:00+00:00'}
        with self.assertRaises(PermissionError): Broker(self.ledger,cap,self.workspace).execute(self.op)

    def test_existing_file_is_never_overwritten(self):
        broker = self.activate()
        (self.workspace/'report.txt').write_text('user content')
        with self.assertRaises(FileExistsError): broker.execute(self.op)
        self.assertEqual((self.workspace/'report.txt').read_text(),'user content')

    def test_link_escape_denied(self):
        broker = self.activate()
        outside = self.root/'outside.txt'; outside.write_text('private')
        os.link(outside, self.workspace/'report.txt')
        with self.assertRaises(PermissionError): broker.execute(self.op|{'action':'read'})

    def test_telemetry_does_not_store_payload_or_exception_message(self):
        broker = self.activate(); broker.execute(self.op)
        self.ledger.event('t','custom', text='secret', api_key='secret')
        trace = json.dumps(self.ledger.trace('t'))
        self.assertNotIn('approved content',trace)
        self.assertNotIn('secret',trace)
        self.assertIn('effect_intent',trace); self.assertIn('effect_committed',trace)

    def test_changed_plan_and_other_worker_cannot_resume(self):
        run(self.ledger,self.cap,self.workspace,[self.op])
        with self.assertRaises(Conflict): run(self.ledger,self.cap,self.workspace,[self.op|{'text':'different'}])
        with self.assertRaises(PermissionError): run(self.ledger,self.cap|{'worker_id':'other'},self.workspace,[self.op])

    def test_resume_cannot_change_workspace_or_authority(self):
        self.activate()
        other = self.root/'other'; other.mkdir()
        with self.assertRaises(Conflict): Broker(self.ledger,self.cap,other)
        with self.assertRaises(Conflict): Broker(self.ledger,self.cap|{'allowed_targets':['*']},self.workspace)

    def test_two_images_have_separate_evidence_and_artifacts(self):
        run(self.ledger,self.cap,self.workspace,[self.op])
        other = self.root/'second'; other.mkdir()
        self.ledger.create('t2','Second report','prime',['Review'])
        cap = self.cap|{'task_id':'t2','worker_id':'image-2'}
        with self.assertRaises(Conflict): Broker(self.ledger,cap,self.workspace)
        result = run(self.ledger,cap,other,[self.op|{'text':'second content'}])
        self.assertEqual(result['worker_id'],'image-2')
        self.assertEqual((self.workspace/'report.txt').read_text(),'approved content')
        self.assertEqual((other/'report.txt').read_text(),'second content')

    def test_real_process_restart_and_fresh_snapshot(self):
        capsule = self.root/'capsule.json'; capsule.write_text(json.dumps(self.cap))
        plan = self.root/'plan.json'; plan.write_text(json.dumps([self.op]))
        runtime = Path(__file__).resolve().parents[1]
        command = [sys.executable, str(runtime/'bounded_worker.py'), '--db', str(self.db),
                   '--capsule', str(capsule), '--workspace', str(self.workspace), '--plan', str(plan)]
        first = subprocess.run(command, capture_output=True, text=True, timeout=20, check=True)
        stamp = (self.workspace/'report.txt').stat().st_mtime_ns
        second = subprocess.run(command, capture_output=True, text=True, timeout=20, check=True)
        self.assertEqual(json.loads(first.stdout)['evidence'], json.loads(second.stdout)['evidence'])
        self.assertEqual(stamp, (self.workspace/'report.txt').stat().st_mtime_ns)
        snapshot = subprocess.run([sys.executable,str(runtime/'ledger.py'),'--db',str(self.db),'snapshot'],
                                  capture_output=True,text=True,timeout=20,check=True)
        task = json.loads(snapshot.stdout)[0]
        self.assertEqual(task['next_action'],'Review handback evidence')
        self.assertEqual(len(task['attempts']),2)

    def test_retry_budget_and_terminal_task_stop_dispatch(self):
        for _ in range(3): run(self.ledger,self.cap,self.workspace,[self.op])
        with self.assertRaises(ValueError): run(self.ledger,self.cap,self.workspace,[self.op])
        task = self.ledger.get('t')
        self.ledger.update('t',task['revision'],'prime',status='cancelled')
        with self.assertRaises(PermissionError): Broker(self.ledger,self.cap,self.workspace).execute(self.op)


if __name__ == '__main__': unittest.main()
