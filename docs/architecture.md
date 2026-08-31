# Architecture

## Purpose

Agent Common provides reusable control-plane patterns for agentic systems without coupling them to one product or repository.

## Roles

- **Orchestrator**: decomposes work, assigns scoped tasks, tracks state, and assembles evidence.
- **Worker agent**: executes a narrowly scoped task with explicitly granted tools and permissions.
- **Reviewer**: independently checks correctness, security, and evidence before promotion.
- **Human authority**: approves or overrides actions that cross configured risk, cost, deployment, or destructiveness thresholds.

## Execution lifecycle

1. Orient to repository, task, constraints, and current evidence.
2. Produce a scoped plan with explicit assumptions and acceptance criteria.
3. Delegate only bounded tasks with defined inputs, outputs, and authority.
4. Execute changes in isolated branches or workspaces where practical.
5. Verify with tests, CI, static analysis, security checks, and review evidence.
6. Require approval for gated actions.
7. Produce a reproducible handoff containing state, decisions, evidence, and unresolved risks.

## State model

Recommended states:

- `PLANNED`
- `IN_PROGRESS`
- `BLOCKED`
- `PENDING_APPROVAL`
- `VERIFYING`
- `READY_FOR_REVIEW`
- `DONE`

State transitions that create external side effects should be attributable and auditable.

## Handoff contract

Every handoff should include:

- objective and scope;
- current branch/ref and relevant artifacts;
- completed work and evidence;
- pending work and blockers;
- security/risk notes;
- exact next action.
