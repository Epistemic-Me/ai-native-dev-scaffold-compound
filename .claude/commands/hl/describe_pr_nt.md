---
description: Generate comprehensive PR descriptions following repository templates
---

# Generate PR Description (Lightweight)

Generate a PR description without requiring a docs/ directory or paper trail structure. Uses only GitHub CLI and code analysis.

## Steps:

1. **Identify the PR:**
   - Check current branch: `gh pr view --json url,number,title,state 2>/dev/null`
   - If no PR, list open PRs: `gh pr list --limit 10 --json number,title,headRefName,author`

2. **Gather PR information:**
   - Full diff: `gh pr diff {number}`
   - Commits: `gh pr view {number} --json commits`
   - Base branch: `gh pr view {number} --json baseRefName`
   - Metadata: `gh pr view {number} --json url,title,number,state`

3. **Check for PR template:**
   - Look for `.github/pull_request_template.md`
   - Use it if found, otherwise use default format

4. **Analyze changes thoroughly:**
   - Read the entire diff
   - Read referenced files for context
   - Identify user-facing vs internal changes
   - Note breaking changes

5. **Run verification commands:**
   - Run available checks (`npm test`, `make check`, etc.)
   - Mark passing checks as `- [x]`
   - Mark failures as `- [ ]` with explanation

6. **Generate and update:**
   - Write description to temp file
   - Update PR: `gh pr edit {number} --body-file /tmp/pr_description.md`
   - Confirm success

## Default Format:

```markdown
## Summary
[2-3 sentences on what and why]

## Changes
- [Change description]

## How to Test
1. [Testing steps]

## Verification
- [x] Tests pass
- [ ] Manual testing: [what]

## Breaking Changes
[List or "None"]
```

## Key Difference from /hl:describe_pr
- Does NOT look for docs/prs/ paper trail
- Does NOT require project docs structure
- Simpler, faster for projects without the full scaffold
