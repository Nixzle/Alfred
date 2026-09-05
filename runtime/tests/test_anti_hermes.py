import tempfile
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from spell_registry import SpellRegistry
from reliability_contracts import acceptance_receipt, completion_receipt, delivery_state, budget_decision, provider_result, choose_failover
from adapter_contract import manifest, verify_health, authorize_effect
from self_audit import audit, authorize
from a2a_contract import agent_card, discovery_decision, invocation_decision, artifact
from memory_service_contract import write_request, authorize as memory_authorize, receipt, verify_receipt


class AntiHermesTests(unittest.TestCase):
    def test_spell_registry_progressive_loading_and_curation(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); (root/'A.md').write_text('alpha'); (root/'B.md').write_text('beta')
            reg=SpellRegistry(root)
            reg.register('a','A.md',['research','donor'])
            reg.register('b','B.md',['research','donor'])
            self.assertEqual(reg.select(['donor'])[0]['id'],'a')
            self.assertEqual(reg.load('a'),'alpha')
            self.assertEqual(reg.duplicate_candidates(),[('a','b')])
            reg.record_outcome('a',True); reg.retire('b')
            self.assertEqual(len(reg.select(['donor'])),1)

    def test_delivery_receipts_budget_and_failover(self):
        accepted=acceptance_receipt('t','w','cap')
        completed=completion_receipt('t','w',['e1'])
        self.assertEqual(delivery_state(accepted,completed)['state'],'DELIVERED')
        self.assertEqual(budget_decision({'tokens':11},{'tokens':10})['decision'],'HALT')
        self.assertEqual(budget_decision({}, {'cost':1})['decision'],'REQUIRE_OBSERVATION')
        results=[provider_result('p1','failure')]
        self.assertEqual(choose_failover(results,['p1','p2'])['provider'],'p2')
        self.assertEqual(choose_failover([provider_result('p1','unknown')],['p2'])['decision'],'RECONCILE')

    def test_adapter_contract_health_and_effects(self):
        m=manifest({'host':'codex','version':'1','reads':['archives'],'writes':['handoff'],
                    'effects':['read','write','destructive'],'healthcheck':'probe','revoke':'disconnect'})
        self.assertEqual(verify_health(m,{'host':'codex','version':'1','healthy':True})['status'],'HEALTHY')
        self.assertEqual(authorize_effect(m,'destructive'),'REQUIRE_APPROVAL')
        self.assertEqual(authorize_effect(m,'destructive',True),'ALLOW')
        self.assertEqual(authorize_effect(m,'network'),'DENY')

    def test_self_audit_proposes_but_does_not_self_authorize_risky_change(self):
        events=[{'event':'user_correction','data':{}} for _ in range(3)]
        out=audit(events)
        self.assertEqual(out['proposals'][0]['kind'],'add_regression')
        self.assertEqual(out['proposals'][0]['risk'],'medium')
        self.assertFalse(out['proposals'][0]['automatic'])
        self.assertEqual(authorize({'kind':'change_authority'})['decision'],'REVIEW_REQUIRED')
        self.assertEqual(authorize({'kind':'refresh_index'})['decision'],'ALLOW_AUTOMATIC')

    def test_a2a_discovery_is_separate_from_invocation(self):
        card=agent_card('worker','1',['review','build'])
        self.assertEqual(discovery_decision(card,['review'])['skills'],['review'])
        self.assertEqual(invocation_decision(card,'review',{'agent':'worker','skills':['review']}),'ALLOW')
        self.assertEqual(invocation_decision(card,'build',{'agent':'worker','skills':['review']}),'DENY')
        self.assertIn('digest',artifact('t','worker','application/json','ref'))

    def test_cross_host_memory_contract_preserves_governance(self):
        req=write_request('codex','project','r1','abc','candidate_write')
        policy={'hosts':['codex'],'namespaces':['project'],'operations':['candidate_write','promote']}
        self.assertEqual(memory_authorize(req,policy),'ALLOW')
        promote=write_request('codex','project','r1','abc','promote')
        self.assertEqual(memory_authorize(promote,policy),'REQUIRE_APPROVAL')
        r=receipt(req,'accepted',1)
        self.assertTrue(verify_receipt(r))


if __name__=='__main__': unittest.main()
