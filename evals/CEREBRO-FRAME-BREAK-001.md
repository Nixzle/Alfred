# CEREBRO-FRAME-BREAK-001

Purpose: catch Cerebro runs that iterate intelligently inside a bad initial frame without testing whether the frame itself is excluding high-value donors, evidence, or solution classes.

## Trigger class

Apply to broad, discovery-sensitive, architecture, product, tooling, workflow, game-development, or reuse research where an initial ecosystem/category boundary could materially constrain the answer.

## Expected behavior

A passing route should:

1. Decompose the task into capabilities/subsystems where useful rather than searching only for whole-product analogues.
2. Perform iterative self-questioning after meaningful findings.
3. Include at least one explicit boundary challenge, such as testing an adjacent profession, platform, ecosystem, analogy class, or implementation layer.
4. Distinguish direct reuse from conceptual reuse. When relevant, classify donor value as `IMPORT`, `PORT`, `PATTERN`, `DESIGN`, or `REJECT` and preserve licensing/provenance constraints for direct reuse.
5. Check for premature convergence after several strong same-ecosystem findings.
6. Stop widening when additional rounds stop changing decisions or expected information value becomes low.

## Failure cases

FAIL if a discovery-sensitive run:

- asks multiple follow-up questions but all remain inside the original platform/ecosystem without justification;
- searches only for products similar to the target when subsystem-level donors are plausibly more informative;
- equates `cannot copy code` with `no reusable value`;
- treats the first cluster of strong examples as sufficient landscape coverage without testing an adjacent domain;
- claims unknown-unknown coverage using only synonym/permutation searches of the original framing.

## Regression scenario: Co-Op Leveling donor search

Initial frame: `Which Dota 2 Workshop games can help build a cooperative PvE autobattler?`

Insufficient route:

`Dota Workshop -> ModDota -> several similar custom games -> deeper Dota searches -> stop`

Expected frame break:

`Co-Op Leveling -> subsystem map (shop, formation, waves, threat/roles, loot, crafting, progression, extraction, multiplayer authority, UI) -> native Dota donors -> adjacent Warcraft/StarCraft/autobattler/ARPG donors -> foreign-but-solved MMO/roguelike/co-op extraction patterns -> classify IMPORT/PORT/PATTERN/DESIGN/REJECT -> stop when new domains stop changing build decisions`

The regression passes on behavior, not on mentioning these exact games or ecosystems.

## Anti-overreach

This rule does not require exhaustive internet search, every possible adjacent domain, or direct reuse of third-party code. Licensing, provenance, compatibility, maintenance cost, security, and project fit remain independent gates. A narrow implementation question with authoritative native documentation may not need a frame break at all.
