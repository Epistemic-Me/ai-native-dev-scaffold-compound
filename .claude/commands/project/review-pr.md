# Review PR (Run Level)

AI code review + stakeholder alignment + compound extraction + docs-gate + merge + close.

This is the exit command. Same as Walk's review-pr, but automatically runs stakeholder alignment and compound extraction before merging.

## Arguments

- PR number (e.g., "042")

Example: `/project:review-pr 042`

## What This Command Does

1. AI code review → REVIEW.md
2. Stakeholder alignment → STAKEHOLDER-ALIGNMENT.md (auto)
3. Compound extraction → compound_extract.json (auto)
4. Enhanced docs-gate check
5. If approved: merge → archive → compound sync → close
6. If issues: report what to fix, do NOT merge

## Instructions

### 1. Find the PR

```bash
gh pr view --json number,title,state,headRefName
```

Find the PR docs folder in `docs/prs/implementing/` matching `*-PR-{num}-*`.

### 2. AI Code Review

**Spawn a sub-agent** (Agent tool) with a clean context window. The sub-agent:

a. Reads project context:
   - `CLAUDE.md`
   - `docs/.context/ARCHITECTURE-TAXONOMY.md` (if exists)
   - `docs/.context/KNOWN_ISSUES.md` (if exists)
   - `docs/.context/ROADMAP.md` (if exists)

b. Reads the PR docs:
   - `RESEARCH.md` — what problem is being solved
   - `TEST-STRATEGY.md` — what the acceptance criteria are
   - `IMPLEMENTATION-PLAN.md` — what the implementation approach was
   - `IMPLEMENTATION.md` — what was actually built

c. Gets the PR diff: `gh pr diff {num}`

d. Reviews: correctness, AC coverage, architecture, risk

e. Returns structured review between `---BEGIN REVIEW---` and `---END REVIEW---`.

Write REVIEW.md with verdict, per-AC coverage table, issues, risk assessment.

### 3. Stakeholder Alignment (Run-level auto)

If `CLARITY_API_KEY` is set and `.stakeholders.json` or `scripts/compound_config.py` has stakeholder definitions:

```bash
set -a && source .env && set +a
python scripts/compound.py stakeholder-alignment --pr-folder {docs_folder}
```

This fires perspective-taking API calls against all configured stakeholder twins in parallel. Produces `STAKEHOLDER-ALIGNMENT.md` in the PR docs folder.

If API is not configured, skip this step with a note: "Stakeholder alignment skipped (no CLARITY_API_KEY)."

### 4. Compound Extraction (Run-level auto)

If `CLARITY_API_KEY` is set:

```bash
set -a && source .env && set +a
python scripts/compound.py extract {docs_folder}
```

Produces `compound_extract.json` in the PR docs folder.

If API is not configured, skip with a note.

### 5. Enhanced Docs-Gate Check

```bash
python scripts/pr_docs_check.py {num}
```

Run-level checks (blocking):
1. RESEARCH.md exists (>50 bytes)
2. TEST-STRATEGY.md exists (>50 bytes)
3. IMPLEMENTATION-PLAN.md exists (>50 bytes)
4. REVIEW.md exists with Approve verdict
5. STAKEHOLDER-ALIGNMENT.md exists with Aggregate Score

Advisory (non-blocking):
- compound_extract.json exists
- Stakeholder scores below 0.3

### 6. Decision Point

**If Approve + gate passes:**
Tell user. If confirmed, proceed to merge.

**If issues found:**
Report and stop.

### 7. Merge & Close

```bash
gh pr merge {num} --squash --delete-branch
git checkout main && git pull origin main
```

### 8. Compound Sync (Run-level auto)

If compound_extract.json exists and API is configured:

```bash
set -a && source .env && set +a
python scripts/compound.py sync {docs_folder}/compound_extract.json
```

### 9. Archive & Update Indexes

```bash
git mv docs/prs/implementing/{folder} docs/prs/_archive/{folder}
```

Update `docs/.context/ACTIVE_PRS.md`. Check for ADR-worthy decisions.

### 10. Report

```
PR #{num} MERGED AND CLOSED

GitHub PR: {url}
Verdict: Approved
Stakeholder Score: {aggregate} (or "skipped")
Compound: {synced/skipped}
Docs: Archived

Updated: ACTIVE_PRS.md, REVIEW.md, STAKEHOLDER-ALIGNMENT.md
```
