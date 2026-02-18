# Close PR

Merge GitHub PR and complete documentation.

## Arguments

The user should provide:
- PR number (e.g., "036")

Example usage: `/project:close-pr 036`

## Instructions

1. **Find the PR folder** in `docs/prs/` matching the PR number

2. **Check GitHub PR status**:
   ```bash
   gh pr view --json number,title,state,url
   ```
   - If no GitHub PR exists, create one first
   - If PR is already merged, skip to documentation update

3. **Merge the GitHub PR** (if not already merged):
   ```bash
   gh pr merge --squash --delete-branch
   ```

4. **Checkout main and pull**:
   ```bash
   git checkout main
   git pull origin main
   ```

5. **Update IMPLEMENTATION.md**:
   - Ensure "Summary" section is filled
   - Ensure "Key Changes" documents what was built
   - Ensure "Testing Done" has checked items
   - Ensure "Learnings" sections are filled
   - Add GitHub PR URL if not present
   - Set "PR Merged" date to today
   - Change "Status" from "In Progress" to "Complete"

6. **Review for completeness**:
   - RESEARCH.md should have problem statement and chosen option
   - PLAN.md should have scope and implementation order
   - IMPLEMENTATION.md should have summary and learnings
   - Flag any incomplete sections to the user

7. **Update ACTIVE_PRS.md**:
   - Move PR from "Open PRs" to "Recently Merged" table
   - Include merge date, GitHub PR URL, and paper trail link

8. **Check for decisions**:
   - Review RESEARCH.md and PLAN.md for significant decisions
   - If architectural decisions were made, ask user if ADR should be created
   - If yes, run `/project:decision {slug}`

9. **Update RECENT_DECISIONS.md** if decisions were captured

10. **Compound loop (optional)**:
    - Check if `.env` has `CLARITY_API_KEY` configured
    - If configured, ask user: "Run compound loop for this PR? [Yes/No]"
    - If yes, run `/project:compound {num}`
    - If no or credentials not configured, skip (this is fine)

11. **Commit documentation updates**:
    ```bash
    git add docs/prs/ docs/.context/
    git commit -m "docs: close PR #{num} - {title}"
    git push origin main
    ```

12. **Report summary**:
    ```
    PR #{num} CLOSED

    GitHub PR: {pr_url}
    Status: Merged
    Merged: {date}

    Documentation Updated:
    - IMPLEMENTATION.md
    - ACTIVE_PRS.md
    ```
