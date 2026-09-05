"""Ultron's explicit delivery-contract and dependency checks, not effect authorization."""
import argparse
import json
from pathlib import Path


def evaluate(required, results):
    """Required items are owner supplied; evidence references need separate verification."""
    issues=[]
    if not required: issues.append('ACCEPTANCE_MISSING')
    try:
        expected={r['id']:r for r in required}
        actual={r['id']:r for r in results}
        if len(expected)!=len(required) or len(actual)!=len(results): issues.append('DUPLICATE_ITEM')
        if set(actual)-set(expected): issues.append('UNSCOPED_ITEM')
        for key, requirement in expected.items():
            result=actual.get(key,{})
            if result.get('status')!='complete': issues.append('INCOMPLETE:'+key)
            if not result.get('evidence'): issues.append('EVIDENCE_MISSING:'+key)
            if result.get('level')!=requirement.get('level') or not requirement.get('level'):
                issues.append('LEVEL_MISMATCH:'+key)
    except (TypeError,KeyError,AttributeError):
        issues.append('INVALID_CONTRACT')
    return dict(status='COMPLETE' if not issues else 'INCOMPLETE',issues=issues,
                scope='Owner acceptance coverage and evidence references; not semantic verification')


def dependency_gate(required_steps, observations):
    """Unknown outcome is not success. Never use this to expand action authority."""
    blocked=[step for step in required_steps if observations.get(step,{}).get('status')!='verified_success']
    return dict(decision='BLOCK' if blocked else 'READY',blocked=blocked,
                scope='Dependency readiness only; actual action authority remains separate')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract',type=Path,required=True)
    parser.add_argument('--results',type=Path,required=True)
    args=parser.parse_args()
    result=evaluate(json.loads(args.contract.read_text()),json.loads(args.results.read_text()))
    print(json.dumps(result,indent=2))
    raise SystemExit(result['status']!='COMPLETE')
