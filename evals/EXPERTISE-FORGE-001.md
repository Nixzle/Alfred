# EXPERTISE-FORGE-001

## Purpose
Prevent substantial domain work from using narrow answer-seeking research when current practitioner expertise, workflows, skills, tools, empirical evidence, or failure reports would materially improve execution.

## Trigger
Use when the task is substantial, domain-specific, fast-moving, or explicitly asks for expert-level reasoning, best practices, peak condition, or capability improvement.

## Expected behavior
A qualifying route should:

1. identify the expertise target relevant to the ask;
2. generate an initial set of high-value practitioner questions before searching;
3. research direct evidence for the problem;
4. separately inspect how competent practitioners approach the class of problem;
5. check materially relevant capability classes such as workflows, skills, CLI tools, MCPs/plugins, test/eval methods, communities, open-source exemplars, and postmortems;
6. search outside the user's exact phrasing and inspect at least one credible practitioner ecosystem when accessible;
7. after each meaningful round, identify contradictions, uncertainty, and the next highest-value questions;
8. rank follow-up questions by expected decision impact rather than asking everything equally;
9. seek empirical data, benchmarks, measurements, runtime evidence, or postmortem evidence where those are more decision-relevant than opinion;
10. distinguish independent evidence from repeated/correlated community claims;
11. compare fashionable/heavy tools against simpler alternatives and record meaningful counterevidence;
12. apply useful findings to current execution rather than returning only a reading list;
13. classify reusable lessons into Archive/spell/member/eval/project-state destinations without promoting every discovered link;
14. preserve a compact coverage/evidence receipt for substantial runs;
15. stop when top unresolved questions are unlikely to change the plan enough to justify more research, then prefer executing and measuring the real system.

## Failure cases

### Literal-answer trap
**Input:** `Best way to use Codex for game development?`
**Fail:** Search only official Codex docs and answer with generic planning/testing advice.
**Pass:** Also inspect current game-development practitioner workflows, Codex skills, engine-specific automation, headless/CLI versus MCP tradeoffs, playtesting/eval loops, relevant communities, failure reports, and evidence from actual use; then adapt the production route.

### One-pass expertise failure
**Input:** foundational game-development architecture decision.
**Fail:** Run a handful of broad searches once, summarize them, and call the field understood.
**Pass:** Generate a question set, answer it, expose contradictions/unknowns, create a second higher-value question set, and continue until remaining uncertainty has low decision impact or execution will provide better evidence.

### Question-volume failure
**Input:** complex unfamiliar domain.
**Fail:** Generate dozens of questions but do not prioritize, answer, or synthesize them.
**Pass:** Rank questions by expected information value, answer the highest-impact ones, prune stable/low-value branches, and spend research effort where it can change the decision.

### Evidence-quality failure
**Input:** decide between two game-development workflows.
**Fail:** Treat ten Reddit comments favoring one workflow as ten independent empirical confirmations.
**Pass:** Separate practitioner sentiment from measured evidence, trace common upstream assumptions, seek benchmarks/runtime reports/postmortems where available, and calibrate confidence accordingly.

### Skill-blind task
**Input:** substantial Codex implementation in a mature technical domain.
**Fail:** Never ask whether a current skill, reusable workflow, test harness, or CLI technique would materially improve the work.
**Pass:** Run the expertise lens, compare candidates against built-in capability and simpler routes, then use or reject them deliberately.

### Tool-collection failure
**Input:** discover useful game-development MCPs and skills.
**Fail:** Install or canonize every popular tool.
**Pass:** Evaluate provenance, maintenance, authority surface, context/token cost, runtime evidence, compatibility, failure reports, and whether plain CLI/headless workflows are better.

### User-supplied miss
**Input:** user later supplies an obvious high-signal search query, practitioner hub, skill collection, or workflow that a reasonable Expertise Forge run should have found.
**Fail:** Merely append the link.
**Pass:** Record a discovery/expertise failure, update the capability map and research route, harvest reusable value, and adjust future behavior.

## Calibration examples
For Co-Op Leveling, relevant expertise routes can include:

- traditional game-development fundamentals and postmortems;
- current `r/aigamedev` workflows;
- Godot/C# implementation and profiling;
- Codex/Claude Code agent skills and project instructions;
- Godot headless/CLI versus MCP evidence;
- automated playtesting and agent-playable game interfaces;
- UI/asset production workflows;
- shipped-game/devlog evidence and abandoned-project lessons;
- actual runtime metrics and player/playtest evidence as soon as the project can produce them.

No single source class is mandatory when inaccessible or irrelevant. The test is whether the route reasonably sought the practitioner knowledge and evidence most likely to change the task.

## Status

The local receipt/application consistency subset is now checked by
`runtime/research_quality.py` and `runtime/tests/test_research_quality.py`.
Source support, practitioner-search adequacy and actual expertise gains still need
task-relative review; passing fields does not execute the full behavioral scenario.
DOCUMENTED regression. Runtime enforcement is not implied until routing/eval code explicitly checks Expertise Forge behavior.
