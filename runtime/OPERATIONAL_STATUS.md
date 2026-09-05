# Operational hardening status

Date: 2026-09-05

## Implemented this tranche

- automatic GitHub Actions trigger on push to `main`, pull request, and manual dispatch;
- deterministic operational SLO evaluation in `runtime/operations.py`;
- longitudinal drift comparison with explicit tolerances;
- bounded fault-injection/chaos invariant evaluation;
- recovery-drill verification;
- repeated-run reliability-distribution summaries;
- deterministic regression coverage in `runtime/tests/test_operations.py`;
- canonical doctrine in `archives/operational-perfection.md`;
- updated enforcement classification in `governance/ENFORCEMENT_STATUS.md`.

## Observed CI state

The automatic workflow is **OBSERVED to trigger** on pushes.

Two push-triggered runs were observed during rollout:

- run `33950748054` on `ddca07003dcefe22b717352f12b677eec5c9866a` — completed with `failure` before usable job-step/log evidence was exposed;
- run `33950781567` on `6f07e5d4e7c152de39046fc1eba89d98552c376f` — completed with `failure` before usable job-step/log evidence was exposed, even after simplifying the workflow to the already-proven Alfred pattern.

Because both failures occurred before normal executable step evidence was available, do **not** classify this as a test-suite failure. The hosted runner/execution environment remains an unresolved infrastructure blocker.

## Current maturity

| Capability | Maturity |
| --- | --- |
| automatic CI trigger | CHECKED / OBSERVED trigger |
| CI test execution | BLOCKED / not observed green |
| operational SLO evaluator | CHECKED |
| drift evaluator | CHECKED |
| chaos invariant evaluator | CHECKED |
| recovery drill evaluator | CHECKED |
| repeated-run distribution summary | CHECKED |
| protected-main required check | NOT ENFORCED |
| signed canonical commits/releases | NOT ENFORCED |
| live cross-surface telemetry | partial/local only |
| scheduled longitudinal replay | not automated |
| independent full restore drill | not yet observed |

## Required next external controls

1. Restore usable GitHub Actions runner execution for the private Sanctum repository or provide an equivalent trusted CI runner.
2. Require the runtime validation check in branch/ruleset protection for canonical `main`.
3. Prefer signed commits/releases where practical.
4. Run a full integrated local validation receipt on an authorized host.
5. Execute representative chaos and recovery drills against real bounded runtime slices, then record results as Watcher/Web evidence.

No green operational claim should be made until the relevant evidence exists.
