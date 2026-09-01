# Plugin Experience Brief

## Product boundary

- Audience: individuals and teams with changing general project tasks.
- Recurring job: take an assignment with existing context to a usable, verified result
  independently.
- Architecture: `skills-only`; no app, no MCP server, and no external runtime required.
- Public domain skill: `agent-common`.
- Baseline skill: `host-workspace-operator` for safe, host-native file and repository work.
- Excluded: deployment, publication, external communication, credential management, and
  irreversible actions without a separate assignment.

## Candidate decisions

| Source | Decision | Rationale |
| --- | --- | --- |
| `prompts/agent-common.md` | `compile_skill` | Contains the reusable flow from assignment to handoff. |
| `AGENTS.md` | `reference_only` | Provides repository rules but is not published as a near-identical second skill. |

## Host workspace profile

| Operation | Classification |
| --- | --- |
| read, list, search, grep | preferred for taking stock |
| write, patch | mutation; only for an assigned change |
| shell | optional; mutation for state-changing commands |
| python | optional for deterministic processing and verification |

The plugin does not grant these capabilities. It only uses them when the host provides them.

## Discovery boundaries

- Direct trigger: structure and implement a general task.
- Indirect trigger: evaluate existing project context and deliver the next reliable state.
- Negative trigger: a specialized security, legal, medical, or financial task that needs a
  narrower domain workflow.

## Status

The configuration is prepared for local validation. The connected GitHub account `Kaancodm`
is recorded as the project publisher. The listing pack and reviewer evidence are under
`submission/`. A public submission is still not in scope and deliberately stays out of scope
without the required URLs and any additionally required marketplace verification.

The local brand pack is present. Website, support, privacy, and terms URLs are still missing.
Publisher verification in the OpenAI Platform and the country/region selection are not
confirmed.
