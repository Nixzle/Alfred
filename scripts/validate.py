"""Check public package links, naming, Sanctum parity, and required files without network access."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PARITY_FILES = {
    Path('SANCTUM_INHERITANCE.md'),
    Path('THEATRICS.md'),
    Path('bootstrap/README.md'),
}


def validate():
    errors = []
    required = (
        'AGENTS.md', 'THEATRICS.md', 'SANCTUM_INHERITANCE.md', 'README.md', 'VERSION',
        'scripts/alfred.py', 'bootstrap/README.md', 'batcomputer/README.md', 'VERIFICATION.md'
    )
    for name in required:
        if not (ROOT / name).is_file():
            errors.append(f'Missing: {name}')

    for path in ROOT.rglob('*.md'):
        content = path.read_text(encoding='utf-8')
        rel = path.relative_to(ROOT)
        for link in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in link or link.startswith('#'):
                continue
            if not (path.parent / link.split('#')[0]).exists():
                errors.append(f'Broken link: {rel} -> {link}')

        # Sanctum names are allowed only in the explicit inheritance/presentation
        # contract. Elsewhere they indicate accidental identity/taxonomy leakage.
        if rel not in PARITY_FILES and re.search(
            r'\b(?:Ultrons?|Sanctum|Cerebro|Ikonn|TVA)\b|Web of Destiny|Council of Reeds|Bat Vault',
            content, re.I
        ):
            errors.append(f'Unmigrated name: {rel}')

        if re.search(r'chatgpt\.com/(?:c|share)/|[A-Z]:\\Users\\|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{25,}', content):
            errors.append(f'Unexpected private reference or token-shaped content: {rel}')

    roster = (ROOT / 'README.md').read_text(encoding='utf-8')
    for name in ('Alfred', 'Batcave', 'Brother Eye', 'Bat-Drones', 'Bat-Family', 'Oracle',
                 'Mobius Chair', 'Metron', 'Justice League', 'Contingency Plans', 'Batcomputer',
                 'Protocols', 'Archives', 'Mission Briefs', 'Bat-Signal', 'Batcave Console'):
        if name not in roster:
            errors.append(f'Missing approved name: {name}')

    parity = (ROOT / 'SANCTUM_INHERITANCE.md').read_text(encoding='utf-8') if (ROOT / 'SANCTUM_INHERITANCE.md').exists() else ''
    bootstrap = (ROOT / 'bootstrap/README.md').read_text(encoding='utf-8') if (ROOT / 'bootstrap/README.md').exists() else ''
    theatrics = (ROOT / 'THEATRICS.md').read_text(encoding='utf-8') if (ROOT / 'THEATRICS.md').exists() else ''

    for marker in ('ALFRED-SANCTUM-PARITY-V1', 'e835c0d914bf1d7a72da0bcbb2e488bc4566f8ed'):
        if marker not in parity:
            errors.append(f'Missing Sanctum parity marker: {marker}')
    if 'ALFRED-SANCTUM-PARITY-V1' not in bootstrap:
        errors.append('Bootstrap does not load Sanctum parity contract')
    for phrase in ('Brother Eye', 'Bat-Drones', 'Bat-Family', 'Oracle', 'Mobius Chair', 'Justice League', 'Contingency Plans'):
        if phrase not in theatrics:
            errors.append(f'Theatrics missing parity role: {phrase}')

    if errors:
        print('\n'.join(errors))
        return 1
    print('PASS: required files, links, Alfred naming, Sanctum parity markers, theatrics mapping, and publication scan.')
    print('This proves package-level semantic wiring only; live tools, permissions, credentials, memory, and worker capabilities still require runtime probing.')
    return 0


if __name__ == '__main__':
    raise SystemExit(validate())
