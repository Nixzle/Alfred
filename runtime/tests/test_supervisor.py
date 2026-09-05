import copy
from pathlib import Path
import secrets
import sys
import tempfile
import time
import unittest
import datetime as dt
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ledger import Ledger
from supervisor import Supervisor, require_containment


class SupervisorTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.ledger=Ledger(Path(self.tmp.name)/'control.sqlite')
        self.ledger.create('task','Objective','prime',['Evidence'])
        self.supervisor=Supervisor(self.ledger,secrets.token_bytes(32))

    def tearDown(self):
        self.ledger.close(); self.tmp.cleanup()

    def grant(self):
        return self.supervisor.issue('task','worker',['create'],['result.txt'])

    def test_tampering_task_worker_and_key_are_rejected(self):
        grant=self.grant()
        forged=copy.deepcopy(grant); forged['body']['actions'].append('delete')
        for item,task,worker in [(forged,'task','worker'),(grant,'other','worker'),(grant,'task','other')]:
            with self.assertRaises(PermissionError): self.supervisor.verify(item,task,worker)
        with self.assertRaises(PermissionError): Supervisor(self.ledger,secrets.token_bytes(32)).verify(grant,'task')

    def test_revocation_invalidates_descendants(self):
        parent=self.grant()
        child=self.supervisor.issue('task','child',['create'],['result.txt'],parent=parent)
        self.supervisor.revoke(parent['body']['id'])
        with self.assertRaises(PermissionError): self.supervisor.verify(child,'task')

    def test_delegation_cannot_expand(self):
        with self.assertRaises(PermissionError):
            self.supervisor.issue('task','child',['delete'],['result.txt'],parent=self.grant())

    def test_leases_fence_stale_owners(self):
        first=self.supervisor.acquire('task','one')
        with self.assertRaises(PermissionError): self.supervisor.acquire('task','two')
        self.supervisor.release('task','one',first)
        second=self.supervisor.acquire('task','two')
        self.assertGreater(second,first)
        with self.assertRaises(PermissionError): self.supervisor.renew('task','one',first)

    def test_expired_lease_needs_explicit_reconciliation(self):
        self.supervisor.acquire('task','one')
        self.ledger.db.execute('UPDATE leases SET expires=0')
        with self.assertRaises(PermissionError): self.supervisor.acquire('task','two')

    def test_unverified_and_stale_sandbox_fail_closed(self):
        probe=dict(workspace_write=True,outside_write_denied=True,outside_read_denied=True,
                   network_denied=True,process_tree_termination=True,observed_at=time.time())
        require_containment(probe)
        with self.assertRaises(PermissionError): require_containment(probe|{'outside_read_denied':False})
        with self.assertRaises(PermissionError): require_containment(probe|{'observed_at':0})

    def test_terminal_task_revokes_authority(self):
        grant=self.grant()
        self.ledger.update('task',1,'prime',status='cancelled')
        with self.assertRaises(PermissionError): self.supervisor.verify(grant,'task')

    def test_signed_plan_reaches_broker_and_denies_extra_effect(self):
        workspace=Path(self.tmp.name)/'worker'; workspace.mkdir()
        cap=dict(task_id='task',worker_id='worker',owner='prime',allowed_actions=['create'],
                 allowed_targets=['*.txt'],expires_at=(dt.datetime.now(dt.timezone.utc)+dt.timedelta(minutes=5)).isoformat())
        operations=[dict(id='one',action='create',target='result.txt',text='yes'),
                    dict(id='two',action='create',target='outside-grant.txt',text='no')]
        result=self.supervisor.run_plan(self.grant(),cap,workspace,operations)
        self.assertEqual(result['blocker'],'PermissionError')
        self.assertTrue((workspace/'result.txt').exists())
        self.assertFalse((workspace/'outside-grant.txt').exists())
        self.assertEqual(self.ledger.db.execute('SELECT status FROM leases').fetchone()[0],'released')

    def test_complete_health_report_acceptance(self):
        from acceptance import exercise
        result=exercise(Path(self.tmp.name)/'accepted-task')
        self.assertEqual(result['status'],'PASS')
        self.assertTrue(result['fresh_session_verified'])
