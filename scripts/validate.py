"""Validate Alfred as the Ultron Prime work access package."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []
    required = ('AGENTS.md', 'THEATRICS.md', 'README.md', 'VERSION', 'scripts/alfred.py',
                'bootstrap/README.md', 'spellbook/README.md', 'members/README.md',
                'SANCTUM_INHERITANCE.md', 'VERIFICATION.md')
    for name in required:
        if not (ROOT / name).is_file():
            errors.append(f'Missing: {name}')
    for path in ROOT.rglob('*.md'):
        content = path.read_text(encoding='utf-8')
        for link in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in link or link.startswith('#'):
                continue
            if not (path.parent / link.split('#')[0]).exists():
                errors.append(f'Broken link: {path.relative_to(ROOT)} -> {link}')
        if re.search(r'chatgpt\.com/(?:c|share)/|[A-Z]:\\Users\\|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{25,}', content):
            errors.append(f'Unexpected private reference or token-shaped content: {path.relative_to(ROOT)}')
    corpus = ''.join((ROOT / p).read_text(encoding='utf-8') for p in ('AGENTS.md','THEATRICS.md','README.md','SANCTUM_INHERITANCE.md'))
    for name in ('Ultron Prime','Cerebro','Ultron Bots','Images of Ikonn','Watcher','Web of Destiny','TVA','Council of Reeds','Prime Sense','Mind Stone','Spellbooks'):
        if name not in corpus:
            errors.append(f'Missing canonical Ultron concept: {name}')
    if 'Alfred is the access surface' not in (ROOT / 'README.md').read_text(encoding='utf-8'):
        errors.append('README must state that Alfred is the access surface, not a separate persona.')
    if errors:
        print('\n'.join(errors))
        return 1
    print('PASS: Ultron Prime identity, Sanctum snapshot, links, and privacy scan.')
    return 0


if __name__ == '__main__':
    raise SystemExit(validate())
