# Failure Harvest — donor community blindness

Date: 2026-09-05

## Failure

During Co-Op Leveling's salvage-first / open-source-first shift, donor discovery focused heavily on repositories, Workshop packages, implementation patterns, and design exemplars. The user had to point out that the surrounding player and developer communities of donor games were not being treated as a mandatory evidence source.

This matters because source code explains how a system is implemented, while communities often expose what the code cannot: exploits, balance pathologies, confusing UX, abandoned mechanics, update regressions, matchmaking pain, retention failures, emergent strategies, accessibility problems, maintenance burden, and the exact reasons players or maintainers dislike a supposedly successful design.

## Evidence from immediate correction

A bounded Reddit pass surfaced materially different information from donor code alone:

- Dota 1x6 community history includes database/stat manipulation through Valve custom-game server-key behavior, showing that persistence/in-game-currency architecture must be threat-modeled rather than copied at face value.
- Current Dota Arcade discussion reports bot-created passive lobbies consuming Arcade server capacity, relevant to release/matchmaking assumptions for any Arcade-first project.
- Historical Auto Chess/custom-game discussion exposes matchmaking fragmentation, player-access restrictions, patch regressions, and custom-game instability that would not be visible from gameplay code alone.

## Root causes

1. **Artifact bias.** Repositories and Workshop packages were treated as the donor, instead of the donor ecosystem being `artifact + maintainers + players + failure history`.
2. **Positive-survivorship bias.** We inspected what shipped and worked without systematically checking what users complained about, what maintainers regretted, or what communities abandoned.
3. **Implementation/design split without experience layer.** `IMPORT/PORT/PATTERN/DESIGN` classified reusable value but did not require a separate `COMMUNITY` evidence pass.
4. **Source-map rule was too broad in practice.** Sanctum already said practitioner communities should be inspected for frontier research, but donor-specific salvage did not operationalize that requirement per donor.

## Generalizable correction

For material donor evaluation, treat a donor as a four-part evidence object:

1. **Artifact:** code, package, docs, implementation.
2. **Maintainer history:** issues, changelogs, postmortems, release notes, abandoned branches.
3. **Player/community evidence:** Reddit, Discord when accessible, Steam/Workshop discussions, forums, guides, community bug threads, creator channels.
4. **Failure/retention evidence:** exploits, regressions, complaints, dead systems, churn, workarounds, balance and UX pain.

A donor should not be considered "understood" merely because its code was inspected. For consequential reuse/design adoption, record what the community praises, what repeatedly breaks, what causes friction, and what should explicitly *not* be inherited.

Community evidence is advisory and noisy. It must be triangulated against primary/maintainer evidence where material; popularity is not proof of correctness.

## Project application

Co-Op Leveling donor research should add a `Community/maintainer evidence checked` field to salvage receipts and maintain community-source notes in its donor registry for high-value donors. Discord should be checked when accessible through public/indexed sources or an authorized connected environment; do not claim Discord inspection when the server is inaccessible.

## Regression expectation

Given a high-value game/system donor with an active or archived player/developer community, a passing salvage route should inspect at least one community/maintainer evidence source in addition to the implementation artifact when that evidence could materially affect adoption. If access is unavailable, mark it explicitly rather than silently treating the donor as fully understood.
