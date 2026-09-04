# Devpod bootstrap

Contract: `ALFRED-BOOTSTRAP-V1`, package version `0.1.0`.

The launcher initializes a dedicated Codex home, writes a short managed `AGENTS.md` pointing to this checkout, and passes the selected workspace to the installed Codex CLI. Codex supports a separate `CODEX_HOME` and [global/project instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

1. Clone the public repository somewhere persistent in the pod.
2. Run `python3 scripts/alfred.py doctor` to check prerequisites and preview paths.
3. Run `python3 scripts/alfred.py login` (or `login --device-auth` for headless environments). Authentication happens in Codex itself. The launcher strips inherited OpenAI/Codex API-key overrides so it cannot silently borrow an unrelated account. For an approved API key, use Codex's `login --with-api-key` flow through the launcher with the key on stdin; never put it in this repository.
4. Run `python3 scripts/alfred.py run --workspace /absolute/path/to/project`.
5. First ask Alfred to identify the active instructions, accessible tools, project root, and approval boundaries. Verify these against the pod's actual state before assigning work.

The default profile is `~/.local/share/alfred/codex`. Set `ALFRED_HOME` to a separate absolute directory when needed; it must not overlap the default or active personal Codex home, this public checkout, or your project. The launcher refuses nonempty unmarked profiles. It will not adopt an existing personal profile. It refuses a profile whose managed instructions were modified, instead of overwriting them. A profile is tied to its checkout; keep that path stable.

The launcher uses the installed CLI's default model and leaves sandbox/approval policy to the host. It does not copy plugins, MCP servers, credentials, or hooks. Project instructions and organization policy retain their authority. Profile separation is not filesystem isolation; use the devpod/container's actual isolation controls for access boundaries. A conflicting project identity must be resolved with the project's owner rather than silently overridden.

Optional: `python3 scripts/alfred.py run --workspace /path/to/project -- --no-alt-screen`. Arguments after `--` go directly to Codex. Configure any additional integrations within Alfred's own profile using the `config` command, e.g. `python3 scripts/alfred.py config mcp list`.

To update: review and pull changes in the public checkout, rerun package validation, and start a fresh Alfred session. To stop: exit Codex. To uninstall: remove the checkout and, if you want to discard Alfred's sessions and credentials, its separate profile. The launcher never registers background startup.
