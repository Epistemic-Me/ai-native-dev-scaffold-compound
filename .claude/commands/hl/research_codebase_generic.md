---
description: Research codebase comprehensively using parallel sub-agents
model: opus
---

# Research Codebase (Generic)

Conduct comprehensive codebase research using parallel sub-agents. This is the most thorough research variant - spawns multiple specialized agents and generates a detailed research document.

## CRITICAL: DOCUMENT AND EXPLAIN ONLY
- DO NOT suggest improvements unless explicitly asked
- DO NOT critique the implementation
- DO NOT recommend changes
- ONLY describe what exists and how it works

## Process:

### 1. Read Mentioned Files First

- Read all directly mentioned files FULLY (no limit/offset)
- Read these in the main context BEFORE spawning sub-tasks

### 2. Decompose the Research Question

- Break into composable research areas
- Think deeply about patterns, connections, and architecture
- Create research plan with TodoWrite

### 3. Deploy Research Agents

Spawn multiple specialized agents in parallel:

**Codebase Research:**
- **codebase-locator** - Find where files and components live
- **codebase-analyzer** - Understand how specific code works
- **codebase-pattern-finder** - Find existing patterns and examples

**Historical Context:**
- **thoughts-locator** - Find existing documentation about the topic
- **thoughts-analyzer** - Extract insights from relevant documents

**External Research (only if explicitly asked):**
- **web-search-researcher** - External docs and resources

### 4. Synthesize Findings

- Wait for ALL agents to complete
- Compile results across components
- Include specific file:line references
- Highlight cross-component connections

### 5. Generate Research Document

Write to `docs/research/YYYY-MM-DD-description.md`:

```markdown
# Research: [Topic]

**Date**: [Current date]
**Branch**: [Current branch]
**Commit**: [Current commit hash]

## Research Question
[Original query]

## Summary
[High-level findings]

## Detailed Findings

### [Component/Area 1]
- Description (file.ext:line)
- How it connects to other components

### [Component/Area 2]
...

## Code References
- `path/to/file:123` - Description

## Architecture Documentation
[Patterns, conventions, design implementations]

## Related Documentation
[Links to ADRs, other research]

## Open Questions
[Areas needing investigation]
```

### 6. Present and Follow Up

- Present concise summary
- Ask about follow-up questions
- Append follow-ups to same document

## Key Difference from Other Research Commands
- **vs /hl:research_codebase**: Same output format, but more aggressive agent deployment
- **vs /hl:research_codebase_nt**: Generates a document file, not just inline findings
- This is the "go deep" variant for comprehensive understanding
