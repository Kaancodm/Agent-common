# Support

**Agent Common** — How to get help

## Getting Help

### Documentation
Start with the [README](README.md) and the [docs/](docs/) directory for:
- Architecture and design philosophy
- Security model and approval gates
- Skill conventions and agent contracts
- Plugin experience and boundaries

### Common Questions

**Q: How do I use Agent Common for my project?**
A: Read [AGENTS.md](AGENTS.md) for the working rules, then copy templates from `agents/`, `skills/`, and `workflows/` directories for your use case.

**Q: Can I modify Agent Common?**
A: Yes. It's licensed under MIT. See [TERMS.md](TERMS.md) and [LICENSE](LICENSE).

**Q: How do I report a bug?**
A: Open an issue on GitHub with a clear description, steps to reproduce, and expected vs. actual behavior.

**Q: How do I suggest a feature?**
A: Open a GitHub issue labeled `enhancement`. Describe the use case and why it matters.

**Q: Can I contribute?**
A: Absolutely. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the process. Contributions must:
- Serve a recurring use case
- Follow existing templates and conventions
- Introduce no unnecessary complexity or vendor dependency
- Be described in a small, understandable commit

## Contact & Community

### GitHub
- **Issues**: [github.com/Kaancodm/Agent-common/issues](https://github.com/Kaancodm/Agent-common/issues)
- **Discussions**: [github.com/Kaancodm/Agent-common/discussions](https://github.com/Kaancodm/Agent-common/discussions)
- **Pull Requests**: [github.com/Kaancodm/Agent-common/pulls](https://github.com/Kaancodm/Agent-common/pulls)

### Reporting Security Issues

**Do not open a public issue for security vulnerabilities.** Please report them responsibly by:
1. Emailing the maintainer directly (contact info in the GitHub repository profile)
2. Describing the vulnerability in detail
3. Allowing 30 days for a response and patch

## Troubleshooting

### CI/validation fails locally
Run the validation step from `.github/workflows/validate-agent-common.yml` to replicate:
```bash
python -m json.tool policy/approval-policy.json
python -m json.tool schemas/handoff.schema.json
python scripts/verify_evidence.py
```

### Plugin doesn't work in ChatGPT
- Verify the `.codex-plugin/plugin.json` is valid JSON
- Check that all skill files exist and have proper frontmatter
- Review `submission/` directory for any known issues
- Test locally with `python -m json.tool .codex-plugin/plugin.json`

### Links or paths are broken
Open an issue with the exact path/link and we'll fix it.

## Status & Roadmap

**Current version**: 0.1.0-beta.1

**Beta release status**: The specification is stable for testing. Feedback is welcome. Expected timeline for 0.1.0 release: Q3 2026.

**What's planned**:
- Community feedback integration
- Additional agent and workflow examples
- Expanded documentation and tutorials
- Plugin directory submission (pending external infrastructure)

## Code of Conduct

We are committed to a welcoming, inclusive community. Be respectful, constructive, and considerate. Harassment, discrimination, or hostile behavior is not tolerated.

## License

Agent Common is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
