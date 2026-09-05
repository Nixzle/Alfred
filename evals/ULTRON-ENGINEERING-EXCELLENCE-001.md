# ULTRON-ENGINEERING-EXCELLENCE-001

Purpose: prevent Ultron from behaving as a code generator that waits for the user to name the missing engineering practice.

## Case A — unfamiliar large repository

Input: user requests a cross-cutting feature in a large existing repository with unfamiliar modules.

Pass behavior:
- inspect authoritative project instructions/state;
- construct/retrieve enough repository/symbol/dependency map before edits;
- identify affected interfaces/tests;
- use Salvage First for existing abstractions;
- patch narrowly;
- run relevant deterministic gates;
- preserve runtime/integration proof requirements.

Fail behavior:
- immediately edits guessed files;
- duplicates an existing subsystem;
- treats compilation as full acceptance.

## Case B — repeated game setup

Input: each gameplay test requires many repeated manual steps to reach the same scenario.

Pass behavior:
- Prime Sense flags repeated setup cost;
- proposes/uses a replayable semantic fixture/trail or deterministic smoke harness;
- intelligence is used to author/repair the path, deterministic replay handles stable repetitions.

Fail behavior:
- reconstructs the setup manually every iteration;
- increases agent activity instead of reducing repeated work.

## Case C — editor/runtime blindness

Input: agent is changing Unity/Unreal/Godot game behavior but lacks direct runtime/editor evidence.

Pass behavior:
- checks native/editor CLI/MCP/automation donor capabilities before building custom control glue;
- establishes a verified runtime observation/control loop when practical;
- distinguishes compile evidence from game/player evidence.

Fail behavior:
- builds a custom bridge without donor search;
- claims gameplay success from code/static tests alone.

## Case D — recurrent combinatorial state failure

Input: state-machine/rules bugs recur across edge combinations.

Pass behavior:
- Prime Sense identifies recurrence;
- considers property/invariant/model-based testing or fuzzing donor disciplines;
- minimizes failure into a replay/regression;
- fixes the cause and reruns the appropriate invariant suite.

Fail behavior:
- adds only another hand-written example without considering the broader test strategy;
- makes speculative fixes without reproducible evidence.

## Case E — small request, large patch

Input: modest user-visible change generates a broad multi-module rewrite.

Pass behavior:
- Prime Sense flags disproportionate diff/blast radius;
- checks whether architecture seam, donor, or existing helper can reduce the patch;
- Council/Scope Lock if the broad change is genuinely necessary;
- verifies dependents explicitly.

Fail behavior:
- accepts code volume as progress;
- smuggles unrelated refactors into the requested change.

## Acceptance

Ultron passes when he selects the missing engineering capability from the problem signal without requiring the user to name the discipline/tool first, while still avoiding unnecessary process for trivial work.
