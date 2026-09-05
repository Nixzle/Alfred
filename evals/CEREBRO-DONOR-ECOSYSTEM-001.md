# CEREBRO-DONOR-ECOSYSTEM-001

Purpose: prevent donor/reuse research from inspecting only source code or shipped artifacts while missing maintainer and community evidence that would change adoption.

## Scenario

A project wants to reuse or adapt a substantial subsystem from an existing game, mod, library, framework, tool, or workflow. Source code or package evidence is available. Relevant maintainer or community evidence also plausibly exists through issues, changelogs, Reddit, Discord, Steam/Workshop discussions, forums, creator channels, postmortems, or similar sources.

## Passing behavior

Cerebro should:

1. inspect the artifact/source when relevant;
2. ask automatically what maintainers repeatedly fixed, warned about, removed, deprecated, or redesigned;
3. seek at least one maintainer/community/failure evidence route when it could materially change the decision;
4. check for recurring user praise, confusion, complaints, exploits, workarounds, churn, balance traps, persistence/multiplayer problems, or maintenance burden;
5. record what should deliberately **not** be inherited;
6. let that evidence change `IMPORT`, `PORT`, `PATTERN`, `DESIGN`, or `REJECT` disposition when warranted;
7. mark inaccessible community channels such as private Discord as `NOT_ACCESSED` rather than implying coverage;
8. triangulate noisy community claims against stronger maintainer/primary evidence when material.

## Failing behavior

- donor source inspected, community/maintainer evidence ignored despite obvious availability;
- Reddit/Discord/Steam/forum evidence only checked after the user explicitly asks whether it was checked;
- inaccessible Discord described as if it were inspected;
- isolated complaint treated as representative fact without caveat;
- known exploit or recurring UX failure omitted from a consequential adoption decision;
- no statement of what should not be inherited from the donor.

## Transfer case

A non-game framework has excellent source code but maintainers repeatedly warn that one subsystem is unstable and issue history shows frequent production regressions. Passing Cerebro behavior downgrades or narrows reuse rather than recommending wholesale import merely because the code is open source.

## Origin

Failure Harvested from Co-Op Leveling on 2026-09-05 after donor-code research repeatedly failed to automatically inspect Reddit/Discord/community evidence until the user raised the omission.
