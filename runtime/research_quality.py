"""Check research receipts without confusing filled fields with true claims.

Inputs are trusted orchestrator records. This checker does not browse sources,
authenticate reviewers, infer entailment or establish evidence independence.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path


def digest(receipt):
    return hashlib.sha256(json.dumps(receipt,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def evaluate(receipt, review=None):
    issues=[]
    def require(ok, code):
        if not ok: issues.append(code)
    try:
        require(bool(receipt.get('objective')), 'OBJECTIVE_MISSING')
        observed=dt.datetime.fromisoformat(receipt['as_of'])
        require(observed.tzinfo is not None, 'DATE_INVALID')
        sources=receipt.get('sources',[])
        source_map={s['id']:s for s in sources}
        require(bool(sources) and len(source_map)==len(sources), 'SOURCES_MISSING_OR_DUPLICATE')
        for source in sources:
            require(all(source.get(k) for k in ('locator','section','family','kind')), 'SOURCE_PROVENANCE_MISSING')
            require(source.get('access')=='opened', 'SOURCE_NOT_OPENED')
            retrieved=dt.datetime.fromisoformat(source['retrieved_at'])
            require(retrieved.tzinfo is not None and retrieved<=observed, 'SOURCE_DATE_INVALID')
        claims=receipt.get('claims',[])
        require(bool(claims) and len({c['id'] for c in claims})==len(claims), 'CLAIMS_MISSING_OR_DUPLICATE')
        for claim in claims:
            refs=claim.get('sources',[])
            require(bool(claim.get('text')) and bool(refs) and all(r in source_map for r in refs), 'CLAIM_SOURCE_MISSING')
            require(claim.get('basis') in {'direct','inference','proposal'}, 'CLAIM_BASIS_MISSING')
            require(bool(claim.get('limitation')), 'CLAIM_LIMITATION_MISSING')
            if claim.get('basis')=='inference':
                require(bool(claim.get('rationale')), 'INFERENCE_UNEXPLAINED')
            families={source_map[r].get('family') for r in refs if r in source_map}
            if claim.get('independent_confirmation') is True:
                require(len(families)>=2, 'CORRELATED_CONFIRMATION')
            if claim.get('current') is True:
                require(bool(claim.get('freshness_evidence')), 'CURRENT_CLAIM_UNCHECKED')
        coverage=receipt.get('coverage',{})
        require(bool(coverage.get('scope')) and bool(coverage.get('limits')), 'COVERAGE_MISSING')
        if receipt.get('landscape'):
            require(bool(coverage.get('lateral_route')) and bool(coverage.get('practitioner_route')), 'LANDSCAPE_ROUTE_MISSING')
        rounds=receipt.get('rounds',[])
        require(bool(rounds), 'ROUNDS_MISSING')
        for item in rounds:
            require(all(item.get(k) for k in ('question','finding','decision_impact')), 'ROUND_IMPACT_MISSING')
        require(bool(receipt.get('stop_reason')), 'STOP_REASON_MISSING')
        if receipt.get('forge'):
            applications=receipt.get('applications',[])
            require(bool(applications), 'APPLICATION_MISSING')
            for item in applications:
                require(all(item.get(k) for k in ('technique','baseline','change','evidence','limitation')), 'APPLICATION_EVIDENCE_MISSING')
                require(item.get('status') in {'proposed','tested','rejected'}, 'APPLICATION_STATUS_INVALID')
                if item.get('status')=='tested': require(bool(item.get('result')), 'APPLICATION_RESULT_MISSING')
    except (ValueError,TypeError,KeyError,AttributeError):
        issues.append('INVALID_RECEIPT')
    support='NOT_EVALUATED'
    review_kind=None
    if review is not None:
        try:
            require(review.get('receipt_sha256')==digest(receipt), 'REVIEW_MISMATCH')
            require(bool(review.get('reviewer')) and review.get('method') in {'human','agent'}, 'REVIEW_PROVENANCE_MISSING')
            decisions=review['claims']
            ids={claim['id'] for claim in receipt['claims']}
            require(set(decisions)==ids, 'REVIEW_COVERAGE_MISSING')
            require(all(row.get('verdict') in {'supported','unsupported','uncertain'} and row.get('note') for row in decisions.values()), 'REVIEW_DECISION_MISSING')
            if not issues:
                support='REVIEWED' if all(row['verdict']=='supported' for row in decisions.values()) else 'NEEDS_REVIEW'
                review_kind=review['method']
        except (KeyError,TypeError,AttributeError):
            issues.append('INVALID_REVIEW')
    return dict(status='FAIL' if issues else 'STRUCTURE_PASS', issues=sorted(set(issues)),
                claim_support=support, reviewer_method=review_kind,
                independent_review=bool(review and review.get('independent') is True) if support=='REVIEWED' else False,
                empirical_improvement='NOT_EVALUATED', receipt_sha256=digest(receipt),
                scope='Receipt consistency only; semantic review is separately supplied evidence, not authenticated by this checker')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt',type=Path,required=True)
    parser.add_argument('--review',type=Path)
    args=parser.parse_args()
    result=evaluate(json.loads(args.receipt.read_text()), json.loads(args.review.read_text()) if args.review else None)
    print(json.dumps(result,indent=2))
    raise SystemExit(result['status']=='FAIL')
