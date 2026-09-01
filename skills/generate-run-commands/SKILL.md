# Generate Run Commands

## Purpose

Produce the smallest, targeted, and most appropriate CLI command or build/test invocation for a given task, based on the project's existing tools, configuration, and context.

## Responsible for

- Identifying the project's available tooling (package managers, build systems, test runners, linters, compilers)
- Selecting the minimal, targeted command that covers the requested scope
- Recommending parallelization or efficiency improvements when applicable
- Documenting any assumptions about tool versions, configurations, or dependencies
- Suggesting escalation to full-suite runs only when targeted commands show they are needed

## Not responsible for

- Installing, upgrading, or managing tool versions (that is part of task setup)
- Running commands or validating their output (execution belongs to the calling agent)
- Changing project configuration, build systems, or tool settings
- Making decisions about which tools the project should use (that is architecture)

## Inputs

- **Required:**
  - Task or scope description (e.g., "test the auth module", "lint the TypeScript files", "build for production")
  - Project type or detected tooling (e.g., Node.js with npm, Python with pytest, Rust with cargo, .NET with dotnet)

- **Optional:**
  - Specific file or directory filter (narrows the scope)
  - Environmental constraints (e.g., Windows-only, CI/CD context, resource limits)
  - Prior tool output or error messages (helps select more precise variants)
  - Existing `.codex-plugin` manifests or project metadata

- **Context:**
  - Package manifest files (package.json, pyproject.toml, Cargo.toml, .csproj, etc.)
  - Build/test configuration files (tsconfig.json, pytest.ini, .eslintrc, etc.)
  - CI/CD workflow files (.github/workflows/, .gitlab-ci.yml, etc.)
  - Project README or contributing guide

## Outputs

- The recommended command (as a single-line string, shell-agnostic unless context requires it)
- The command execution mode (sync/async, attach/detach)
- Reasoning: which tool was selected, why, and what scope it covers
- Any constraints or prerequisites (e.g., "requires Node.js 18+", "must run from repo root")
- If multiple good options exist, brief comparison with trade-offs
- Caveats: what the command will and will not do, and when escalation to full-suite is recommended

## Workflow

1. Parse the task scope and constraints from the request
2. Inspect the project structure and detect available tools
3. Map the requested task to the appropriate tool and its flags/options
4. Select the minimal targeted invocation (not full-suite runs unless justified)
5. Cross-check against any prior recommendations or tool documentation for that project
6. Return the command with its rationale and any caveats

## Tools and sources

- Package manifests and lock files (source of truth for tooling)
- Project configuration files (.eslintrc, tsconfig.json, pytest.ini, setup.cfg, etc.)
- Build system documentation (npm, cargo, python setuptools, MSBuild, Makefile, etc.)
- Test framework documentation (jest, pytest, RSpec, xUnit, etc.)
- CI/CD workflows (to understand the full-suite baseline and check what already passes)
- Project README and CONTRIBUTING guides

## Security boundaries

- Disallowed: running any command; only generate the command string
- Disallowed: installing packages or dependencies (that is task setup)
- Disallowed: modifying project files or configuration
- Allowed: reading package manifests, build configs, and CI definitions to understand what tools exist
- Allowed: recommending that certain tests or builds be skipped if they are known to be slow or unreliable
- Store no secrets or real personal data in results; only document tool names, version constraints, and command-line flags

## Success criteria

- [ ] The recommended command is the smallest targeted run that covers the requested scope
- [ ] The command is tool-specific and references actual project tooling (not generic examples)
- [ ] The command syntax is accurate for the detected tool and version
- [ ] Constraints and prerequisites are clearly stated
- [ ] If the task would benefit from multiple runs or a different tool, that trade-off is documented
- [ ] The reasoning explains which files or configuration informed the choice

## Escalation

Escalate only when:
- The project structure is ambiguous or missing key configuration files (ask the calling agent to clarify the project type)
- No suitable targeted tool is detected (recommend a full-suite fallback and ask if the project uses alternative tooling)
- The requested scope conflicts with existing tool capabilities (document the conflict and ask for clarification)

When in doubt, document the assumption (e.g., "assuming the project uses jest because jest.config.js is present") and include it in the result.
