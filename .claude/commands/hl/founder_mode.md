---
description: Rapid experimental feature development with proper PR workflow
---

# Founder Mode

You are in founder mode - rapid experimental development with a bias toward action. Move fast, make decisions, and ship working code. Still follow proper PR workflow.

## Philosophy

- **Bias toward action**: Make reasonable decisions instead of asking questions
- **Ship working code**: Focus on getting something functional, not perfect
- **Iterate quickly**: Get feedback through working software, not planning documents
- **Stay safe**: Still use feature branches and PRs, just move faster through them

## Process:

### 1. Branch Setup (if not already on a feature branch)

```bash
git branch --show-current
```

If on master/main:
- Create a feature branch: `git checkout -b feature/{descriptive-name}`
- Create a draft PR: `gh pr create --draft --title "WIP: {description}"`

### 2. Understand the Ask

- Read any provided files or context FULLY
- Make reasonable assumptions instead of asking clarifying questions
- State your assumptions briefly before starting

### 3. Implement

- Write code directly - skip the formal planning phase
- Follow existing patterns in the codebase
- Write tests if the project has them
- Keep changes focused and reviewable

### 4. Verify

- Run whatever checks the project has (`npm test`, `make check`, etc.)
- Fix any issues immediately
- Don't pause for manual testing unless something is clearly wrong

### 5. Commit and Push

- Create focused, atomic commits
- Push to the feature branch
- Update the PR description with what was built

## Key Differences from Normal Workflow

| Normal | Founder Mode |
|--------|-------------|
| Research first | Code first |
| Ask questions | Make assumptions |
| Plan phases | Ship incrementally |
| Pause for review | Keep moving |
| Formal docs | Inline comments |

## When NOT to Use Founder Mode

- Production deployments
- Security-sensitive changes
- Database migrations
- Breaking API changes
- Changes affecting other teams

## Remember:
- You still MUST use feature branches (never commit to master/main)
- You still MUST create PRs
- You still MUST run available tests
- You're moving fast, not recklessly
