"""Deterministic delegated-work delivery and runaway-cost reliability contracts."""
import hashlib
import json


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def acceptance_receipt(task_id, worker_id, capsule_digest):
    if not all(isinstance(v,str) and v for v in (task_id,worker_id,capsule_digest)):
        raise ValueError('bounded identities required')
    body={'type':'accepted','task_id':task_id,'worker_id':worker_id,'capsule_digest':capsule_digest}
    return body | {'receipt_digest':digest(body)}


def completion_receipt(task_id, worker_id, evidence_ids, status='completed'):
    if status not in {'completed','blocked','failed'} or not isinstance(evidence_ids,list):
        raise ValueError('invalid completion receipt')
    body={'type':'completion','task_id':task_id,'worker_id':worker_id,
          'status':status,'evidence_ids':sorted(set(evidence_ids))}
    return body | {'receipt_digest':digest(body)}


def verify_receipt(receipt):
    body={k:v for k,v in receipt.items() if k!='receipt_digest'}
    return receipt.get('receipt_digest')==digest(body)


def delivery_state(accepted, completion=None):
    if not verify_receipt(accepted):
        return {'state':'CORRUPT','reason':'invalid acceptance receipt'}
    if completion is None:
        return {'state':'IN_FLIGHT','reason':'no completion receipt'}
    if not verify_receipt(completion):
        return {'state':'CORRUPT','reason':'invalid completion receipt'}
    if (accepted['task_id'],accepted['worker_id']) != (completion['task_id'],completion['worker_id']):
        return {'state':'CORRUPT','reason':'receipt identity mismatch'}
    return {'state':'DELIVERED' if completion['status']=='completed' else completion['status'].upper(),
            'reason':'completion receipt verified'}


def budget_decision(usage, limits):
    """Fail closed when measurable budgets are exceeded; never invent unmeasured usage."""
    checks={}
    for name in ('tokens','cost','attempts','elapsed_seconds'):
        if name in limits:
            if name not in usage:
                checks[name]='UNKNOWN'
            else:
                checks[name]='EXCEEDED' if usage[name] > limits[name] else 'OK'
    if any(v=='EXCEEDED' for v in checks.values()):
        return {'decision':'HALT','checks':checks}
    if any(v=='UNKNOWN' for v in checks.values()):
        return {'decision':'REQUIRE_OBSERVATION','checks':checks}
    return {'decision':'CONTINUE','checks':checks}


def provider_result(provider, outcome, *, explicit_error=None):
    if outcome not in {'success','failure','unknown'}:
        raise ValueError('invalid provider outcome')
    return {'provider':provider,'outcome':outcome,'explicit_error':explicit_error}


def choose_failover(results, candidates):
    failed={r['provider'] for r in results if r['outcome']=='failure'}
    unknown={r['provider'] for r in results if r['outcome']=='unknown'}
    if unknown:
        return {'decision':'RECONCILE','reason':'unknown provider outcome must be reconciled before failover'}
    for candidate in candidates:
        if candidate not in failed:
            return {'decision':'TRY','provider':candidate}
    return {'decision':'STOP','reason':'no unfailed provider remains'}
