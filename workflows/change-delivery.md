# Change Delivery Workflow

## Goal

Provide a reusable path for taking a repository or system change from intake through implementation, independent review, approval gates, and evidence-backed handoff.

## Trigger

Use this workflow when a requested change has multiple meaningful steps, affects shared behavior, or needs a reviewable handoff.

## Roles

- `agents/orchestrator-agent.md`: owns decomposition, delegation, state, evidence collection, and handoff.
- Implementing agent or skill: owns one bounded execution task.
- `agents/review-agent.md`: independently evaluates the change and evidence.
- Human approver: decides actions gated by `policy/approval-policy.json`.

## Inputs

- objective and expected outcome;
- target repository/service and current ref;
- constraints, deadline, and cost/risk ceiling;
- available tools and explicit permissions;
- relevant existing artifacts and prior handoff.

## State model

Use the states defined by `schemas/handoff.schema.json`:

`PLANNED -> IN_PROGRESS -> VERIFYING -> READY_FOR_REVIEW -> DONE`

A task may enter `BLOCKED` at any point. Any gated action must enter `PENDING_APPROVAL` before execution.

## Steps

### 1. Intake and boundary check

The orchestrator confirms scope, target, success criteria, permissions, and trust boundaries. It checks the approval policy before any mutation.

Exit condition: objective and execution boundary are explicit.

### 2. Decomposition

Break the objective into the smallest independently verifiable tasks. Assign one primary owner to each task and identify required evidence in advance.

Exit condition: each task has owner, inputs, expected output, and verification method.

### 3. Execute bounded tasks

Implementers work only within assigned scope and authority. After each material change, record artifacts or refs changed and verification performed.

If a gated action becomes necessary, stop with `PENDING_APPROVAL` and return the requested action, target, rationale, risk/cost, and expected effect.

Exit condition: implementation tasks are complete or explicitly blocked.

### 4. Verification

Run the checks appropriate to the change, such as tests, CI, static analysis, policy validation, security scanning, diff inspection, or smoke tests.

Do not convert missing evidence into a success claim.

Exit condition: evidence is collected and failures are resolved or recorded.

### 5. Independent review

The review agent examines the intended outcome, changed artifacts, security/approval boundaries, and verification evidence.

- `APPROVE`: continue.
- `REQUEST_CHANGES`: return findings to the relevant implementer and repeat verification.
- `BLOCKED`: stop and surface the blocker.

Exit condition: review disposition is explicit.

### 6. Final gated action

If merge, deployment, publication, destructive mutation, meaningful spend, privilege change, or external communication is gated by policy, require the human decision here.

Exit condition: approval state is recorded and any approved action is verified after execution.

### 7. Handoff

Produce a handoff conforming to `schemas/handoff.schema.json` with:

- objective and scope;
- state and current ref;
- completed work;
- evidence;
- decisions and assumptions;
- risks;
- approval state;
- exact next action.

## Abort and escalation conditions

Stop or escalate when:

- required authority is missing;
- the requested scope conflicts with repository rules;
- a secret or sensitive-data exposure is suspected;
- verification fails and cannot be resolved inside scope;
- a required human approval is absent;
- external state has changed enough that prior assumptions are no longer reliable.

## Success criteria

- Scope and permissions stayed bounded.
- Gated actions have an auditable decision.
- Shared or security-relevant changes received independent review.
- Readiness claims are supported by evidence.
- The final handoff is sufficient for another agent or human to continue without hidden context.
