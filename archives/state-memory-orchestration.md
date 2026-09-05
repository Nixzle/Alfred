# State, Memory, and Orchestration Operations

Promoted 2026-09-05 after a peer-system donor review of agent operating systems, orchestration frameworks, and memory-centric agent runtimes.

## Principle

Reliable orchestration improves when execution state can be checkpointed and inspected, memory is actively maintained rather than only accumulated, transient context has an explicit promotion path into durable knowledge, worker context inheritance is deliberate, and deterministic operations own work that does not require model judgment.

These capabilities extend existing Sanctum members and planes. They do not create new members.

## Checkpoint and fork

For material long-running, multi-step, autonomous, or failure-prone work, preserve enough state at meaningful boundaries to answer:

- what objective and constraints were active;
- what authoritative/project state was read;
- what evidence was known;
- what actions/effects had occurred;
- what decisions were made;
- what remained uncertain;
- what operation/task/state version applied.

A checkpoint may support **resume**, **replay**, or **fork**, but those semantics must be explicit. A fork creates a new branch of work from a prior verified snapshot; it does not rewrite history or imply external effects can be undone. Before resuming or forking, revalidate freshness-sensitive external state and authority.

Watcher should record checkpoint/fork lineage when the runtime exposes it. Web of Destiny may compare branches counterfactually. TVA may prune divergent branches when a real scope/constraint decision is applied.

## Memory defragmentation

Durable memory must be maintained, not merely appended.

Periodically or when retrieval quality degrades:

1. detect duplicate or near-duplicate doctrine/facts;
2. identify overloaded entries spanning unrelated concepts;
3. consolidate one canonical location per durable fact/rule where practical;
4. split entries whose size or topic breadth harms retrieval;
5. preserve provenance and supersession links;
6. retire stale duplicates without destroying audit history;
7. rebuild or refresh indexes/retrieval pointers when the runtime supports it.

The goal is lower retrieval ambiguity and less contradictory context, not stylistic tidiness.

## Transient to durable promotion

Mindscape is transient attention, not automatic memory. Promote material experience through an explicit path:

`observation -> candidate -> review/consolidation -> durable project truth / Archive / Spellbook / eval -> reject or supersede`

Promotion criteria include future usefulness, confidence/evidence, scope, freshness, privacy, and whether the lesson is project-specific or generalizable. Repetition alone does not make a fact true. User corrections and Failure Harvests are high-signal candidates but still retain provenance and scope.

## Worker context inheritance modes

Choose context inheritance deliberately per worker/task:

- **ISOLATED** — worker receives only its Task Capsule and explicitly referenced evidence. Use for independence, adversarial review, privacy minimization, or avoiding narrative contamination.
- **PROJECTED** — worker receives a role-specific filtered projection of relevant parent/project context. Default for most specialist work.
- **FORKED** — worker receives a snapshot of the parent orchestration context when shared reasoning state materially reduces reconstruction cost or coordination risk.

Context mode does not transfer authority. Forked context remains a snapshot; mutable state must still be revalidated before commit/effect.

## Deterministic-step-first orchestration

Do not assign a model a step that a deterministic function, test, parser, policy engine, static check, query, or workflow primitive can own reliably at lower cost and uncertainty.

Prefer mixed workflows such as:

`deterministic preflight -> Ultron judgment -> deterministic retrieval/check -> specialist implementation -> deterministic tests -> Web evaluation -> deterministic release gate`

Use model judgment where interpretation, synthesis, planning, creative generation, ambiguity resolution, or counterfactual reasoning adds value. Use deterministic machinery for invariants, parsing, validation, state transitions, exact comparisons, and repeatable checks when practical.

## Git/versioned memory

Where durable memory is stored in version control, use history as an audit surface:

- identify which rule/fact changed;
- link superseded and replacement doctrine;
- recover prior state when diagnosing regressions;
- determine which projects/surfaces remain pinned to earlier semantics;
- preserve provenance instead of silently overwriting institutional memory.

This strengthens planned doctrine-provenance and compatibility automation; it does not imply every transient memory item belongs in Git.

## Failure modes

- checkpoint theatre without enough state to resume correctly;
- replaying an effectful branch as if effects were reversible;
- memory compaction that deletes provenance or historical truth;
- automatic promotion of transient speculation into canonical memory;
- forked workers silently committing against stale parent state;
- deterministic-step doctrine becoming rigid when model judgment is genuinely needed;
- memory maintenance becoming process overhead rather than retrieval improvement.

## Evidence and provenance

The peer-system review found comparable patterns in modern agent runtimes: execution checkpoint/fork semantics, dedicated memory-maintenance agents, explicit session-to-durable memory promotion, versioned memory surfaces, differentiated subagent context inheritance, and workflows mixing deterministic functions with agent steps. Sanctum already possessed adjacent doctrine but lacked a single explicit operating model tying these together.

## Revisit trigger

Revisit when Watcher evidence shows repeated resume/recovery failures, memory retrieval degradation, duplicated/superseded doctrine contamination, worker context mismatch, excessive model use for deterministic tasks, or when peer runtimes demonstrate a materially safer/simpler mechanism.
