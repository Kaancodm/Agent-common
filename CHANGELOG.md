# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
- `scripts/verify_evidence.py` — rebuild and check `submission/reviewer-packet.json`
  (`--update` refreshes the evidence deliberately).
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

### Not in scope

- Public submission blockers that live outside the repository: website / support / privacy /
  terms URLs, OpenAI Platform publisher verification, and country/region selection.
- Creating or pushing a Git tag or a GitHub Release.
