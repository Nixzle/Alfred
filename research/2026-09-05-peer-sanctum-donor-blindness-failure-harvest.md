# Failure Harvest — peer orchestration donor blindness

Date: 2026-09-05

## Failure

While evolving Sanctum, Ultron and Cerebro searched broadly across agent engineering, game development, tooling, communities, and adjacent implementation domains, but did not routinely treat **other agent operating systems, orchestration frameworks, memory runtimes, second-brain systems, and prompt/agent playbooks as a donor ecosystem for Sanctum itself**.

The user had to explicitly ask whether useful ideas could be taken from other people's "Sanctums". That surfaced checkpoint/fork state, memory defragmentation, transient-to-durable promotion, explicit context inheritance modes, deterministic-step-first workflows, and stronger versioned-memory ergonomics.

## Why it happened

1. **Object-level bias.** Cerebro searched for solutions to active tasks but did not consistently inspect systems solving the same meta-orchestration problem as Sanctum.
2. **Taxonomy confidence.** Because Sanctum already had named members, planes, spells, Archives and governance, the search implicitly assumed the architecture was broad enough and focused on filling known gaps.
3. **Peer-framework avoidance.** Prior doctrine correctly warned against importing giant fashionable agent frameworks, but that caution generalized too far into under-inspecting them as pattern donors.
4. **Unknown-unknown weakness at the meta layer.** Cerebro's frame-breaking loop expanded by domain, but not reliably by **peer operating system / orchestration architecture** when Sanctum itself was the object being improved.
5. **Premature internal sufficiency.** Existing adjacent doctrine made missing ergonomics look like implementation detail rather than capability gaps.

## Generalizable correction

When the system being improved is itself an orchestration, research, memory, workflow, agent, or operating framework, Cerebro/Meta-Cerebro should explicitly inspect **peer systems solving the same coordination problem** before concluding the capability landscape is understood.

The sweep should ask:

- Which peer frameworks solve this same orchestration/memory/state problem differently?
- What capabilities do they treat as first-class that Sanctum currently treats as implicit?
- Which of their mechanisms reduce state loss, memory entropy, coordination cost, tool misuse, recovery time, or context pollution?
- Which patterns can be absorbed without importing the whole framework?
- What are their maintainer/community-reported scars and trade-offs?
- Are we rejecting a useful idea merely because its host framework is overbuilt for us?

This is `Salvage First` applied to Sanctum itself.

## Corrections

- Added `archives/state-memory-orchestration.md` covering checkpoint/fork, memory defragmentation, transient-to-durable promotion, worker context modes, deterministic-step-first orchestration, and versioned-memory use.
- Update Cerebro/Meta-Cerebro doctrine to include peer-system donor sweeps when Sanctum or another orchestration framework is itself under review.
- Add a regression so future meta-research that only inspects papers/tool primitives but skips peer operating systems is incomplete.

## Regression expectation

Given a request to improve Sanctum, an agent OS, second-brain system, orchestration framework, or durable-memory architecture, Cerebro should inspect at least one credible peer implementation class and extract both useful mechanisms and failure/maintenance evidence before concluding the design space is covered, unless a recent sufficient peer-system sweep is already fresh and reusable.
