# PR Status

Quick view of current PR progress.

## Arguments

- Optional: PR number (defaults to detecting active PR)

Example usage:
- `/project:pr-status` - Show status of current/active PR
- `/project:pr-status 002` - Show status of specific PR

## Instructions

1. **Find PR**:
   - If number provided, find that PR folder in `docs/prs/`
   - If not, check ACTIVE_PRS.md for current "In Progress" PR
   - If no active PR found, report "No active PR"

2. **Read PR state**:
   - Read PLAN.md for total tasks
   - Read IMPLEMENTATION.md for status and completed work
   - Check for any verification results

3. **Count tasks**:
   - Total tasks from PLAN.md `[ ]` items
   - Completed tasks from PLAN.md `[x]` items (if tracked there)
   - Or from IMPLEMENTATION.md "Testing Done" section

4. **Check verification status**:
   - Has verification been run?
   - Last result: pass/fail?

5. **Check GitHub PR status** (if gh CLI available):
   ```bash
   gh pr view --json number,state,url,reviewDecision
   ```

6. **Output status report**:

```
PR-{num}: {title}

Status: {In Progress | Ready to Verify | Ready to Close | Complete}
Branch: feature/pr-{num}-{slug}
GitHub PR: {url or "Not created"}

Progress: {X}/{Y} tasks ({Z}%)

Phase: {Implementation | Verification | Review | Closing | Done}

Last Verification: {Not run | PASS | FAIL}

Next Step: {action}
```

7. **Suggest next action**:
   - If tasks remain: "Continue implementation with `/project:implement-pr {num}`"
   - If tasks done but not verified: "Run `/project:verify-pr {num}`"
   - If verified but no GH PR: "Push and create PR"
   - If PR created but not reviewed: "Waiting for review"
   - If reviewed but not closed: "Run `/project:close-pr {num}`"
   - If complete: "Start next PR with `/project:start-pr {num+1} {slug}`"

## Quick Commands

Also show relevant quick commands:
```
Quick Commands:
  /project:execute-pr {num}    - Run full lifecycle
  /project:implement-pr {num}  - Continue implementation
  /project:verify-pr {num}     - Run verification checks
  /project:close-pr {num}      - Close and document PR
  /project:context-status      - View project context
```
