# Agentic Software Delivery

Reusable doctrine for software delivery where one or more AI agents plan, implement, review, verify, hand off, or integrate work.

## Principle
Agentic delivery is reliable when work is deliberately bounded, canonical state is explicit, workers receive only the context and authority they need, acceptance evidence is defined before implementation, review remains meaningfully independent, and autonomy stops when its expected value falls below its coordination or risk cost.

The objective is not maximum agent activity. The objective is the smallest delivery system that repeatedly produces correct, verifiable outcomes.

## Procedure

### 1. Establish canonical task state
Before substantial implementation, identify:
- objective and user-visible outcome;
- authoritative project/repository state;
- scope and non-goals;
- hard constraints and authority boundaries;
- acceptance criteria and proof classes;
- current verified state;
- blocker and next action when incomplete.

Do not use conversation history as the sole task database when durable project state is available.

### 2. Bound the work slice
For narrow fixes or urgent work, invoke Scope Lock. Separate required work from adjacent improvements. Expand only when correctness, safety, or the acceptance contract makes expansion necessary.

For larger features, decompose by dependency and integration boundary rather than by arbitrary file count. Parallelize only work that can proceed independently without creating hidden merge or authority coupling.

### 3. Give workers task capsules, not the universe
A worker should receive the objective, relevant files/interfaces, constraints, authority, acceptance evidence, and expected handback. Avoid flooding every worker with the coordinator's entire accumulated conversation when a smaller operational context is sufficient.

Keep execution-heavy debugging detail with the worker performing the work unless it becomes material to project truth, integration, a decision, a reusable lesson, or a blocker.

### 4. Lock evidence before implementation
Use Evidence Lock to define what will count as done. Distinguish portable/unit/static evidence from runtime, integration, multiplayer, production, or human-observed evidence when those proof classes materially differ.

A passing test suite is evidence for the behavior it actually exercises, not permission to upgrade the claim beyond that scope.

### 5. Implement with bounded autonomy
Use the minimum effective autonomy level. Prefer one integration owner. When multiple workers write concurrently, isolate their work where practical and make dependencies explicit.

Retries and autonomous repair loops require a reason: changed evidence, corrected input, a different route, or a bounded transient retry. Repeating the same failed trajectory is not persistence; it is tokenized superstition.

### 6. Review from fresh enough context
For material changes, use a reviewer/integrator who can challenge the implementation rather than merely inherit the builder's narrative. Provide the task anchor, relevant artifacts, and evidence, but preserve independence when the review exists to detect design or reasoning errors.

Builder-reviewer loops must have a bounded round limit proportional to risk and cost. Persistent disagreement, repeated failure, or a lack of materially new evidence should trigger Ultron Prime resolution, rerouting, narrowing, or human escalation.

### 7. Integrate through declared gates
The finish line is the declared acceptance state. Use Ship Until Green when the task requires build/CI/review/conflict/retest loops. Do not describe a PR, generated patch, or worker completion message as shipped when required gates remain incomplete.

### 8. Handoff from verified reality
When a session or worker changes, use Compact & Handoff. Preserve the smallest state needed to continue correctly:
- objective and acceptance criteria;
- current verified state;
- changed artifacts;
- evidence and blockers;
- next action;
- files/resources to read first;
- rejected decisions worth preserving and why;
- assumptions or capabilities that must be revalidated because they can go stale.

Do not preserve debugging debris simply because generating it was expensive.

## Human checkpoint placement
Human involvement should be placed where it changes risk or judgment, not sprayed uniformly across every tool call.

Use **pre-execution checkpoints** before materially consequential, expensive, security-sensitive, irreversible, or difficult-to-reverse choices when user authority or preference is required before the effect.

Use **in-loop checkpoints** when uncertainty, conflict, scope pressure, authority ambiguity, or unexpected state crosses the task's agreed tolerance and autonomous continuation would risk solving the wrong problem.

Use **post-execution, pre-release checkpoints** when implementation may be performed autonomously but publication, deployment, merge, communication, purchase, deletion, or another consequential release action still requires human judgment or authority.

Use **sampled audit** for repetitive low-risk autonomous work where reviewing every action would add little safety but periodic inspection can detect drift, gaming, or quality decay.

Avoid approval fatigue. A checkpoint that humans routinely approve without meaningful inspection is ceremony, not control.

## Knowledge plane versus worker context
Ultron Prime should coordinate durable knowledge and integration decisions without becoming a mandatory participant in every execution detail. Workers may retain operational context locally while returning only material deltas: decisions, changed state, evidence, blockers, risks, and reusable lessons.

Promote execution detail into durable project or Sanctum state only when it has future value. This reduces context load while preserving the information needed for correct orchestration.

## Failure modes
- **Scope creep:** a bounded fix absorbs nearby cleanup or architecture work and delays the requested outcome.
- **Post-hoc evidence:** acceptance criteria are invented after implementation to match what happened to pass.
- **Narrative-contaminated review:** reviewer inherits the builder's assumptions and confirms rather than challenges them.
- **Infinite correction loop:** builder and reviewer exchange patches without a stop rule or materially new evidence.
- **Coordinator saturation:** the orchestrator receives every debugging detail and becomes the bottleneck or loses the task anchor.
- **Context amnesia:** handoff preserves a vague summary but omits authoritative files, rejected decisions, or stale assumptions.
- **Approval fatigue:** humans are asked to approve too many low-value steps and stop examining consequential ones carefully.
- **Proof inflation:** portable checks are described as runtime or production verification.
- **Parallelism theatre:** workers are spawned despite dependencies that force serial integration or duplicate effort.

## Tooling
Use repository-native task state, issue/PR metadata, CI, deterministic tests, version control, isolated worktrees/branches where useful, durable handoff artifacts, and explicit operation/task identifiers before inventing additional orchestration infrastructure.

Tool availability does not itself justify use. Prefer deterministic checks over model judgment when they can test the required property directly.

## Verification
A strong agentic delivery run should be able to answer:
- Was the requested scope preserved?
- Are acceptance criteria traceable to evidence?
- Did each worker operate within its authority and context contract?
- Was review meaningfully independent where independence mattered?
- Were autonomous loops bounded?
- Were required gates green on the exact integrated state?
- Can a new worker resume from durable verified state without reconstructing the entire conversation?
- Were human checkpoints placed at consequential decision/effect boundaries rather than everywhere?

## Evidence and provenance
Promoted 2026-09-04 after repeated Sanctum and Co-Op Leveling delivery experience exposed distinct failure classes around scope expansion, handoff continuity, completion gates, review independence, and orchestration overhead. The entry consolidates existing Sanctum doctrine and the newly promoted Scope Lock maneuver rather than creating a new member.

Project-specific incidents remain with their source projects. This Archive contains only the generalizable delivery pattern.

## Freshness and revisit trigger
Revisit when material changes occur in coding-agent execution models, repository/worktree isolation, tool permission systems, CI/evaluation practice, long-context behavior, autonomous review reliability, or human-approval interfaces.

Also revisit when Watcher or Failure Harvest identifies repeated cases where this procedure adds coordination cost without measurable reliability benefit. Subtractive revision is preferred over accumulating more stages.
