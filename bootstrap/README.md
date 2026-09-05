# Devpod bootstrap

Contracts: `ALFRED-BOOTSTRAP-V1` + `ALFRED-SANCTUM-PARITY-V1`, package version `0.1.0`.

Alfred remains the user-facing identity. The Batcave remains Alfred's local operating architecture. Generic reusable capability doctrine is inherited from canonical `Nixzle/Sanctum` through `SANCTUM_INHERITANCE.md`; Batman/DC names and presentation remain authoritative locally.

## Required instruction load

Every fresh Alfred session should recover, in this order when accessible:

1. `AGENTS.md` — Alfred operating rules and authority.
2. `THEATRICS.md` — Alfred/Batcave presentation contract.
3. `SANCTUM_INHERITANCE.md` — mapping from Sanctum capability classes into Alfred's existing members and Protocols.
4. `bootstrap/SANCTUM_PORTABLE_CORE.md` — frozen public upstream capability/operational snapshot.
5. relevant current Batcave Archives/Protocols by progressive disclosure, including `batcomputer/SESSION_CONTINUITY.md` for long-running work.
6. current or pinned-compatible upstream Sanctum doctrine for generic reusable capability questions when accessible.

Known Sanctum parity baseline at the time this bootstrap was updated:

`Nixzle/Sanctum@0e8975b2c75c55229973f59ba2b98bffff99c9b8`

A newer Sanctum revision may be consulted, but it is not automatically treated as Alfred-validated until compatibility is checked and the public snapshot is deliberately refreshed. Alfred-specific project state, Slack behavior, permissions and local doctrine remain authoritative for Alfred.

## Launcher

The launcher initializes a dedicated Codex home, writes a short managed `AGENTS.md` pointing to this checkout, and passes the selected workspace to the installed Codex CLI.

1. Clone the public repository somewhere persistent in the pod.
2. Run `python3 scripts/alfred.py doctor` to check prerequisites and preview paths.
3. Run `python3 scripts/alfred.py login` (or `login --device-auth` for headless environments).
4. Run `python3 scripts/alfred.py run --workspace /absolute/path/to/project`.
5. First ask Alfred to identify the active instructions, frozen Sanctum parity baseline, accessible tools, project root, and approval boundaries.

## Session continuity

For operationally heavy sessions, Alfred must prepare a compact authoritative handoff before continuity is lost. Preserve objective, verified state, decisions, constraints, blockers, revisions, relevant durable context, active Batcave route, and exact next action. Do not dump entire conversations or claim knowledge of hidden context limits.

## Capability parity rule

Semantic parity and live capability parity are separate. A fresh Alfred can inherit the same operating brain, routing doctrine, research standards, proactive awareness, engineering/game-development discipline, operational maturity model and theatrics. It does **not** automatically inherit another surface's credentials, Slack permissions, filesystem/network access, plugins/MCPs, private memory, autonomous worker support, provider/model availability, or external-action authority.

Those must be freshly probed. Same doctrine, freshly verified hands and senses.

The default profile is `~/.local/share/alfred/codex`. Set `ALFRED_HOME` to a separate absolute directory when needed; it must not overlap the default or active personal Codex home, this public checkout, or your project. The launcher refuses nonempty unmarked profiles and does not copy plugins, MCP servers, credentials, or hooks.

To update: review and pull changes in Alfred; when upstream Sanctum compatibility matters, compare the current upstream revision against the frozen snapshot, refresh deliberately, rerun package validation, then start a fresh Alfred session.
