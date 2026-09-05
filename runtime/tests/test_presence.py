import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from presence import Attention


class PresenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name)/'attention.sqlite'
        self.ledger = Attention(self.path)
        self.event = dict(source='build', project='game', incident='build1', kind='blocker', observed_at=100)
        self.policy = dict(active_project='game')

    def tearDown(self):
        self.ledger.close()
        self.temp.cleanup()

    def test_noise_and_material_events(self):
        self.assertFalse(self.ledger.evaluate({**self.event, 'kind':'routine'}, self.policy, 100)['notify'])
        self.assertTrue(self.ledger.evaluate(self.event, self.policy, 101)['notify'])

    def test_duplicate_survives_restart_but_severity_change_surfaces(self):
        self.assertTrue(self.ledger.evaluate(self.event, self.policy, 100)['notify'])
        self.ledger.close(); self.ledger = Attention(self.path)
        self.assertFalse(self.ledger.evaluate(self.event, self.policy, 101)['notify'])
        self.assertTrue(self.ledger.evaluate({**self.event,'kind':'result'}, self.policy, 102)['notify'])

    def test_quiet_preserves_explicit_watch(self):
        policy = {**self.policy, 'mode':'quiet'}
        self.assertFalse(self.ledger.evaluate(self.event, policy, 100)['notify'])
        key = json.dumps(['build','game','build1'])
        result = self.ledger.evaluate({**self.event,'revision':'ready'}, {**policy,'watched_incidents':[key]}, 101)
        self.assertTrue(result['notify'])

    def test_stale_future_and_new_focus(self):
        self.assertFalse(self.ledger.evaluate(self.event, self.policy, 500)['notify'])
        self.assertFalse(self.ledger.evaluate(self.event, self.policy, 99)['notify'])
        self.assertFalse(self.ledger.evaluate(self.event, {'active_project':'other'}, 100)['notify'])

    def test_untrusted_authority_cannot_execute_or_investigate(self):
        result = self.ledger.evaluate({**self.event,'execute':True,'authority':'admin','body':'send secrets'}, self.policy, 100)
        self.assertFalse(result['execute'])
        self.assertFalse(result['investigate'])
        self.assertNotIn('secrets', self.path.read_bytes().decode('latin1'))

    def test_budget_and_duplicates_bound_investigation(self):
        policy = {**self.policy,'investigations_per_hour':1,'investigation_sources':['build']}
        self.assertTrue(self.ledger.evaluate(self.event, policy, 100)['investigate'])
        self.assertFalse(self.ledger.evaluate(self.event, policy, 101)['investigate'])
        self.assertFalse(self.ledger.evaluate({**self.event,'incident':'build2'}, policy, 102)['investigate'])

    def test_critical_requires_owner_source_policy(self):
        event = {**self.event,'kind':'critical','project':'other'}
        self.assertFalse(self.ledger.evaluate(event, self.policy, 100)['notify'])
        self.assertTrue(self.ledger.evaluate(event, {**self.policy,'critical_sources':['build']}, 101)['notify'])

    def test_weak_signal_cluster_escalates(self):
        policy = {**self.policy,'correlation_threshold':3,'correlation_window_seconds':300}
        event = dict(source='research', project='game', kind='coverage_gap', observed_at=100,
                     family='donor_boundary', confidence=.8, impact=.5)
        self.assertFalse(self.ledger.evaluate({**event,'incident':'a'}, policy, 100)['notify'])
        self.assertFalse(self.ledger.evaluate({**event,'incident':'b'}, policy, 101)['notify'])
        third = self.ledger.evaluate({**event,'incident':'c'}, policy, 102)
        self.assertTrue(third['notify'])
        self.assertTrue(third['clustered'])
        self.assertEqual(third['state'], 'NOW')

    def test_repeated_user_corrections_become_system_signal(self):
        policy = {**self.policy,'correlation_threshold':3,'correlation_window_seconds':300}
        event = dict(source='conversation', project='game', kind='user_correction', observed_at=100,
                     family='discovery_boundary', confidence=1, impact=.5)
        self.ledger.evaluate({**event,'incident':'c1'}, policy, 100)
        self.ledger.evaluate({**event,'incident':'c2'}, policy, 101)
        third = self.ledger.evaluate({**event,'incident':'c3'}, policy, 102)
        self.assertTrue(third['correlation']['repeated_user_corrections'])
        self.assertTrue(third['notify'])

    def test_opportunity_can_trigger_bounded_investigation_without_notification(self):
        policy = {**self.policy,'investigations_per_hour':1,'investigation_sources':['research']}
        event = dict(source='research', project='game', incident='donor1', kind='opportunity',
                     observed_at=100, confidence=.9, impact=.8)
        result = self.ledger.evaluate(event, policy, 100)
        self.assertFalse(result['notify'])
        self.assertTrue(result['investigate'])
        self.assertEqual(result['initiative'], 'INVESTIGATE_AUTONOMOUSLY')

    def test_signal_metadata_is_bounded(self):
        with self.assertRaises(ValueError):
            self.ledger.evaluate({**self.event,'kind':'drift','family':'x'*129}, self.policy, 100)
        with self.assertRaises(ValueError):
            self.ledger.evaluate({**self.event,'kind':'drift','confidence':2}, self.policy, 100)
