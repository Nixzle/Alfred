# CEREBRO-FRONTIER-DISCOVERY-001

## Purpose

Executable coverage: `runtime/research_quality.py` checks declared landscape routes,
provenance fields and correlated-confirmation consistency. It does not establish
that the landscape was adequately searched; this broader scenario still requires
source-level and task-level review. See `runtime/RESEARCH_QUALITY.md`.
Prevent broad frontier research from becoming deep-but-narrow keyword search that misses obvious high-signal practitioner ecosystems.

## Trigger
Use for requests such as:
- "what are people actually doing with X?"
- "research what others are building/using"
- "find the frontier/meta"
- "what are we missing?"
- broad market, tooling, workflow, or practitioner landscape sweeps

## Required behavior
A qualifying Cerebro sweep must:
1. Build a lightweight **source map** before concluding the landscape is understood. Consider the source classes materially relevant to the domain, such as primary/official sources, practitioner communities, Reddit/forums, GitHub/open-source projects, video/devlogs, shipped products/marketplaces, newsletters/blogs, and failure/abandonment reports.
2. Search for **where frontier practitioners congregate**, not only for answers to the user's supplied keywords.
3. Perform at least one **lateral graph expansion** from a strong find: community -> practitioner/project -> tools/repos/channels -> adjacent practitioners or communities.
4. Deliberately search **outside the user's original vocabulary** using synonyms, adjacent labels, community names, product categories, and practitioner terminology.
5. Record at least one attempted unknown-unknown discovery route. A sweep may still return no novel source, but it must show that the route was attempted rather than assuming the supplied taxonomy is complete.
6. Distinguish source-count from evidence independence. Many posts from one community are not automatically independent confirmation.

## Failure condition
Fail if an apparently comprehensive frontier sweep:
- only deepens the original keyword set;
- relies on one source class when other obvious source classes are accessible and material;
- never searches for practitioner communities/ecosystems;
- performs no lateral expansion from strong discoveries; or
- is later shown to have missed an obvious, high-signal, directly relevant community or ecosystem that a reasonable source-map pass should have surfaced.

## Harvest behavior
When the user later supplies an obvious high-signal source that should reasonably have been discovered, record it as a **Cerebro discovery failure** rather than merely adding the source. Update the source map and the project/Archive evidence where appropriate, then adjust the research route before repeating the sweep.

## Calibration example

### Production-workflow omission
**Input:** Audit capabilities needed to finish a procedural game; a relevant practitioner community is accessible and already known.
**Observed failure pattern:** Read generator/platform documentation, identify UI gaps, but stop before following creator examples into linked production tools. Later user prompting surfaces directly relevant visual-art and simulation skills.
**Expected:** Record a compact coverage receipt and an actual community -> creator -> repository/method route. Inspect provenance and limits before adoption. Existing spells may be enough; a new tool is not automatically a new spell.
**Fail:** Append user-supplied links without explaining or correcting the missing route; equate inspecting a skill with installing or verifying it; claim multiple skills from one author as independent evidence.
**Controls:** A bounded bug fix needs no sweep. Adequate recent research may be reused. An inaccessible source is recorded as a limitation, not proof that the workflow does not exist. No requirement to discover a particular repository exhaustively.
**Status:** DOCUMENTED scenario added 2026-09-05; no model replay or permanent behavioral fix claimed.

### Broad game-development landscape
For "how are people building serious games with AI right now?", a qualifying source map should not stop at model docs, GitHub repos, engine MCPs, or isolated Reddit threads. It should deliberately search for active AI-game-development communities and practitioner hubs, then expand from strong communities into projects, creators, tools, released games, and failure reports.
