---
description: Set up worktree for reviewing colleague's branch
---

# Local Review

You are tasked with helping review a colleague's branch locally. This sets up a clean worktree for reviewing code changes without disrupting your current work.

## Process:

### 1. Identify the Branch to Review

If a PR number or branch name was provided, use it. Otherwise:

```bash
gh pr list --limit 10 --json number,title,headRefName,author
```

Ask which PR/branch they want to review.

### 2. Gather PR Context

```bash
# Get PR details
gh pr view {number} --json title,body,commits,files,additions,deletions

# Get the diff
gh pr diff {number}

# Check CI status
gh pr checks {number}
```

### 3. Analyze the Changes

1. **Read the PR description** to understand intent
2. **Review the diff** file by file:
   - Look for correctness issues
   - Check for edge cases
   - Verify error handling
   - Assess code style consistency
   - Look for security concerns
3. **Check for missing items**:
   - Are there tests for new functionality?
   - Is documentation updated if needed?
   - Are there breaking changes?

### 4. Present Review Summary

```markdown
## Review: PR #{number} - {title}

### Overview
[Brief summary of what this PR does]

### Files Changed
- `path/to/file.ext` - [What changed and why]
- `another/file.ext` - [What changed and why]

### Findings

#### Looks Good
- [Positive observation]
- [Good pattern used]

#### Suggestions
- [Non-blocking suggestion with file:line reference]
- [Another suggestion]

#### Issues
- [Blocking issue with file:line reference]
- [Another issue]

### CI Status
- [x] Tests pass
- [x] Lint passes
- [ ] [Any failing checks]

### Recommendation
[Approve / Request Changes / Comment]
```

### 5. Post Review (if requested)

If the user wants to post the review to GitHub:

```bash
gh pr review {number} --approve --body "review text"
# or
gh pr review {number} --request-changes --body "review text"
# or
gh pr review {number} --comment --body "review text"
```

## Important Notes:
- Focus on meaningful feedback, not style nitpicks
- Consider the overall design, not just line-by-line changes
- Be constructive and specific with suggestions
- Include file:line references for all findings
- Check if the PR achieves what it claims to do
