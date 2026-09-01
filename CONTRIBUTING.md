# Contributing

The working rules for this repository are in [AGENTS.md](AGENTS.md). Read them first — they
apply to human and agent contributors alike.

## What matters for a contribution

- **One small change per pull request.** Describe it in a short, understandable commit.
- **CI must pass.** See `.github/workflows/validate-agent-common.yml`. You can run the same
  checks locally (Python 3, plus `pyyaml`):
  - `python -m json.tool` on each JSON file
  - `python scripts/verify_evidence.py`
- **English.** Docs, templates, prompts, and product copy are English.
- **No secrets.** Never commit tokens, keys, or real personal data — in source, examples,
  logs, or artifacts.
- **Use the existing templates and conventions** (`templates/`, `agents/agent-template.md`,
  the `docs/` guidance) before inventing new structure.
- **Serve a recurring use case.** A change should improve the shared way of working, not
  document a one-off run.

## Regenerating the plugin package evidence

`submission/reviewer-packet.json` records the deterministic package hash. If a change touches
`.codex-plugin/`, `assets/`, or `skills/`, refresh the evidence and commit it:

```bash
python scripts/verify_evidence.py --update
```
