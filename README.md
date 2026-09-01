# Agent Common

A lean, framework-agnostic foundation for developing, documenting, and orchestrating agents.

## Purpose

Agent Common provides shared conventions so that agents:

- have clearly bounded tasks and responsibilities,
- reuse well-defined skills,
- work together in traceable workflows,
- document assumptions, sources, and results transparently,
- operate securely and with as little unnecessary complexity as possible.

The repository deliberately carries no binding to a particular model, SDK, or runtime yet.
Concrete integrations can be added later without restructuring the domain definitions.

## Structure

```text
.
├── AGENTS.md                       # Working rules for agents in this repository
├── agents/
│   ├── README.md                   # Conventions for agent definitions
│   ├── agent-template.md           # Copyable template for new agents
│   ├── orchestrator-agent.md       # Coordinates a multi-step change to verified handoff
│   └── review-agent.md             # Independently assesses a change and its evidence
├── skills/
│   ├── agent-common/               # General end-to-end working skill
│   └── host-workspace-operator/    # Safe host-native workspace operations
├── workflows/
│   ├── README.md                   # Conventions for agent workflows
│   └── change-delivery.md          # Intake → review → approval → handoff workflow
├── prompts/
│   └── agent-common.md             # Ready-to-use project prompt
├── templates/
│   └── task-brief.md               # Template for concrete tasks
├── schemas/
│   └── handoff.schema.json         # Machine-readable handoff contract
├── policy/
│   └── approval-policy.json        # Human-approval gates for high-impact actions
├── scripts/
│   ├── build_plugin_package.py     # Deterministic plugin-package build
│   └── verify_evidence.py          # Rebuild + check submission evidence
├── assets/                         # Brand assets (light/dark logo, composer icon)
├── submission/                     # Repository-maintained submission evidence
├── .codex-plugin/
│   └── plugin.json                 # Manifest for the skills-only plugin
├── .github/workflows/              # CI validation
└── docs/
    ├── architecture.md             # Architecture, lifecycle, and extension points
    ├── agent-contract.md           # What every reusable agent must declare
    ├── security.md                 # Security model and approval gates
    ├── skills.md                   # Conventions for reusable skills
    ├── brand-rationale.md          # Brand mark rationale
    └── plugin-experience.md        # Product boundary and plugin decisions
```

## Quick start

1. Read [AGENTS.md](AGENTS.md) before you add or change files.
2. Create a definition under `agents/` for each clearly bounded role.
3. Describe recurring capabilities under `skills/`.
4. Only compose multiple agents and skills into a workflow under `workflows/` once they exist.
5. Before committing, check that purpose, inputs, outputs, boundaries, and success criteria
   are unambiguous.

For general project work, the contents of
[`prompts/agent-common.md`](prompts/agent-common.md) can be used directly as a project
instruction. New assignments start from [`templates/task-brief.md`](templates/task-brief.md).
The bundled `skills-only` plugin provides the same flow in a Codex-compatible form.

## Core principles

- **Pragmatic:** the smallest solution that reliably covers the use case comes first.
- **Precise:** every definition names purpose, responsibility, inputs, outputs, and boundaries.
- **Autonomous:** agents work independently within their assignment and escalate only on
  genuine decision or security questions.
- **Traceable:** results include the relevant assumptions, sources, and open points.
- **Secure:** no secrets, credentials, or personal data in definitions, examples, or commits.
- **Composable:** skills provide capabilities; workflows connect them; agents take on roles.

## Status

This is a `0.1.0-beta.1` pre-release. The repository contains the project foundation,
reusable agents and workflows, a locally verifiable `skills-only` plugin, brand assets, and
a reproducible package build with matching evidence under [`submission/`](submission/).

A public plugin submission is **not** in scope for this beta and is intentionally not
released. The remaining steps are outside the repository and belong to the publisher:

- public website, customer-support, privacy-policy, and terms-of-service URLs
  (currently `null` in [`submission/listing.json`](submission/listing.json)),
- publisher verification in the OpenAI Platform,
- a country/region availability selection,
- any additionally required marketplace verification.

See [`docs/plugin-experience.md`](docs/plugin-experience.md) for the product boundary.

## Contributing

New content should:

- serve a concrete, recurring use case,
- use the existing templates and conventions,
- introduce no unnecessary runtime or vendor dependency,
- be described in a small, understandable commit.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md).
