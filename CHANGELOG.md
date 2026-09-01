# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0-beta.2] - 2026-09-01

### Added

- `agents/debug-agent.md`: diagnosis role for tracing root causes and collecting evidence;
  does not implement fixes.
- `workflows/bug-fix.md`: focused defect workflow — report → reproduce → diagnose
  (debug-agent) → fix → verify → review → handoff.
- `workflows/release-prep.md`: publisher-side checklist for version bumps, evidence rebuild,
  listing URL population, OpenAI Platform verification, tag and release creation.
- `agents/README.md` and `workflows/README.md` now include a listing table of defined files.
- `scripts/check_release_readiness.py`: executable gate for the release-prep checklist
  (version consistency, dated CHANGELOG entry, package evidence, clean tree, listing URLs).
  `--public` additionally requires the listing URLs; `--allow-dirty` skips the tree check.
- `.github/workflows/release.yml`: on a `v*` tag, confirms the tag matches the manifest,
  runs the readiness gate, builds the package, and publishes a GitHub Release with the
  CHANGELOG section as notes and the `dist/` zip attached.
- `SECURITY.md`: vulnerability reporting policy, supported versions, and reporting scope.

### Changed

- `.codex-plugin/plugin.json` version → `0.1.0-beta.2`.
- `submission/reviewer-packet.json` `source.version` → `0.1.0-beta.2`; release notes updated.
  The four listing URLs moved from `missing` to `resolved`; publisher verification and
  country/region selection remain open.
- `README.md`: Status section updated to `0.1.0-beta.2` and to the now-populated listing
  URLs; structure tree extended with the new agent, workflows, script, `public/`, and
  `SECURITY.md`.
- `workflows/release-prep.md`: the listing-URL trigger prerequisite is now explicitly
  public-submission-only; version bumps are committed before the evidence rebuild so the
  package is built from a clean tree; the gated actions now merge to `main` and verify the
  tag target before tagging.
- `public/support.md`, `public/terms.md`, `public/index.html`: repository links now use
  absolute GitHub URLs (they resolved to nothing from inside the deployed `public/` root),
  and the displayed version tracks `0.1.0-beta.2`.
- CI additionally runs `scripts/check_release_readiness.py`.

---

## [0.1.0-beta.1] - 2026-09-01

First tagged pre-release. Consolidates the initial foundation work and makes the repository
internally consistent and reproducible.

### Added

- Project foundation: `AGENTS.md`, `README.md`, and `docs/` (architecture, agent contract,
  security model, skills, brand rationale, plugin experience).
- `agents/` roles: `orchestrator-agent`, `review-agent`, and a copyable `agent-template`.
- `skills/agent-common` (public end-to-end workflow) and `skills/host-workspace-operator`
  (safe host-native workspace operations).
- `workflows/change-delivery.md`, `prompts/agent-common.md`, `templates/task-brief.md`.
- `policy/approval-policy.json` and `schemas/handoff.schema.json`.
- `.codex-plugin/plugin.json` skills-only plugin manifest, brand assets, and `submission/`
  listing and reviewer evidence.
- `scripts/build_plugin_package.py` — deterministic plugin-package build (`dist/`).
- `scripts/verify_evidence.py` — rebuild twice, confirm determinism, extract-check the
  package, and compare against `submission/reviewer-packet.json` (`--update` refreshes the
  evidence deliberately). The evidence records no commit SHA, since a file cannot contain
  the hash of the commit that introduces it.
- `LICENSE` (MIT) and `CONTRIBUTING.md`.
- CI: JSON validation for `submission/*.json`, YAML validation for skill adapters,
  a Markdown relative-link check, a version-consistency check, and an evidence-rebuild check.

### Changed

- Unified the repository to English: docs, templates, prompts, the plugin product copy
  (`plugin.json`, `submission/listing.json`, `submission/reviewer-packet.json`), and the
  `agent-common` skill's default response language.
- `README.md` structure tree rewritten to match the actual repository; Status section
  rewritten for the beta.
- `.codex-plugin/plugin.json` version → `0.1.0-beta.1`;
  `submission/reviewer-packet.json` `source.version` → `0.1.0-beta.1`
  (`submission/listing.json` stays at the intended public `0.1.0`).
- `schemas/handoff.schema.json` `$id` now points at the repository raw URL instead of a
  `.local` placeholder.
- Regenerated `submission/reviewer-packet.json` package evidence from the new canonical
  build script.
- CI committed-secret scan no longer blanket-excludes `*.md`.

### Removed

- Empty `inputs/` and `outputs/` placeholder directories (the architecture doc states that
  empty placeholder folders are not versioned).

### Fixed

- Dead cross-reference in `agents/README.md` (`../skills/README.md` → `../docs/skills.md`).
- Ambiguous wording in `skills/agent-common/SKILL.md` ("Preserve others' work and work
  outside the scope") that could be read as an instruction to work out of scope.

### Not in scope

- Public submission blockers that live outside the repository: website / support / privacy /
  terms URLs, OpenAI Platform publisher verification, and country/region selection.
- Creating or pushing a Git tag or a GitHub Release.
