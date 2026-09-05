"""Governed on-demand Spellbook index, usage evidence, and curation helpers."""
import hashlib
import json
from pathlib import Path


def _digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


class SpellRegistry:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.records = {}

    def register(self, spell_id, path, triggers, version=1, status='active'):
        p = (self.root / path).resolve()
        if not p.is_relative_to(self.root) or not p.is_file():
            raise ValueError('spell must be an existing file inside registry root')
        if status not in {'candidate','active','retired'} or not triggers:
            raise ValueError('invalid spell metadata')
        body = p.read_text(encoding='utf-8')
        rec = dict(id=spell_id, path=str(p.relative_to(self.root)), triggers=sorted(set(triggers)),
                   version=int(version), status=status, sha256=hashlib.sha256(body.encode()).hexdigest(),
                   uses=0, successes=0, failures=0)
        if spell_id in self.records and self.records[spell_id]['version'] >= rec['version']:
            raise ValueError('spell version must increase')
        self.records[spell_id] = rec
        return dict(rec)

    def select(self, signals):
        signals = set(signals)
        ranked=[]
        for rec in self.records.values():
            if rec['status'] != 'active':
                continue
            overlap=len(signals & set(rec['triggers']))
            if overlap:
                quality=(rec['successes']+1)/(rec['uses']+2)
                ranked.append((overlap, quality, rec['id'], rec))
        ranked.sort(key=lambda row:(-row[0],-row[1],row[2]))
        return [dict(row[3]) for row in ranked]

    def load(self, spell_id):
        rec=self.records[spell_id]
        if rec['status']!='active':
            raise PermissionError('spell is not active')
        path=(self.root/rec['path']).resolve()
        body=path.read_text(encoding='utf-8')
        if hashlib.sha256(body.encode()).hexdigest()!=rec['sha256']:
            raise ValueError('spell content changed without registry update')
        return body

    def record_outcome(self, spell_id, success):
        rec=self.records[spell_id]
        rec['uses']+=1
        rec['successes' if success else 'failures']+=1
        return dict(rec)

    def duplicate_candidates(self):
        by_triggers={}
        pairs=[]
        for rec in self.records.values():
            key=tuple(rec['triggers'])
            if key in by_triggers:
                pairs.append(tuple(sorted((by_triggers[key],rec['id']))))
            else:
                by_triggers[key]=rec['id']
        return sorted(set(pairs))

    def retire(self, spell_id):
        self.records[spell_id]['status']='retired'

    def manifest(self):
        payload={'spells':sorted((dict(r) for r in self.records.values()), key=lambda r:r['id'])}
        return payload | {'digest':_digest(payload)}
