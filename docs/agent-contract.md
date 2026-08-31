# Agent Contract

Every reusable Agent Common agent or subagent should declare the following before execution.

## Identity and purpose

- Role name.
- Single primary responsibility.
- Explicit non-goals.

## Inputs

- Required context and artifacts.
- Assumptions that must be true.
- Trust level of external/retrieved input.

## Authority

- Allowed tools.
- Allowed repositories/services.
- Read/write scope.
- Cost/risk ceiling.
- Actions that require human approval.

## Output contract

Return:

1. work completed;
2. artifacts or refs changed;
3. verification evidence;
4. assumptions and decisions;
5. unresolved risks/blockers;
6. exact recommended next action.

## Safety rules

- Do not broaden scope or privileges implicitly.
- Do not treat tool availability as authorization.
- Stop at `PENDING_APPROVAL` for gated actions.
- Do not claim tests, reviews, CI, or deployments passed without evidence.
- Surface uncertainty that affects correctness or security.

## Handoff quality

A different agent or human should be able to continue from the handoff without reconstructing hidden context. Prefer concrete refs, paths, commands, evidence, and decision rationale over narrative summaries.
