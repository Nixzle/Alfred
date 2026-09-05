from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from operations import Threshold, compare_baseline, evaluate_chaos_case, evaluate_recovery, evaluate_slos, summarize_runs


class OperationsTests(unittest.TestCase):
    def test_hard_slos_fail_closed(self):
        self.assertEqual(evaluate_slos({})['status'], 'PASS')
        self.assertEqual(evaluate_slos({'stale_write_accepts': 1})['status'], 'FAIL')

    def test_extra_thresholds(self):
        result = evaluate_slos({'success_rate': 0.995}, [Threshold('success_rate', '>=', 0.99)])
        self.assertEqual(result['status'], 'PASS')

    def test_harmful_drift(self):
        baseline = {'latency_ms': 100, 'success_rate': 0.99}
        current = {'latency_ms': 130, 'success_rate': 0.95}
        result = compare_baseline(baseline, current, {'latency_ms': 0.2, 'success_rate': 0.02})
        self.assertEqual(result['status'], 'FAIL')

    def test_chaos_case(self):
        case = {
            'name': 'timeout-after-commit',
            'fault': 'ack_lost',
            'observed': {'effect_state': 'UNKNOWN_OUTCOME', 'blind_retry': False},
            'expected': {'effect_state': 'UNKNOWN_OUTCOME', 'blind_retry': False},
        }
        self.assertEqual(evaluate_chaos_case(case)['status'], 'PASS')

    def test_recovery_drill(self):
        drill = dict(last_known_good='abc', restored_revision='abc', acceptance_passed=True,
                     regressions_passed=True, unknown_effects_reconciled=True,
                     authority_revalidated=True)
        self.assertEqual(evaluate_recovery(drill)['status'], 'PASS')
        self.assertEqual(evaluate_recovery({**drill, 'authority_revalidated': False})['status'], 'FAIL')

    def test_distribution_summary(self):
        result = summarize_runs([
            {'success_rate': 1.0, 'latency_ms': 100},
            {'success_rate': 0.9, 'latency_ms': 150},
        ])
        self.assertEqual(result['run_count'], 2.0)
        self.assertEqual(result['worst_success_rate'], 0.9)
        self.assertEqual(result['worst_latency_ms'], 150.0)


if __name__ == '__main__':
    unittest.main()
