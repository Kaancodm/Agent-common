# Security Model

## Security objectives

Agent Common treats cybersecurity as a core system property, not an afterthought.

Primary objectives:

- least privilege for every agent and tool;
- explicit authorization boundaries;
- prevention of silent privilege escalation;
- auditable high-impact actions;
- secure handling of secrets and external systems;
- independent verification before release or destructive operations.

## Trust boundaries

Agents, tools, external services, repositories, user input, retrieved content, generated code, and deployment environments are separate trust domains. Data crossing a boundary should be validated according to its risk.

## Approval gates

Require human approval before actions that are materially:

- destructive or difficult to reverse;
- security-sensitive or privilege-changing;
- financially consequential;
- production/deployment related;
- externally communicative on the user's behalf;
- capable of exposing secrets or private data.

The default gated state is `PENDING_APPROVAL`.

## Tool policy

Each task should grant only the minimum tools and permissions required. Tool access must not imply blanket authorization to use every available capability.

## Secrets

- Never commit secrets to source control.
- Prefer environment/secret managers over plaintext configuration.
- Redact credentials from logs and handoffs.
- Rotate a credential if exposure is suspected.

## Verification gates

Before promotion or release, collect relevant evidence such as:

- tests;
- CI status;
- lint/static analysis;
- dependency/security scanning;
- reviewer findings;
- deployment or smoke-test results when applicable.

A claim of readiness should reference evidence rather than agent confidence alone.

## Audit record

For gated decisions record, where applicable:

- actor;
- requested action;
- scope and target;
- risk/cost rationale;
- approval or override decision;
- resulting evidence and outcome.
