---
description: Generate comprehensive PR descriptions following repository templates
---

# Generate PR Description

You are tasked with generating a comprehensive pull request description following the repository's standard template.

## Steps to follow:

1. **Check for PR description template:**
   - Look for a PR template in `.github/pull_request_template.md` or `docs/prs/_TEMPLATE/`
   - If a template exists, read it to understand all sections and requirements
   - If no template exists, use the default format below

2. **Identify the PR to describe:**
   - Check if the current branch has an associated PR: `gh pr view --json url,number,title,state 2>/dev/null`
   - If no PR exists for the current branch, or if on main/master, list open PRs: `gh pr list --limit 10 --json number,title,headRefName,author`

3. **Gather comprehensive PR information:**
   - Get the full PR diff: `gh pr diff {number}`
   - If you get an error about no default remote repository, instruct the user to run `gh repo set-default`
   - Get commit history: `gh pr view {number} --json commits`
   - Review the base branch: `gh pr view {number} --json baseRefName`
   - Get PR metadata: `gh pr view {number} --json url,title,number,state`

4. **Analyze the changes thoroughly:**
   - Read through the entire diff carefully
   - For context, read any files that are referenced but not shown in the diff
   - Understand the purpose and impact of each change
   - Identify user-facing changes vs internal implementation details
   - Look for breaking changes or migration requirements

5. **Handle verification requirements:**
   - For each verification step:
     - If it's a command you can run (like `make check test`, `npm test`, etc.), run it
     - If it passes, mark the checkbox as checked: `- [x]`
     - If it fails, keep it unchecked and note what failed: `- [ ]` with explanation
     - If it requires manual testing, leave unchecked and note for user
   - Document any verification steps you couldn't complete

6. **Generate the description:**
   - Fill out each section from the template thoroughly
   - Be specific about problems solved and changes made
   - Focus on user impact where relevant
   - Include technical details in appropriate sections
   - Write a concise changelog entry
   - Ensure all checklist items are addressed

7. **Update the PR:**
   - Write the description to a temp file
   - Update the PR description directly: `gh pr edit {number} --body-file /tmp/pr_description.md`
   - Confirm the update was successful
   - If any verification steps remain unchecked, remind the user to complete them before merging

## Important notes:
- This command works across different repositories - always read the local template
- Be thorough but concise - descriptions should be scannable
- Focus on the "why" as much as the "what"
- Include any breaking changes or migration notes prominently
- If the PR touches multiple components, organize the description accordingly
- Always attempt to run verification commands when possible
- Clearly communicate which verification steps need manual testing
