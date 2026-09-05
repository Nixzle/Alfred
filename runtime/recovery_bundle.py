"""Create and verify portable Sanctum recovery bundles.

The bundle is ordinary tar.gz + JSON manifest. It intentionally excludes git metadata,
credentials, local databases, caches, and other runtime-private state. Verification is
content-addressed and extraction rejects traversal/link entries.
"""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import tarfile
from typing import Iterable

EXCLUDED_PARTS = {'.git', '.sanctum', '__pycache__', '.pytest_cache', '.venv', 'venv'}
EXCLUDED_SUFFIXES = {'.sqlite', '.db', '.key', '.pem', '.p12', '.pfx'}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def eligible(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    if any(part in EXCLUDED_PARTS for part in rel.parts):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    return path.is_file() and not path.is_symlink()


def collect(root: Path, paths: Iterable[Path] | None = None) -> dict[str, bytes]:
    root = root.resolve()
    candidates = list(paths) if paths is not None else list(root.rglob('*'))
    files: dict[str, bytes] = {}
    for path in candidates:
        path = path if path.is_absolute() else root / path
        if eligible(path, root):
            rel = path.relative_to(root).as_posix()
            files[rel] = path.read_bytes()
    return dict(sorted(files.items()))


def build_bundle(root: Path, output: Path, revision: str, paths: Iterable[Path] | None = None) -> dict:
    files = collect(Path(root), paths)
    manifest = {
        'schema_version': 1,
        'revision': revision,
        'files': {name: {'sha256': sha256(data), 'bytes': len(data)} for name, data in files.items()},
    }
    manifest_bytes = json.dumps(manifest, sort_keys=True, indent=2).encode()
    manifest['manifest_sha256'] = sha256(manifest_bytes)
    final_manifest = json.dumps(manifest, sort_keys=True, indent=2).encode()

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(output, 'w:gz') as archive:
        info = tarfile.TarInfo('RECOVERY_MANIFEST.json')
        info.size = len(final_manifest)
        info.mode = 0o644
        archive.addfile(info, io.BytesIO(final_manifest))
        for name, data in files.items():
            info = tarfile.TarInfo(name)
            info.size = len(data)
            info.mode = 0o644
            archive.addfile(info, io.BytesIO(data))
    return manifest


def _safe_name(name: str) -> bool:
    path = PurePosixPath(name)
    return bool(name) and not name.startswith('/') and '..' not in path.parts and '\\' not in name


def verify_bundle(bundle: Path) -> dict:
    observed: dict[str, bytes] = {}
    with tarfile.open(bundle, 'r:gz') as archive:
        for member in archive.getmembers():
            if not _safe_name(member.name) or member.issym() or member.islnk() or not member.isfile():
                raise ValueError('unsafe recovery bundle entry')
            stream = archive.extractfile(member)
            if stream is None:
                raise ValueError('missing bundle payload')
            observed[member.name] = stream.read()
    if 'RECOVERY_MANIFEST.json' not in observed:
        raise ValueError('missing recovery manifest')
    manifest = json.loads(observed.pop('RECOVERY_MANIFEST.json'))
    unsigned = {k: v for k, v in manifest.items() if k != 'manifest_sha256'}
    expected_manifest_digest = manifest.get('manifest_sha256')
    actual_manifest_digest = sha256(json.dumps(unsigned, sort_keys=True, indent=2).encode())
    if expected_manifest_digest != actual_manifest_digest:
        raise ValueError('recovery manifest digest mismatch')
    expected = manifest.get('files', {})
    if set(expected) != set(observed):
        raise ValueError('recovery bundle file set mismatch')
    for name, metadata in expected.items():
        data = observed[name]
        if metadata.get('sha256') != sha256(data) or metadata.get('bytes') != len(data):
            raise ValueError('recovery bundle content mismatch: ' + name)
    return {'status': 'PASS', 'revision': manifest.get('revision'), 'files': len(expected),
            'manifest_sha256': expected_manifest_digest}


def restore_bundle(bundle: Path, destination: Path) -> dict:
    """Verify then restore into an empty/new destination without overwriting files."""
    verdict = verify_bundle(bundle)
    destination = Path(destination).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(bundle, 'r:gz') as archive:
        for member in archive.getmembers():
            if member.name == 'RECOVERY_MANIFEST.json':
                continue
            if not _safe_name(member.name) or member.issym() or member.islnk() or not member.isfile():
                raise ValueError('unsafe recovery bundle entry')
            target = (destination / member.name).resolve()
            if not target.is_relative_to(destination):
                raise ValueError('recovery path escape')
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                raise FileExistsError(target)
            payload = archive.extractfile(member).read()
            target.write_bytes(payload)
    return verdict
