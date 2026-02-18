# Compound Loop

Run the compound self-reflection loop for a PR: extract episodes/beliefs, run stakeholder alignment, sync to Clarity API, and generate report.

## Prerequisites

- Clarity API credentials configured in `.env` (see `.env.example`)
- `compound.py` available at `$CLARITY_API_PATH/scripts/compound.py`
- Python 3.8+ with `requests` and `pyyaml` installed
- Builder self-model initialized (run `compound.py init` first)

If credentials are not configured, skip this command — PR lifecycle works without it.

## Arguments

- PR number or folder path (optional — auto-detects from current branch)
- `--dry-run` — show what would happen without calling the API
- `--skip-align` — skip stakeholder alignment step
- `--skip-sync` — extract only, don't sync to API
- `--report-only` — just regenerate the compound report

Example usage:
- `/project:compound` — auto-detect current PR
- `/project:compound 042` — specific PR number
- `/project:compound --report-only` — just refresh the report

## Instructions

### Pre-flight Check

1. **Check for Clarity API credentials**:
   - Look for `.env` file with `CLARITY_API_KEY` set
   - If not configured, inform user:
     ```
     Compound loop requires Clarity API credentials.
     See .env.example and GETTING-STARTED.md for setup instructions.
     Skipping compound loop — PR lifecycle continues without it.
     ```
   - Stop here if credentials missing (this is not an error)

2. **Verify compound.py is available**:
   ```bash
   test -f "${CLARITY_API_PATH}/scripts/compound.py" && echo "found" || echo "not found"
   ```
   - If not found, inform user to set `CLARITY_API_PATH` environment variable
   - Point them to GETTING-STARTED.md

### Phase 1: Extract

3. **Find the PR folder**:
   - If PR number given, search `docs/prs/` for `*-PR-{num}-*`
   - If folder path given, use directly
   - If neither, detect from current branch name (`feature/pr-{num}-*`)

4. **Verify REVIEW.md exists** in the PR folder:
   - If missing, warn user: "REVIEW.md not found — compound extract needs review data"
   - Suggest filling in REVIEW.md first, or at minimum the "Compound Loop Data" section

5. **Run extract**:
   ```bash
   python3 "${CLARITY_API_PATH}/scripts/compound.py" \
     --config-dir ./scripts \
     extract "docs/prs/{pr-folder}/"
   ```
   - This produces `compound_extract.json` in the PR folder
   - Report what was extracted: episode summary, beliefs found, context transitions

### Phase 2: Stakeholder Alignment (unless --skip-align)

6. **Run stakeholder alignment**:
   ```bash
   python3 "${CLARITY_API_PATH}/scripts/compound.py" \
     --config-dir ./scripts \
     stakeholder-alignment "docs/prs/{pr-folder}/"
   ```
   - This produces `STAKEHOLDER-ALIGNMENT.md` in the PR folder
   - Report alignment scores for each stakeholder

### Phase 3: Sync (unless --skip-sync or --dry-run)

7. **Sync extract to Clarity API**:
   ```bash
   python3 "${CLARITY_API_PATH}/scripts/compound.py" \
     --config-dir ./scripts \
     sync "docs/prs/{pr-folder}/compound_extract.json"
   ```
   - Report sync result: session ID, episode count, belief count

### Phase 4: Report

8. **Generate compound report**:
   ```bash
   python3 "${CLARITY_API_PATH}/scripts/compound.py" \
     --config-dir ./scripts \
     report
   ```
   - This produces/updates `docs/.context/COMPOUND_REPORT.md`
   - Report current state vs target state for each observation context

### Commit

9. **Stage and commit compound artifacts**:
   ```bash
   git add docs/prs/{pr-folder}/compound_extract.json \
           docs/prs/{pr-folder}/STAKEHOLDER-ALIGNMENT.md \
           docs/.context/COMPOUND_REPORT.md
   git commit -m "docs: compound loop for PR #{num}"
   ```

### Report

10. **Print summary**:
    ```
    Compound Loop Complete — PR #{num}

    Extract:
    - Episode: {summary}
    - Beliefs: {count} extracted
    - Context: {primary_context} ({from} → {to})

    Stakeholder Alignment:
    - {stakeholder1}: {score}%
    - {stakeholder2}: {score}%
    - Aggregate: {aggregate_score}%

    Report: docs/.context/COMPOUND_REPORT.md (updated)

    Artifacts:
    - docs/prs/{folder}/compound_extract.json
    - docs/prs/{folder}/STAKEHOLDER-ALIGNMENT.md
    - docs/.context/COMPOUND_REPORT.md
    ```
