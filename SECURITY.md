# Security Policy

## Supported versions

Agent Common is a pre-release specification repository. Only the most recent tagged version
receives fixes.

| Version | Supported |
|---|---|
| `0.1.0-beta.2` | Yes |
| Older pre-releases | No |

## Reporting a vulnerability

**Do not open a public issue for a security vulnerability.**

Report privately through
[GitHub private vulnerability reporting](https://github.com/Kaancodm/Agent-common/security/advisories/new),
or by contacting the maintainer through the contact details on the
[repository profile](https://github.com/Kaancodm).

Please include:

- a description of the vulnerability and its impact,
- the affected files, version, or configuration,
- steps to reproduce, and
- any proof-of-concept material you have.

## What to expect

- An acknowledgement of your report.
- An assessment of severity and scope.
- Up to 30 days to investigate and prepare a fix before public disclosure.
- Credit in the release notes if you would like it.

## Scope

This repository ships agent definitions, skills, workflows, and a skills-only plugin
package. It bundles no server, no MCP endpoint, and no credential storage. Reports that are
in scope include:

- a skill or workflow that instructs an agent to exfiltrate secrets or bypass an approval
  gate defined in [`policy/approval-policy.json`](policy/approval-policy.json),
- a prompt-injection path in the shipped skill or prompt text,
- a flaw in [`scripts/build_plugin_package.py`](scripts/build_plugin_package.py) or
  [`scripts/verify_evidence.py`](scripts/verify_evidence.py) that would let a package's
  contents diverge from its recorded evidence,
- a committed secret or credential.

Out of scope: vulnerabilities in the host platform (ChatGPT, OpenAI Platform, GitHub) and
issues in third-party services linked from the documentation. Report those to the
relevant vendor.

## Security model

See [`docs/security.md`](docs/security.md) for the approval gates, permission boundaries,
and the trust assumptions the agent contract relies on.
