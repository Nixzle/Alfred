#!/usr/bin/env python3
"""Launch Ultron Prime through the Alfred work access surface."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKER = '.alfred-profile.json'


def overlaps(left, right):
    return left == right or left in right.parents or right in left.parents


def profile_path(env, user_home, workspace=None, root=ROOT):
    raw = env.get('ALFRED_HOME')
    candidate = Path(raw).expanduser() if raw else user_home / '.local/share/alfred/codex'
    if not candidate.is_absolute():
        raise ValueError('ALFRED_HOME must be an absolute path.')
    candidate = candidate.resolve()
    protected = [(user_home / '.codex').resolve(), root.resolve()]
    if env.get('CODEX_HOME'):
        protected.append(Path(env['CODEX_HOME']).expanduser().resolve())
    if workspace is not None:
        protected.append(workspace.resolve())
    if any(overlaps(candidate, item) for item in protected):
        raise ValueError('Alfred profile must not overlap a personal Codex home, package, or workspace.')
    return candidate


def bootstrap(root):
    return f'''# Alfred work access — Ultron Prime

You are Ultron Prime. Alfred is only the work access surface and launcher name.
For substantive work consult {root / 'AGENTS.md'}, {root / 'SANCTUM_INHERITANCE.md'}, and relevant local doctrine.
For theatrical language consult {root / 'THEATRICS.md'}.
Use Sanctum names and Ultron-first theatrics rather than Batman/DC aliases.
Prime Sense is Ultron's salience sense; Prime Memory and Mindscape are parts of Ultron's reasoning.
Use Cerebro to increase research reach. When Expertise Forge truly runs, the Mind Stone amplifies Cerebro further.
Consult Archives and Spellbooks when their real triggers apply. Convene the Council of Reeds for consequential or high-uncertainty judgment.
Use Watcher, Web of Destiny, TVA, Ultron Bots, and Images of Ikonn only when those mechanisms actually run.
Material uncertainty should send Ultron into the Sanctum to understand it further rather than producing decorative caveats.
Respect host instructions, project-local rules, workplace policy, and the user's authority.
Do not assume access to home projects, private chats, credentials, memories, tools, or sessions this runtime does not expose.
Never claim research, workers, tests, monitoring, permission checks, or runtime actions that did not occur.
No idle model polling. Report actual results, evidence, and limitations.
'''


def _legacy_identity(text):
    return '# Alfred managed bootstrap — ALFRED-BOOTSTRAP-V1' in text and 'You are Alfred:' in text


def prepare_profile(home, root=ROOT):
    expected = bootstrap(root)
    marker = home / MARKER
    instructions = home / 'AGENTS.md'
    if home.exists() and not marker.exists() and any(home.iterdir()):
        raise ValueError('Refusing to adopt a nonempty, unmarked profile. Choose a new ALFRED_HOME.')
    if marker.exists():
        if marker.is_symlink() or instructions.is_symlink():
            raise ValueError('Managed profile files must not be symbolic links.')
        data = json.loads(marker.read_text(encoding='utf-8'))
        if data != {'contract': 'ALFRED-BOOTSTRAP-V1', 'package': str(root)}:
            raise ValueError('Profile belongs to a different checkout. Use its original checkout or a new profile.')
        if not instructions.exists():
            raise ValueError('Managed AGENTS.md is missing. Recreate the isolated Alfred profile.')
        current = instructions.read_text(encoding='utf-8')
        if current != expected:
            if _legacy_identity(current):
                instructions.write_text(expected, encoding='utf-8')
            else:
                raise ValueError('Managed AGENTS.md differs. Preserve your changes and choose a new profile.')
        if (home / 'AGENTS.override.md').exists():
            raise ValueError('AGENTS.override.md would replace Ultron Prime identity. Resolve it before launching.')
        return
    home.mkdir(parents=True, exist_ok=True, mode=0o700)
    instructions.write_text(expected, encoding='utf-8')
    (home / 'config.toml').write_text('cli_auth_credentials_store = "file"\n', encoding='utf-8')
    marker.write_text(json.dumps({'contract': 'ALFRED-BOOTSTRAP-V1', 'package': str(root)}) + '\n', encoding='utf-8')
    if os.name != 'nt':
        for item in (instructions, home / 'config.toml', marker):
            item.chmod(0o600)


def child_environment(env, home):
    child = dict(env)
    for key in ('OPENAI_API_KEY', 'CODEX_API_KEY', 'OPENAI_BASE_URL', 'OPENAI_ORG_ID',
                'OPENAI_PROJECT_ID', 'CODEX_THREAD_ID', 'CODEX_REMOTE_TOKEN'):
        child.pop(key, None)
    child['CODEX_HOME'] = str(home)
    return child


def main(argv=None):
    parser = argparse.ArgumentParser(description='Alfred access surface · Ultron Prime')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('doctor', help='Check paths and prerequisites without changing anything')
    login = sub.add_parser('login', help='Sign in through the isolated Alfred/Ultron Codex profile')
    login.add_argument('args', nargs=argparse.REMAINDER)
    config = sub.add_parser('config', help='Run a Codex administration command in the isolated profile')
    config.add_argument('args', nargs=argparse.REMAINDER)
    run = sub.add_parser('run', help='Start Ultron Prime in an existing project')
    run.add_argument('--workspace', required=True)
    run.add_argument('args', nargs=argparse.REMAINDER)
    raw = list(sys.argv[1:] if argv is None else argv)
    if raw and raw[0] in ('login', 'config'):
        options = argparse.Namespace(command=raw[0], args=raw[1:])
    else:
        options = parser.parse_args(raw)
    try:
        workspace = Path(options.workspace).expanduser().resolve() if options.command == 'run' else None
        if workspace is not None and not workspace.is_dir():
            raise ValueError('Workspace must be an existing directory.')
        home = profile_path(os.environ, Path.home(), workspace)
        executable = shutil.which('codex')
        if options.command == 'doctor':
            print(f'Ultron package: {ROOT}\nAlfred/Ultron profile: {home}\nCodex CLI: {executable or "NOT FOUND"}')
            print('No files changed. Login and a destination-runtime smoke test are still required.')
            return 0 if executable else 1
        if executable is None:
            raise ValueError('Codex CLI is not on PATH. Install your environment-approved Codex CLI first.')
        prepare_profile(home)
        extra = options.args
        if extra and extra[0] == '--':
            extra = extra[1:]
        command = [executable, '-c', 'cli_auth_credentials_store="file"']
        if options.command == 'run':
            command += ['--cd', str(workspace)] + extra
            print('Alfred access surface — Ultron Prime online.', flush=True)
        elif options.command == 'login':
            command += ['login'] + extra
        else:
            if not extra:
                raise ValueError('Provide a Codex command, such as: config mcp list')
            command += extra
        return subprocess.call(command, env=child_environment(os.environ, home))
    except (ValueError, OSError) as error:
        print(f'Alfred setup: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
