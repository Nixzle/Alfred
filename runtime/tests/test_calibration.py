import copy
import json
from pathlib import Path
import unittest
from runtime.calibration import digest, score

DATA = Path(__file__).resolve().parents[2]/'evals/research-calibration/cases.json'


class CalibrationTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(DATA.read_text(encoding='utf-8'))
        self.trial = dict(dataset_sha256=digest(self.data), reviewer=dict(name='test oracle', method='deterministic'),
                          answers=[dict(id=c['id'], verdict=c['label'], note='test fixture',
                                        sources=[c['sources'][0]['id']]) for c in self.data['cases']])

    def test_scoring_and_false_support_denominator(self):
        self.assertEqual(score(self.data, self.trial)['agreement'], 1)
        for a in self.trial['answers']: a['verdict'] = 'supported'
        result = score(self.data, self.trial)
        self.assertEqual(result['false_support_rate'], 1)
        self.assertEqual(result['false_support_count'], 8)
        self.assertAlmostEqual(result['agreement'], 1/3)

    def test_missing_duplicate_unknown_and_stale_answers_rejected(self):
        for mutation in ('missing', 'duplicate', 'unknown', 'digest'):
            trial = copy.deepcopy(self.trial)
            if mutation == 'missing': trial['answers'].pop()
            if mutation == 'duplicate': trial['answers'].append(trial['answers'][0])
            if mutation == 'unknown': trial['answers'][0]['id'] = 'not-a-case'
            if mutation == 'digest': trial['dataset_sha256'] = 'old'
            with self.subTest(mutation=mutation), self.assertRaises(ValueError): score(self.data, trial)

    def test_evidence_and_provenance_required(self):
        for mutation in ('source', 'reviewer', 'label', 'note'):
            trial = copy.deepcopy(self.trial)
            if mutation == 'source': trial['answers'][0]['sources'] = ['invented']
            if mutation == 'reviewer': trial['reviewer']['method'] = 'independent because named'
            if mutation == 'label': trial['answers'][0]['verdict'] = 'probably'
            if mutation == 'note': trial['answers'][0]['note'] = ''
            with self.subTest(mutation=mutation), self.assertRaises(ValueError): score(self.data, trial)

    def test_uncertainty_is_distinct_from_false_support(self):
        for a in self.trial['answers']: a['verdict'] = 'uncertain'
        result = score(self.data, self.trial)
        self.assertEqual(result['false_support_count'], 0)
        self.assertEqual(result['uncertain_predictions'], 12)
        self.assertLess(result['agreement'], 1)
