# Generate Run Commands: Node.js Project Examples

## Context

A Node.js project with the following detected structure:
- **Package manager:** npm (package.json, package-lock.json present)
- **Test runner:** Jest (jest.config.js, tests in __tests__/)
- **Linter:** ESLint (.eslintrc.js configured)
- **Build system:** TypeScript compiler and rollup (tsconfig.json, build script in package.json)

## Example 1: Test a single module

**Task:** "Run tests for the auth module only"

**Recommendation:**
```
npm test -- auth
```

**Reasoning:** Jest is detected via jest.config.js. `npm test` maps to the "test" script in package.json. The `-- auth` suffix passes a pattern filter to Jest to match only auth-related test files. This is a targeted run that avoids running the full test suite.

**Mode:** sync, initial_wait: 60 (tests may take a minute or more)

**Caveats:** This assumes Jest's default pattern matching. If the project uses a custom Jest config that doesn't match test files by directory name, the command may not work as expected. Recommend checking jest.config.js for testMatch patterns.

---

## Example 2: Lint only TypeScript files

**Task:** "Lint the src/ directory"

**Recommendation:**
```
npm run lint -- src/
```

**Reasoning:** ESLint is detected via .eslintrc.js. Running the lint script with a directory argument applies ESLint only to that path. This avoids linting the entire project (including node_modules, dist, etc.).

**Mode:** sync, initial_wait: 10

**Caveats:** Assumes a "lint" script exists in package.json. If not, recommend `npx eslint src/` as a fallback.

---

## Example 3: Build for production

**Task:** "Build the project for production"

**Recommendation:**
```
npm run build
```

**Reasoning:** The build script in package.json typically handles TypeScript compilation, bundling with rollup, and minification. Running the standard build command is the correct full-suite approach for a production build; no targeted filtering makes sense here.

**Mode:** sync, initial_wait: 120

**Prerequisites:** npm install must have been run and all dependencies resolved.

---

## Example 4: Run linter with fix enabled

**Task:** "Fix linting errors in the utils module"

**Recommendation:**
```
npm run lint -- --fix src/utils/
```

**Reasoning:** ESLint supports a --fix flag to auto-correct style and formatting violations. The targeted path ensures only the utils module is processed, reducing risk and time.

**Mode:** sync, initial_wait: 10

**Caveats:** --fix writes to disk and is a modifying operation. Ensure the working tree is committed before running. Some violations may require manual fixes and will be reported but not auto-corrected.

---

## Example 5: Run a full test suite (escalation case)

**Task:** "Test the entire codebase before releasing"

**Recommendation:**
```
npm test -- --coverage
```

**Reasoning:** A release requires comprehensive testing. The --coverage flag generates a coverage report alongside the test output. A full-suite run (without pattern filters) is appropriate here. This is an escalation from targeted runs because the scope is intentionally complete.

**Mode:** sync, initial_wait: 180 (coverage reporting adds overhead)

**Caveats:** Coverage reports may fail if code is not instrumented correctly. Check that istanbul or the configured coverage tool is installed.
