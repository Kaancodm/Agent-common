# Working rules for Agent Common

## Mandate

This repository collects reusable agent definitions, skills, and workflows. Changes should
improve the shared way of working, not merely document a single one-off run.

## Before every change

1. Read the README and the relevant area documentation under `agents/`, `docs/skills.md`,
   or `workflows/`.
2. Determine the concrete user value and the smallest meaningful change scope.
3. Check whether a suitable definition already exists before creating a new one.
4. Keep assumptions visible when requirements are not fully specified.

## Rules for agents and skills

- An agent has exactly one primary role.
- A skill describes one reusable capability, not a general wish list.
- A workflow names order, handoffs, abort conditions, and success criteria.
- Inputs and outputs must be understandable and checkable by another agent.
- Security and permission boundaries belong in the definition, not only in the implementation.
- Vendor- or model-specific details are documented as adapters and not baked into domain rules.
- Never commit secrets, tokens, private keys, or real personal data.

## Way of working

- Answer briefly, concretely, and action-oriented.
- Prefer existing files, sources, and tools.
- Ask questions only when a wrong assumption would materially change scope, security, or result.
- Explicitly report uncertainties, missing sources, and checks that were not run.
- Avoid unnecessary abstractions, frameworks, and dependencies.
- Change only files that belong to the assignment.

## Definition of Done

A change is finished when:

- purpose and use are traceable in the appropriate README or template,
- responsibilities and boundaries are unambiguous,
- examples contain no sensitive data,
- cross-references and paths are correct,
- the change has been checked for inconsistencies and typos.
