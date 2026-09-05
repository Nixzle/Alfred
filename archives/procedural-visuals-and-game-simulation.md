# Procedural Visuals and Game Simulation

Reusable production guidance for coherent code-drawn visuals and repeatable game-balance experiments. Use either section independently; a small app does not need a custom renderer or simulation platform to qualify as well engineered.

## Principle

Keep visual rules shared across outputs and keep experiments connected to the behavior actually shipped. Treat visual inspection and human playtesting as distinct evidence from structural checks and automated play.

## Procedure: visual production

1. Define a compact design specification: semantic colours, typography, line weights, spacing, visual motifs and motion. Implement it with the project's existing drawing/components first. Give decorative marks their own stable random seed so a texture or animation cannot change the generated puzzle or game outcome.
2. Give presentation a read-only view of game state. Reuse component/scene definitions for menus, boards and results; avoid separately maintained copies of the same visual system. Cache expensive static decoration where useful, while keeping text and controls responsive.
3. Build a small visual specimen covering shapes, type, state changes and clipping before expanding across screens. Fix dimensions, fonts, scale, seed and animation time for comparisons. Include a structural description when pixel changes are otherwise hard to diagnose.
4. Recompose for portrait, landscape and small icons. Check essential content remains inside safe regions and backgrounds cover intended edges. A stretched or blindly cropped screen is not an adequate composition for every format.
5. Inspect representative empty/full, enabled/disabled, selected/error/completed and accessibility states at actual output size. Automate objective properties such as missing elements, clipping and bounds when useful. Visual hierarchy, legibility and awkward composition still need inspection.
6. Fix repeated defects in shared rules, then inspect dependent outputs. Review baseline changes as intentional visual changes; do not accept a new screenshot merely because it makes a comparison pass.

### Visual limits and failure modes

- Shared styling does not guarantee good design; templates can consistently reproduce a poor choice.
- Decorative noise, wobble and motion can impair reading, accessibility and device performance. Reduced-motion behavior and clear boards take priority.
- Platform text/rendering differences can make pixel comparisons brittle. Record the environment and justify tolerances rather than silently widening them.
- A custom drawing framework or baked atlas may cost more than native components and a few static assets. Prototype the smallest representative screen before a renderer investment.

## Procedure: game simulation

1. State one falsifiable balance question and its metrics. Reuse the shipped initialization, legal-action, transition, randomness, score and termination functions. Replace presentation, input and waiting with a controlled runner. This is a simulation of the product, not a second implementation of its rules.
2. Version the executable, configuration, player policy and seed list. Keep policy decisions separate from game rules. Start with a useful limited strategy and an oracle/search upper bound where relevant; policy failure does not prove a board is impossible.
3. Compare candidate changes on paired seeds with the same policies. Preserve a baseline and change one coherent factor at a time. Inspect outliers and per-seed changes as well as averages. Bound total runs, actions and time; make nontermination visible.
4. Record enough to reproduce results: versions, seeds, outcomes, effort/score and failure reason. Capture detailed traces for anomalies, not every frame of every run. Investigate nondeterminism before interpreting a balance difference.
5. Test hard invariants separately from statistical observations. Use noisy balance results to trigger review unless a justified threshold exists. Inspect representative human play before labeling a game easy, fair or enjoyable.

### Simulation limits and failure modes

- An oracle's success measures a ceiling, not a novice experience; bot win rates do not establish human difficulty or retention.
- Changing a policy between balance variants confounds the comparison.
- Reusing production logic for simulations does not replace independent correctness validation. Independent validators deliberately provide a different route for detecting shared bugs; these two purposes are complementary.
- Small games may need only a bounded script over existing engines. Avoid a platform, benchmark farm or architecture rewrite without a demonstrated need.

## Tooling and spell routing

Prefer existing native/vector components, theme modules, fixed-state renders, seeded runners and compact reports. No imported executable, plugin, account or background job is required by this entry.

Use [Scout First, Scope Lock and Evidence Lock](../spellbook/README.md) to choose a bounded slice; use existing critique/review spells when consequence warrants them. This adds domain procedures, not another named spell. Connect puzzle work to [Procedural Puzzle App Development](procedural-puzzle-app-development.md).

## Verification

Before adoption in a project, establish the appropriate evidence:

- Same state/seed yields stable drawing instructions; decoration leaves game randomness unchanged.
- Representative renders are legible at actual device/output sizes and accessible states are covered.
- Same revision/configuration/policy/seed reproduces the simulation trace.
- The simulation calls production rules; an independently implemented validator remains distinct where needed.
- Reported claims distinguish checked structure, observed visuals, simulated results and human outcomes.

These are acceptance criteria, not checks executed by the presence of this document.

## Evidence, provenance and freshness

Promoted 2026-09-05 under the user's request to absorb two practitioner skills discovered through an AI-game-development community. Adapted from Nitzan Wilnai's pinned Procedural Game Art and Headless Game Balance guidance, including its conformance, composition and simulation-contract references. See the [source and disposition ledger](../research/2026-09-05-game-workflow-discovery.md) and retained [MIT notice](../research/notices/nitzan-wilnai-game-skills-MIT.txt).

Evidence level: DOCUMENTED, source-reviewed procedure. Both skill repositories share an author and originating project; they are not independent proof of effectiveness. No source script was executed, no skill installed, and no renderer or simulator was verified in a Sanctum consumer by this promotion. Existing project results remain project-local.

Revisit on actual adoption, upstream revision/licence changes, rendering/platform changes, simulation nondeterminism or measured overhead. Simplify or retire portions that add cost without useful evidence.
