import copy
import datetime
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from runtime.release_event import observe


class ReleaseEventTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = str(Path(self.tmp.name)/'attention.db')
        self.now = datetime.datetime.now(datetime.timezone.utc)
        self.receipt = dict(generated_at=self.now.isoformat(), revision='abc123', status='PASS',
                            checks=[dict(check=c, exit_code=0, passed=True) for c in ('tests','lint','acceptance','diff')])

    def test_real_process_restart_suppresses_duplicate(self):
        first = observe(self.receipt, self.db, 'sanctum')
        self.assertTrue(first['decision']['notify'])
        path = Path(self.tmp.name)/'receipt.json'
        path.write_text(json.dumps(self.receipt), encoding='utf-8')
        output = subprocess.check_output([sys.executable, '-m', 'runtime.release_event', '--receipt', str(path),
                                          '--db', self.db, '--project', 'sanctum'], text=True)
        replay = json.loads(output)
        self.assertFalse(replay['decision']['notify'])
        self.assertEqual(replay['decision']['reason'], 'duplicate event')
        self.assertEqual(first['event']['incident'], replay['event']['incident'])

    def test_failed_checks_route_as_blocker(self):
        self.receipt.update(status='FAIL')
        self.receipt['checks'][0].update(passed=False, exit_code=1)
        result = observe(self.receipt, self.db, 'sanctum')
        self.assertEqual(result['event']['kind'], 'blocker')
        self.assertTrue(result['decision']['notify'])
        self.assertFalse(result['decision']['execute'])
        self.assertFalse(result['decision']['investigate'])

    def test_zero_tests_can_fail_despite_zero_exit(self):
        self.receipt.update(status='FAIL')
        self.receipt['checks'][0].update(passed=False)
        self.assertEqual(observe(self.receipt, self.db, 'sanctum')['event']['kind'], 'blocker')

    def test_inconsistent_or_partial_receipts_rejected(self):
        for mutation in ('partial', 'duplicate', 'summary', 'exit', 'naive'):
            receipt = copy.deepcopy(self.receipt)
            if mutation == 'partial': receipt['checks'].pop()
            if mutation == 'duplicate': receipt['checks'].append(receipt['checks'][0])
            if mutation == 'summary': receipt['status'] = 'FAIL'
            if mutation == 'exit': receipt['checks'][0]['exit_code'] = 1
            if mutation == 'naive': receipt['generated_at'] = '2026-01-01T00:00:00'
            with self.subTest(mutation=mutation), self.assertRaises(ValueError): observe(receipt, self.db, 'sanctum')

    def test_replay_does_not_refresh_stale_or_future_observations(self):
        for delta in (3601, -1):
            result = observe(self.receipt, self.db, 'sanctum', now=self.now.timestamp()+delta)
            self.assertEqual(result['decision']['state'], 'SUPPRESSED')

    def test_ledger_stores_no_receipt_body_or_authority(self):
        self.receipt.update(body='private payload canary', execute=True)
        result = observe(self.receipt, self.db, 'sanctum')
        self.assertFalse(result['decision']['execute'])
        self.assertNotIn(b'private payload canary', Path(self.db).read_bytes())
