---
description: Research ticket and launch planning session
---

# Oneshot

Quick research-to-planning pipeline. Reads a ticket/task, does focused research, and launches into plan creation.

## Process:

### 1. Read the Input

If a file path or description was provided:
- Read the file FULLY
- Extract the key requirements and constraints
- Identify the scope and components involved

If no input:
```
What would you like me to research and plan? Provide a ticket file, task description, or area of focus.
```

### 2. Quick Research Sprint

Spawn parallel research tasks:

- **codebase-locator**: Find all files related to the task
- **codebase-analyzer**: Understand current implementation
- **codebase-pattern-finder**: Find similar patterns to model after

Wait for all to complete.

### 3. Synthesize and Transition to Planning

Present a brief research summary:
```
Here's what I found:

**Relevant Code:**
- [file:line references]

**Current Patterns:**
- [Pattern description]

**Key Constraints:**
- [Constraint discovered]

Now let me create an implementation plan based on these findings.
```

### 4. Create the Plan

Follow the `/hl:create_plan` workflow but skip the initial research phase since you've already done it:

1. Present design options based on your research
2. Get alignment on approach
3. Write the plan to `docs/plans/YYYY-MM-DD-description.md`
4. Include all discovered file:line references

## Key Difference from /hl:create_plan

This command is optimized for speed:
- Does research first without asking questions
- Presents findings and plan outline together
- Fewer pauses for confirmation
- Best for well-defined tasks where the scope is clear

Use `/hl:create_plan` instead when:
- Requirements are ambiguous
- Multiple stakeholders need alignment
- The task touches many systems
- You need extensive back-and-forth
