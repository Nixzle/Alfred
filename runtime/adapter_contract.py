"""Portable host-adapter contract for projecting Sanctum into external agent surfaces."""
import hashlib
import json

VALID_EFFECTS={'read','write','destructive','network','tool','memory'}


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def validate_adapter(spec):
    required=('host','version','reads','writes','effects','healthcheck','revoke')
    missing=[k for k in required if k not in spec]
    if missing:
        raise ValueError('missing adapter fields: '+','.join(missing))
    if not all(isinstance(spec[k],list) for k in ('reads','writes','effects')):
        raise ValueError('reads/writes/effects must be lists')
    if not set(spec['effects']) <= VALID_EFFECTS:
        raise ValueError('unknown adapter effect class')
    if not isinstance(spec['healthcheck'],str) or not spec['healthcheck']:
        raise ValueError('healthcheck required')
    if not isinstance(spec['revoke'],str) or not spec['revoke']:
        raise ValueError('revocation behavior required')
    return True


def manifest(spec):
    validate_adapter(spec)
    body={k:spec[k] for k in ('host','version','reads','writes','effects','healthcheck','revoke')}
    body['destructive_requires_confirmation']=bool(spec.get('destructive_requires_confirmation',True))
    body['context_mode']=spec.get('context_mode','PROJECTED')
    if body['context_mode'] not in {'ISOLATED','PROJECTED','FORKED'}:
        raise ValueError('invalid context mode')
    return body | {'digest':digest(body)}


def verify_health(manifest_value, observation):
    body={k:v for k,v in manifest_value.items() if k!='digest'}
    if manifest_value.get('digest')!=digest(body):
        return {'status':'INVALID','reason':'adapter manifest digest mismatch'}
    if observation.get('host')!=body['host'] or observation.get('version')!=body['version']:
        return {'status':'MISMATCH','reason':'health observation targets another adapter'}
    if observation.get('healthy') is not True:
        return {'status':'UNHEALTHY','reason':observation.get('reason','health check failed')}
    return {'status':'HEALTHY','reason':'adapter health check passed'}


def authorize_effect(manifest_value, effect, confirmed=False):
    if effect not in manifest_value.get('effects',[]):
        return 'DENY'
    if effect=='destructive' and manifest_value.get('destructive_requires_confirmation',True) and not confirmed:
        return 'REQUIRE_APPROVAL'
    return 'ALLOW'
