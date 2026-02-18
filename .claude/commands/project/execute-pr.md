# Execute PR

Master orchestrator that runs the complete PR lifecycle from start to finish, creating an actual GitHub Pull Request.

## Arguments

- PR number (e.g., "036")
- Optional: `--skip-start` if PR folder already exists
- Optional: `--skip-verify` to skip verification (not recommended)
- Optional: `--skip-compound` to skip compound loop

Example usage:
- `/project:execute-pr 036` - Full lifecycle
- `/project:execute-pr 036 --skip-start` - PR already started, just implement

## Workflow Chain

```
┌─────────────────────────────────────────────────────────────┐
│                    /project:execute-pr                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. CHECK EXISTING STATE                                     │
│     └─► Does PR folder exist?                                │
│         ├─► No: Run /project:start-pr (creates branch)       │
│         └─► Yes: Checkout existing branch                    │
│                                                              │
│  2. IMPLEMENT (/project:implement-pr)                        │
│     ├─► Read PLAN.md                                         │
│     ├─► Create/Update IMPLEMENTATION.md                      │
│     ├─► Parse tasks → TodoWrite                              │
│     ├─► Execute each task                                    │
│     ├─► Track progress                                       │
│     └─► Update docs as we go                                 │
│                                                              │
│  3. VERIFY (/project:verify-pr)                              │
│     ├─► Run lint/typecheck/tests/build                       │
│     └─► All must PASS to continue                            │
│                                                              │
│  4. PUSH & CREATE GITHUB PR                                  │
│     ├─► git push -u origin feature/pr-{num}-{slug}           │
│     ├─► gh pr create --title "..." --body "..."              │
│     └─► Update IMPLEMENTATION.md with PR URL                 │
│                                                              │
│  5. USER APPROVAL GATE                                       │
│     └─► "GitHub PR created. Ready for review?"               │
│         ├─► Yes: Continue to merge                           │
│         └─► No: Stop here, wait for review                   │
│                                                              │
│  6. MERGE & CLOSE (/project:close-pr)                        │
│     ├─► gh pr merge --squash                                 │
│     ├─► Update IMPLEMENTATION.md                             │
│     ├─► Update ACTIVE_PRS.md                                 │
│     ├─► Check for architectural decisions → ADR creation     │
│     └─► Delete feature branch                                │
│                                                              │
│  7. COMPOUND LOOP (optional, /project:compound)              │
│     ├─► Extract episodes/beliefs from REVIEW.md              │
│     ├─► Run stakeholder alignment                            │
│     ├─► Sync to Clarity API                                  │
│     └─► Generate compound report                             │
│                                                              │
│  8. UPDATE CONTEXT (/project:context-update)                 │
│     ├─► Refresh ACTIVE_PRS.md                                │
│     └─► Refresh RECENT_DECISIONS.md                          │
│                                                              │
│  9. REPORT                                                   │
│     └─► Report completion summary with PR URL                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Instructions

### Phase 1: Initialization

1. **Find PR folder**:
   - Search `docs/prs/` for folder matching PR number
   - Handle formats: `*-PR-{num}-*`

2. **Check PR state**:
   - If no folder exists AND no `--skip-start`:
     - Ask user for PR slug
     - Run `/project:start-pr {num} {slug}` (creates branch + folder)
   - If folder exists:
     - Extract branch name from RESEARCH.md or PLAN.md
     - Checkout the feature branch: `git checkout feature/pr-{num}-{slug}`
     - Announce "Found existing PR-{num}: {title}"

3. **Verify PLAN.md exists and is complete**:
   - Check for Tasks/Implementation Order section
   - Check for Definition of Done
   - If incomplete, ask user to fill gaps before proceeding

### Phase 2: Implementation

4. **Execute `/project:implement-pr {num}`**:
   - Follow all steps in implement-pr.md
   - Create IMPLEMENTATION.md if needed
   - Track progress with TodoWrite
   - Execute all tasks from PLAN.md
   - Update docs incrementally

5. **Handle implementation issues**:
   - If blocker encountered, pause and ask user
   - Log all deviations in IMPLEMENTATION.md
   - Don't proceed to verification until all tasks done

### Phase 3: Verification

6. **Execute `/project:verify-pr {num}`**:
   - Run all available verification checks (lint, typecheck, test, build)
   - Collect results

7. **Handle verification failures**:
   - If ANY check fails:
     ```
     Verification failed. Issues found:
     - {issue 1}
     - {issue 2}

     Fix these issues before creating GitHub PR.
     ```
   - Return to implementation phase to fix
   - Re-run verification after fixes

### Phase 4: Push & Create GitHub PR

8. **Push branch to remote**:
   ```bash
   git add -A
   git commit -m "feat: {brief description of changes}"
   git push -u origin feature/pr-{num}-{slug}
   ```

9. **Create GitHub Pull Request**:
   ```bash
   gh pr create \
     --title "PR #{num}: {title from PLAN.md}" \
     --body "$(cat <<EOF
   ## Summary
   {Summary from IMPLEMENTATION.md}

   ## Changes
   {Key changes from IMPLEMENTATION.md}

   ## Testing
   - [ ] Lint passes
   - [ ] Tests pass

   ## Paper Trail
   See \`docs/prs/{date}-PR-{num}-{slug}/\`

   ---
   Generated with Claude Code
   EOF
   )"
   ```

10. **Update IMPLEMENTATION.md** with GitHub PR URL

### Phase 5: User Approval Gate

11. **Request user approval**:
    ```
    GitHub PR created!

    PR #{num}: {title}
    URL: {github_pr_url}

    - Tasks completed: {X}/{X}
    - Verification: Passing

    Ready to merge this PR?
    [Yes, merge now] / [No, wait for review]
    ```

12. **If user says No**:
    - Stop workflow
    - Report current state
    - User can resume later with `/project:close-pr {num}`

### Phase 6: Merge & Close

13. **Execute `/project:close-pr {num}`**:
    - Merges the GitHub PR via `gh pr merge --squash --delete-branch`
    - Checks out main and pulls
    - Completes IMPLEMENTATION.md
    - Updates ACTIVE_PRS.md
    - Checks for architectural decisions and prompts ADR creation
    - Updates RECENT_DECISIONS.md if needed
    - Commits and pushes documentation

### Phase 7: Compound Loop (optional)

14. **Check for Clarity API credentials**:
    - If `.env` has `CLARITY_API_KEY` configured:
      - Ask user: "Run compound self-reflection loop? [Yes/No]"
      - If yes, execute `/project:compound {num}`
    - If not configured, skip silently (compound loop is opt-in)

### Phase 8: Update Context

15. **Execute `/project:context-update`**:
    - Refresh ACTIVE_PRS.md with current state
    - Refresh RECENT_DECISIONS.md with any new ADRs
    - Ensure all documentation is current

### Phase 9: Report

16. **Final report**:
    ```
    PR #{num} COMPLETE

    Status: Merged
    GitHub PR: {pr_url}
    Tasks: {X}/{X} completed

    Documentation Updated:
    - IMPLEMENTATION.md
    - ACTIVE_PRS.md
    - RECENT_DECISIONS.md (if decisions made)
    - COMPOUND_REPORT.md (if compound loop ran)

    Next PR ready: PR #{num+1}
    ```

## Recovery & Resume

If workflow is interrupted:
- Progress is saved in TodoWrite
- IMPLEMENTATION.md tracks completed work
- Feature branch preserves all changes
- User can resume with `/project:execute-pr {num} --skip-start`
- Workflow will detect existing state and continue from there

## Flags

| Flag | Effect |
|------|--------|
| `--skip-start` | Skip PR creation, use existing folder |
| `--skip-verify` | Skip verification (not recommended) |
| `--skip-compound` | Skip compound loop even if credentials configured |
| `--auto-merge` | Merge without asking (use with caution) |
| `--dry-run` | Show what would happen without executing |
