import datetime as dt
from pathlib import Path
import tempfile
import unittest

from runtime.ledger import Ledger, Conflict
from runtime.bounded_worker import Broker
from runtime.supervisor import Supervisor


class FaultIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.workspace = self.root / 'workspace'
        self.workspace.mkdir()
        self.ledger = Ledger(self.root / 'control.sqlite')
        self.task = self.ledger.create('t1', 'fault test', 'owner', ['evidence'])
        self.capsule = {
            'task_id': 't1',
            'worker_id': 'worker-1',
            'owner': 'owner',
            'allowed_actions': ['read', 'create'],
            'allowed_targets': ['*.txt'],
            'approval_required_actions': [],
            'expires_at': (dt.datetime.now(dt.timezone.utc) + dt.timedelta(minutes=5)).isoformat(),
        }
        self.ledger.update('t1', self.task['revision'], 'owner', status='active', worker='worker-1')
        self.broker = Broker(self.ledger, self.capsule, self.workspace)
        self.supervisor = Supervisor(self.ledger, b'x' * 32)

    def tearDown(self):
        self.ledger.close()
        self.temp.cleanup()

    def test_duplicate_committed_effect_is_not_replayed(self):
        op = {'id': 'op1', 'action': 'create', 'target': 'a.txt', 'text': 'hello'}
        first = self.broker.execute(op)
        second = self.broker.execute(op)
        self.assertEqual(first['sha256'], second['sha256'])
        self.assertEqual((self.workspace / 'a.txt').read_text(), 'hello')

    def test_operation_id_payload_change_is_conflict(self):
        self.broker.execute({'id': 'op1', 'action': 'create', 'target': 'a.txt', 'text': 'hello'})
        with self.assertRaises(Conflict):
            self.broker.execute({'id': 'op1', 'action': 'create', 'target': 'b.txt', 'text': 'different'})

    def test_revoked_grant_stops_dispatch(self):
        grant = self.supervisor.issue('t1', 'worker-1', ['create'], ['a.txt'])
        self.supervisor.revoke(grant['body']['id'])
        with self.assertRaises(PermissionError):
            self.supervisor.dispatch(grant, self.broker,
                                     {'id': 'op2', 'action': 'create', 'target': 'a.txt', 'text': 'x'})
        self.assertFalse((self.workspace / 'a.txt').exists())

    def test_expired_capsule_denies_effect(self):
        task = self.ledger.create('t2', 'expiry test', 'owner', ['evidence'])
        expired = {
            'task_id': 't2',
            'worker_id': 'worker-expired',
            'owner': 'owner',
            'allowed_actions': ['create'],
            'allowed_targets': ['*.txt'],
            'approval_required_actions': [],
            'expires_at': (dt.datetime.now(dt.timezone.utc) - dt.timedelta(seconds=1)).isoformat(),
        }
        self.ledger.update('t2', task['revision'], 'owner', status='active', worker='worker-expired')
        workspace2 = self.root / 'workspace2'
        workspace2.mkdir()
        broker = Broker(self.ledger, expired, workspace2)
        self.assertEqual(broker.decide({'id':'op3','action':'create','target':'a.txt','text':'x'}), 'deny')
        self.assertFalse((workspace2 / 'a.txt').exists())

    def test_workspace_escape_is_denied(self):
        decision = self.broker.decide({'id':'op4','action':'create','target':'../escape.txt','text':'x'})
        self.assertEqual(decision, 'deny')
        self.assertFalse((self.root / 'escape.txt').exists())


if __name__ == '__main__':
    unittest.main()
