# Architecture

## Guiding idea

Agent Common separates domain description from technical execution:

- Agents define roles and responsibility boundaries.
- Skills define reusable capabilities.
- Workflows define order and handoffs.
- Adapters connect these definitions to models, tools, or runtimes later.

This lets domain rules be maintained and tested independently of any single vendor.

## Lifecycle

1. **Requirement:** describe goal, user value, and boundaries.
2. **Definition:** create the agent, skill, or workflow from the appropriate template.
3. **Review:** sharpen inputs, outputs, risks, and success criteria.
4. **Adapter:** add a technical execution only when needed.
5. **Verification:** check behavior with synthetic examples and realistic failure cases.
6. **Maintenance:** document changes to contracts and dependencies traceably.

## Extension points

The initial structure allows later additions:

- `adapters/` for model, tool, or runtime integrations,
- `tests/` for structured definition tests,
- `examples/` for complete, synthetic runs,
- `config/` for non-secret, environment-independent configuration.

These directories are introduced only when there is a concrete need. Empty placeholder
folders are not versioned. `scripts/` already exists and holds the deterministic
plugin-package build and the evidence-verification tooling.

## Security model

Definitions may describe which permissions a flow needs. Secrets and concrete credentials
belong exclusively in the secure runtime environment. Actions with external or irreversible
effects must be recognizable as such; an agent must not silently assume the permission
required for them.
