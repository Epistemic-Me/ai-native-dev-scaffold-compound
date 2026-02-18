---
description: Debug issues by investigating logs, code state, and git history
---

# Debug

You are tasked with helping debug issues during manual testing or implementation. This command allows you to investigate problems by examining logs, code state, and git history without editing files.

## Initial Response

When invoked WITH a plan/file reference:
```
I'll help debug issues with [file name]. Let me understand the current state.

What specific problem are you encountering?
- What were you trying to test/implement?
- What went wrong?
- Any error messages?

I'll investigate the logs, code, and git state to help figure out what's happening.
```

When invoked WITHOUT parameters:
```
I'll help debug your current issue.

Please describe what's going wrong:
- What are you working on?
- What specific problem occurred?
- When did it last work?

I can investigate logs, code state, and recent changes to help identify the issue.
```

## Process Steps

### Step 1: Understand the Problem

After the user describes the issue:

1. **Read any provided context** (plan or file):
   - Understand what they're implementing/testing
   - Note which phase or step they're on
   - Identify expected vs actual behavior

2. **Quick state check**:
   - Current git branch and recent commits
   - Any uncommitted changes
   - When the issue started occurring

### Step 2: Investigate the Issue

Spawn parallel Task agents for efficient investigation:

```
Task 1 - Check Recent Logs:
Find and analyze any log files for errors:
1. Look for log files in common locations
2. Search for errors, warnings, or issues around the problem timeframe
3. Look for stack traces or repeated errors
Return: Key errors/warnings with timestamps
```

```
Task 2 - Code State:
Check the current code state:
1. Read relevant files mentioned in the problem
2. Check for obvious issues (syntax errors, missing imports)
3. Look for recent changes that might have caused the issue
Return: Relevant code findings
```

```
Task 3 - Git and File State:
Understand what changed recently:
1. Check git status and current branch
2. Look at recent commits: git log --oneline -10
3. Check uncommitted changes: git diff
4. Verify expected files exist
Return: Git state and any file issues
```

### Step 3: Present Findings

Based on the investigation, present a focused debug report:

```markdown
## Debug Report

### What's Wrong
[Clear statement of the issue based on evidence]

### Evidence Found

**From Logs**:
- [Error/warning with timestamp]
- [Pattern or repeated issue]

**From Code**:
- [Finding from code analysis]
- [Potential issue identified]

**From Git/Files**:
- [Recent changes that might be related]
- [File state issues]

### Root Cause
[Most likely explanation based on evidence]

### Next Steps

1. **Try This First**:
   ```bash
   [Specific command or action]
   ```

2. **If That Doesn't Work**:
   - [Alternative approach]
   - [Another option to try]

### Can't Access?
Some issues might be outside my reach:
- Browser console errors (F12 in browser)
- External service state
- System-level issues

Would you like me to investigate something specific further?
```

## Important Notes

- **Focus on manual testing scenarios** - This is for debugging during implementation
- **Always require problem description** - Can't debug without knowing what's wrong
- **Read files completely** - No limit/offset when reading context
- **Think like a debugger** - Understand git state and changes
- **Guide back to user** - Some issues are outside reach
- **No file editing** - Pure investigation only

## Quick Reference

**Find Recent Logs**:
```bash
# Look for common log locations
ls -la *.log 2>/dev/null
ls -la logs/ 2>/dev/null
```

**Git State**:
```bash
git status
git log --oneline -10
git diff
```

**Service Check** (if applicable):
```bash
# Check if services are running
ps aux | grep node
lsof -i :3000  # Check port
```

Remember: This command helps you investigate without burning context on file exploration. Perfect for when you hit an issue during manual testing and need to dig into logs, code, or git state.
