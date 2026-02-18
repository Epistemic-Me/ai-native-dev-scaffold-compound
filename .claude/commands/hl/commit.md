---
description: Create git commits with user approval (enforces PR workflow)
---

# Commit Changes

You are tasked with creating git commits for the changes made during this session.

## MANDATORY: Branch Safety Check

**BEFORE creating ANY commits:**

1. **Check current branch:**
   ```bash
   git branch --show-current
   ```

2. **If on `master` or `main`:**
   - ❌ **STOP IMMEDIATELY**
   - Tell user: "Cannot commit directly to [branch]. PR workflow required."
   - Suggest: "Please create a feature branch: `git checkout -b feature/pr-XXX-description`"
   - **DO NOT proceed with commits until on a feature branch**

3. **Check for existing PR:**
   ```bash
   gh pr view --json number,url 2>/dev/null
   ```
   - If no PR exists, warn user and suggest creating one
   - Can proceed without PR but must be on feature branch

---

## Process (after branch safety passes):

1. **Think about what changed:**
   - Review the conversation history and understand what was accomplished
   - Run `git status` to see current changes
   - Run `git diff` to understand the modifications
   - Consider whether changes should be one commit or multiple logical commits

2. **Plan your commit(s):**
   - Identify which files belong together
   - Draft clear, descriptive commit messages
   - Use imperative mood in commit messages
   - Focus on why the changes were made, not just what

3. **Present your plan to the user:**
   - Confirm current branch name
   - List the files you plan to add for each commit
   - Show the commit message(s) you'll use
   - Ask: "I plan to create [N] commit(s) on branch `[branch-name]`. Shall I proceed?"

4. **Execute upon confirmation:**
   - Use `git add` with specific files (never use `-A` or `.`)
   - Create commits with your planned messages
   - Show the result with `git log --oneline -n [number]`
   - Suggest pushing: `git push -u origin [branch-name]`

## Commit Message Guidelines

### Format
```
<type>: <short summary in imperative mood>

<optional body explaining why and context>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `docs`: Documentation only changes
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples
```
feat: Add user authentication flow

Implements OAuth2 login with Google and GitHub providers.
Stores session tokens in secure HTTP-only cookies.
```

```
fix: Prevent duplicate form submissions

Disables submit button while request is in flight.
Closes #123
```

## Important:
- **NEVER commit to master/main** - this is non-negotiable
- Group related changes together
- Keep commits focused and atomic when possible
- The user trusts your judgment - they asked you to commit
- Always push to feature branch, never to master/main
