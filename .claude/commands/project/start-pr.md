# Start PR

Create a feature branch and paper trail folder for a new PR.

## Arguments

The user should provide:
- PR number (e.g., "036")
- Short slug describing the PR (e.g., "feature-name")

Example usage: `/project:start-pr 036 feature-name`

## Instructions

1. **Get today's date** in YYYY-MM-DD format

2. **Create feature branch**:
   ```bash
   git checkout -b feature/pr-{num}-{slug}
   ```
   Example: `git checkout -b feature/pr-036-feature-name`

3. **Create PR folder**:
   ```
   docs/prs/{date}-PR-{num}-{slug}/
   ```
   Example: `docs/prs/2025-01-15-PR-036-feature-name/`

4. **Create RESEARCH.md** with this template:

```markdown
# PR #{num}: {slug} - Research

**Created**: {date}
**Author**: @{get from git config}
**Branch**: `feature/pr-{num}-{slug}`

## Problem Statement

{To be filled: What problem are we solving? Why now?}

## Context Gathered

### Existing Code
- {To be filled: Relevant files and patterns}

### Related Work
- {To be filled: Related PRs, decisions}

### User/Business Context
- {To be filled: Relevant user feedback, business requirements}

## Options Considered

### Option A: {Name}
- **Approach**:
- **Pros**:
- **Cons**:
- **Effort**: {Low|Medium|High}

### Option B: {Name}
- **Approach**:
- **Pros**:
- **Cons**:
- **Effort**:

## Recommendation

{To be filled after research}

## Open Questions

- [ ] {Questions to answer before planning}
```

5. **Create PLAN.md** with this template:

```markdown
# PR #{num}: {slug} - Plan

**Created**: {date}
**Based on**: [RESEARCH.md](./RESEARCH.md)
**Branch**: `feature/pr-{num}-{slug}`

## Chosen Approach

{To be filled after research complete}

## Scope

### In Scope
-

### Out of Scope
-

## Technical Design

### Changes Required

| File | Change | Why |
|------|--------|-----|
| | | |

### New Files

| File | Purpose |
|------|---------|
| | |

## Implementation Order

1.
2.
3.

## Testing Strategy

- [ ]

## Rollback Plan

{How to revert if needed}

## Definition of Done

- [ ] Code complete
- [ ] Tests passing
- [ ] Documentation updated
- [ ] GitHub PR created
- [ ] PR reviewed and approved
- [ ] PR merged
```

6. **Create IMPLEMENTATION.md** with this template:

```markdown
# PR #{num}: {slug} - Implementation

**Status**: In Progress
**Based on**: [PLAN.md](./PLAN.md)
**Branch**: `feature/pr-{num}-{slug}`
**GitHub PR**: {to be filled when PR created}

## Summary

{To be filled when PR complete}

## Key Changes

### {Component/Area}
-

## Deviations from Plan

| Planned | Actual | Reason |
|---------|--------|--------|
| | | |

## Testing Done

- [ ]

## Learnings

### What Worked Well
-

### What Was Harder Than Expected
-

### What We'd Do Differently
-

## Follow-up Items

- [ ]

---
*PR Merged: {to be filled}*
```

7. **Create REVIEW.md** with this template:

```markdown
# PR #{num}: {slug} - Review

**Reviewed**: {date}
**PR Branch**: `feature/pr-{num}-{slug}`
**Reviewer**: @{reviewer}

## Overview

{Brief summary of what this PR does and why}

## Code Quality Assessment

### Architecture & Design
- [ ] Changes follow existing patterns
- [ ] No unnecessary complexity introduced
- [ ] Appropriate separation of concerns

### Testing
- [ ] New code has adequate test coverage
- [ ] Edge cases considered
- [ ] Tests are meaningful (not just for coverage)

### Security
- [ ] No credentials or secrets in code
- [ ] Input validation where needed
- [ ] No injection vulnerabilities

## Observations

### What Went Well
-

### Concerns
-

### Suggestions
-

## Compound Loop Data (optional)

### Observation Context Changes

{Which observation contexts did this PR advance? Reference scripts/compound_config.py for context IDs.}

| Context | Before | After | Confidence |
|---------|--------|-------|------------|
| | | | |

### Beliefs

{Key beliefs or assumptions validated/invalidated by this PR.}

- **Belief**: {description}
  - **Status**: validated | invalidated | uncertain
  - **Evidence**: {what evidence supports this}

## Verdict

- [ ] **Approve** - Ready to merge
- [ ] **Request Changes** - Issues to address
- [ ] **Comment** - Discussion needed
```

8. **Update ACTIVE_PRS.md**:
   - Add entry for this PR in the "Open PRs" section
   - Include link to paper trail folder and branch name

9. **Stage and commit the paper trail**:
   ```bash
   git add docs/prs/{date}-PR-{num}-{slug}/
   git commit -m "docs: start PR #{num} - {slug}"
   ```

10. **Report to user** what was created:
   ```
   PR #{num} Started

   Branch: feature/pr-{num}-{slug}
   Paper Trail: docs/prs/{date}-PR-{num}-{slug}/

   Next steps:
   1. Fill in RESEARCH.md with problem statement
   2. Complete PLAN.md with implementation details
   3. Run /project:implement-pr {num} to implement
   4. Or run /project:execute-pr {num} for full lifecycle
   ```
