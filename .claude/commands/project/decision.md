# Decision

Create a new Architecture Decision Record (ADR).

## Arguments

The user should provide:
- Slug for the decision (e.g., "api-versioning-strategy")

Example usage: `/project:decision api-versioning-strategy`

## Instructions

1. **Get today's date** in YYYY-MM-DD format

2. **Determine ADR number**:
   - Read `docs/decisions/_INDEX.md`
   - Find the highest existing ADR number
   - New ADR number = highest + 1

3. **Create ADR file** at `docs/decisions/{date}-{slug}.md`:

```markdown
# ADR-{number}: {Title from slug, humanized}

**Date**: {date}
**Status**: Proposed
**PR**: #{number if applicable, or "N/A"}

## Context

{To be filled: What issue motivates this decision?}

## Decision

{To be filled: What are we doing?}

## Consequences

### Positive
-

### Negative
-

### Neutral
-

## Alternatives Considered

### {Alternative 1}
- **Description**:
- **Pros**:
- **Cons**:
- **Why not chosen**:

### {Alternative 2}
- **Description**:
- **Pros**:
- **Cons**:
- **Why not chosen**:

## Related

- PR: `docs/prs/{date}-PR-{num}-{slug}/` (if applicable)
- References: {external resources, docs, related ADRs}
```

4. **Update `docs/decisions/_INDEX.md`**:
   - Add row to the table:
     ```
     | {number} | {date} | {title} | Proposed | [Link](/{date}-{slug}.md) |
     ```
   - Add to "Proposed" section under "By Status" (if section exists)

5. **Update `docs/.context/RECENT_DECISIONS.md`**:
   - Add to top of table (shift others down, keep only 10)

6. **Prompt user** to fill in the Context and Decision sections

7. **After user fills in**, remind them to:
   - Update Status to "Accepted" when finalized
   - Update _INDEX.md status accordingly
   - Link from relevant PR paper trail if applicable
