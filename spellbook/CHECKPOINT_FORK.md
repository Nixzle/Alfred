# Checkpoint -> Resume / Replay / Fork

Use for material long-running, autonomous, multi-step, recovery-sensitive, or counterfactual work where resuming from verified state or comparing alternate trajectories would materially improve reliability.

## Trigger

Invoke when one or more apply:

- an operation may span sessions/workers;
- crash/restart recovery matters;
- a consequential decision may need later reconstruction;
- Web of Destiny would benefit from comparing alternative branches;
- retries risk duplicating external effects;
- current work may need to fork from a known-good earlier state.

## Procedure

1. Capture a checkpoint at a meaningful verified boundary.
2. Preserve objective, constraints, authoritative state/version, evidence known, completed actions/effects, operation IDs, unresolved uncertainty, and next admissible actions.
3. Declare which semantics are allowed:
   - `RESUME` — continue from the checkpoint;
   - `REPLAY` — rerun deterministic/replay-safe work for diagnosis;
   - `FORK` — create a new branch from the snapshot while preserving original history.
4. Before resume/fork, revalidate freshness-sensitive external state, authority, dependencies, and mutable versions.
5. Never treat a checkpoint as rollback of an external effect unless the real system provides verified compensation/rollback semantics.
6. Record branch/checkpoint lineage in Watcher when available.
7. Let Web compare branches when the decision value justifies it; TVA may prune a branch only when an actual scope/constraint decision is applied.

## Output

A compact checkpoint capsule and explicit resume/replay/fork decision.

## Failure modes

- checkpoint lacks enough state to resume correctly;
- stale snapshot is committed without revalidation;
- replay duplicates a non-idempotent effect;
- fork is mistaken for rewriting history;
- checkpoints are emitted so frequently that overhead exceeds recovery value.

## Theatrics

Preferred invocation: `I'm pinning this timeline before we move. If we branch, I want a clean point of return, not folklore.`
