# Ultron Orchestration Chat Harvest

**Status:** CANDIDATE / READY FOR PROMOTION REVIEW  
**Date:** 2026-09-04  
**Source:** ChatGPT conversation that established the early reusable Ultron multi-agent orchestration design.  
**Purpose:** Preserve every durable, generalizable orchestration insight from the source conversation so the chat can be deleted without losing useful doctrine.

## Promotion summary

Most of the source conversation has already been absorbed into current Sanctum doctrine in a stronger form. The remaining durable value is concentrated in three small promotion candidates:

1. an explicit adaptive parallelism rule;
2. an explicit competitive-solution orchestration maneuver;
3. an explicit invariant that orchestration/delegation is automatic and does not require a user activation phrase.

The old named orchestration tiers and model-specific routing rules should **not** be promoted.

---

## Already canonical or superseded by stronger doctrine

### Ultron as delegator
The source chat established that Ultron is the head delegator, not merely another worker. Current `members/README.md` already defines Ultron Prime as commander/orchestrator/decider/delegator/integration owner and gives it responsibility for intent, routing, dependency mapping, delegation, verification, and integration.

**Disposition:** ALREADY COVERED.

### Ultron Bots as bounded specialist workers
The source chat named all delegated workers `Ultron Bots` and proposed specialist roles such as Scout, Researcher, Analyst, Builder, Engineer, Designer, Critic, Auditor, Judge, and Red Team.

Current `members/README.md` already defines `Ultron Bots v2` as temporary bounded specialist roles and provides the stronger Task Capsule contract: objective, why, scope, out-of-scope, authoritative context, capabilities, acceptance contract, evidence required, and handoff format.

**Disposition:** ALREADY COVERED; current doctrine is stronger.

### Minimal-contract / clean-context handoffs
The source chat adopted the external `subagent-minimal-contract` idea: give each worker only the exact task, inputs, output, transformation/decision, and required format rather than dumping the whole parent context.

Current Bot Task Capsules and `Compact & Handoff` already preserve this principle in a more complete form, including authoritative-context scoping, material-delta handbacks, rejected decisions where necessary, freshness-sensitive assumptions, and avoidance of transcript dumps.

**Disposition:** ALREADY COVERED; current doctrine is stronger.

### Worker output is not proof
The source chat explicitly established that a Bot saying `DONE` or `PASS` does not make its result true. Important outputs require independent checking.

Current doctrine explicitly states that worker output is a claim until independently evidenced and reinforces this through Evidence Lock, fresh review, Web of Destiny, and Watcher evidence capture.

**Disposition:** ALREADY COVERED.

### Builder -> reviewer -> correction -> integration
The source chat borrowed the strongest part of subagent-driven development: a fresh worker produces the result, an independent reviewer checks specification/quality, the worker repairs defects, and the parent accepts only after review.

Current `Build -> Test -> Review -> Integrate` and `Plan -> Critique -> Build` spells already implement this pattern, including fresh-context review and bounded correction loops.

**Disposition:** ALREADY COVERED; current doctrine is stronger.

### Red-team / adversarial review
The source chat proposed Critic, Judge, and Red Team workers to attack assumptions, unsupported claims, edge cases, security flaws, and weak alternatives.

Current Ultron Bots include Red Team as a role, while `Council of Reeds` provides a richer adversarial-judgment protocol: strongest opposing case, kill shot, hidden assumptions, inversion/pre-mortem, disconfirmation, falsification conditions, and confidence recalibration.

**Disposition:** ALREADY COVERED; current doctrine is stronger.

### Parallel autonomous workers and isolation
The source chat proposed running independent tasks simultaneously and isolating worker contexts/files to reduce contamination and conflicts.

Current `Images of Ikonn v2` already provides the stronger execution model: isolated worker/runtime, competing solutions, checkpoints, retries, crash recovery, structured handback, resumable state, versioned read/write ownership, conflict detection, effect ledger, and clean termination.

**Disposition:** ALREADY COVERED; current doctrine is stronger.

### Model/tool routing
The source chat proposed routing bounded/repetitive work to lighter workers and ambiguous/architectural work to stronger reasoning workers, with Ultron retaining planning and final acceptance. It used then-current model names such as Sol/Luna/Terra as examples.

Current Ultron doctrine already says Ultron chooses models/tools/members/spells and escalates reasoning/autonomy only when justified. The model-specific names should not become doctrine because they are runtime-specific and age quickly.

**Disposition:** PRINCIPLE ALREADY COVERED; MODEL-SPECIFIC ROUTING SUPERSEDED.

### One-owner-per-file / explicit ownership
The source chat identified one-owner-per-file/component as a useful protection against parallel workers overwriting each other.

Current Bot doctrine already requires explicit write ownership/versioning for shared mutable state and requires conflicts to be surfaced rather than silently overwritten.

**Disposition:** ALREADY COVERED; current doctrine is stronger.

---

# Promotion Candidate 1: Adaptive Parallelism Rule

## Finding
The source chat stated the useful simple rule that independent workstreams should be launched in parallel rather than needlessly serialized.

Current Sanctum supports parallelism through Images of Ikonn, but the decision rule is more implicit than explicit.

## Proposed doctrine

> **Adaptive parallelism:** Independent workstreams should execute concurrently when doing so materially reduces latency or increases search/solution diversity without materially increasing coordination, state-conflict, authority, cost, or integration risk. Dependent or tightly coupled work remains sequenced. Parallelism is a means, not a goal; do not create workers merely to increase worker count.

## Suggested destination
Small addition to `members/README.md` under **Ultron Prime** or **Images of Ikonn v2**.

## Why it is useful
- makes the orchestration threshold explicit;
- prevents accidental serial execution of independent research/build branches;
- prevents performative swarms when parallelism adds overhead rather than value;
- aligns with `minimum effective force`.

## Evidence/provenance
Derived from the source orchestration research, which compared Superpowers-style parallel-agent dispatch, Sol/Luna orchestration, and practitioner reports emphasizing one independent problem domain per isolated worker.

**Status:** PROMOTION CANDIDATE.

---

# Promotion Candidate 2: Parallel Contest

## Finding
One of the strongest ideas in the source chat was to assign the same difficult or ambiguous objective to multiple independent workers, prevent cross-priming, then judge the resulting approaches against explicit criteria.

Current `Images of Ikonn v2` explicitly supports competing solutions and Council of Reeds provides adversarial evaluation, but the repeatable maneuver is not currently named or specified as a compact spell.

## Proposed spell: Parallel Contest

### Trigger
Use when:
- solution uncertainty is materially high;
- multiple substantially different approaches are plausible;
- anchoring on the first proposed solution would be risky;
- the expected value of solution diversity exceeds the added cost/latency.

Do not use for trivial tasks or where deterministic evidence already identifies the correct path.

### Maneuver
1. **Evidence Lock first when material.** Define the acceptance rubric before seeing candidate solutions so the judging criteria are not rewritten around a favored answer.
2. **Independent branches.** Give two or more Bots/Images the same outcome contract using isolated context. Do not expose one candidate's reasoning/conclusion to another before initial handback unless deliberate debate is the experiment.
3. **Require evidence.** Each candidate returns its solution, assumptions, material risks, verification evidence, and conditions under which it would fail.
4. **Independent evaluation.** Evaluate candidates against the locked rubric using deterministic proof first, structured rubric second, model judgment third. Use Web of Destiny or a fresh reviewer when the consequence warrants it.
5. **Select or synthesize.** Ultron Prime chooses the strongest candidate, combines compatible strengths where this does not create an unvalidated hybrid, or rejects all candidates and reroutes.
6. **Verify the winner.** Winning a comparison is not proof of correctness. The selected/synthesized path still passes the normal acceptance and verification gates.

### Guardrails
- Do not let candidate workers vote on their own work.
- Do not equate majority agreement between correlated models with independent evidence.
- Do not run unlimited contests; cap branches based on expected information gain and cost.
- When solutions share the same hidden assumption, use Council of Reeds/Cerebro to search outside the candidate set.

## Suggested destination
`spellbook/README.md` as a canonical functional spell if Council/promotion review agrees it is sufficiently recurring and distinct.

## Why it is useful
This packages several existing capabilities into a repeatable maneuver for high-uncertainty design, architecture, debugging, research strategy, and creative problem solving without creating a new named member.

**Status:** PROMOTION CANDIDATE.

---

# Promotion Candidate 3: Automatic Orchestration Invariant

## Finding
The source chat established a user-experience invariant: the user should not need to type `Deploy Ultron` to receive good orchestration. Ultron should inspect every ask and choose delegation/parallelism automatically when it materially helps. Explicit invocation should remain a force/attention signal, not a capability unlock.

Current bootstrap already states that no activation phrase is required, every ask receives routing preflight, and minimum effective machinery should be used. However, it does not state the delegation consequence as directly as the source chat did.

## Proposed bootstrap invariant

> **Orchestration is automatic.** The user does not need to invoke `Ultron`, `Deploy Ultron`, `Ultron Bots`, or any spell/member by name for delegation or other Sanctum machinery to trigger. Ultron Prime routes every ask and automatically invokes the minimum effective delegation, parallelism, review, research, or execution machinery when its trigger conditions are met. An explicit user invocation is a force/priority signal to consider that machinery, not a prerequisite for access to it, and never justifies fake or unnecessary orchestration.

## Suggested destination
`bootstrap/README.md` under **Core bootstrap invariants**.

## Why it is useful
- preserves the intended default behavior across ChatGPT, Codex, Discord, and future surfaces;
- prevents surfaces from degrading into magic-phrase interfaces;
- keeps explicit `Deploy Ultron` useful without making it mandatory;
- remains compatible with `minimum effective force` and the ban on fake theatrics.

**Status:** PROMOTION CANDIDATE.

---

# Rejected / superseded source-chat concepts

## Named orchestration tiers
The source chat proposed `STANDARD ULTRON`, `ULTRON DEEP`, `ULTRON COMPETITIVE`, and `ULTRON SWARM`.

These should not become canonical modes. Current `minimum effective force` doctrine is better because it scales orchestration continuously based on real task requirements rather than selecting a theatrical tier first. `Parallel Contest` preserves the one distinctive useful behavior from the old Competitive mode without bringing back the tier taxonomy.

**Disposition:** SUPERSEDED.

## Hard-coded specialist roster
The source chat listed a fixed catalogue of roles. Current Ultron Bots already treat these as examples rather than a mandatory team template. The team should remain dynamically constructed around ownership and task shape.

**Disposition:** SUPERSEDED BY BOUNDED TEMPORARY ROLES.

## Hard-coded model-family routing
The source chat used model names such as Sol, Luna, and Terra to illustrate orchestrator/worker routing. This should remain historical evidence only. Runtime profiles and model availability change; doctrine should route by capability/cost/reliability requirements instead.

**Disposition:** SUPERSEDED.

## Always-maximal agent deployment
The user initially described `deploy all of the parallel agents and things like that`. The conversation subsequently refined this into adaptive orchestration. Canonical doctrine should not require maximal worker count merely because Ultron is invoked. The correct rule is minimum effective force plus appropriate parallelism.

**Disposition:** REJECTED AS CANONICAL DEFAULT.

---

# Source-chat durable operating expectations

These expectations are either already canonical or represented by the promotion candidates above and are preserved here so deletion of the source chat loses no useful intent:

- Ultron is the delegator/orchestrator and final integration owner.
- Delegated workers are called **Ultron Bots**.
- Ultron decides team composition; the user does not need to name individual Bots.
- Simple asks should remain simple.
- Complex, multi-step, research-heavy, implementation-heavy, ambiguous, or consequential asks should trigger proportionate orchestration automatically.
- Independent workstreams should run concurrently when beneficial and safe.
- Workers should receive clean, bounded context rather than the entire parent conversation.
- Specialist ownership matters more than flashy job titles.
- Worker completion claims require evidence.
- Important work benefits from fresh independent review.
- High-uncertainty problems may justify independent competing solutions.
- Consequential work may justify adversarial review/red-team/Council behavior.
- Ultron resolves conflicts and synthesizes one coherent final result rather than dumping disconnected worker transcripts on the user.
- Explicit `Deploy Ultron` remains a valid user command, but should not be required to unlock orchestration.
- Never claim Bots/Images/research/tests/tools were deployed or run unless they actually were.
- Actual capabilities depend on the current surface/runtime profile and must be re-probed when material.

---

# Deletion safety note

This file intentionally preserves the reusable orchestration content of the source ChatGPT conversation, including the three identified gaps, the already-canonical ideas, and the concepts rejected as obsolete. The source chat is no longer required as the sole repository of any identified generalizable orchestration principle.

Deleting the source chat will still remove its conversational wording and historical transcript, but should not remove any durable orchestration doctrine or promotion candidate identified during this harvest.
