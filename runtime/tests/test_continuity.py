import unittest

from runtime.continuity import PressurePolicy, assess_pressure, build_handoff, verify_handoff


class ContinuityTests(unittest.TestCase):
    def test_pressure_states(self):
        policy = PressurePolicy(warning_ratio=0.75, critical_ratio=0.9)
        self.assertEqual(assess_pressure(50, 100, policy)['action'], 'CONTINUE')
        self.assertEqual(assess_pressure(80, 100, policy)['action'], 'PREPARE_HANDOFF')
        self.assertEqual(assess_pressure(95, 100, policy)['action'], 'HANDOFF_NOW')

    def test_compact_handoff_roundtrip(self):
        state = {
            'objective': 'finish current project safely',
            'verified_state': ['tests added', 'repo head abc'],
            'decisions': ['keep Dota-first direction'],
            'constraints': ['no fake runtime claims'],
            'blockers': ['remote host unavailable'],
            'revisions': {'Sanctum': 'abc', 'project': 'def'},
            'relevant_memory': ['user prefers Salvage First'],
            'sanctum_route': ['Prime Sense', 'Archives', 'Spellbooks'],
            'next_action': 'run integrated validation on an authorized host',
        }
        record = build_handoff(state)
        self.assertTrue(verify_handoff(record))
        tampered = dict(record)
        tampered['next_action'] = 'pretend it passed'
        self.assertFalse(verify_handoff(tampered))

    def test_missing_fields_rejected(self):
        with self.assertRaises(ValueError):
            build_handoff({'objective': 'x'})

    def test_archaeological_dump_rejected(self):
        state = {
            'objective': 'x',
            'verified_state': ['y' * 5000] * 10,
            'decisions': [], 'constraints': [], 'blockers': [],
            'revisions': {}, 'relevant_memory': [], 'sanctum_route': [],
            'next_action': 'z',
        }
        with self.assertRaises(ValueError):
            build_handoff(state, PressurePolicy(max_handoff_chars=2000))


if __name__ == '__main__':
    unittest.main()
