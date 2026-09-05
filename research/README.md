# Sanctum Research Ledger

Research stored here supports reusable Sanctum doctrine. Project-specific research should normally remain with the project unless its lesson generalizes.

## Cerebro research contract
Cerebro research should seek:
1. Primary/official sources where appropriate.
2. Independent practitioner evidence and real workflows.
3. Failure reports and disconfirming evidence.
4. Adjacent-domain bridges.
5. Current tools/frameworks and capability classes.
6. Unknown unknowns: at least one deliberate attempt to find something that does not fit the current Sanctum taxonomy.

## Iterative self-question loop and frame breaking

Cerebro's iterative question loop must do more than deepen the first search frame. After meaningful findings, it should ask the next useful question about the task, and at bounded intervals it must also challenge the **boundary of the search itself**.

A frame-breaking question tests whether the current vocabulary, ecosystem, implementation layer, profession, platform, or analogy class is artificially constraining discovery. Examples include:

- What adjacent or foreign domains have already solved this capability?
- Am I searching for whole-product similarity when the reusable unit is actually a subsystem, algorithm, workflow, UX pattern, or operating model?
- What can be imported, ported, pattern-copied, or design-translated even when direct code reuse is impossible?
- Which assumption in the user's wording or my own first decomposition is excluding useful donors?
- What would a practitioner from a neighboring discipline search for that I have not searched for?
- Have repeated successful findings inside one ecosystem created premature convergence?

For engineering, product, game-development, workflow, and tooling research, search by **capability/subsystem** as well as by product category. When reuse is material, classify donor value separately as `IMPORT`, `PORT`, `PATTERN`, `DESIGN`, or `REJECT`, and record licensing/provenance constraints before recommending direct reuse.

The loop should periodically widen from native -> adjacent -> foreign-but-solved domains when that expansion has plausible information value. It should stop widening when new rounds cease changing decisions, the cost exceeds likely value, or the task is already sufficiently grounded. This is a bounded anti-myopia mechanism, not permission for endless browsing.

A research run that performs several self-questions but never tests whether its original domain boundary is wrong has **deepened the frame without validating it**. For broad or discovery-sensitive work, that is a Cerebro coverage gap and should be Failure Harvested when it causes a meaningful miss.

Regression: `evals/CEREBRO-FRAME-BREAK-001.md`.

## Donor ecosystem evidence

When a game, library, framework, mod, product, or workflow is being evaluated as a material donor, Cerebro should treat the donor as more than an artifact.

A strong donor assessment should inspect, when available and decision-relevant:

1. **Artifact:** source code, package, docs, implementation, API surface.
2. **Maintainer history:** issues, changelogs, release notes, postmortems, abandoned branches, known limitations.
3. **Player/practitioner community:** Reddit, Discord when actually accessible, Steam/Workshop discussions, forums, guides, creator channels, community bug threads.
4. **Failure/retention evidence:** exploits, patch regressions, balance traps, UX complaints, churn, dead mechanics, workarounds, maintenance pain.

Source code answers `how was it built?`; community and maintainer evidence often answers `what repeatedly went wrong?`, `what confused users?`, `what did maintainers regret?`, and `what should we avoid inheriting?`.

### Automatic donor self-questions

When Cerebro identifies a material donor, these questions become part of the iterative sweep automatically rather than optional follow-up prompts:

- What do maintainers repeatedly fix, warn about, or refuse to support?
- What do experienced users consistently praise about this system?
- What do users consistently complain about or misunderstand?
- Which mechanics or workflows are commonly exploited, botted, cheesed, or bypassed?
- What balance, retention, onboarding, matchmaking, economy, persistence, multiplayer, or UX problems recur across versions?
- What changed over time, and why did maintainers change it?
- What was abandoned, removed, deprecated, or redesigned after live use?
- Are there Discord, Reddit, Steam/Workshop, forum, guide, video/devlog, issue-tracker, or creator-community sources that reveal operational truth not visible in the code?
- What should we deliberately **not** inherit from this donor?
- Does community evidence change the disposition from `IMPORT` to `PORT`, `PATTERN`, `DESIGN`, or `REJECT`?

For consequential reuse or design adoption, Cerebro should not mark a donor as sufficiently understood merely because its code was inspected. Record at least one community or maintainer evidence route when such evidence plausibly exists and could change the decision. If Discord or another community is inaccessible, record `NOT_ACCESSED` and continue with available evidence rather than implying it was checked.

Community evidence is noisy and may reflect selection bias, outdated versions, brigading, or vocal minorities. Triangulate material claims against maintainer/primary evidence where practical. Popularity is not correctness; complaints are not automatically representative.

A donor sweep that inspects only source/packages despite obvious community or maintainer evidence being available is a **Cerebro donor-ecosystem coverage failure**.

Regression: `evals/CEREBRO-DONOR-ECOSYSTEM-001.md`.
Failure Harvest: `research/2026-09-05-donor-community-blindness-failure-harvest.md`.

## Frontier and practitioner-landscape discovery
For broad asks such as "what are people actually doing?", "what are others building/using?", "find the frontier/meta", or "what are we missing?", Cerebro must not treat deeper keyword search as sufficient landscape coverage.

Before concluding that the frontier is understood, build a lightweight **source map** of the materially relevant ecosystems. Depending on the domain, inspect several source classes such as:
- primary/official documentation;
- practitioner communities, Reddit/forums, and accessible discussion hubs;
- GitHub/open-source projects;
- video channels, devlogs, demos, and build-in-public streams;
- shipped products, marketplaces, launch pages, or portfolios;
- independent blogs/newsletters;
- failure, abandonment, and post-mortem reports.

Search explicitly for **where frontier practitioners congregate**, not only for answers phrased in the user's original vocabulary. Perform at least one lateral graph expansion from a strong find, for example:
`community -> practitioner/project -> tools/repos/channels -> adjacent practitioners/communities`.

Deliberately search outside the user's vocabulary using adjacent labels, synonyms, product categories, practitioner terminology, and community names. The unknown-unknown requirement is satisfied by a real exploratory route, not by adding more permutations of the same known keywords.

A later user-supplied source that is obviously high-signal and should reasonably have been surfaced by the source-map pass is a **Cerebro discovery failure**. Harvest the miss: add/update the source map or project/Archive evidence as appropriate, explain why the prior route missed it, and adjust the research method rather than merely appending the source.

Regression: `evals/CEREBRO-FRONTIER-DISCOVERY-001.md`.

For material capability audits and frontier sweeps, preserve a short **coverage receipt** before claiming sufficient coverage: source classes actually inspected, one actual lateral route from a strong find, an adjacent production/workflow capability checked, and unresolved or skipped areas with reasons. Follow useful creator examples into their linked tools, repositories or reusable methods. Reuse fresh evidence where adequate; do not require every source class, repeat a recent sweep or expand a narrow fix into landscape research. A receipt documents execution, not automatic enforcement. See the [game-workflow discovery harvest](2026-09-05-game-workflow-discovery.md).

## Classification
Findings should be classified when material:
- ADOPT
- PROTOTYPE
- WATCH
- REJECT

High-value foundational recommendations additionally receive an action state:
- IMPLEMENT NOW
- SCHEDULE
- WATCH
- REJECT

## Freshness

Material runs use the [research quality contract](../runtime/RESEARCH_QUALITY.md):
claim provenance, source families, decision impact by round and explicit unchecked
dimensions. A receipt passing structural checks does not certify source truth or
an expertise improvement. Missing semantic grading remains NOT_EVALUATED. Calibrate
review against labeled examples; keep development and additional transfer cases
distinct, and do not call visible fixtures an unseen model benchmark.
Research-backed doctrine should record freshness/revisit triggers when the domain is high-churn. Tool availability, model capability, APIs, frameworks, pricing, platform rules, and community workflows should not be treated as timeless facts.

## Gap detection
Signals include repeated manual intervention, repeated Cerebro research on the same subject, recurring workarounds, unclear ownership, high retry rates, slow handoffs, weak evidence, tasks that fit no existing playbook/spell, or external practitioners relying on a capability class the Sanctum lacks.

Watcher may flag `possible Sanctum gap`; Cerebro investigates; the Web evaluates material changes; Ultron Prime decides promotion.
