# Agent Common

Agent Common is the reusable, project-agnostic foundation for building, operating, reviewing, and handing off agent systems.

## Goals

- Reusable agent and subagent structures across projects.
- Explicit human approval and override for risky, costly, or irreversible actions.
- Cybersecurity as a first-class architectural concern.
- Evidence-first delivery: tests, CI, reviews, auditability, and reproducible handoffs.
- Clear separation between planning, execution, review, and release authority.

## Core areas

- `docs/architecture.md` — system boundaries, orchestration, handoffs, and execution model.
- `docs/security.md` — trust model, approvals, audit requirements, and security gates.
- `docs/agent-contract.md` — baseline contract every reusable agent/subagent should satisfy.

## Operating principle

No agent should silently escalate authority. Actions with material security, financial, deployment, destructive, or external side effects must be gated, attributable, and reviewable.

## Status

Foundation bootstrap in progress.
