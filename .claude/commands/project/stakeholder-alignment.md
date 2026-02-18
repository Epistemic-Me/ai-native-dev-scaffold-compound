# Stakeholder Alignment

Run stakeholder alignment scoring for a PR against configured stakeholders.

## Prerequisites

- Clarity API credentials configured in `.env` (see `.env.example`)
- `compound.py` available at `$CLARITY_API_PATH/scripts/compound.py`
- Stakeholders configured in `scripts/compound_config.py` or `.stakeholders.json`
- Stakeholder self-models initialized (run `stakeholder_setup.py` first)

## Arguments

- PR number or folder path (optional — auto-detects from current branch)
- `--dry-run` — show what would be sent without calling the API

Example usage:
- `/project:stakeholder-alignment` — auto-detect current PR
- `/project:stakeholder-alignment 042` — specific PR number

## Instructions

1. **Check for Clarity API credentials**:
   - Look for `.env` file with `CLARITY_API_KEY` set
   - If not configured, inform user and stop (not an error)

2. **Find the PR folder**:
   - If PR number given, search `docs/prs/` for `*-PR-{num}-*`
   - If folder path given, use directly
   - If neither, detect from current branch name

3. **Verify REVIEW.md exists** in the PR folder:
   - REVIEW.md provides the content that gets scored against stakeholder goals
   - If missing, fall back to RESEARCH.md + IMPLEMENTATION.md

4. **Run stakeholder alignment**:
   ```bash
   python3 "${CLARITY_API_PATH}/scripts/compound.py" \
     --config-dir ./scripts \
     stakeholder-alignment "docs/prs/{pr-folder}/"
   ```

5. **Report results**:
   ```
   Stakeholder Alignment — PR #{num}

   | Stakeholder | Role | Score | App ID |
   |-------------|------|-------|--------|
   | {name} | {role} | {score}% | {app_id} |

   Aggregate Score: {weighted_average}%

   Full report: docs/prs/{folder}/STAKEHOLDER-ALIGNMENT.md
   ```

6. **Stage the alignment report**:
   ```bash
   git add docs/prs/{pr-folder}/STAKEHOLDER-ALIGNMENT.md
   ```
   (Don't commit — let the user decide when to commit)
