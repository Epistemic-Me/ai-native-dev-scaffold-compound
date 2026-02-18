# Active PRs

Living document tracking currently open pull requests and their status.

## Open PRs

| PR | Title | Started | Paper Trail | Status |
|----|-------|---------|-------------|--------|
| <!-- PRs will be added here --> |

## Recently Merged

| PR | Title | Merged | Paper Trail |
|----|-------|--------|-------------|
| <!-- Merged PRs will be moved here --> |

## How to Use

### Starting a PR
```
/project:start-pr {number} {slug}
```
This creates a paper trail folder and adds an entry here.

### Closing a PR
```
/project:close-pr {number}
```
This moves the PR from "Open PRs" to "Recently Merged" and completes documentation.

## Paper Trail Location

All PR documentation lives in `docs/prs/{date}-PR-{num}-{slug}/`:
- `RESEARCH.md` - Problem exploration and options
- `PLAN.md` - Implementation strategy
- `IMPLEMENTATION.md` - What was actually built
