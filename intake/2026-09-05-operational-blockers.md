# Operational blockers — 2026-09-05

## 1. Hosted Sanctum CI runner

**State:** BLOCKED.

Automatic GitHub Actions triggers are configured and observed. Push-triggered runs on the private Sanctum repository currently fail before normal executable job-step/log evidence is exposed.

**Evidence:** runs `33950748054`, `33950781567`, `33950839592`.

**Do not infer:** test-suite failure, green validation, or a specific billing/runner cause without stronger evidence.

**Unblock condition:** GitHub/private-runner execution produces normal job steps/logs and the canonical runtime suite can execute.

**Meanwhile:** local/authorized-host validator remains the strongest available integrated validation path.

## 2. Canonical-main protection

**State:** NOT ENFORCED.

Repository branch metadata previously showed `main` unprotected with no required status checks.

**Unblock condition:** repository admin/ruleset configuration requires the validated runtime check before canonical merge/push where practical.

## 3. Commit/release signing

**State:** NOT ENFORCED.

Current GitHub-created commits are reported unsigned.

**Unblock condition:** a supported signing/release-attestation path is configured and verified.

## 4. Full restore drill

**State:** CHECKED contract, not OBSERVED drill.

The recovery evaluator exists, but a full repository/runtime restore from an independent clone/export has not yet been observed and recorded.

## 5. Scheduled drift replay

**State:** CHECKED evaluator, not automated schedule.

The drift comparator exists; live baseline capture/replay cadence remains surface/runtime specific.

## Rule

These are operational-evidence gaps, not missing architecture classes. Resolve by enforcement/observation rather than inventing new members or conceptual layers.
