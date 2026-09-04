"""Check public package links, naming, and required files without network access."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []
    for name in ('AGENTS.md', 'THEATRICS.md', 'README.md', 'VERSION', 'scripts/alfred.py',
                 'bootstrap/README.md', 'batcomputer/README.md', 'VERIFICATION.md'):
        if not (ROOT / name).is_file():
            errors.append(f'Missing: {name}')
    for path in ROOT.rglob('*.md'):
        content = path.read_text(encoding='utf-8')
        for link in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in link or link.startswith('#'):
                continue
            if not (path.parent / link.split('#')[0]).exists():
                errors.append(f'Broken link: {path.relative_to(ROOT)} -> {link}')
        if re.search(r'\b(?:Ultrons?|Sanctum|Cerebro|Ikonn|TVA)\b|Web of Destiny|Council of Reeds|Bat Vault', content, re.I):
            errors.append(f'Unmigrated name: {path.relative_to(ROOT)}')
        if re.search(r'chatgpt\.com/(?:c|share)/|[A-Z]:\\Users\\|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{25,}', content):
            errors.append(f'Unexpected private reference or token-shaped content: {path.relative_to(ROOT)}')
    roster = (ROOT / 'README.md').read_text(encoding='utf-8')
    for name in ('Alfred', 'Batcave', 'Brother Eye', 'Bat-Drones', 'Bat-Family', 'Oracle',
                 'Mobius Chair', 'Metron', 'Justice League', 'Contingency Plans', 'Batcomputer',
                 'Protocols', 'Archives', 'Mission Briefs', 'Bat-Signal', 'Batcave Console'):
        if name not in roster:
            errors.append(f'Missing approved name: {name}')
    if errors:
        print('\n'.join(errors))
        return 1
    print('PASS: required files, local Markdown links, approved naming, and basic publication scan.')
    print('This is a bounded check, not proof that arbitrary content is safe or model behavior is correct.')
    return 0


if __name__ == '__main__':
    raise SystemExit(validate())
