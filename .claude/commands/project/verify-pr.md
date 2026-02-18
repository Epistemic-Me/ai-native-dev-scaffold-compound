# Verify PR

Run all available verification checks before closing a PR.

## Arguments

- PR number (e.g., "002")

Example usage: `/project:verify-pr 002`

## Instructions

1. **Announce verification starting**:
   ```
   Verifying PR-{num}...
   ```

2. **Detect available checks**:
   - Look at `package.json` scripts for: lint, typecheck, test, test:coverage, build
   - Look at `Makefile` for: lint, test, check targets
   - Look at `pyproject.toml` / `setup.cfg` for Python projects: pytest, mypy, ruff/flake8
   - Look at `Cargo.toml` for Rust projects: cargo check, cargo test, cargo clippy
   - Use whatever verification tools the project has configured

3. **Run lint check** (if available):
   ```bash
   # Example: npm run lint, make lint, ruff check ., cargo clippy
   ```
   - Record pass/fail

4. **Run type check** (if available):
   ```bash
   # Example: npm run typecheck, mypy ., cargo check
   ```
   - Record pass/fail

5. **Run tests** (if available):
   ```bash
   # Example: npm test, pytest, cargo test, make test
   ```
   - Record pass/fail
   - Note coverage percentages if available

6. **Run build check** (if available):
   ```bash
   # Example: npm run build, cargo build, make build
   ```
   - Record pass/fail

7. **Report results**:
   ```
   PR-{num} Verification Results

   | Check     | Status | Notes          |
   |-----------|--------|----------------|
   | Lint      | PASS/FAIL/N/A |         |
   | TypeCheck | PASS/FAIL/N/A |         |
   | Tests     | PASS/FAIL/N/A | {coverage}% |
   | Build     | PASS/FAIL/N/A |         |

   Overall: PASS/FAIL
   ```

8. **If any failures**:
   - List specific errors
   - Do NOT proceed to close-pr
   - Suggest fixes for each failure

9. **If all pass**:
   - Report success
   - Suggest: "Ready to close. Run `/project:close-pr {num}` or `/project:execute-pr {num} --skip-start`"

## Exit Codes

- **PASS**: All available checks green, safe to close PR
- **FAIL**: One or more checks failed, must fix before closing
