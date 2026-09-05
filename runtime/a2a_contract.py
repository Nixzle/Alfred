"""Dormant A2A interoperability contract: discovery/artifact semantics without networking."""
import hashlib
import json


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def agent_card(name, version, skills, endpoint=None, auth='required'):
    if not name or not version or not isinstance(skills,list) or not skills:
        raise ValueError('bounded agent identity and skills required')
    if auth not in {'required','none'}:
        raise ValueError('invalid auth mode')
    body={'name':name,'version':version,'skills':sorted(set(skills)),'endpoint':endpoint,'auth':auth}
    return body | {'digest':digest(body)}


def verify_card(card):
    body={k:v for k,v in card.items() if k!='digest'}
    return card.get('digest')==digest(body)


def discovery_decision(card, allowed_skills):
    if not verify_card(card):
        return {'decision':'DENY','reason':'invalid agent card'}
    visible=sorted(set(card['skills']) & set(allowed_skills))
    return {'decision':'DISCOVERABLE' if visible else 'HIDDEN','skills':visible}


def invocation_decision(card, skill, grant):
    if not verify_card(card): return 'DENY'
    if skill not in card['skills']: return 'DENY'
    if grant.get('agent')!=card['name'] or skill not in grant.get('skills',[]): return 'DENY'
    return 'ALLOW'


def artifact(task_id, producer, media_type, reference, sha256=None):
    if not all(isinstance(v,str) and v for v in (task_id,producer,media_type,reference)):
        raise ValueError('artifact metadata required')
    body={'task_id':task_id,'producer':producer,'media_type':media_type,'reference':reference,'sha256':sha256}
    return body | {'digest':digest(body)}
