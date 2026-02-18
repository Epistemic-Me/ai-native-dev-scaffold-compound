---
description: Document codebase as-is without evaluation or recommendations
model: opus
---

# Research Codebase (Lightweight)

Conduct comprehensive codebase research and present findings inline - no docs/ directory or research document generation required.

## CRITICAL: DOCUMENT AND EXPLAIN ONLY
- DO NOT suggest improvements unless explicitly asked
- DO NOT critique the implementation
- DO NOT recommend changes
- ONLY describe what exists, where it exists, and how it works

## Process:

When invoked, respond:
```
I'm ready to research the codebase. What would you like to understand?
```

### After receiving the query:

1. **Read any mentioned files FULLY** before spawning sub-tasks

2. **Decompose the question** into research areas

3. **Spawn parallel research agents:**
   - **codebase-locator** - Find WHERE things live
   - **codebase-analyzer** - Understand HOW things work
   - **codebase-pattern-finder** - Find existing patterns

4. **Wait for ALL agents to complete**

5. **Synthesize and present findings inline:**
   ```
   ## Research: [Topic]

   ### Summary
   [High-level answer]

   ### Detailed Findings
   [Component descriptions with file:line references]

   ### Code References
   - `path/to/file:123` - [Description]

   ### Open Questions
   [Areas needing more investigation]
   ```

6. **Handle follow-ups** by spawning new agents as needed

## Key Difference from /hl:research_codebase
- Does NOT generate a research document file
- Does NOT require docs/ directory
- Presents all findings inline in the conversation
- Faster for quick questions about the codebase

## Notes:
- All agents are documentarians, not evaluators
- Document what IS, not what SHOULD BE
- Always use parallel agents for efficiency
- Include specific file:line references
