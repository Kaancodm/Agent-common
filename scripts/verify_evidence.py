#!/usr/bin/env python3
"""Rebuild the plugin package and check it against submission/reviewer-packet.json.

Exit non-zero if the committed evidence does not match a fresh deterministic
build, or if the recorded ``source.version`` disagrees with the plugin manifest.

  python scripts/verify_evidence.py             # check only
  python scripts/verify_evidence.py --update    # rewrite the evidence from the build
"""
from __future__ import annotations

import io
import json
import subprocess
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKET_PATH = REPO_ROOT / "submission" / "reviewer-packet.json"
MANIFEST_PATH = REPO_ROOT / ".codex-plugin" / "plugin.json"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import build_plugin_package as builder  # noqa: E402


def git_head() -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def reproduce() -> tuple[dict, int]:
    """Build twice, confirm byte-identical output, and confirm the zip extracts."""
    _, first = builder.build()
    _, second = builder.build()
    if first != second:
        raise SystemExit("build is not deterministic: two builds differ")

    with zipfile.ZipFile(io.BytesIO(first)) as zf:
        bad = zf.testzip()
        if bad is not None:
            raise SystemExit(f"corrupt entry in built package: {bad}")
        names = zf.namelist()
        for name in names:
            zf.read(name)  # decompresses and CRC-checks every entry

    return builder.summarize(first), 2


def main() -> int:
    update = "--update" in sys.argv[1:]

    info, builds = reproduce()
    manifest_version = str(json.loads(MANIFEST_PATH.read_text("utf-8"))["version"])

    packet = json.loads(PACKET_PATH.read_text("utf-8"))
    artifact = packet.setdefault("artifact", {})
    source = packet.setdefault("source", {})

    if update:
        artifact["sha256"] = info["sha256"]
        artifact["bytes"] = info["bytes"]
        artifact["entries"] = info["entries"]
        artifact["deterministicBuilds"] = builds
        artifact["extractedCopyValidated"] = True
        source["version"] = manifest_version
        head = git_head()
        if head:
            source["commit"] = head
        PACKET_PATH.write_text(
            json.dumps(packet, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        rel = PACKET_PATH.relative_to(REPO_ROOT).as_posix()
        print(f"updated {rel}")
        print(f"  sha256  {info['sha256']}")
        print(f"  bytes   {info['bytes']}")
        print(f"  entries {info['entries']}")
        return 0

    problems: list[str] = []
    for key in ("sha256", "bytes", "entries"):
        if artifact.get(key) != info[key]:
            problems.append(f"artifact.{key}: evidence={artifact.get(key)!r} rebuild={info[key]!r}")
    if source.get("version") != manifest_version:
        problems.append(
            f"source.version: evidence={source.get('version')!r} "
            f"plugin.json={manifest_version!r}"
        )

    if problems:
        print("evidence mismatch:")
        for problem in problems:
            print(f"  {problem}")
        print("run: python scripts/verify_evidence.py --update")
        return 1

    print("evidence OK")
    print(f"  sha256  {info['sha256']}")
    print(f"  bytes   {info['bytes']}")
    print(f"  entries {info['entries']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
