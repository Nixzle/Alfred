# Expertise Forge

## Purpose
Turn a substantial ask into a just-in-time expertise acquisition loop before or alongside execution, so Ultron reasons from current practitioner knowledge rather than only generic model priors or narrow answer-seeking search.

This spell does not require exhaustive mastery. It acquires the smallest body of domain expertise that materially improves the current decision or implementation, then harvests reusable lessons into the Sanctum when they generalize.

## Trigger
Invoke when one or more of these apply:

- the task is substantial, technical, creative, strategic, or domain-specific;
- practitioner convention materially affects quality, speed, reliability, polish, safety, or maintainability;
- the field has fast-moving tools, workflows, skills, MCPs, plugins, frameworks, communities, or production practices;
- the user asks for best practices, peak condition, expert-level reasoning, current workflows, or broad capability improvement;
- prior work exposed a discovery miss or an obvious source/tool/community was supplied later by the user;
- the task would benefit from knowing not only `what is the answer?` but `how do strong practitioners actually do this?`.

Do not invoke for trivial factual asks or bounded fixes where domain immersion would add more latency than value.

## Procedure

### 1. Define the expertise target
State the current ask and the practitioner capability classes that could materially improve it.

### 2. Build the first question set
Before searching, generate the highest-value questions an experienced practitioner would want answered before acting. Cover, when material:

- first principles and fundamentals;
- current standard practice;
- alternatives and trade-offs;
- common failure modes;
- real-world constraints;
- measurable success criteria;
- tools/skills/workflows used by strong practitioners;
- current evidence or data that should drive the decision;
- unknown assumptions that could invalidate the plan.

Questions are a research plan, not a questionnaire for the user. Cerebro should answer what it can from evidence first and only ask the user when the missing information is genuinely user-specific or preference-dependent.

### 3. Search both the problem and the profession
Run two parallel research lenses.

**Answer lens**
- direct evidence for the current ask;
- official documentation;
- current APIs/specifications;
- primary technical references;
- empirical data, benchmarks, measurements, postmortems, or runtime evidence when material.

**Expertise lens**
- `best practices for <domain>`;
- `best workflow for <domain>`;
- `best skills/tools/plugins/MCPs for <domain or agent>`;
- `how experienced practitioners use <tool>`;
- `mistakes / failure modes / postmortems`;
- active practitioner communities and discussion hubs;
- open-source exemplars, templates, harnesses, skills, and automation;
- shipped products, devlogs, benchmarks, and production reports where relevant.

Search outside the user's phrasing and include adjacent practitioner vocabulary.

### 4. Run the Expert Question Loop
Research proceeds iteratively rather than as one search pass:

`questions -> evidence -> synthesis -> uncertainty -> better questions -> evidence`

After each meaningful round, Cerebro should:

1. answer the current question set with sourced evidence;
2. separate established facts, practitioner convention, contested claims, assumptions, and unknowns;
3. identify contradictions or evidence gaps;
4. generate the next highest-value questions that could materially change the decision or implementation;
5. rank those questions by expected information value;
6. research the highest-value unresolved questions first;
7. stop asking variants of questions whose answers are already stable unless new evidence challenges them.

The loop may run many iterations when the task warrants it. The objective is not a fixed number of rounds. The objective is **decision sufficiency**: enough grounded knowledge that the remaining uncertainty is unlikely to change the chosen route enough to justify more research.

For foundational/high-consequence work, deliberately include adversarial questions such as:

- What would make this recommendation wrong?
- What do experienced practitioners disagree about here?
- What evidence would falsify the favored approach?
- What hidden constraint tends to appear only after implementation begins?
- What simpler approach produces the same outcome?
- What failed projects or postmortems contradict the success stories?

### 5. Maintain an Evidence Ledger

For decision-driving claims, record the source actually opened, the relevant section,
source family, direct support versus inference, freshness evidence for current claims,
and the material limitation. A source count is not a count of independent evidence.
Use the small receipt contract in `../runtime/RESEARCH_QUALITY.md` for substantial
runs. Structural checks do not establish semantic support.
For material Expertise Forge runs, preserve a compact evidence model containing:

- claim/question;
- evidence/source class;
- freshness/date where relevant;
- confidence;
- independent versus correlated evidence;
- supporting and contradicting evidence;
- decision impact;
- unresolved uncertainty.

Prefer measurable evidence over rhetoric where measurable evidence exists. Practitioner opinion is useful evidence of practice and failure modes, but should not be presented as controlled empirical proof.

When recommendations depend on numeric thresholds, performance, cost, conversion, retention, latency, balance, or reliability, seek actual measurements when practical instead of guessing from prose.

### 6. Build a compact capability map
Classify useful findings into capability classes rather than accumulating links:

- knowledge/fundamentals;
- reusable workflow;
- tool/integration;
- skill;
- test/eval method;
- observability/debugging method;
- production/polish technique;
- failure pattern;
- community/source worth revisiting.

### 7. Challenge the shiny tools
Do not adopt a skill, MCP, plugin, framework, or workflow because it exists or is popular. Evaluate necessity, provenance, maintenance, authority/security surface, context/token/latency cost, compatibility, practitioner evidence, simpler alternatives, and failure reports.

Prefer the smallest mechanism that improves the task. `No new tool` is a valid outcome.

### 8. Apply just in time

Record the baseline, technique applied, actual task change, result evidence and
limitation for each material adoption. Distinguish proposed, tested and rejected
applications. One successful task does not establish general expertise. Prefer a
small comparative task or labeled failure case over a larger reading list.
Use the newly acquired expertise to improve the current plan, implementation, critique, test strategy, or decision immediately when useful. Important recommendations are classified as `IMPLEMENT NOW`, `SCHEDULE`, `WATCH`, or `REJECT`.

The final recommendation should make the reasoning auditable at the decision level: what evidence mattered, what alternatives were rejected, what uncertainty remains, and what would change the decision. Do not expose or retain unnecessary chain-of-thought transcripts.

### 9. Harvest durable value
Promote only material generalizable lessons:

- durable knowledge/fundamentals -> Archive candidate;
- repeatable beneficial trajectory -> Spell candidate or existing spell upgrade;
- distinct active responsibility -> member candidate only if the admission rule is met;
- reusable tool procedure -> skill/integration guidance;
- repeated/material failure -> Web regression;
- project-specific fact -> project state;
- noisy or weak finding -> reject or keep only as research evidence.

Do not convert every useful link into doctrine. The Sanctum should become more capable, not merely heavier.

### 10. Preserve a coverage receipt
For substantial runs, retain a compact record of:

- source classes checked;
- practitioner ecosystems checked;
- capability classes considered;
- expert-question rounds completed;
- high-value findings adopted/rejected;
- material contradictions/gaps;
- inaccessible sources;
- what changed in execution because of the research.

## Stop condition
Stop when additional research is unlikely to change the current plan, capability selection, acceptance criteria, or risk posture enough to justify its cost.

A useful stopping test is:

- the top unresolved questions have low expected decision impact;
- independent evidence lines broadly support the selected route;
- important counterarguments have been checked;
- material uncertainty is explicit and tolerable;
- the next best research round is less valuable than executing and measuring the real system.

Resume when execution exposes a blocker, a milestone reveals a new capability need, a practitioner source exposes an unknown unknown, tool/provider state changes, the user supplies an obvious missed source, new empirical evidence appears, or a meaningful failure suggests the expertise model was incomplete.

## Failure conditions
Fail if research only answers the literal question and never checks practitioner methods; performs one shallow search pass on a foundational task; generates many questions without prioritizing or answering them; treats repeated community opinion as independent data; adopts tools/skills/MCPs without simpler comparisons; misses obvious domain communities or workflow resources during an apparently comprehensive sweep; produces a reading list with no effect on execution; repeatedly rediscovers reusable lessons; or indiscriminately promotes every discovered resource.

## Relationship to other mechanisms
- **Cerebro** performs discovery, iterative questioning, and evidence gathering.
- **Scout First** inspects project/runtime terrain.
- **Council of Reeds** challenges consequential recommendations and fashionable consensus.
- **TVA** checks timeline and scope divergence where implemented; actual user/tool/runtime controls govern authority for integrations.
- **Watcher** measures cost, latency, failure, and usefulness where observable.
- **Web of Destiny** evaluates whether adopted methods improve outcomes.
- **Failure Harvest** captures lessons when the expertise route misses something.

Frontier discovery asks `what exists and what are we missing?`; Expertise Forge asks `what must we learn or adopt now to perform this task like a strong practitioner?`.

## Example: Co-Op Leveling
For a substantial Co-Op Leveling milestone, Expertise Forge may iterate through questions such as:

- What player experience is this milestone supposed to improve?
- What do successful co-op/autobattler games do here, and why?
- What failure modes repeatedly appear in similar games?
- What does current Godot/C# practice recommend?
- What do AI-game-development practitioners actually use for this workflow?
- Would Codex skills, plain CLI/headless Godot, or an MCP shorten the feedback loop most reliably?
- What runtime evidence proves the feature feels and behaves correctly?
- What polish problems will become expensive if deferred?
- What data should we collect during playtests?
- What would make the chosen architecture wrong?

Cerebro may run several rounds until the milestone has a strong evidence-backed foundation, then execution proceeds and real runtime/player data becomes the next evidence source.
