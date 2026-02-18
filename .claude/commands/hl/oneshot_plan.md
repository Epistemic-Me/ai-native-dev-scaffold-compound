---
description: Execute research, planning, and implementation for a ticket in one session
---

# Oneshot Plan

End-to-end execution: research a ticket, create a plan, and implement it - all in one session. Best for small-to-medium well-scoped tasks.

## Process:

### Phase 1: Research (Quick)

1. Read any provided files FULLY
2. Spawn parallel research tasks:
   - **codebase-locator**: Find related files
   - **codebase-analyzer**: Understand current implementation
   - **codebase-pattern-finder**: Find patterns to follow
3. Wait for all to complete
4. Synthesize key findings

### Phase 2: Plan (Lightweight)

1. Present a brief plan:
   ```
   Based on my research, here's the implementation plan:

   **What we're doing:** [Summary]
   **Approach:** [Strategy]

   **Changes:**
   1. [File/component] - [What to change]
   2. [File/component] - [What to change]

   **What we're NOT doing:** [Scope limits]

   **Verification:**
   - [ ] [Automated check]
   - [ ] [Manual check]

   Shall I proceed with implementation?
   ```

2. Get confirmation before proceeding

### Phase 3: Implement

1. **Branch safety check:**
   ```bash
   git branch --show-current
   ```
   If on master/main, create feature branch first.

2. Implement changes following the plan
3. Run verification after each logical group of changes
4. Fix any issues immediately

### Phase 4: Wrap Up

1. Run all verification checks
2. Present summary:
   ```
   Implementation complete!

   **Changes made:**
   - [File changes]

   **Verification:**
   - [x] Tests pass
   - [x] Lint passes
   - [ ] Manual testing: [what to test]

   **Next steps:**
   - Run `/hl:commit` to create commits
   - Run `/hl:describe_pr` to update PR description
   ```

## When to Use This vs Separate Commands

| Use `/hl:oneshot_plan` | Use separate commands |
|------------------------|----------------------|
| Small, well-scoped tasks | Large, complex features |
| Clear requirements | Ambiguous requirements |
| Single-session work | Multi-session projects |
| Familiar codebase area | New/complex systems |

## Important:
- Still requires feature branch (never implement on master/main)
- Skip the handoff document since this is a single-session workflow
- If the task turns out to be bigger than expected, pause and switch to `/hl:create_plan`
