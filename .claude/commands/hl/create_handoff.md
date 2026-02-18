---
description: Create handoff document for transferring work to another session
---

# Create Handoff

You are tasked with writing a handoff document to hand off your work to another agent in a new session. You will create a handoff document that is thorough, but also **concise**. The goal is to compact and summarize your context without losing any of the key details of what you're working on.

## Process

### 1. Filepath & Metadata

Create your file under `docs/handoffs/YYYY-MM-DD_HH-MM-SS_description.md`, where:
- YYYY-MM-DD is today's date
- HH-MM-SS is the current time in 24-hour format
- description is a brief kebab-case description

Examples:
- `docs/handoffs/2025-01-08_13-55-22_user-authentication-flow.md`
- `docs/handoffs/2025-01-08_14-30-00_api-refactoring.md`

Gather metadata:
- Current git branch: `git branch --show-current`
- Current commit: `git rev-parse --short HEAD`
- Repository name: basename of the git root directory

### 2. Handoff Writing

Use the following template structure:

```markdown
---
date: [Current date and time with timezone in ISO format]
git_commit: [Current commit hash]
branch: [Current branch name]
repository: [Repository name]
topic: "[Feature/Task Name]"
tags: [implementation, strategy, relevant-component-names]
status: complete
---

# Handoff: {very concise description}

## Task(s)

{Description of the task(s) you were working on, along with the status of each:
- completed
- work in progress
- planned/discussed

If working on an implementation plan, note which phase you are on. Reference the plan document and/or research documents you are working from.}

## Critical References

{List any critical specification documents, architectural decisions, or design docs that must be followed. Include only 2-3 most important file paths. Leave blank if none.}

## Recent Changes

{Describe recent changes made to the codebase in file:line syntax}

## Learnings

{Describe important things you learned:
- patterns discovered
- root causes of bugs
- other important information someone picking up your work should know
- include explicit file paths where relevant}

## Artifacts

{An exhaustive list of artifacts you produced or updated as filepaths and/or file:line references:
- feature documents
- implementation plans
- research documents
- code files modified}

## Action Items & Next Steps

{A list of action items and next steps for the next agent to accomplish based on your tasks and their statuses}

## Other Notes

{Other notes, references, or useful information:
- where relevant sections of the codebase are
- where relevant documents are
- other important things that don't fall into above categories}
```

### 3. Confirm and Report

After writing the handoff document, respond with:

```
Handoff created! You can resume from this handoff in a new session with:

/hl:resume_handoff docs/handoffs/{filename}.md
```

## Additional Notes & Instructions

- **More information, not less**: This template defines the minimum. Always include more if necessary.
- **Be thorough and precise**: Include both top-level objectives and lower-level details.
- **Avoid excessive code snippets**: While brief snippets are fine for describing key changes, prefer using `path/to/file.ext:line` references that an agent can follow later, e.g. `src/components/Auth.tsx:12-24`.
- **Keep it scannable**: Use clear headers and bullet points.
- **Include YAML frontmatter**: This enables future tooling to parse and index handoffs.
