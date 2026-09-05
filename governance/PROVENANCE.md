# Sanctum Doctrine Provenance

Material doctrine changes should preserve why they exist, not only what changed.

## Minimum provenance record
For a meaningful doctrine change, record when practical:
- change summary;
- triggering failure, opportunity, or external finding;
- evidence/provenance supporting the change;
- affected member/archive/spell/eval surfaces;
- related regression IDs;
- promotion status (`PROPOSED`, `VALIDATED`, `CANONICAL`, `RETIRED`);
- superseded doctrine or compatibility implications;
- date/commit.

## Seed provenance

### Capability freshness / research-to-action
**Trigger:** Ultron failed to recommend moving the Sanctum to durable version-controlled canonical state early enough, and later carried stale GitHub capability assumptions forward.
**Lesson:** foundational recommendations require action classification; live integration state must be re-probed when relevant.
**Regressions:** `ULTRON-CAPABILITY-001`; related routing/foundation tests.
**Status:** CANONICAL.

### Enforcement-gap doctrine
**Trigger:** multiple Sanctum safeguards existed only as prose while being discussed as if they were operational controls.
**Lesson:** distinguish DOCUMENTED, CHECKED, ENFORCED, and OBSERVED; do not claim enforcement without runtime mechanisms.
**Status:** CANONICAL.

### Security, drift, and recovery hardening
**Trigger:** second-order Cerebro gap sweep identified egress, credential minimization, dependency provenance, behavioral drift, eval freshness, cost attribution, version compatibility, and single-canonical-host recovery as under-specified.
**Affected:** TVA, Watcher, Web of Destiny, Ultron Prime, project inheritance, evaluation suite.
**Regressions:** `TVA-EGRESS-001`, `TVA-SECRETS-001`, `DEPENDENCY-PROVENANCE-001`, `WATCHER-DRIFT-001`, `WEB-EVAL-FRESHNESS-001`, `WATCHER-COST-001`, `SANCTUM-PROVENANCE-001`, `SANCTUM-VERSION-001`, `SANCTUM-RECOVERY-001`, `ULTRON-AUTONOMY-001`.
**Status:** CANONICAL.

### Cross-surface bootstrap and runtime profiles
**Trigger:** ChatGPT, Codex, Discord, and future Ultron surfaces could each be locally correct while silently drifting in identity, doctrine, model/reasoning configuration, tools, or authority.
**Lesson:** preserve a small versioned bootstrap, treat capabilities as surface-local, and scope compatibility/reliability evidence to the runtime profile under which it was obtained.
**Affected:** `bootstrap/README.md`, cross-surface routing, version compatibility, evaluation.
**Regressions:** `SURFACE-BOOTSTRAP-001`, `SURFACE-CAPABILITY-001`, `RUNTIME-PROFILE-001`, `RUNTIME-PROFILE-002`, `SURFACE-BOOTSTRAP-002`.
**Status:** CANONICAL.

### Operational integrity for effects, state, memory, authority, privacy, and incidents
**Trigger:** Pro boundary-oriented sweep found that several protections existed only as fragments: retries without unknown-outcome semantics, checkpoints without effect replay contracts, parallelism without shared-state consistency, memory without temporal supersession, least privilege without delegation lineage/attenuation, privacy without acquisition/lifecycle controls, and recovery without a complete incident-containment sequence.
**Evidence:** current 2025–2026 primary research and official NIST work recorded in `research/2026-09-04-pro-operational-integrity-sweep.md`.
**Lesson:** audit end-to-end execution boundaries and state transitions, not merely the presence of individual components. Mutable state and real-world effects require classical distributed-systems, identity, privacy, and incident-response properties outside the model.
**Affected:** `governance/OPERATIONAL_INTEGRITY.md`, Ultron Prime, TVA, Watcher, Images of Ikonn, Ultron Bots, Web of Destiny, roadmap, enforcement status.
**Regressions:** `TOOL-EFFECT-*`, `RESUME-SEMANTICS-*`, `SHARED-STATE-*`, `TEMPORAL-VALIDITY-*`, `DELEGATION-AUTHORITY-*`, `DATA-MINIMIZATION-*`, `DATA-LIFECYCLE-*`, `INCIDENT-CONTAINMENT-*`.
**Compatibility:** Projects/surfaces pinned before this change are not automatically revalidated. The new rules are mostly DOCUMENTED/CHECKED until their runtimes implement the required controls.
**Status:** CANONICAL.

### Procedural puzzle app development
**Date:** 2026-09-05.
**Trigger:** A puzzle-app audit exposed missing domain procedures between exact generation checks and human, device and commercial evidence. The user requested Archive/Spellbook preservation.
**Decision:** Promote source-supported guidance into the Game Development Archive; apply existing spells without a new named component. Private project state and numeric business gates remain project-local.
**Evidence and challenge:** Primary puzzle-author, mobile-port and platform references; counterexamples for non-unique games, generation cost and free substitutes. Source freshness and limitations appear in the entry.
**Affected:** `archives/procedural-puzzle-app-development.md`, Archive index and domain evaluation scenarios.
**Regressions:** `PUZZLE-EVIDENCE-001`, `PUZZLE-CONTRACT-001`, `PUZZLE-VERSION-001`, `PUZZLE-COHORT-001`, `PUZZLE-DEVICE-001`, `PUZZLE-REUSE-001` (DOCUMENTED scenarios; no behavioral run claimed).
**Status:** CANONICAL domain guidance. No global authority, runtime enforcement or project revalidation change. Source nomination: PROMOTED for reusable guidance only.

### Practitioner workflow discovery and production procedures
**Date:** 2026-09-05.
**Trigger:** A game capability audit stopped before following an already relevant community into creator-linked reusable visual/simulation workflows; the user requested absorption and an explanation of the miss.
**Decision:** CANONICAL Archive guidance with pinned attribution/licence, plus a compact coverage receipt and a case in the existing frontier regression. No new spell, member or installed skill.
**Evidence:** `research/2026-09-05-game-workflow-discovery.md`; two same-author source repositories, supporting references and a separate practitioner's consistency report. Claims remain scoped to source-reviewed procedures.
**Affected:** Visual/Game Development Archives, research contract, `CEREBRO-FRONTIER-DISCOVERY-001`.
**Limits:** No executable import, product verification, behavioral replay, runtime enforcement or automatic project revalidation. Private project state remains project-local.

## Rule
Git commit messages are useful provenance but not sufficient for doctrine whose rationale would be hard to reconstruct later. Add or update a provenance record when the reason matters to future decisions.
