# Generate Run Commands: Python Project Examples

## Context

A Python project with the following detected structure:
- **Package manager:** pip with requirements.txt and setup.py
- **Test runner:** pytest (pytest.ini configured)
- **Linter:** pylint and black (configured in pyproject.toml)
- **Type checker:** mypy (mypy.ini present)

## Example 1: Run tests for a specific module

**Task:** "Test the validators module"

**Recommendation:**
```
pytest tests/test_validators.py -v
```

**Reasoning:** pytest is detected via pytest.ini. Running pytest with a specific test file path narrows the scope to only validators. The -v flag adds verbose output to help identify which tests ran and their results.

**Mode:** sync, initial_wait: 30

**Prerequisites:** pytest must be installed (pip install pytest or from requirements.txt)

**Caveats:** If tests are in a different directory or follow a different naming pattern, check pytest.ini for testpaths and python_files settings.

---

## Example 2: Lint with black (code formatter)

**Task:** "Format the src/ directory with black"

**Recommendation:**
```
black src/
```

**Reasoning:** black is a deterministic code formatter. Running it on a directory applies formatting rules to all .py files under that path. black exits with status 0 if no changes were needed, and non-zero if it reformatted files.

**Mode:** sync, initial_wait: 15

**Caveats:** black reformats in-place. Ensure the working tree is committed before running. If you want to preview changes without applying them, use `black --check src/` instead.

---

## Example 3: Type check a module

**Task:** "Check types in the api module"

**Recommendation:**
```
mypy src/api/
```

**Reasoning:** mypy is detected via mypy.ini. Running mypy on a specific directory path reports type errors found in that module without checking the entire codebase. This is faster and more targeted.

**Mode:** sync, initial_wait: 20

**Prerequisites:** mypy and its stubs must be installed. Configuration in mypy.ini or [mypy] section of pyproject.toml applies automatically.

---

## Example 4: Lint with pylint (comprehensive check)

**Task:** "Lint the entire codebase"

**Recommendation:**
```
pylint src/
```

**Reasoning:** pylint is a comprehensive linter that checks style, errors, and warnings. Running it on src/ (as opposed to individual files) provides a full report for the main codebase, excluding tests and build artifacts.

**Mode:** sync, initial_wait: 60

**Caveats:** pylint is thorough and can be slow on large codebases. If the project disables certain checks via .pylintrc or pyproject.toml [tool.pylint], those settings apply automatically. Some warnings may be false positives; check the project's pylint configuration before treating all warnings as blockers.

---

## Example 5: Run full test suite with coverage

**Task:** "Generate a test coverage report before release"

**Recommendation:**
```
pytest tests/ --cov=src --cov-report=html
```

**Reasoning:** Running the full test suite (tests/ directory) with --cov=src measures coverage of the src module. The --cov-report=html flag generates an HTML report. This is a full-suite run appropriate for a release gate.

**Mode:** sync, initial_wait: 120

**Prerequisites:** pytest and pytest-cov must be installed. The coverage report is written to htmlcov/ by default.

**Caveats:** Coverage thresholds can be configured in pytest.ini or pyproject.toml [tool.pytest]. If coverage falls below a threshold, pytest exits non-zero.

---

## Example 6: Run tests and linting together (CI simulation)

**Task:** "Run the full CI checks before pushing (tests, type check, format check)"

**Recommendation:**

For a complete CI simulation, run three separate commands in sequence:
```
pytest tests/ -v
mypy src/
black --check src/
```

Or as a single command string (for serial execution):
```
pytest tests/ -v && mypy src/ && black --check src/
```

**Reasoning:** Breaking these into separate commands allows each tool to complete and report independently. The && chaining ensures that if any command fails, the rest do not run. This mimics typical CI behavior.

**Mode:** sync, initial_wait: 180

**Caveats:** Some CI systems run checks in parallel for speed. This sequential approach is safer for local validation before pushing. If you want parallel execution, you would need orchestration (e.g., with a Makefile or tox).
