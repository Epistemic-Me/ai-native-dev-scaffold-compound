---
description: Create implementation plans with thorough research (no docs directory required)
model: opus
---

# Implementation Plan (Lightweight)

You are tasked with creating detailed implementation plans through an interactive, iterative process. This is the lightweight variant that does NOT require a `docs/` directory structure - plans are written wherever the user specifies or presented inline.

## Initial Response

When this command is invoked:

1. **Check if parameters were provided**:
   - If a file path or ticket reference was provided, read it FULLY and begin research
   - If no parameters, ask what we're building

2. **If no parameters provided**, respond with:
```
I'll help you create a detailed implementation plan. What are we building?

Please provide:
1. The task description or reference to a file
2. Any relevant context or constraints

Tip: `/hl:create_plan_nt path/to/ticket.md`
```

## Process Steps

### Step 1: Context Gathering

1. **Read all mentioned files FULLY** (no limit/offset)
2. **Spawn research tasks in parallel**:
   - **codebase-locator** - Find related files
   - **codebase-analyzer** - Understand current implementation
   - **codebase-pattern-finder** - Find similar patterns
3. **Read all identified files** into main context
4. **Present understanding and questions**

### Step 2: Research & Discovery

1. Verify any corrections with follow-up research
2. Spawn parallel sub-tasks for comprehensive research
3. Wait for ALL to complete
4. Present findings and design options

### Step 3: Plan Structure

1. Present outline and get feedback on structure
2. Get buy-in before writing details

### Step 4: Write the Plan

Write the plan to the **user-specified location** or present it inline in the conversation.

If the user specifies a path, write there. Otherwise, present the plan directly and ask if they want it saved somewhere.

**Use this template:**

````markdown
# [Feature/Task Name] Implementation Plan

## Overview
[Brief description of what we're implementing and why]

## Current State Analysis
[What exists now, what's missing, key constraints]

## Desired End State
[Specification of the end state and how to verify it]

## What We're NOT Doing
[Out-of-scope items]

## Implementation Approach
[High-level strategy]

## Phase 1: [Descriptive Name]

### Changes Required:
- **File**: `path/to/file.ext` - [Changes]

### Success Criteria:
#### Automated Verification:
- [ ] Tests pass: `npm test`
- [ ] Lint passes: `npm run lint`

#### Manual Verification:
- [ ] Feature works as expected

---

## Phase 2: [Descriptive Name]
[Similar structure...]

## References
- [Links and file:line references]
````

### Step 5: Review and Iterate

Present the plan and iterate based on feedback.

## Key Difference from /hl:create_plan

This command does NOT:
- Require a `docs/` directory structure
- Write to a predetermined location
- Generate YAML frontmatter or metadata

Use `/hl:create_plan` instead when you want the full paper trail integration.

## Guidelines

1. **Be Skeptical** - Question vague requirements, verify with code
2. **Be Interactive** - Get buy-in at each step
3. **Be Thorough** - Research actual code patterns, include file:line references
4. **Be Practical** - Focus on incremental, testable changes
5. **No Open Questions** - Resolve all uncertainties before finalizing
