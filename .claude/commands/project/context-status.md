# Context Status

Report on documentation health and identify gaps.

## When to Use

Run this to understand:
- What PRs are currently in progress
- Recent architectural decisions
- Current project state
- Documentation health

Example usage: `/project:context-status`

## Instructions

1. **Check `.context/` freshness**:
   - Read each file in `docs/.context/`
   - Check "Last updated" dates if present
   - Flag any file not updated in the last 7 days

2. **Check PR paper trails**:
   - Run `gh pr list --state open` or check git branches
   - For each open PR, verify `docs/prs/*-PR-{num}-*/` exists
   - List any PRs missing paper trails

3. **Check decisions**:
   - Read `docs/decisions/_INDEX.md`
   - Verify all listed decisions have corresponding files
   - Check for any "Proposed" decisions that need resolution

4. **Check for staleness**:
   - PRs open for >2 weeks
   - Missing paper trails
   - Decisions needing follow-up

5. **Present summary** in structured format:

```
## Documentation Health Report

### .context/ Files
- ACTIVE_PRS.md: {status} (updated {X days ago})
- RECENT_DECISIONS.md: {status} (updated {X days ago})

### PR Paper Trails
- {X} open PRs
- {Y} with paper trails
- {Z} missing paper trails:
  - PR #{num}: {title}

### Decisions
- {X} total decisions
- {Y} accepted
- {Z} proposed (pending)

### Recommendations
1. {Action item}
2. {Action item}
```
