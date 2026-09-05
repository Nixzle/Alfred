"""Run local release checks and save evidence without hosted CI or model calls."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]

def validate(output, attention_db=None, project=None):
    if (attention_db is None) != (project is None):
        raise ValueError('attention database and project must be supplied together')
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=False)
    def git(*args):
        return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
    files = {}
    for line in git('ls-files','--cached','--others','--exclude-standard').splitlines():
        path = ROOT/line
        if path.is_file(): files[line] = hashlib.sha256(path.read_bytes()).hexdigest()
    checks = [('tests',[sys.executable,'-m','unittest','discover','-s','runtime/tests','-p','test_*.py']),
              ('lint',[sys.executable,'runtime/sanctum.py','lint']),
              ('acceptance',[sys.executable,'runtime/acceptance.py','--out',str(output/'acceptance')]),
              ('diff',['git','diff','--check'])]
    results=[]
    for name,command in checks:
        started=time.perf_counter()
        result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,timeout=180)
        log=result.stdout+result.stderr
        (output/(name+'.txt')).write_text(log,encoding='utf-8')
        ok=result.returncode==0
        if name=='tests':
            count=re.search(r'Ran (\d+) tests?',log)
            ok=ok and count is not None and int(count[1])>0
        results.append(dict(check=name,exit_code=result.returncode,passed=ok,
                            elapsed_seconds=round(time.perf_counter()-started,3)))
    receipt=dict(generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                 revision=git('rev-parse','HEAD'),dirty=bool(git('status','--porcelain')),
                 file_sha256=files,checks=results,status='PASS' if all(r['passed'] for r in results) else 'FAIL',
                 scope='local tests, doctrine lint, signed task acceptance; no hosted CI')
    (output/'receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    if attention_db is not None:
        try:
            from .release_event import observe
        except ImportError:
            from release_event import observe
        event=observe(receipt, attention_db, project)
        (output/'attention.json').write_text(json.dumps(event,indent=2),encoding='utf-8')
    return receipt

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',required=True)
    parser.add_argument('--attention-db')
    parser.add_argument('--project')
    args=parser.parse_args()
    result=validate(args.out,args.attention_db,args.project)
    summary={k:v for k,v in result.items() if k!='file_sha256'}
    if args.attention_db is not None:
        summary['attention']=json.loads((Path(args.out)/'attention.json').read_text(encoding='utf-8'))
    print(json.dumps(summary,indent=2))
    raise SystemExit(result['status']!='PASS')
