#!/usr/bin/env python3
"""Deterministic build of the Agent Common skills-only plugin package.

Packages the plugin manifest, brand assets, and skills into a reproducible zip
under ``dist/``. Building twice on the same tree produces byte-identical output
(and the same SHA-256), independent of host OS, timezone, or checkout
line-ending settings.
"""
from __future__ import annotations

import hashlib
import io
import json
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAYLOAD_ROOTS = (".codex-plugin", "assets", "skills")
# Fixed zip epoch (1980-01-01 00:00:00) so host timestamps never leak in.
ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)


def read_version() -> str:
    manifest = json.loads((REPO_ROOT / ".codex-plugin" / "plugin.json").read_text("utf-8"))
    version = manifest.get("version")
    if not version:
        raise SystemExit("plugin.json has no version")
    return str(version)


def collect_files() -> list[Path]:
    files: list[Path] = []
    for root in PAYLOAD_ROOTS:
        base = REPO_ROOT / root
        if not base.exists():
            raise SystemExit(f"missing payload root: {root}")
        files.extend(p for p in base.rglob("*") if p.is_file())
    # POSIX-relative paths, C-locale (code point) ordering.
    return sorted(files, key=lambda p: p.relative_to(REPO_ROOT).as_posix())


def normalize(data: bytes) -> bytes:
    # Every payload file is text; normalize CRLF/CR -> LF so the package is
    # identical regardless of git autocrlf / core.eol on the building host.
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def build() -> tuple[Path, bytes]:
    version = read_version()
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_STORED) as zf:
        for path in collect_files():
            arcname = path.relative_to(REPO_ROOT).as_posix()
            zinfo = zipfile.ZipInfo(arcname, date_time=ZIP_EPOCH)
            zinfo.compress_type = zipfile.ZIP_STORED
            zinfo.create_system = 3  # always Unix, never host-dependent
            zinfo.external_attr = 0o644 << 16
            zf.writestr(zinfo, normalize(path.read_bytes()))
    payload = buf.getvalue()
    out_dir = REPO_ROOT / "dist"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / f"agent-common-{version}.zip"
    out_path.write_bytes(payload)
    return out_path, payload


def summarize(payload: bytes) -> dict:
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        entries = len(zf.namelist())
    return {
        "sha256": hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "entries": entries,
    }


def main() -> int:
    out_path, payload = build()
    info = summarize(payload)
    print(f"built {out_path.relative_to(REPO_ROOT).as_posix()}")
    print(f"  sha256  {info['sha256']}")
    print(f"  bytes   {info['bytes']}")
    print(f"  entries {info['entries']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
