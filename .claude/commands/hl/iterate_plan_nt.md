---
description: Iterate on existing implementation plans with thorough research and updates
model: opus
---

# Iterate Implementation Plan (Lightweight)

Update existing implementation plans based on user feedback. This is the lightweight variant that works with plans stored anywhere - no docs/ directory required.

## Initial Response

1. **Parse the input** for plan file path and requested changes
2. **Handle scenarios**:
   - No plan file: Ask for the path
   - Plan file but no feedback: Ask what to change
   - Both provided: Proceed immediately

## Process

### Step 1: Read and Understand

1. Read the existing plan file COMPLETELY (no limit/offset)
2. Parse what the user wants to add/modify/remove
3. Determine if changes require codebase research

### Step 2: Research If Needed

Only if changes require new technical understanding:

1. Spawn parallel sub-tasks:
   - **codebase-locator** - Find relevant files
   - **codebase-analyzer** - Understand implementation details
   - **codebase-pattern-finder** - Find similar patterns
2. Read identified files FULLY
3. Wait for ALL tasks to complete

### Step 3: Confirm and Update

1. Present understanding of requested changes
2. Get confirmation before proceeding
3. Make focused, precise edits using Edit tool
4. Maintain existing structure and quality
5. Keep automated vs manual success criteria distinction

### Step 4: Review

Present changes made and ask for further adjustments.

## Guidelines

1. **Be Surgical** - Precise edits, not wholesale rewrites
2. **Be Skeptical** - Question problematic change requests
3. **Be Thorough** - Read entire plan before changing
4. **No Open Questions** - Resolve all uncertainties

## Key Difference from /hl:iterate_plan
- Works with plans stored anywhere
- No docs/ directory assumptions
- No YAML frontmatter requirements
