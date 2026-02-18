---
description: Execute implementation from PR paper trail
---

# Execute PR

You are tasked with implementing the work described in a PR paper trail. This command reads the RESEARCH.md and PLAN.md documents and executes the implementation.

## Initial Response

When this command is invoked:

1. **If a PR number or path was provided**:
   - Find the PR folder in `docs/prs/` matching the PR number
   - Read RESEARCH.md and PLAN.md FULLY
   - Begin the implementation process

2. **If no parameters provided**, respond with:
```
I'll help you execute an implementation from a PR paper trail.

Please provide the PR number or path to the PR folder.

Tip: List PRs with `ls docs/prs/`
```

Then wait for the user's input.

## Process Steps

### Step 1: Load PR Context

1. **Find and read the PR paper trail**:
   - Locate `docs/prs/*-PR-{number}-*/`
   - Read RESEARCH.md completely - understand the problem and chosen solution
   - Read PLAN.md completely - understand the implementation approach
   - Check if IMPLEMENTATION.md has any existing progress

2. **Verify readiness**:
   - RESEARCH.md should have a clear recommendation
   - PLAN.md should have defined phases and success criteria
   - If either is incomplete, inform the user:
     ```
     The PR paper trail appears incomplete:
     - RESEARCH.md: [Complete/Missing sections]
     - PLAN.md: [Complete/Missing sections]

     Would you like me to help complete these first?
     ```

### Step 2: Create Implementation Plan

1. **Extract implementation phases from PLAN.md**:
   - List all phases and their scope
   - Identify dependencies between phases
   - Note success criteria for each phase

2. **Create todo list** using TodoWrite:
   - One todo per implementation phase
   - Include verification steps
   - Add documentation updates

3. **Present the execution plan**:
   ```
   Based on the PR paper trail, here's the implementation plan:

   ## PR #{number}: {title}

   **Problem**: [Summary from RESEARCH.md]
   **Approach**: [Summary from PLAN.md]

   **Phases to implement**:
   1. [Phase 1] - [Description]
   2. [Phase 2] - [Description]
   3. [Phase 3] - [Description]

   **Success criteria**:
   - [Criteria from PLAN.md]

   Ready to begin with Phase 1?
   ```

### Step 3: Execute Implementation

For each phase:

1. **Announce the phase**:
   ```
   Starting Phase {N}: {Name}

   This phase will:
   - [What it accomplishes]
   - [Files to modify/create]
   ```

2. **Implement the changes**:
   - Follow the technical design from PLAN.md
   - Use existing patterns from RESEARCH.md findings
   - Make incremental, testable changes

3. **Verify the phase**:
   - Run automated checks (tests, lint, typecheck)
   - Check off success criteria
   - Update IMPLEMENTATION.md with progress

4. **Report phase completion**:
   ```
   Phase {N} Complete

   Changes made:
   - [File changes]

   Verification:
   - [x] Tests pass
   - [x] Lint passes
   - [ ] Manual testing needed: [what to test]

   Ready to proceed to Phase {N+1}?
   ```

### Step 4: Update Documentation

As implementation progresses:

1. **Update IMPLEMENTATION.md** with:
   - Summary of what was built
   - Key changes made
   - Any deviations from the plan
   - Learnings discovered

2. **Track progress**:
   - Check off completed items in PLAN.md
   - Update todo list status
   - Note any blockers or issues

### Step 5: Complete Implementation

When all phases are done:

1. **Final verification**:
   - Run all tests
   - Check all success criteria
   - Verify no regressions

2. **Complete IMPLEMENTATION.md**:
   - Fill in all sections
   - Document learnings
   - List follow-up items

3. **Report completion**:
   ```
   ## Implementation Complete: PR #{number}

   **Summary**: [What was built]

   **All phases completed**:
   - [x] Phase 1: [Name]
   - [x] Phase 2: [Name]
   - [x] Phase 3: [Name]

   **Verification status**:
   - [x] All tests pass
   - [x] Lint/typecheck pass
   - [ ] Manual testing: [items for user]

   **Next steps**:
   1. Complete manual testing
   2. Run `/hl:commit` to create commits
   3. Run `/hl:describe_pr` to update PR description
   4. Run `/project:close-pr {number}` when merged
   ```

## Important Guidelines

1. **Follow the paper trail**:
   - The RESEARCH.md contains important context and decisions
   - The PLAN.md defines the agreed-upon approach
   - Don't deviate without discussing first

2. **Incremental progress**:
   - Implement one phase at a time
   - Verify before moving forward
   - Update documentation as you go

3. **Communication**:
   - Report progress clearly
   - Pause for confirmation between phases
   - Surface issues early

4. **Quality**:
   - Follow existing code patterns
   - Write tests for new functionality
   - Keep changes focused and reviewable
