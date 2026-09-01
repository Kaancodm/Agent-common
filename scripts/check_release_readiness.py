#!/usr/bin/env python3
"""Executable gate for the release-prep workflow.

Runs the mechanical checks from ``workflows/release-prep.md`` steps 1-4 in one
command and prints a pass/fail line per check. Exits non-zero if any required
check fails, so it can be wired into CI and used as a pre-tag gate.

  python scripts/check_release_readiness.py            # beta / internal release
  python scripts/check_release_readiness.py --public   # also require listing URLs
  python scripts/check_release_readiness.py --allow-dirty
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / ".codex-plugin" / "plugin.json"
PACKET_PATH = REPO_ROOT / "submission" / "reviewer-packet.json"
LISTING_PATH = REPO_ROOT / "submission" / "listing.json"
CHANGELOG_PATH = REPO_ROOT / "CHANGELOG.md"

REQUIRED_LISTING_URLS = (
    "websiteURL",
    "customerSupportURL",
    "privacyPolicyURL",
    "termsOfServiceURL",
)

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import verify_evidence  # noqa: E402


def load_json(path: Path) -> dict:
    return json.loads(path.read_text("utf-8"))


def changelog_version() -> str | None:
    match = re.search(r"^## \[([^\]]+)\]", CHANGELOG_PATH.read_text("utf-8"), re.MULTILINE)
    return match.group(1) if match else None


def check_version_consistency() -> tuple[bool, str]:
    values = {
        "plugin.json": str(load_json(MANIFEST_PATH)["version"]),
        "reviewer-packet.json": str(load_json(PACKET_PATH)["source"]["version"]),
        "CHANGELOG.md": changelog_version(),
    }
    if len(set(values.values())) != 1:
        detail = ", ".join(f"{name}={value!r}" for name, value in values.items())
        return False, f"version mismatch: {detail}"
    return True, f"version consistent: {values['plugin.json']}"


def check_changelog_entry() -> tuple[bool, str]:
    version = changelog_version()
    if version is None:
        return False, "CHANGELOG.md has no '## [version]' section"
    heading = re.search(
        rf"^## \[{re.escape(version)}\] - (\d{{4}}-\d{{2}}-\d{{2}})\s*$",
        CHANGELOG_PATH.read_text("utf-8"),
        re.MULTILINE,
    )
    if not heading:
        return False, f"CHANGELOG section for {version} has no 'YYYY-MM-DD' date"
    return True, f"CHANGELOG entry dated {heading.group(1)}"


def check_evidence() -> tuple[bool, str]:
    info, _ = verify_evidence.reproduce()
    artifact = load_json(PACKET_PATH).get("artifact", {})
    problems = [
        f"{key}: evidence={artifact.get(key)!r} rebuild={info[key]!r}"
        for key in ("sha256", "bytes", "entries")
        if artifact.get(key) != info[key]
    ]
    if problems:
        return False, "evidence mismatch: " + "; ".join(problems)
    return True, f"evidence matches rebuild (sha256 {info['sha256'][:12]}…)"


def check_clean_tree() -> tuple[bool, str]:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        return False, f"could not read git status: {exc}"
    dirty = [line for line in result.stdout.splitlines() if line.strip()]
    if dirty:
        shown = ", ".join(line[3:] for line in dirty[:5])
        more = f" (+{len(dirty) - 5} more)" if len(dirty) > 5 else ""
        return False, f"working tree not clean: {shown}{more}"
    return True, "working tree clean"


def check_listing_urls() -> tuple[bool, str]:
    listing = load_json(LISTING_PATH)
    missing = [field for field in REQUIRED_LISTING_URLS if not listing.get(field)]
    if missing:
        return False, "listing URLs still empty: " + ", ".join(missing)
    return True, "all required listing URLs are set"


def main() -> int:
    args = sys.argv[1:]
    public = "--public" in args
    allow_dirty = "--allow-dirty" in args

    checks: list[tuple[str, tuple[bool, str], bool]] = []
    checks.append(("version consistency", check_version_consistency(), True))
    checks.append(("changelog entry", check_changelog_entry(), True))
    checks.append(("package evidence", check_evidence(), True))
    if not allow_dirty:
        checks.append(("clean working tree", check_clean_tree(), True))
    checks.append(("listing URLs", check_listing_urls(), public))

    failures = 0
    for name, (ok, detail), required in checks:
        if ok:
            mark = "PASS"
        elif required:
            mark = "FAIL"
            failures += 1
        else:
            mark = "WARN"
        print(f"[{mark}] {name}: {detail}")

    print()
    if failures:
        scope = "public release" if public else "release"
        print(f"NOT READY for {scope}: {failures} blocking check(s) failed.")
        return 1
    if public:
        print("READY: all release checks passed (public submission scope).")
    else:
        print("READY: all release checks passed. Re-run with --public before submitting.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
