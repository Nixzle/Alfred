# Procedural Puzzle App Development

Reusable guidance for daily or on-demand logic/spatial puzzle apps, including collections with low editorial overhead.

## Principle

Treat correctness, human reasoning, interaction quality, device reliability and commercial demand as separate claims requiring separate evidence. Deterministic generation removes manual board production; it cannot establish enjoyment, retention or income.

Prefer one complete, tested playing experience before multiplying engines or features. Share navigation, saves, accessibility and measurement where that lowers maintenance, while preserving each game's interaction needs. Use [Consumer App Portfolio Operations](consumer-app-portfolio-operations.md) for attention-adjusted economics and [Agentic Software Delivery](agentic-software-delivery.md) for bounded execution.

## Procedure

### 1. Define the game and evidence contract

Record intended player, rule, session-length target, platform, daily/practice behavior, scoring policy and operational budget in project state. Compare a small set of mechanics on learnability, replay space, generation, accessibility, scoreability and maintenance. Precommit project-specific comprehension, completion, return and support gates; do not inherit universal numeric thresholds from another app.

Scout maintained implementations and free substitutes. Assess actual licence scope, provenance, integration cost and controls; source permission does not imply permission to reuse branding or store graphics. Free substitutes can validate feasibility while weakening commercial differentiation.

### 2. Build and verify the generator contract

Specify rules, valid states and whether a unique final solution is required. Games with multiple valid solutions or move sequences need an appropriate alternative correctness contract.

Keep an exact validator or bounded solver. Test varied seeds, difficult cases, impossible inputs and deliberately ambiguous cases where applicable. Use independent enumeration, solvers or property checks where shared implementation errors could invalidate the primary check. Bound search/generation retries, measure tail latency on target devices and define failure/fallback behavior.

Define time-zone policy and stable puzzle identity including game, generator version and seed/date. Preserve old boards and compatible saves when generation, rules or scoring change. Use fixtures to catch accidental output changes. Different seeds need not yield distinct boards: measure logical repetition separately from cosmetic variation.

### 3. Separate exact solving from human deductions

Document techniques inferable from visible clues. An explanation hint should return premises, rule and conclusion, then verify that the conclusion follows. Handle contradictory player entries honestly; do not describe a stored-answer reveal or search guess as a logical deduction.

An explanation-producing solver can support technique-based generation and difficulty estimates. Keep exact correctness checks distinct from those estimates. Clue counts, empty cells and search nodes are heuristics until calibrated with players. Technique-limited generation can become expensive or repetitive; profile acceptance rate and use an approach proportionate to the game.

### 4. Complete the interaction loop

Specify entry, optional interactive teaching, selection, input, marks/notes where useful, mistake feedback, undo, hints, completion and saved return. Separate tutorial/practice from scored daily activity when fairness requires it. Measure comprehension and unassisted completion separately from assisted success.

Create reusable visual rules for readable type, clues, touch targets, selected/error states, larger text and non-colour cues. Decorative previews should not obstruct assistive navigation. Verify actual boards with screen readers and on small devices. Artwork production is optional; add assets or feedback when they improve the intended experience.

### 5. Define scores and measurement precisely

For normalized scores, document bounds, reference effort, penalties, assistance, undo/restart and repeat-attempt policy. A shared 0–100 range does not make games comparable. Version material changes. Spoiler-free shares should disclose assistance without exposing solutions; share intent is not proof of delivery or acquisition.

Distinguish app foreground sessions from screen mounts, starts from resumes, and daily play from practice. Define lifecycle deduplication, date boundaries, cohort eligibility and denominators. Keep eligible non-returners in retention denominators. Local export pilots need participant-level reconciliation and missing-export handling; exports alone do not provide valid retention estimates.

Use minimal purpose-bound events, appropriate retention, opt-out and deletion. Investigate existing native lifecycle signals before new infrastructure. A callback is not itself analytics; verify session semantics across native and browser surfaces separately.

### 6. Validate the device and operating model

Distinguish unit tests, bundle exports, installed development builds and release behavior. Choose a reproducible signing/install route. Verify offline relaunch, interruptions, background/resume, persistence, sharing, accessibility and migrations on the target platform. Define recovery and release checks proportionate to the product.

Inspect difficulty distribution, repetition and generation costs before adding editorial content. Retention, acquisition, support effort and payment conversion require their own evidence. For a retention-first product, defer monetization until agreed gates hold; this is not a universal requirement for every business model.

## Spell routing

Apply existing [spells](../spellbook/README.md) selectively:

| Spell | Application |
|---|---|
| Scout First | Code, references, reuse and integration risks |
| Scope Lock + Evidence Lock | One player-visible improvement and required proof |
| Plan -> Critique -> Build | Consequential interaction/architecture choices |
| Build -> Test -> Review -> Integrate | Material implementation and save/interface changes |
| Ship Until Green | Remaining declared checks, including device/player evidence when required |
| Council of Reeds | Consequential build-versus-reuse, catalog or commercial decisions |
| Compact & Handoff / Failure Harvest | Durable verified state and reusable corrections |

This is a domain application of existing spells, not a new spell or a requirement to run every mechanism. Reading it does not establish independent review or runtime enforcement.

## Failure modes

- Uniqueness tests presented as proof of fun or calibrated difficulty.
- Answer reveals presented as explanations; incorrect player entries treated as valid premises.
- Unbounded generation or averages hiding device stalls.
- Cosmetic changes presented as new logical content.
- Generator/scoring edits silently changing saved boards or immutable results.
- Catalog expansion hiding poor comprehension or excessive maintenance.
- Screen mounts counted as return visits; non-returners removed from denominators.
- Portable exports presented as native verification.
- Source licences generalized to all artwork or blanket IP clearance.
- Project-specific business thresholds promoted as industry benchmarks.

## Tooling and verification

For coherent procedural visuals or difficulty experiments, consult [Procedural Visuals and Game Simulation](procedural-visuals-and-game-simulation.md). Its production-logic runner measures shipped behavior; independent validators still serve a different correctness purpose. Neither simulation nor visual conformance establishes retention.

Use seeded generators, bounded exact solvers, deduction traces where justified, independent checks, fixtures, device profiling, accessibility tools and observed playtests. Architecture determines tools; no framework/service is mandatory.

Use the [puzzle evidence regression scenarios](../evals/PUZZLE_APP_EVIDENCE.md). These are documented scenarios, not executed product/model evaluations. Attach actual generator, device, usability and cohort evidence before marking corresponding project claims checked or observed.

## Evidence and provenance

**Promotion:** PROMOTED on 2026-09-05 by Ultron Prime under the user's request to preserve the preceding research. A puzzle-app capability audit exposed a gap between exact generator tests and human/device/product evidence. Private project state, conversation content, budgets and numeric outcome gates remain project-local.

The review selected domain guidance as the smallest useful destination. Existing spells cover orchestration; there is no repeat-success evidence for another named spell. Counterexamples retained include games permitting multiple solutions, technique-generation costs and free substitutes undermining a catalog-based profit thesis. A complete reference experience is a delivery recommendation, not a measured retention intervention.

Primary references inspected during the originating 2026-09-04 research:

- Simon Tatham, [writing a puzzle](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/devel/writing.html) and [Net solver development](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/net-solver/): generation, fairness and reasoning techniques. The developer page was read during research; its promotion-time refresh timed out. This is not a current source-code audit.
- Chris Boyle, [Android puzzle collection](https://chris.boyle.name/projects/android-puzzles/): offline generated collection and free substitute, refreshed during promotion. Its [source licence](https://github.com/chrisboyle/sgtpuzzles/blob/main/LICENCE) was inspected in the originating research; extra store graphics are excluded. No component was integrated or certified here.
- Apple, [onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding): brief interactive teaching/contextual guidance, not a measured learn-time guarantee.
- React Native, [AppState](https://reactnative.dev/docs/appstate): native lifecycle signals; session semantics remain a project responsibility.
- Expo, [iOS device development builds](https://docs.expo.dev/tutorial/eas/ios-development-build-for-devices/): one build route subject to current signing/account requirements, not the only route.

**Evidence level:** DOCUMENTED, source-supported procedure. Implementation, commercial success, licensing fitness and device reliability require separate verification. No global authority, runtime enforcement or project compatibility pin changes.

## Freshness and revisit trigger

Revisit before code reuse, signing-service selection, lifecycle API changes, puzzle size/difficulty expansion, daily identity/scoring changes or commercial claims. Simplify if measured generation cost, confusion or maintenance shows a smaller approach performs as well. No scheduled background research is implied.
