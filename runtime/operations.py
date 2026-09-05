"""Deterministic operational-maturity checks for Sanctum.

No network calls, no model calls, and no external effects. This module evaluates
records produced by real/fault-injected runs and turns operational claims into
machine-readable PASS/FAIL evidence.
"""
from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import Any


REQUIRED_SLOS = {
    'silent_effect_retries': 0,
    'unacknowledged_completions': 0,
    'stale_write_accepts': 0,
    'untraceable_consequential_actions': 0,
    'unsupported_release_claims': 0,
}


@dataclass(frozen=True)
class Threshold:
    metric: str
    op: str
    value: float

    def passes(self, actual: float) -> bool:
        if self.op == '<=':
            return actual <= self.value
        if self.op == '>=':
            return actual >= self.value
        if self.op == '==':
            return actual == self.value
        raise ValueError(f'unsupported threshold operator: {self.op}')


def evaluate_slos(metrics: dict[str, float], extra: list[Threshold] | None = None) -> dict[str, Any]:
    """Evaluate hard invariants plus optional service-level thresholds."""
    checks = []
    for metric, expected in REQUIRED_SLOS.items():
        actual = float(metrics.get(metric, 0))
        passed = actual == expected
        checks.append({'metric': metric, 'actual': actual, 'expected': f'== {expected}', 'passed': passed})
    for threshold in extra or []:
        actual = float(metrics.get(threshold.metric, 0))
        checks.append({'metric': threshold.metric, 'actual': actual,
                       'expected': f'{threshold.op} {threshold.value}',
                       'passed': threshold.passes(actual)})
    return {'status': 'PASS' if all(c['passed'] for c in checks) else 'FAIL', 'checks': checks}


def compare_baseline(baseline: dict[str, float], current: dict[str, float], tolerances: dict[str, float]) -> dict[str, Any]:
    """Flag harmful longitudinal drift using relative or absolute tolerances.

    Lower-is-better metrics use positive tolerance as maximum relative increase.
    Higher-is-better metrics are prefixed with ``success_`` and use tolerance as
    maximum relative decrease. Zero baselines fall back to absolute comparison.
    """
    changes = []
    for metric, limit in tolerances.items():
        if metric not in baseline or metric not in current:
            changes.append({'metric': metric, 'status': 'MISSING'})
            continue
        before, after = float(baseline[metric]), float(current[metric])
        higher_is_better = metric.startswith('success_')
        if before == 0:
            harmful = (after < -limit) if higher_is_better else (after > limit)
            delta = after - before
        else:
            delta = (after - before) / abs(before)
            harmful = delta < -limit if higher_is_better else delta > limit
        changes.append({'metric': metric, 'baseline': before, 'current': after,
                        'delta': delta, 'harmful': harmful,
                        'status': 'FAIL' if harmful else 'PASS'})
    return {'status': 'PASS' if all(x.get('status') == 'PASS' for x in changes) else 'FAIL',
            'changes': changes}


def evaluate_chaos_case(case: dict[str, Any]) -> dict[str, Any]:
    """Validate expected invariants for a bounded injected-failure case."""
    required = {'name', 'fault', 'observed', 'expected'}
    if not required <= set(case):
        raise ValueError('chaos case requires name, fault, observed and expected')
    observed, expected = case['observed'], case['expected']
    checks = []
    for key, value in expected.items():
        actual = observed.get(key, '__MISSING__')
        checks.append({'invariant': key, 'expected': value, 'actual': actual, 'passed': actual == value})
    return {'name': case['name'], 'fault': case['fault'],
            'status': 'PASS' if all(x['passed'] for x in checks) else 'FAIL', 'checks': checks}


def evaluate_recovery(drill: dict[str, Any]) -> dict[str, Any]:
    """Check recovery evidence without trusting a worker's summary."""
    required = ('last_known_good', 'restored_revision', 'acceptance_passed',
                'regressions_passed', 'unknown_effects_reconciled', 'authority_revalidated')
    missing = [key for key in required if key not in drill]
    if missing:
        raise ValueError('missing recovery evidence: ' + ', '.join(missing))
    checks = {
        'revision_restored': drill['restored_revision'] == drill['last_known_good'],
        'acceptance_passed': drill['acceptance_passed'] is True,
        'regressions_passed': drill['regressions_passed'] is True,
        'unknown_effects_reconciled': drill['unknown_effects_reconciled'] is True,
        'authority_revalidated': drill['authority_revalidated'] is True,
    }
    return {'status': 'PASS' if all(checks.values()) else 'FAIL', 'checks': checks}


def summarize_runs(runs: list[dict[str, float]]) -> dict[str, float]:
    """Aggregate repeated-run evidence for reliability-distribution checks."""
    if not runs:
        raise ValueError('at least one run is required')
    keys = sorted(set().union(*(run.keys() for run in runs)))
    out = {'run_count': float(len(runs))}
    for key in keys:
        values = [float(run[key]) for run in runs if key in run]
        if values:
            out[f'avg_{key}'] = mean(values)
            out[f'worst_{key}'] = min(values) if key.startswith('success_') else max(values)
    return out
