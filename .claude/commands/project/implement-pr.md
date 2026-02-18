# Implement PR

Execute the implementation plan for a PR with structured progress tracking.

## Arguments

- PR number (e.g., "036")

Example usage: `/project:implement-pr 036`

## Instructions

1. **Find the PR folder** in `docs/prs/` matching the PR number
   - Handle formats: `YYYY-MM-DD-PR-{num}-*`

2. **Ensure on correct branch**:
   - Extract branch name from RESEARCH.md or PLAN.md
   - If not on feature branch, checkout: `git checkout feature/pr-{num}-{slug}`
   - If branch doesn't exist, run `/project:start-pr` first

3. **Read PLAN.md** completely to understand:
   - Scope (In Scope / Out of Scope)
   - Tasks list and implementation order
   - Files to create/modify
   - Dependencies to install
   - Definition of Done

4. **Create IMPLEMENTATION.md** if it doesn't exist:
   - Use the template from start-pr.md
   - Set Status to "In Progress"
   - Link to PLAN.md
   - Include branch name

5. **Parse tasks from PLAN.md**:
   - Find all `[ ]` checkbox items in Implementation Order / Tasks section
   - Group by section if applicable
   - Create TodoWrite items for trackable progress

6. **Create TodoWrite list** with all tasks:
   ```
   Example:
   - [ ] Install dependencies (from PLAN.md task 1)
   - [ ] Create component (from PLAN.md task 2)
   - [ ] Write tests (from PLAN.md task 3)
   ```

7. **Begin implementation**:
   - Work through tasks in order specified by PLAN.md
   - Mark todos complete as each task finishes
   - Update IMPLEMENTATION.md "Key Changes" section as you go
   - Note any deviations from plan in "Deviations from Plan" table

8. **Track dependencies**:
   - If PLAN.md specifies dependencies, install them first
   - Verify installation succeeds before proceeding

9. **Incremental commits** (recommended):
   - Commit after each logical unit of work
   - Use conventional commit messages:
     - `feat: add X component`
     - `fix: resolve Y issue`
     - `test: add tests for Z`
     - `docs: update implementation notes`
   - Stay on feature branch

10. **Update progress**:
    - After each major section, update IMPLEMENTATION.md
    - Keep "Deviations from Plan" current if changes needed

11. **When all tasks complete**:
    - Mark all todos done
    - Update IMPLEMENTATION.md summary
    - Prompt to run `/project:verify-pr {num}`

## Output During Implementation

Keep user informed:
```
PR #{num}: {title}

Branch: feature/pr-{num}-{slug}
Progress: {X}/{Y} tasks
Current: {task description}
```

## Handling Blockers

If a task cannot be completed:
1. Note the blocker in IMPLEMENTATION.md
2. Ask user how to proceed:
   - Skip and continue?
   - Modify approach?
   - Stop implementation?
