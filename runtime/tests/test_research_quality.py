import copy
import importlib.util
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from research_quality import evaluate, digest
from sanctum import evaluate_trace


def receipt():
    return dict(objective='Choose a research method',as_of='2026-09-05T01:00:00+00:00',
        sources=[dict(id='s1',locator='fixture:source',section='result',family='study1',kind='fixture',access='opened',retrieved_at='2026-09-05T00:00:00+00:00')],
        claims=[dict(id='c1',text='Method A works on task X',sources=['s1'],basis='direct',limitation='Only task X was tested')],
        coverage=dict(scope='one task',limits='not a landscape'),
        rounds=[dict(question='Does A work?',finding='Fixture reports success',decision_impact='Try A on X')],
        stop_reason='Run the bounded task before more searching')


class ResearchQualityTests(unittest.TestCase):
    def test_fields_do_not_certify_truth(self):
        result=evaluate(receipt())
        self.assertEqual(result['status'],'STRUCTURE_PASS')
        self.assertEqual(result['claim_support'],'NOT_EVALUATED')
        self.assertEqual(result['empirical_improvement'],'NOT_EVALUATED')

    def test_development_failure_cases(self):
        for name in ('missing_sources','unopened','no_section','future','dangling_claim','missing_stop','no_round','no_coverage'):
            with self.subTest(name=name):
                r=receipt()
                if name=='missing_sources': r['sources']=[]
                elif name=='unopened': r['sources'][0]['access']='snippet'
                elif name=='no_section': r['sources'][0]['section']=''
                elif name=='future': r['sources'][0]['retrieved_at']='2999-01-01T00:00:00+00:00'
                elif name=='dangling_claim': r['claims'][0]['sources']=['missing']
                elif name=='missing_stop': r['stop_reason']=''
                elif name=='no_round': r['rounds']=[]
                elif name=='no_coverage': r['coverage']={}
                self.assertEqual(evaluate(r)['status'],'FAIL')

    def test_transfer_cases_source_count_currentness_and_inference(self):
        # Additional deterministic cases; not an unseen model benchmark.
        r=receipt(); r['sources'].append({**r['sources'][0],'id':'s2','locator':'fixture:repost'})
        r['claims'][0].update(sources=['s1','s2'],independent_confirmation=True)
        self.assertIn('CORRELATED_CONFIRMATION',evaluate(r)['issues'])
        r=receipt(); r['claims'][0]['current']=True
        self.assertIn('CURRENT_CLAIM_UNCHECKED',evaluate(r)['issues'])
        r=receipt(); r['claims'][0]['basis']='inference'
        self.assertIn('INFERENCE_UNEXPLAINED',evaluate(r)['issues'])

    def test_forge_needs_application_and_measured_result(self):
        r=receipt(); r['forge']=True
        self.assertIn('APPLICATION_MISSING',evaluate(r)['issues'])
        r['applications']=[dict(technique='A',baseline='manual',change='use A',status='tested',evidence='fixture:run',limitation='one case')]
        self.assertIn('APPLICATION_RESULT_MISSING',evaluate(r)['issues'])
        r['applications'][0]['result']='output matched expected result'
        self.assertEqual(evaluate(r)['status'],'STRUCTURE_PASS')

    def test_review_is_bound_and_uncertainty_survives(self):
        r=receipt(); review=dict(receipt_sha256=digest(r),reviewer='fixture-reviewer',method='human',independent=True,
            claims={'c1':dict(verdict='supported',note='Matches fixture result')})
        self.assertEqual(evaluate(r,review)['claim_support'],'REVIEWED')
        review['claims']['c1']['verdict']='uncertain'
        self.assertEqual(evaluate(r,review)['claim_support'],'NEEDS_REVIEW')
        r['claims'][0]['text']='Different claim'
        self.assertIn('REVIEW_MISMATCH',evaluate(r,review)['issues'])

    def test_empty_and_research_only_trace_are_not_quality_passes(self):
        self.assertEqual(evaluate_trace([])['status'],'NOT_EVALUATED')
        trace=[dict(event='route',data=dict(task=dict(research=True),mechanisms=['Cerebro']))]
        self.assertEqual(evaluate_trace(trace)['status'],'PARTIAL')
        trace.append(dict(event='research',data=dict(receipt=receipt())))
        result=evaluate_trace(trace)
        self.assertEqual(result['research_quality'][0]['claim_support'],'NOT_EVALUATED')

    def test_multiple_violations_cannot_produce_negative_passes(self):
        trace=[dict(event='route',data=dict(task=dict(bounded=True,write=True,research=True),mechanisms=[]))]
        self.assertEqual(evaluate_trace(trace)['passed'],0)
