# Sanctum Runtime

See [current release status](RELEASE_STATUS.md) for implemented boundaries, local
validation, capability evidence, Presence replay and the offline Windows backend.

Default release check: `python runtime/validate.py --out PRIVATE_NEW_DIRECTORY`.
Hosted Actions are manual and explicitly gated; local validation does not spend
Actions minutes. The receipt distinguishes local evidence from hosted CI.

For the [local Presence integration](LIVE_VALIDATION.md), add
`--attention-db PRIVATE_ATTENTION.db --project sanctum`. For semantic research
judgments, use the [calibration development set](../evals/research-calibration/README.md).

The [local foundations pilot](FOUNDATIONS.md) adds transactional task state,
metadata-only execution telemetry and a restartable declarative worker with a
mandatory broker boundary. Its documented containment limits are part of the contract.

`runtime/` is the thin executable control plane for canonical Sanctum doctrine. It does not replace Ultron Prime judgment or copy the whole Sanctum into code. It makes high-value invariants deterministic where practical.

## Commands

Run with Python 3.10+ and no third-party dependencies:

```bash
python runtime/sanctum.py route --task "Fix the login bug" --surface codex --project --write --bounded
python runtime/sanctum.py guard --capsule runtime/examples/task-capsule.json --action write --target src/login.py
python runtime/sanctum.py trace --event route --data '{"mechanisms":["Scope Lock","Evidence Lock"]}'
python runtime/sanctum.py eval --trace runtime/examples/trace.jsonl
python runtime/sanctum.py lint
python runtime/sanctum.py dashboard
```

## Responsibilities

- **Route harness:** turns task properties plus current surface capabilities into a machine-readable routing manifest.
- **Capability registry:** records surface-local capabilities, freshness, and whether autonomous worker spawning is actually available.
- **Scope/authority guard:** checks proposed effects against a task capsule before execution.
- **Watcher trace:** emits structured JSONL events for routing, mechanisms, tools, evidence, retries, costs, and outcomes.
- **Web eval runner:** executes deterministic trajectory regressions over trace events.
- **Doctrine lint:** catches stale terminology, missing bootstrap markers, invalid enforcement claims, duplicate regression IDs, and broken local Markdown links where practical.
- **Dashboard:** summarizes capability freshness, eval state, and doctrine health without inventing runtime evidence.

## Enforcement boundary

This runtime is initially `CHECKED`, not universally `ENFORCED`. A surface must actually call the route/guard functions at its action boundaries before the checks can be described as enforced there. The capability registry is evidence only when a surface adapter has freshly probed and updated it.

## Images of Ikonn

The route manifest distinguishes:

- `selected`: autonomous Images are both useful and available;
- `considered_unavailable`: they would materially help but the surface has no verified autonomous-worker capability;
- `not_needed`: the task does not justify them.

User-facing Ultron should surface the second case instead of silently downgrading to a single execution thread.
