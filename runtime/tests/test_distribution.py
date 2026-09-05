import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from distribution import evaluate, profile_parity, repository_parity


class DistributionParityTests(unittest.TestCase):
    def test_repository_semantic_parity(self):
        result = repository_parity(Path(__file__).resolve().parents[2])
        self.assertEqual(result['status'], 'PASS', result)

    def test_profile_requires_all_semantic_parity(self):
        template = json.loads((Path(__file__).resolve().parents[2] / 'bootstrap' / 'runtime-profile.template.json').read_text())
        result = profile_parity(template)
        self.assertEqual(result['status'], 'FAIL')
        self.assertTrue(any('semantic parity unverified' in issue for issue in result['issues']))

    def test_verified_profile_passes_without_claiming_live_capability_equivalence(self):
        template = json.loads((Path(__file__).resolve().parents[2] / 'bootstrap' / 'runtime-profile.template.json').read_text())
        template['semantic_parity'] = {key: True for key in template['semantic_parity']}
        template['validation'].update(observed_at='2026-09-05T06:30:00+00:00', evidence=['canonical repository read'])
        result = evaluate(template, Path(__file__).resolve().parents[2])
        self.assertEqual(result['status'], 'PASS', result)
        self.assertIn('Live tools', result['scope'])
        self.assertEqual(template['capabilities']['autonomous_workers'], 'unknown')


if __name__ == '__main__':
    unittest.main()
