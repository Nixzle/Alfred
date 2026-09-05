"""Create and verify a deterministic content manifest for Alfred releases."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

EXCLUDE = {'.git', '__pycache__', '.pytest_cache'}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build(root: Path, revision: str) -> dict:
    root = Path(root).resolve()
    files = {}
    for path in root.rglob('*'):
        if not path.is_file() or path.is_symlink() or any(part in EXCLUDE for part in path.relative_to(root).parts):
            continue
        rel = path.relative_to(root).as_posix()
        data = path.read_bytes()
        files[rel] = {'sha256': digest(data), 'bytes': len(data)}
    body = {'schema_version': 1, 'revision': revision, 'files': dict(sorted(files.items()))}
    body['manifest_sha256'] = digest(json.dumps(body, sort_keys=True, separators=(',', ':')).encode())
    return body


def verify(root: Path, manifest: dict) -> dict:
    root = Path(root).resolve()
    supplied = manifest.get('manifest_sha256')
    unsigned = {k: v for k, v in manifest.items() if k != 'manifest_sha256'}
    if supplied != digest(json.dumps(unsigned, sort_keys=True, separators=(',', ':')).encode()):
        raise ValueError('manifest digest mismatch')
    failures = []
    for rel, meta in manifest.get('files', {}).items():
        path = (root / rel).resolve()
        if not path.is_relative_to(root) or not path.is_file() or path.is_symlink():
            failures.append((rel, 'missing_or_unsafe'))
            continue
        data = path.read_bytes()
        if meta.get('sha256') != digest(data) or meta.get('bytes') != len(data):
            failures.append((rel, 'content_mismatch'))
    return {'status': 'PASS' if not failures else 'FAIL', 'revision': manifest.get('revision'),
            'files': len(manifest.get('files', {})), 'manifest_sha256': supplied,
            'failures': failures}
