# Execute PR

Implement the plan with progress tracking. This is the "code" phase — you've already filled RESEARCH.md, TEST-STRATEGY.md, and IMPLEMENTATION-IMPLEMENTATION-PLAN.md. Now execute.

## Arguments

- PR number (e.g., "042")

Example: `/project:execute-pr 042`

## Prerequisites

Before running this command, ensure these docs are filled:
1. **RESEARCH.md** — problem understood, options considered, recommendation made
2. **TEST-STRATEGY.md** — acceptance criteria defined, test matrix mapped
3. **IMPLEMENTATION-IMPLEMENTATION-PLAN.md** — step-by-step implementation mapped to ACs

If any are empty, stop and fill them first. The thinking happens BEFORE this command.

## Instructions

### 1. Find the PR folder

Search `docs/prs/planning/` and `docs/prs/implementing/` for a folder matching `*-PR-{num}-*`.

If found in `planning/`:
- Move to `implementing/`: `git mv docs/prs/planning/{folder} docs/prs/implementing/{folder}`
- Commit: `git commit -m "docs: move PR #{num} to implementing"`

If found in `implementing/`: resume where we left off.

### 2. Verify docs are ready

Check that IMPLEMENTATION-IMPLEMENTATION-PLAN.md has:
- A scope section (in/out)
- Implementation steps
- A definition of done or verification checklist

If incomplete, tell the user what's missing and stop.

### 3. Implement from IMPLEMENTATION-IMPLEMENTATION-PLAN.md

- Read IMPLEMENTATION-IMPLEMENTATION-PLAN.md step by step
- Create a task list (TodoWrite) from the implementation steps
- Execute each task:
  - Write the code
  - Run relevant tests
  - Commit incrementally on the feature branch
- Track progress: "Step 3/7 complete"

### 4. Update IMPLEMENTATION.md

As you work, update IMPLEMENTATION.md with:
- Summary of what was built
- Key changes (files modified/created)
- Any deviations from the plan and why
- Learnings

### 5. Handle blockers

If you encounter a blocker:
- Log it in IMPLEMENTATION.md
- Ask the user how to proceed
- Don't skip steps or make assumptions about blocked work

### 6. Push when done

```bash
git add -A
git commit -m "feat: {brief description}"
git push -u origin {branch-name}
```

Create GitHub PR if one doesn't exist:
```bash
gh pr create --title "PR #{num}: {title}" --body "See docs/prs/implementing/{folder}/"
```

### 7. Report

```
PR #{num} implementation complete.

Tasks: {X}/{X} completed
Branch: {branch}
GitHub PR: {url}

Next step: /project:review-pr {num}
```
