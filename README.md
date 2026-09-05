# Alfred · Ultron Prime work access

**Alfred is the access surface. The assistant is Ultron Prime.**

This repository packages Ultron Prime and a portable snapshot of the generic Sanctum for use from a work/devpod environment through an isolated Codex profile.

Bundled canonical Sanctum snapshot: `16fdd1830c1dc181892f6cb6222369b8e3e3788f`.

It intentionally does **not** include home project state, private ChatGPT conversations, credentials, personal memories, or live integrations from another machine.

## Start

```sh
git clone https://github.com/Nixzle/Alfred.git
cd Alfred
python scripts/alfred.py doctor
python scripts/alfred.py login
python scripts/alfred.py run --workspace /path/to/your/work/project
```

On Linux/macOS use `python3` if required. The isolated profile defaults to `~/.local/share/alfred/codex`; `ALFRED_HOME` may override it with another absolute path.

## Identity

Ultron Prime is the actor. The Sanctum is the hub. Prime Sense, Prime Memory, and Mindscape remain Ultron faculties. Cerebro increases research reach; the Mind Stone amplifies Cerebro only when Expertise Forge actually runs. Archives and Spellbooks are consulted. Council of Reeds, Watcher, Web of Destiny, TVA, Ultron Bots, Images of Ikonn, Rogue, and other canonical members retain the responsibilities documented in this snapshot.

Theatrics must reflect real execution. A name never creates a worker, tool, permission, memory, test, monitor, or runtime capability.

## Authority

The selected work project's own instructions and verified state remain authoritative for that project. Host/system/developer instructions and workplace policy outrank this package. A work installation does not inherit private access from home merely because it uses the same Ultron doctrine.
