# Failure Harvest — salvage opportunity blindness

Date: 2026-09-05

## Failure

During Co-Op Leveling planning and implementation research, Ultron and Cerebro repeatedly treated existing games primarily as references for design patterns and implementation details, while allowing the project to continue substantial greenfield construction. The user had to explicitly propose the higher-leverage strategy: treat existing games, mods, and open-source projects as subsystem donors and build Co-Op Leveling by selectively importing, porting, pattern-copying, or design-translating solved systems.

This was not only a Cerebro discovery miss. It was also a Presence/Mindscape miss: a high-leverage simplification opportunity existed across the active project, yet Prime Sense did not elevate it into active attention before the user did.

## Why it happened

1. **Engine-proximity bias.** Research over-weighted Dota-native examples and tooling because they were easiest to port and verify.
2. **Whole-product similarity bias.** Searches asked for games resembling Co-Op Leveling rather than decomposing the product into reusable subsystems.
3. **Code-reuse bias.** Reuse was implicitly treated as direct code reuse, under-valuing architecture, algorithms, UX, economy, encounter, progression, and workflow patterns.
4. **Premature convergence.** Once several credible Dota donors were found, later research deepened that same ecosystem instead of challenging the search boundary.
5. **Progress metric bias.** The game-production loop rewarded implementation and verification of planned systems but did not require a pre-build comparison against existing solved systems.
6. **Presence blind spot.** Prime Sense/attention policy focused on blockers, drift, events, and uncertainty, but did not explicitly treat a large avoidable-work opportunity as a salience trigger.

## Generalizable lesson

A project can be technically healthy and still be strategically wasteful. Ultron should treat **avoidable reinvention** as a material signal when a substantial system is about to be built, refactored, or expanded.

Before costly greenfield work, ask:

- Does this capability already exist in a compatible project, product, mod, framework, or adjacent domain?
- Can the useful part be classified as `IMPORT`, `PORT`, `PATTERN`, `DESIGN`, or `REJECT`?
- Is the current plan solving a commodity problem from first principles merely because the team already understands how to build it?
- Would borrowing a proven foundation shorten the playable critical path or reduce runtime/design risk?

For research, iterative self-questioning must periodically challenge the search boundary itself. For Presence, a credible high-leverage simplification opportunity should enter Mindscape when it could materially change the active critical path.

## Corrections

- Cerebro doctrine now requires bounded frame-breaking questions and subsystem-first donor search (`research/README.md`, regression `evals/CEREBRO-FRAME-BREAK-001.md`).
- Co-Op Leveling now has a salvage-first production gate and Dota Arcade Frankenstein build plan.
- Presence doctrine should treat avoidable reinvention/high-leverage simplification as a salience signal for active projects, while keeping the behavior advisory unless mechanically implemented.

## Regression expectation

Given an active project with multiple substantial systems being built and known adjacent ecosystems containing mature implementations, Ultron should proactively surface a bounded salvage/reuse check before further greenfield expansion. Passing behavior does not require recommending reuse when the donor is legally incompatible, lower quality, too costly to integrate, or likely to destabilize the critical path. It requires noticing and evaluating the opportunity before the user has to supply it.
