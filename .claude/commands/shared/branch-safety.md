---
description: Branch safety checks for PR workflow enforcement
---

# Branch Safety Framework

**MANDATORY checks before ANY code modifications or commits.**

## Pre-Modification Check

Before modifying code or creating commits, Claude MUST:

### 1. Verify Current Branch
```bash
git branch --show-current
```

**If on `master` or `main`:**
- ❌ **STOP IMMEDIATELY**
- Inform user: "Cannot make changes on master/main. Please create a feature branch first."
- Suggest: `git checkout -b feature/pr-{num}-{description}`
- DO NOT proceed until user confirms they're on a feature branch

### 2. Check for Existing PR
```bash
gh pr view --json number,url 2>/dev/null
```

**If no PR exists:**
- ⚠️ **WARN** the user
- Suggest creating draft PR: `gh pr create --draft --title "WIP: [description]"`
- Ask: "Would you like me to create a draft PR before proceeding?"

### 3. Verify Clean State (for batch operations)
```bash
git status --porcelain
```

**If uncommitted changes exist:**
- Inform user of pending changes
- Suggest committing or stashing first

---

## Integration in Commands

All code-modifying commands MUST include at the top:

```markdown
## MANDATORY: Branch Safety

**BEFORE making ANY code changes:**

1. Run `git branch --show-current`
2. If on master/main → STOP and require feature branch
3. Run `gh pr view` to check for PR
4. If no PR → warn user and suggest creating one
5. Only proceed after on feature branch
```

---

## Blocked Operations on master/main

The following should NEVER be done on master/main:
- `git commit` (any form)
- `git push origin master/main`
- File edits via Edit/Write tools
- Batch operations via cleanup/improve commands

---

## Enforcement

When user attempts operation on master:

```
❌ BLOCKED: Cannot [operation] on master branch

This project requires PR workflow:
1. Create feature branch: git checkout -b feature/pr-XXX-description
2. Make changes on feature branch
3. Create PR: gh pr create --draft
4. Request review before merging

Would you like me to help create a feature branch?
```

---

## Recovery: Already Committed to Master

If commits were accidentally made to master:

```bash
# Note the commit SHA
git log -1 --format="%H"

# Reset master (keep changes staged)
git reset --soft HEAD~1

# Create feature branch
git checkout -b feature/pr-XXX-recovery

# Commit on feature branch
git commit -m "..."

# Push feature branch
git push -u origin feature/pr-XXX-recovery
```
