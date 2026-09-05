"""Build and verify deterministic release identity manifests for Sanctum."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterable


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_manifest(root: Path, revision: str, paths: Iterable[Path] | None = None) -> dict:
    root = Path(root).resolve()
    if paths is None:
        paths = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and '.sanctum' not in p.parts]
    files = {}
    for path in paths:
        path = path if path.is_absolute() else root / path
        if path.is_symlink() or not path.is_file():
            continue
        rel = path.resolve().relative_to(root).as_posix()
        data = path.read_bytes()
        files[rel] = {'sha256': sha256(data), 'bytes': len(data)}
    body = {'schema_version': 1, 'revision': revision, 'files': dict(sorted(files.items()))}
    body['manifest_sha256'] = sha256(json.dumps(body, sort_keys=True, separators=(',', ':')).encode())
    return body


def verify_manifest(root: Path, manifest: dict) -> dict:
    root = Path(root).resolve()
    supplied_digest = manifest.get('manifest_sha256')
    unsigned = {k: v for k, v in manifest.items() if k != 'manifest_sha256'}
    actual_digest = sha256(json.dumps(unsigned, sort_keys=True, separators=(',', ':')).encode())
    if supplied_digest != actual_digest:
        raise ValueError('release manifest digest mismatch')
    failures = []
    for rel, metadata in manifest.get('files', {}).items():
        path = (root / rel).resolve()
        if not path.is_relative_to(root) or not path.is_file() or path.is_symlink():
            failures.append({'file': rel, 'reason': 'missing_or_unsafe'})
            continue
        data = path.read_bytes()
        if metadata.get('sha256') != sha256(data) or metadata.get('bytes') != len(data):
            failures.append({'file': rel, 'reason': 'content_mismatch'})
    return {'status': 'PASS' if not failures else 'FAIL', 'revision': manifest.get('revision'),
            'files': len(manifest.get('files', {})), 'failures': failures,
            'manifest_sha256': supplied_digest}
