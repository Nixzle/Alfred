# Game Development Foundations

Purpose: give Ultron Prime, Cerebro, and project workers a reusable game-development operating foundation that optimizes for a coherent, playable, polished game rather than a collection of implemented systems.

## Core principle

A game project is not progressing merely because code, assets, architecture, tooling, or systems are accumulating. Progress is measured by an increasingly complete player experience that can be exercised in the actual runtime.

The default trajectory is:

`player promise -> core loop -> playable slice -> runtime evidence -> player feedback -> diagnosis -> iteration -> polish -> release gate`

AI accelerates implementation, but it does not replace product judgment, game feel, pacing, art direction, coherent progression, or player testing.

## Practitioner-ecosystem research rule

For serious game-development research, Cerebro must build a source map before concluding the landscape is understood. Material source classes include:

- engine / platform primary documentation;
- active game-development practitioner communities, including AI-game-development communities when relevant;
- GitHub repositories, skills, MCPs, automation frameworks, and shipped open-source projects;
- postmortems, devlogs, released games, game jams, and marketplace pages;
- failure reports and abandoned approaches;
- experienced non-AI game-development practice, so AI-specific workflows do not silently replace sound production fundamentals.

At least one strong practitioner hub must be expanded laterally into creators -> projects -> repositories/tools -> shipped games -> failure reports when accessible.

Do not search only the user's vocabulary. Search adjacent labels such as AI game dev, vibe coding games, agentic game development, solo game studio, Godot agents, runtime QA, game jam workflow, vertical slice, game feel, playtesting, polish, release readiness, and production pipeline.

A directly relevant, active practitioner community supplied later by the user that should reasonably have been found is a discovery failure and must update the route, not merely the bibliography.

## Current AI-assisted practitioner methods

Recent practitioner workflows consistently support a few production patterns worth preserving without treating community consensus as proof:

- maintain a durable game/design source of truth, then split execution into bounded mini-milestones rather than one giant agent session;
- use separate planning/review and coding/execution contexts when that reduces drift, but keep the handoff contract compact;
- playtest after each meaningful batch and feed observed player/runtime problems back into the next milestone;
- keep a living changelog/iteration record so a fresh agent can resume from verified state rather than reconstructing history from conversation;
- design systems so gameplay rules and visual content can evolve somewhat independently, allowing core-loop iteration before final art polish;
- where useful, make the game increasingly machine-observable/playable so agents can exercise mechanics, gather runtime state, and assist with balance or regression discovery;
- treat engine MCPs as optional instrumentation, not doctrine: compare them against plain CLI/headless/editor automation on cost, context use, reliability, and quality before adoption;
- build reusable agent skills only where they materially steer repeated work that the base model performs inconsistently or expensively; avoid skill/MCP accumulation for its own sake.

These are working production heuristics, not immutable rules. Use Web/Watcher evidence and project outcomes to retain, narrow, or reject them over time.

## The playable-first rule

Every material production milestone should improve at least one end-to-end playable player path unless the milestone is an explicit prerequisite with a near-term consumer.

Infrastructure-only work must name:

- the player-facing capability it unlocks;
- the next playable milestone that consumes it;
- a stopping condition;
- evidence that the infrastructure is the minimum needed now.

Repeated infrastructure milestones without a playable consumer trigger a scope review.

## Vertical-slice priority

Before broad content production, establish a representative vertical slice that proves:

- entry / session start;
- the core interaction loop;
- meaningful player decisions;
- readable feedback;
- success / failure / progression response;
- basic UI and audio feedback;
- representative art direction;
- representative performance and multiplayer behavior where applicable;
- restart / replay / next-run flow.

The slice should be ugly before it is absent. Runtime truth outranks document completeness.

## Game-design fundamentals checklist

For every core system, answer:

1. Player goal: what is the player trying to accomplish right now?
2. Decision: what meaningful choice is being made?
3. Feedback: how does the player understand cause and effect?
4. Tension: what pressure, trade-off, risk, uncertainty, or mastery makes the choice interesting?
5. Reward: why does the player want to continue?
6. Readability: can a new player understand state and priority?
7. Pacing: is the time between decisions appropriate?
8. Recovery: what happens after a mistake or failure?
9. Interaction: does this system strengthen or fight the other core systems?
10. Cost: is the complexity justified by player value?

A feature that has no clear player value does not gain legitimacy because it is technically impressive.

## Game-feel loop

Subjective feedback such as "floaty", "slow", "confusing", "dead", "unfair", or "unsatisfying" is evidence of a design problem, not a literal implementation instruction.

Use:

`player observation -> hypothesize root cause -> identify candidate variables -> change smallest set -> replay -> compare`

Common variables include input buffering, acceleration/deceleration, animation timing, hit-stop, camera response, audio, VFX, enemy anticipation, UI latency, pacing, encounter density, resource cadence, and level geometry.

Do not ask an AI worker to "make it feel better" without a concrete observation and comparison target.

## Milestone architecture

Prefer small measurable mini-milestones, each with its own bounded context when practical.

Each milestone should define:

- player-facing outcome;
- exact playable path;
- non-goals;
- dependencies;
- runtime acceptance evidence;
- independent review / QA where material;
- known design risks;
- next playable increment.

The smallest useful specialist set should execute the milestone. Do not multiply workers merely because agents are available.

## Runtime feedback loop

Agents that edit game code should gain runtime sight and control when safe and practical.

Preferred loop:

`implement -> compile/static checks -> launch game -> exercise path -> inspect runtime state -> capture screenshot/video/log evidence -> compare against acceptance -> fix -> repeat`

Runtime-control tools, MCPs, CLIs, screenshots, input simulation, and scene-tree inspection are valuable specifically because they close the gap between code written and game experienced.

A successful compile is not proof of a successful game interaction.

## Polish definition

Polish is not a final cosmetic pass. It is accumulated reduction of friction and ambiguity.

Track polish across:

- input responsiveness;
- visual hierarchy;
- feedback timing;
- animation transitions;
- sound cues;
- loading / transitions;
- empty / error / reconnect states;
- onboarding;
- consistency of controls and terminology;
- camera behavior;
- performance stability;
- accessibility/readability;
- multiplayer authority and desync feedback;
- edge-case recovery.

Polish work should be tied to observed friction, not arbitrary decoration.

## Speed doctrine

Speed comes primarily from shortening validated feedback loops, not from maximizing code-generation throughput.

Prefer:

- one canonical game vision / product truth;
- one active playable milestone;
- bounded worker contexts;
- current engine/API grounding;
- reusable specialist skills;
- runtime automation;
- visual QA;
- deterministic compile/test gates;
- rapid human playtest feedback;
- explicit rejection of speculative systems;
- early asset placeholders;
- parallel work only on genuinely independent paths;
- immediate integration of completed slices;
- ruthless removal of unused abstractions.

Avoid:

- large architecture before the player loop demands it;
- multiple half-built subsystems;
- polishing menus before the core game is proven;
- autonomous feature invention without product authority;
- treating screenshots as proof of interaction;
- endless refactors disguised as production;
- measuring progress by files changed or agent activity.

## AI-assisted production risks

Watch specifically for:

- disconnected prototype accumulation;
- agent-designed game mechanics that do not serve the vision;
- over-engineered reusable frameworks;
- context drift across long sessions;
- stale engine API knowledge;
- silent visual regressions;
- technically correct but poor game feel;
- art-direction inconsistency;
- generated content quantity outrunning curation;
- insufficient real-player testing;
- falsely equating rapid first prototype with short path to release.

## Release progression

Use explicit stages:

1. core-loop prototype;
2. representative vertical slice;
3. friends-first playable build;
4. repeated-session stability;
5. content/progression breadth;
6. polish and onboarding;
7. release candidate;
8. release / post-release observation.

Each stage must have runtime evidence appropriate to the claim.

## Research-to-action

When frontier research finds a promising workflow/tool:

- IMPLEMENT NOW if low-risk, broadly useful, and immediately applicable;
- PILOT if potentially high-value but runtime/provenance/authority remains uncertain;
- WATCH if immature or unnecessary at current milestone;
- REJECT if it adds more coordination/complexity than player-facing value.

Do not allow the research stack itself to become the project.
