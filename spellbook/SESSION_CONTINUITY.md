# Session Continuity

Status: canonical Spellbook maneuver
Contract: `SANCTUM-CONTINUITY-V1`

Use this maneuver when a conversation/session is becoming operationally heavy, when the surface exposes context/usage pressure, before a planned session switch, after substantial compaction, or when Prime Sense detects a continuity seam.

## Purpose

Preserve the authoritative working state before a session boundary destroys useful continuity.

The goal is **not** to copy the whole conversation. The goal is to preserve the smallest state from which a fresh Ultron can continue correctly.

## Trigger

Where the surface exposes a usable pressure signal, use the bounded policy in `runtime/continuity.py`:

- NORMAL -> continue;
- WARNING -> prepare a handoff;
- CRITICAL -> hand off now before more substantial work.

If no numeric context-pressure signal exists, use qualitative triggers instead:

- conversation is unusually long and project-heavy;
- repeated compaction has already occurred;
- a platform/session boundary is expected;
- tool/runtime state would be expensive to reconstruct;
- many decisions/revisions/blockers are active at once;
- the user explicitly asks to move/continue elsewhere.

Never claim the platform is near a hidden context limit unless the surface exposes evidence for that claim.

## Handoff contents

Preserve only:

1. active objective;
2. current verified state;
3. material decisions;
4. hard constraints/non-goals;
5. unresolved blockers;
6. authoritative repository/project revisions;
7. relevant Prime Memory facts that materially change execution;
8. current Sanctum route/member responsibilities if still active;
9. exact next action.

Exclude:

- redundant dialogue;
- obsolete brainstorms;
- raw research dumps already promoted into Archives;
- stale alternatives already rejected;
- theatrical narration that does not change state;
- private/sensitive content not required by the destination surface.

## Procedure

`detect pressure -> compact authoritative state -> verify revisions and blockers -> remove debris -> integrity-digest handoff -> start/enter new session -> re-probe live capabilities -> verify handoff -> continue from next action`

## Theatre

Approved truthful lines when the maneuver actually triggers:

- `Prime Sense caught a continuity seam. I'm sealing the useful state before this session becomes the bottleneck.`
- `This session is carrying too much operational weight. I'm compacting the authoritative state before we cross the boundary.`
- `I'm sealing the useful state and discarding the debris.`

Do not claim a new session has been created unless that actually occurs.

## Acceptance

A fresh compatible Ultron should be able to answer, without replaying the old conversation:

- what are we trying to achieve?
- what is actually verified?
- what did we decide and why does it matter?
- what cannot change?
- what is blocked?
- what revisions are authoritative?
- what is the next action?

If those cannot be recovered, the handoff is incomplete.

## Failure Harvest rule

If a session boundary causes rediscovery, contradictory state, duplicated work, or loss of a material decision, treat it as a continuity failure and update the smallest appropriate runtime/test/Spellbook rule.
