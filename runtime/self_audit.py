"""Evidence-driven harness self-audit that proposes improvements without self-authorizing them."""
from collections import Counter

RISK_ORDER={'low':0,'medium':1,'high':2,'forbidden':3}


def classify(proposal):
    kind=proposal['kind']
    if kind in {'deduplicate_spell','refresh_index','retire_stale_cache'}:
        return 'low'
    if kind in {'add_regression','adjust_threshold','promote_candidate_spell'}:
        return 'medium'
    if kind in {'change_authority','enable_network','install_dependency','alter_governance'}:
        return 'high'
    return 'forbidden'


def audit(events):
    """Consume normalized Watcher-style metadata and emit bounded proposals."""
    counts=Counter()
    for event in events:
        name=event.get('event')
        data=event.get('data',{})
        if name=='user_correction': counts['user_correction']+=1
        if name in {'effect_unknown','worker_stopped'}: counts['runtime_failure']+=1
        if name=='research' and data.get('status')=='FAIL': counts['research_failure']+=1
        if name=='cache' and data.get('decision')=='miss': counts['cache_miss']+=1
        if name=='spell_used': counts['spell:'+str(data.get('spell'))]+=1
    proposals=[]
    if counts['user_correction']>=3:
        proposals.append({'kind':'add_regression','reason':'repeated user corrections indicate systemic miss'})
    if counts['runtime_failure']>=2:
        proposals.append({'kind':'add_regression','reason':'repeated runtime failures need replay pressure'})
    if counts['research_failure']>=2:
        proposals.append({'kind':'adjust_threshold','reason':'repeated research-quality failures'})
    if counts['cache_miss']>=5:
        proposals.append({'kind':'refresh_index','reason':'high cache miss rate'})
    for proposal in proposals:
        proposal['risk']=classify(proposal)
        proposal['automatic']=proposal['risk']=='low'
    return {'counts':dict(counts),'proposals':proposals}


def authorize(proposal, max_auto_risk='low'):
    risk=classify(proposal)
    return {'decision':'ALLOW_AUTOMATIC' if RISK_ORDER[risk] <= RISK_ORDER[max_auto_risk] else 'REVIEW_REQUIRED',
            'risk':risk}
