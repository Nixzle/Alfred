"""Check public package links, naming, Sanctum parity, and required files without network access."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PARITY_FILES = {
    Path('SANCTUM_INHERITANCE.md'),
    Path('THEATRICS.md'),
    Path('OPERATIONAL_STATUS.md'),
    Path('governance/ADMIN_HARDENING.md'),
    Path('bootstrap/README.md'),
    Path('bootstrap/SANCTUM_PORTABLE_CORE.md'),
}

CURRENT_SANCTUM_BASELINE = 'b997221b889138e40d8797fca13efc89d41afaf0'


def validate():
    errors = []
    required = (
        'AGENTS.md', 'THEATRICS.md', 'SANCTUM_INHERITANCE.md', 'OPERATIONAL_STATUS.md',
        'README.md', 'VERSION', 'scripts/alfred.py', 'scripts/package_manifest.py',
        'bootstrap/README.md', 'bootstrap/SANCTUM_PORTABLE_CORE.md',
        'batcomputer/README.md', 'governance/ADMIN_HARDENING.md', 'VERIFICATION.md'
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
    snapshot = (ROOT / 'bootstrap/SANCTUM_PORTABLE_CORE.md').read_text(encoding='utf-8') if (ROOT / 'bootstrap/SANCTUM_PORTABLE_CORE.md').exists() else ''
    bootstrap = (ROOT / 'bootstrap/README.md').read_text(encoding='utf-8') if (ROOT / 'bootstrap/README.md').exists() else ''
    theatrics = (ROOT / 'THEATRICS.md').read_text(encoding='utf-8') if (ROOT / 'THEATRICS.md').exists() else ''

    for marker in ('ALFRED-SANCTUM-PARITY-V1', CURRENT_SANCTUM_BASELINE):
        if marker not in parity:
            errors.append(f'Missing Sanctum parity marker: {marker}')
    for marker in ('ALFRED-SANCTUM-SNAPSHOT-V1', CURRENT_SANCTUM_BASELINE,
                   'ENFORCE -> OBSERVE -> BREAK DELIBERATELY -> RECOVER -> MEASURE -> TIGHTEN'):
        if marker not in snapshot:
            errors.append(f'Missing public Sanctum snapshot marker: {marker}')
    if 'ALFRED-SANCTUM-PARITY-V1' not in bootstrap:
        errors.append('Bootstrap does not load Sanctum parity contract')
    if CURRENT_SANCTUM_BASELINE not in bootstrap:
        errors.append('Bootstrap is not pinned to the current Sanctum parity baseline')
    for phrase in ('Brother Eye', 'Bat-Drones', 'Bat-Family', 'Oracle', 'Mobius Chair', 'Justice League', 'Contingency Plans'):
        if phrase not in theatrics:
            errors.append(f'Theatrics missing parity role: {phrase}')

    if errors:
        print('\n'.join(errors))
        return 1
    print('PASS: required files, public Sanctum snapshot, Alfred naming, parity markers, release identity tooling, theatrics mapping, and publication scan.')
    print('This proves package-level semantic wiring only; live tools, permissions, credentials, memory, and worker capabilities still require runtime probing.')
    return 0


if __name__ == '__main__':
    raise SystemExit(validate())
