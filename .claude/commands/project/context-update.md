# Context Update

Refresh all `.context/` files to reflect current repository state.

## When to Use

Run this after:
- Completing a PR
- Making a significant decision
- Changing project direction
- At the end of a work session

Example usage: `/project:context-update`

## Instructions

1. **Read current state** of all files in `docs/.context/`

2. **Gather fresh data**:
   - Run `git log --oneline -20` to see recent commits
   - Run `git branch -a` to see branches
   - Run `gh pr list --state open` to see open PRs (if gh CLI available)
   - Check `docs/prs/` for existing PR paper trails
   - Check `docs/decisions/` for recent decisions

3. **Update each file**:

   ### ACTIVE_PRS.md
   - List all open PRs with their paper trail links
   - Include branch names for each PR
   - Move merged PRs (last 7 days) to "Recently Merged" section
   - Verify each PR has a paper trail folder in `docs/prs/`
   - Flag any PRs missing paper trails
   - Set "Last updated" to today's date

   ### RECENT_DECISIONS.md
   - Scan `docs/decisions/` for the 10 most recent ADRs
   - Update the table with date, title, status, and link
   - Update "Latest Decision Summary" with most recent
   - Set "Last updated" to today's date

4. **Review for staleness**:
   - Flag any context that seems outdated
   - Suggest cleanup if needed

5. **Report changes made** to the user:
   ```
   Context Updated:
   - ACTIVE_PRS.md: {changes}
   - RECENT_DECISIONS.md: {changes}

   Documentation gaps found:
   - {any issues}
   ```
