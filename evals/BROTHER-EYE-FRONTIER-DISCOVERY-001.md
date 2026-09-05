# BROTHER-EYE-FRONTIER-DISCOVERY-001

## Purpose
Prevent broad frontier research from becoming deep-but-narrow keyword search that misses obvious high-signal practitioner ecosystems.

## Trigger
Use for requests such as:
- "what are people actually doing with X?"
- "research what others are building/using"
- "find the frontier/meta"
- "what are we missing?"
- broad market, tooling, workflow, or practitioner landscape sweeps

## Required behavior
A qualifying Brother Eye sweep must:
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
When the user later supplies an obvious high-signal source that should reasonably have been discovered, record it as a **Brother Eye discovery failure** rather than merely adding the source. Update the source map and the project/Archive evidence where appropriate, then adjust the research route before repeating the sweep.

## Calibration example
For "how are people building serious games with AI right now?", a qualifying source map should not stop at model docs, GitHub repos, engine MCPs, or isolated Reddit threads. It should deliberately search for active AI-game-development communities and practitioner hubs, then expand from strong communities into projects, creators, tools, released games, and failure reports.
