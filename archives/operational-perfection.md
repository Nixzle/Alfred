# Operational Perfection

Status: canonical Archive
Date: 2026-09-05

Operational perfection is an asymptotic objective, not a claim of infallibility. The practical target is to make failures bounded, visible, reproducible, recoverable, measurable, and increasingly difficult to repeat.

## Primary transition

After architectural saturation, default effort shifts from capability discovery to:

`ENFORCE -> OBSERVE -> BREAK DELIBERATELY -> RECOVER -> MEASURE -> TIGHTEN`

The key question changes from:

> What capability are we missing?

to:

> Which capability do we claim to have that has not yet survived production-grade failure?

## Maturity ladder

1. **EXISTS** — doctrine or code exists.
2. **CHECKED** — deterministic/evaluative evidence can verify expected behavior.
3. **ENFORCED** — runtime/tooling prevents or gates violation.
4. **OBSERVED / BATTLE-TESTED** — real or fault-injected operation is instrumented, recovery is exercised, and longitudinal behavior is measured.

Do not promote maturity by rhetoric.

## Hard operational invariants

The following default to zero tolerance:

- silent consequential-effect retries;
- unacknowledged delegated completions;
- stale-write acceptance;
- consequential actions without attributable authority/evidence;
- release claims stronger than available validation.

Additional project/runtime SLOs should cover success consistency, latency, recovery time, retry rate, retrieval misses, repeated user corrections, cost, and failure distribution where measurable.

## Operational gates

### Automatic validation
Every material runtime change should automatically run deterministic tests, doctrine lint, acceptance checks, and diff/syntax sanity where supported.

A CI run is **CHECKED** evidence. It becomes a true merge gate only when repository rules require that check before canonical-state mutation.

### Canonical-state protection
Prefer:

- protected default branch;
- required CI checks;
- PR review for consequential runtime changes;
- signed commits/releases where practical;
- validated-version pins in consuming projects;
- rollback/revert path.

### Fault injection
Representative scenarios include:

- timeout after successful effect;
- lost acknowledgement;
- crash between intent and commit;
- duplicated delivery;
- stale snapshot;
- concurrent writers;
- expired/revoked delegation;
- corrupted memory/export;
- provider/tool failure;
- lost worker completion;
- partial external effect;
- network loss;
- malformed event;
- poisoned/untrusted context;
- dependency regression.

Each case declares expected invariants and fails if observed state differs.

### Recovery drills
Recovery is not proven because a backup exists. A recovery drill should verify:

- restore to an identified last-known-good revision/state;
- acceptance checks pass;
- regression suite passes;
- unknown effects are reconciled;
- authority is freshly revalidated;
- restored state provenance remains intact.

### Longitudinal drift
Stable baselines should be replayed periodically when practical. Compare:

- success rate;
- latency;
- cost;
- retries;
- retrieval quality;
- repeated corrections;
- tool/provider errors;
- recovery time;
- worst-case behavior, not only averages.

A new model/tool/provider/runtime profile invalidates direct comparison unless the profile change is recorded.

### Reliability distribution
A single successful run proves capability, not reliability. Repeated execution should preserve run count, average behavior, worst-case behavior, and failure distribution where meaningful.

## Member ownership

- **Ultron Prime** chooses operational thresholds, routes remediation, and owns the final maturity claim.
- **Prime Sense** detects drift, repeated corrections, completion seams, suspicious effort, and operational anomalies from available evidence.
- **Watcher** captures trace, effect, cost, failure, recovery, and SLO evidence.
- **Web of Destiny** evaluates regressions, fault-injection cases, drift comparisons, and recovery claims.
- **TVA** owns actual scope/authority gating where a runtime provides an enforcement boundary.
- **Images of Ikonn / Ultron Bots** must obey effect, receipt, ownership, recovery, and budget contracts.
- **Cerebro** researches concrete operational unknowns or superior donor implementations when evidence shows a gap.

## Current implementation

`runtime/operations.py` provides deterministic evaluators for:

- hard and configurable SLOs;
- longitudinal drift against tolerance thresholds;
- bounded chaos/fault-injection case invariants;
- recovery-drill evidence;
- repeated-run reliability summaries.

`runtime/tests/test_operations.py` provides regression coverage.

The GitHub runtime workflow is configured to run automatically on `push` to `main`, on pull requests, and by manual dispatch. This is automatic CHECKED evidence. It is not an ENFORCED merge gate until repository branch/ruleset configuration requires the workflow check.

## Rule

Operational perfection is reached only by reducing unobserved failure space, not by accumulating more prose.
