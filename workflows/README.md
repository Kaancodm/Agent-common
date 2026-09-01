# Workflows

Workflows connect agents and skills into a traceable flow. They describe not only the order
but also the handoffs, decisions, and completion conditions.

## Minimum content

Every workflow should document:

- goal and trigger,
- participating agents and skills,
- inputs and expected final output,
- steps with clear handoffs,
- conditions for asking back, aborting, or escalating,
- security and permission boundaries,
- success criteria and verification.

## Recommended flow

```text
Input
  -> check context and permissions
  -> break the task into checkable steps
  -> run the matching agent/skill
  -> check the result
  -> return result, assumptions, and open points
```

## Conventions

Workflows are named in lowercase with hyphens. A workflow must not assume credentials that
are not described as secure runtime configuration. External or irreversible actions must be
explicitly marked and require a matching confirmation or permission.

If a workflow contains recurring steps, those steps belong in a skill rather than being
copied into multiple workflows.
