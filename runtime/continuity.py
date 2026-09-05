"""Deterministic pre-exhaustion handoff records for long-running sessions.

This module does not estimate a model provider's hidden context window. It evaluates
explicit session pressure signals supplied by the current surface and produces a
minimal authoritative handoff record before continuity is lost.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
import hashlib
import json
from typing import Any


REQUIRED_HANDOFF_FIELDS = (
    'objective', 'verified_state', 'decisions', 'constraints', 'blockers',
    'revisions', 'relevant_memory', 'sanctum_route', 'next_action'
)


@dataclass(frozen=True)
class PressurePolicy:
    warning_ratio: float = 0.75
    critical_ratio: float = 0.90
    max_handoff_chars: int = 12000

    def __post_init__(self):
        if not 0 < self.warning_ratio < self.critical_ratio <= 1:
            raise ValueError('require 0 < warning_ratio < critical_ratio <= 1')
        if self.max_handoff_chars < 1000:
            raise ValueError('max_handoff_chars too small')


def assess_pressure(used: int, limit: int, policy: PressurePolicy | None = None) -> dict[str, Any]:
    policy = policy or PressurePolicy()
    if used < 0 or limit <= 0:
        raise ValueError('used must be >= 0 and limit must be > 0')
    ratio = used / limit
    if ratio >= policy.critical_ratio:
        state = 'CRITICAL'
        action = 'HANDOFF_NOW'
    elif ratio >= policy.warning_ratio:
        state = 'WARNING'
        action = 'PREPARE_HANDOFF'
    else:
        state = 'NORMAL'
        action = 'CONTINUE'
    return {'used': used, 'limit': limit, 'ratio': ratio, 'state': state, 'action': action}


def _bounded_list(value: Any, max_items: int = 20) -> list[Any]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError('handoff list fields must be lists')
    return value[:max_items]


def build_handoff(state: dict[str, Any], policy: PressurePolicy | None = None) -> dict[str, Any]:
    policy = policy or PressurePolicy()
    missing = [field for field in REQUIRED_HANDOFF_FIELDS if field not in state]
    if missing:
        raise ValueError('missing handoff fields: ' + ', '.join(missing))

    record = {
        'contract': 'SANCTUM-CONTINUITY-V1',
        'objective': str(state['objective']).strip(),
        'verified_state': _bounded_list(state['verified_state']),
        'decisions': _bounded_list(state['decisions']),
        'constraints': _bounded_list(state['constraints']),
        'blockers': _bounded_list(state['blockers']),
        'revisions': dict(state['revisions']),
        'relevant_memory': _bounded_list(state['relevant_memory']),
        'sanctum_route': _bounded_list(state['sanctum_route']),
        'next_action': str(state['next_action']).strip(),
    }
    if not record['objective'] or not record['next_action']:
        raise ValueError('objective and next_action must be non-empty')

    raw = json.dumps(record, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    if len(raw) > policy.max_handoff_chars:
        raise ValueError('handoff exceeds configured compactness budget')
    record['sha256'] = hashlib.sha256(raw.encode('utf-8')).hexdigest()
    return record


def verify_handoff(record: dict[str, Any]) -> bool:
    if record.get('contract') != 'SANCTUM-CONTINUITY-V1' or 'sha256' not in record:
        return False
    body = dict(record)
    digest = body.pop('sha256')
    raw = json.dumps(body, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    return hashlib.sha256(raw.encode('utf-8')).hexdigest() == digest
