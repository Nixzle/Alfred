"""Host-neutral memory service contract; no server or network transport is provided."""
import hashlib
import json


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def write_request(host, namespace, record_id, payload_digest, operation='candidate_write'):
    if operation not in {'candidate_write','promote','supersede','delete','read'}:
        raise ValueError('unknown memory operation')
    if not all(isinstance(v,str) and v for v in (host,namespace,record_id)):
        raise ValueError('host/namespace/record required')
    body={'host':host,'namespace':namespace,'record_id':record_id,'payload_digest':payload_digest,'operation':operation}
    return body | {'request_digest':digest(body)}


def authorize(request, policy):
    allowed_hosts=set(policy.get('hosts',[]))
    allowed_namespaces=set(policy.get('namespaces',[]))
    allowed_ops=set(policy.get('operations',[]))
    if request.get('host') not in allowed_hosts: return 'DENY'
    if request.get('namespace') not in allowed_namespaces: return 'DENY'
    if request.get('operation') not in allowed_ops: return 'DENY'
    if request['operation'] in {'promote','supersede','delete'} and not policy.get('allow_governed_mutation',False):
        return 'REQUIRE_APPROVAL'
    return 'ALLOW'


def receipt(request, outcome, revision=None):
    if outcome not in {'accepted','rejected','applied','not_found'}:
        raise ValueError('invalid memory outcome')
    body={'request_digest':request['request_digest'],'outcome':outcome,'revision':revision}
    return body | {'receipt_digest':digest(body)}


def verify_receipt(value):
    body={k:v for k,v in value.items() if k!='receipt_digest'}
    return value.get('receipt_digest')==digest(body)
