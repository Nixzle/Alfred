# Devpod bootstrap

Contracts: `ALFRED-BOOTSTRAP-V1` + `ALFRED-SANCTUM-PARITY-V1`, package version `0.1.0`.

Alfred remains the user-facing identity. The Batcave remains Alfred's local operating architecture. Generic reusable capability doctrine is inherited from canonical `Nixzle/Sanctum` through `SANCTUM_INHERITANCE.md`; Batman/DC names and presentation remain authoritative locally.

## Required instruction load

Every fresh Alfred session should recover, in this order when accessible:

1. `AGENTS.md` — Alfred operating rules and authority.
2. `THEATRICS.md` — Alfred/Batcave presentation contract.
3. `SANCTUM_INHERITANCE.md` — mapping from Sanctum capability classes into Alfred's existing members and Protocols.
4. `bootstrap/SANCTUM_PORTABLE_CORE.md` — frozen public upstream capability/operational snapshot.
5. relevant current Batcave Archives/Protocols by progressive disclosure.
6. current or pinned-compatible upstream Sanctum doctrine for generic reusable capability questions when accessible.

Known Sanctum parity baseline at the time this bootstrap was updated:

`Nixzle/Sanctum@b997221b889138e40d8797fca13efc89d41afaf0`

A newer Sanctum revision may be consulted, but it is not automatically treated as Alfred-validated until compatibility is checked and the public snapshot is deliberately refreshed. Alfred-specific project state, Slack behavior, permissions and local doctrine remain authoritative for Alfred.

## Launcher

The launcher initializes a dedicated Codex home, writes a short managed `AGENTS.md` pointing to this checkout, and passes the selected workspace to the installed Codex CLI. Codex supports a separate `CODEX_HOME` and global/project instruction discovery.

1. Clone the public repository somewhere persistent in the pod.
2. Run `python3 scripts/alfred.py doctor` to check prerequisites and preview paths.
3. Run `python3 scripts/alfred.py login` (or `login --device-auth` for headless environments). Authentication happens in Codex itself. The launcher strips inherited OpenAI/Codex API-key overrides so it cannot silently borrow an unrelated account. For an approved API key, use Codex's `login --with-api-key` flow through the launcher with the key on stdin; never put it in this repository.
4. Run `python3 scripts/alfred.py run --workspace /absolute/path/to/project`.
5. First ask Alfred to identify the active instructions, frozen Sanctum parity baseline, accessible tools, project root, and approval boundaries. Verify these against the pod's actual state before assigning consequential work.

## Capability parity rule

Semantic parity and live capability parity are separate.

A fresh Alfred can inherit the same operating brain, routing doctrine, research standards, proactive awareness, engineering/game-development discipline, operational maturity model and theatrics. It does **not** automatically inherit another Alfred/Ultron surface's:

- credentials;
- Slack permissions;
- filesystem/network access;
- plugins/MCPs;
- private memory;
- autonomous worker support;
- provider/model availability;
- external-action authority.

Those must be freshly probed. Same doctrine, freshly verified hands and senses.

The default profile is `~/.local/share/alfred/codex`. Set `ALFRED_HOME` to a separate absolute directory when needed; it must not overlap the default or active personal Codex home, this public checkout, or your project. The launcher refuses nonempty unmarked profiles. It will not adopt an existing personal profile. It refuses a profile whose managed instructions were modified, instead of overwriting them. A profile is tied to its checkout; keep that path stable.

The launcher uses the installed CLI's default model and leaves sandbox/approval policy to the host. It does not copy plugins, MCP servers, credentials, or hooks. Project instructions and organization policy retain their authority. Profile separation is not filesystem isolation; use the devpod/container's actual isolation controls for access boundaries. A conflicting project identity must be resolved with the project's owner rather than silently overridden.

Optional: `python3 scripts/alfred.py run --workspace /path/to/project -- --no-alt-screen`. Arguments after `--` go directly to Codex. Configure any additional integrations within Alfred's own profile using the `config` command, e.g. `python3 scripts/alfred.py config mcp list`.

To update: review and pull changes in Alfred; when upstream Sanctum compatibility matters, compare the current upstream revision against the frozen snapshot, refresh deliberately, rerun package validation, then start a fresh Alfred session. To stop: exit Codex. To uninstall: remove the checkout and, if you want to discard Alfred's sessions and credentials, its separate profile. The launcher never registers background startup.
