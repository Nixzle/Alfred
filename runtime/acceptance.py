"""Execute a useful local health-report task and verify it from a fresh session."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import secrets

from ledger import Ledger
from supervisor import Supervisor
from sanctum import lint_repo


def exercise(output):
    output=Path(output)
    output.mkdir(parents=True,exist_ok=False)
    workspace=output/'worker'; workspace.mkdir()
    db=output/'control.sqlite'
    ledger=Ledger(db)
    try:
        lint=lint_repo()
        if lint['status']!='PASS':
            raise ValueError('doctrine lint failed')
        payload=json.dumps({'doctrine_lint':lint,'purpose':'Sanctum local health report'},indent=2)
        task=ledger.create('health-report','Produce a verified runtime health report','prime',
                           ['Report matches fresh doctrine lint','Fresh session recovers completion and evidence'])
        supervisor=Supervisor(ledger,secrets.token_bytes(32))
        grant=supervisor.issue(task['id'],'health-worker',['create'],['health.json'])
        capsule=dict(task_id=task['id'],worker_id='health-worker',owner='prime',
                     allowed_actions=['create'],allowed_targets=['health.json'],
                     expires_at=(dt.datetime.now(dt.timezone.utc)+dt.timedelta(minutes=5)).isoformat())
        plan=[dict(id='health-report-v1',action='create',target='health.json',text=payload)]
        handback=supervisor.run_plan(grant,capsule,workspace,plan)
        if handback['blocker']!='Acceptance review required':
            raise ValueError('worker did not finish')
        artifact=workspace/'health.json'
        actual=artifact.read_bytes()
        if actual!=payload.encode():
            raise ValueError('artifact differs from verified report')
        task=ledger.get(task['id'])
        ledger.update(task['id'],task['revision'],'prime',status='complete',blocker=None,
                      next_action='None: accepted',evidence=handback['evidence'])
        supervisor.revoke(grant['body']['id'])
    finally:
        ledger.close()
    fresh=Ledger(db)
    try:
        task=fresh.get('health-report'); trace=fresh.trace('health-report')
        if task['status']!='complete' or not task['evidence']:
            raise ValueError('fresh session cannot recover acceptance')
        events={row['event'] for row in trace}
        if not {'grant_issued','delegation','effect_intent','effect_committed','grant_revoked'} <= events:
            raise ValueError('missing execution evidence')
        result=dict(status='PASS',task_status=task['status'],artifact_sha256=hashlib.sha256(actual).hexdigest(),
                    trace_events=len(trace),fresh_session_verified=True,scope='signed declarative worker only')
        (output/'acceptance.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
        return result
    finally:
        fresh.close()


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    print(json.dumps(exercise(parser.parse_args().out),indent=2))
