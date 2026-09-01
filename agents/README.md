# Agent definitions

Under `agents/` are domain roles. An agent definition explains what an agent is responsible
for and how a good result is recognized.

## When a new definition makes sense

A new definition makes sense when a role:

- has a recurring assignment,
- has its own inputs, decisions, or outputs,
- can be tested or replaced separately from other roles.

For a single one-off task, a workflow step or a short task description is usually enough.

## Minimum content

Every agent definition should contain:

- name and purpose,
- responsibility area and clear non-responsibilities,
- expected inputs,
- expected outputs,
- workflow,
- available tools or sources,
- security and permission boundaries,
- success criteria and escalation cases.

Use [agent-template.md](agent-template.md) as a starting point.

## Defined agents

| File | Role |
|---|---|
| [orchestrator-agent.md](orchestrator-agent.md) | Coordinates a multi-step change to verified handoff |
| [review-agent.md](review-agent.md) | Independently assesses a change and its evidence |
| [debug-agent.md](debug-agent.md) | Diagnoses failures and traces root causes |

## Naming convention

Files are named in lowercase with hyphens, for example `research-agent.md` or
`review-agent.md`. The file name describes the role, not the model or vendor used.

## Distinctions

Agents are roles. Reusable capabilities belong in [../docs/skills.md](../docs/skills.md).
Connecting multiple roles belongs in [../workflows/README.md](../workflows/README.md).
