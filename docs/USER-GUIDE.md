# AI-Native PR Workflow: A Tactical Guide for Engineering Teams

> Works with **any project management tool** — Linear, Jira, Shortcut, GitHub Issues. The workflow is PM-tool-agnostic.
>
> **Repos**: [Walk (Level 1-2)](https://github.com/Epistemic-Me/ai-native-dev-scaffold-walk) | [Run (Level 3-4)](https://github.com/Epistemic-Me/ai-native-dev-scaffold-run)

---

## Why This Exists

Traditional software has deterministic outputs. You write tests. They pass or fail. Done.

AI products are different. The same input produces different outputs. "Good" is subjective per user. You can't unit test vibes.

And yet you still need to ship with confidence, trace decisions, and not regress when you deploy.

This guide covers the PR workflow, repo structure, documentation system, CI/CD gates, and decision tracking that lets a small team (2-4 engineers) ship production AI with the rigor of a 50-person org — using Claude Code as an AI-native development partner.

## Quick Start (5 Minutes)

```bash
# Clone the scaffold
git clone https://github.com/Epistemic-Me/ai-native-dev-scaffold-walk.git my-project
cd my-project && rm -rf .git && git init && git add -A && git commit -m "init"

# Start your first PR
/project:start-pr 001 my-first-feature

# Fill the docs (THIS IS WHERE 65% OF BRAINPOWER GOES):
# 1. RESEARCH.md — understand the problem
# 2. TEST-STRATEGY.md — define exit criteria BEFORE code
# 3. IMPLEMENTATION-PLAN.md — step-by-step plan mapped to ACs

# Execute the plan
/project:execute-pr 001

# Review, merge, and close — all in one command
/project:review-pr 001
```

Three commands. Zero ambiguity. Read on for the full guide.

---


---

## The Big Idea: Brainpower Moves Left

**Old world**: Think a little, code a lot, discover problems in QA, patch in prod.
**New world**: Think a LOT, define exit criteria with AI, then execute fast with confidence.

The research and planning phase is where you spend 60-70% of your cognitive effort now. You iterate with the AI — "what am I missing? what are the edge cases? what does the acceptance criteria actually look like?" — until you KNOW what you're building and how you'll verify it works. Then execution is just following the plan.

```
┌─────────────────────────────────────────────────────────────┐
│                    RESEARCH & PLAN (60-70% of brain work)   │
│                                                             │
│  /start-pr        Create branch + docs folder + templates   │
│      │                                                      │
│      v                                                      │
│  RESEARCH.md      Iterate with AI: requirements, current    │
│                   state, gaps, risks, options considered     │
│      │                                                      │
│      v                                                      │
│  TEST-STRATEGY    Define exit criteria: acceptance criteria  │
│  .md              table, test matrix, what "done" looks     │
│                   like BEFORE writing a line of code         │
│      │                                                      │
│      v                                                      │
│  IMPLEMENTATION   Step-by-step plan: files to change,       │
│  -PLAN.md         code examples, verification checklist     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                    EXECUTE (30-40% — follow the plan)        │
│                                                             │
│  /execute-pr      Implement against the plan. Fast.         │
│                   Reads PLAN.md, tracks progress, commits.  │
│      │                                                      │
│      v                                                      │
│  /review-pr       AI review + docs-gate + merge + close     │
│                   Walk: review → gate → merge → archive     │
│                   Run: + stakeholder-alignment + compound    │
│                                                             │
└─────────────────────────────────────────────────────────────┘

THE 3-COMMAND LOOP:  /start-pr  →  /execute-pr  →  /review-pr
Walk: review-pr does review + gate + merge + close
Run:  review-pr also runs stakeholder-alignment + compound automatically
```

---

## PM Tool Integration (Linear / Jira / Shortcut / GitHub Issues)

The workflow connects to your PM tool at three points:

| Lifecycle moment | What happens in PM tool                                                | Command      |
| ---------------- | ---------------------------------------------------------------------- | ------------ |
| **PR created**   | Ticket moves to "In Progress", branch + docs path added to description | `/start-pr`  |
| **PR in review** | Ticket moves to "In Review" (optional)                                 | `/review-pr` |
| **PR merged**    | Ticket moves to "Done", PR link added                                  | `/review-pr` (auto on merge) |

**The rule**: 1 ticket = 1 PR = 1 docs folder. If work spans multiple PRs, create a parent ticket with sub-issues.

**For Linear**: We use the Linear MCP to read/update tickets automatically. For Jira: use `jira-mcp` or the `jira` CLI. For GitHub Issues: use `gh issue` commands. The commands in `.claude/commands/` can be customized to call your PM tool's API.

**Ticket description template** (works in any tool):
```markdown
## Context
[Link to docs/prs/YYYY-MM-DD-PR-{num}-{slug}/RESEARCH.md]

## Acceptance Criteria
[Copied from TEST-STRATEGY.md AC table]

## Branch
feature/{ticket-id}-pr-{num}-{slug}

## Paper Trail
- Research: docs/prs/.../RESEARCH.md
- Plan: docs/prs/.../IMPLEMENTATION-PLAN.md
- Tests: docs/prs/.../TEST-STRATEGY.md
```

---

## Part 1: Repo Structure

### The Starter Template

Any team can adopt this structure. Clone it, delete the example content, keep the skeleton.

```
your-repo/
├── .claude/
│   ├── commands/                    # Slash commands for Claude Code
│   │   ├── start-pr.md             # 1. Create branch + docs scaffold
│   │   ├── execute-pr.md           # 2. Implement from plan with tracking
│   │   ├── review-pr.md            # 3. Review + gate + merge + close
│   │   ├── decision.md             # Utility: create ADR
│   │   └── context-update.md       # Utility: refresh .context docs
│   │   # Run level adds: stakeholder-alignment.md, compound.md
│   └── settings.json               # Claude Code hooks config
│
├── .github/
│   └── workflows/
│       └── pr-docs-gate.yml        # CI gate: blocks merge if docs missing
│
├── docs/
│   ├── .context/                    # AI-readable project context (the brain)
│   │   ├── JTBD.md                  # Jobs to be done with evidence
│   │   ├── ICP.md                   # Ideal customer profiles
│   │   ├── ROADMAP.md               # Phase-level roadmap
│   │   ├── ARCHITECTURE-TAXONOMY.md # System layers and boundaries
│   │   ├── KNOWN_ISSUES.md          # Active bugs and tech debt
│   │   ├── CURRENT_SPRINT.md        # What's in flight right now
│   │   ├── ACTIVE_PRS.md            # Open + recently merged PRs
│   │   ├── RECENT_DECISIONS.md      # Rolling 10-decision log
│   │   ├── ADR_CONTEXT.md           # Machine-readable decision lookup
│   │   ├── COMPOUND_REPORT.md       # Self-model health report
│   │   └── BRAND-GUIDELINES.md      # Voice, tone, naming conventions
│   │
│   ├── decisions/                   # Architecture Decision Records
│   │   ├── _INDEX.md                # Master registry (ID, date, title, status)
│   │   ├── _TEMPLATE.md             # Blank ADR template
│   │   └── YYYY-MM-DD-slug.md       # Individual ADR files
│   │
│   ├── brainstorms/                 # Pre-ADR thinking documents
│   │   └── YYYY-MM-DD-slug.md       # Informal design explorations
│   │
│   └── prs/                         # Per-PR documentation folders
│       └── YYYY-MM-DD-PR-{num}-{slug}/
│           ├── RESEARCH.md           # Requirements, current state, gaps
│           ├── IMPLEMENTATION-PLAN.md # Step-by-step with code examples
│           ├── TEST-STRATEGY.md      # AC coverage table + test matrix
│           ├── REVIEW.md             # AI code review with verdict
│           ├── STAKEHOLDER-ALIGNMENT.md # Per-stakeholder scores
│           ├── stakeholder-alignment.json # Machine-readable alignment data
│           └── compound_extract.json  # Episode payload for self-model API
│
├── scripts/
│   ├── pr_docs_check.py             # Docs-gate validation logic
│   └── compound.py                  # Self-model CLI (extract, sync, report)
│
├── CLAUDE.md                        # Project instructions for Claude Code
└── .stakeholders.json.example       # Stakeholder config template
```

### What Each Layer Does

| Layer | Purpose | Updated by |
|---|---|---|
| `.claude/commands/` | Slash commands that enforce workflow | Engineers (rarely, when process evolves) |
| `docs/.context/` | The project's brain — AI reads these at session start | `/context-update` command + manual |
| `docs/decisions/` | ADRs — permanent record of architectural choices | `/decision` command |
| `docs/brainstorms/` | Pre-decision thinking — informal, not indexed | Engineers before major work |
| `docs/prs/` | Per-PR artifacts — the paper trail | PR lifecycle commands |
| `scripts/` | Automation — docs-gate checks, self-model sync | Engineers |
| `CLAUDE.md` | Master instructions for Claude Code sessions | Engineers (carefully) |

---

## Part 2: The PR Lifecycle — Step by Step

### Step 1: `/start-pr` — Create the Paper Trail

**What it does**: Creates a feature branch, a `docs/prs/` folder with templates, updates `ACTIVE_PRS.md`, and moves the linked ticket (Linear/Jira/etc.) to "In Progress."

**Input**: A slug (e.g., `add-batch-endpoint`), optionally a ticket ID (e.g., `CLA-75`, `PROJ-123`).

**What you get**:
```
docs/prs/2026-04-10-PR-345-add-batch-endpoint/
├── RESEARCH.md              # Fill in FIRST: requirements, current state, gaps
├── TEST-STRATEGY.md         # Fill in SECOND: exit criteria, AC table, test matrix
└── IMPLEMENTATION-PLAN.md   # Fill in THIRD: step-by-step plan to satisfy the ACs
```

**Why it matters**: Every PR starts with research, not code. The templates force you to understand the problem before proposing a solution.

**How to get started** (without Claude Code):
```bash
mkdir -p docs/prs/$(date +%Y-%m-%d)-PR-XXX-your-slug
cp docs/prs/_templates/* docs/prs/$(date +%Y-%m-%d)-PR-XXX-your-slug/
```

---

### Step 2: Research & Plan — Where You Spend Your Brain

**This is the most important step.** You spend 60-70% of your cognitive effort here. You iterate with the AI until you deeply understand what you're building, why, and how you'll know it works.

#### 2a. RESEARCH.md — Understand the Problem

Iterate with the AI: "Read the codebase. What exists today? What's the gap? What are the risks?"

```markdown
## Requirements Analysis
What does the ticket/user story actually need? (Link to ticket)

## Current State Analysis
What exists today? What code, APIs, data models are relevant?

## Implementation Gap Analysis
What's missing between current state and requirements?

## Options Considered
### Option A: {approach}
Pros / Cons / Effort estimate

### Option B: {approach}
Pros / Cons / Effort estimate

## Recommendation
Which option and why.

## Dependencies and Risks
What could go wrong? What do we depend on?

## Open Questions
What do we still not know? (These get answered before moving to TEST-STRATEGY)
```

**Key iteration pattern**: Ask the AI to read the relevant code, then ask "what am I missing?" and "what are the edge cases?" Do this 3-5 times. Each round surfaces things you didn't think of.

#### 2b. TEST-STRATEGY.md — Define Exit Criteria BEFORE Code

This is the grading rubric. What does "done" look like? If you can't write this, you don't understand the problem yet — go back to RESEARCH.

```markdown
## Acceptance Criteria
| AC-ID | Criteria | Priority |
|-------|----------|----------|
| AC1 | Batch endpoint accepts 1-500 items and returns results | P0 |
| AC2 | Invalid schema returns 422 with field-level errors | P0 |
| AC3 | Timeout after 30s with partial results returned | P1 |

## Test Matrix
| Test-ID | File | Test Case | AC Covered | Pass Criteria |
|---------|------|-----------|------------|---------------|
| T1 | test_batch.py | test_batch_100_items | AC1 | 200 status, all items processed |
| T2 | test_batch.py | test_invalid_schema | AC2 | 422 status, errors array present |
| T3 | test_batch.py | test_timeout_partial | AC1, AC3 | 200 status, partial flag true |

## Definition of Done
- [ ] All ACs covered by at least one test
- [ ] Tests pass in CI
- [ ] No P0 regressions
- [ ] IMPLEMENTATION-PLAN.md verification checklist complete
```

**Why test strategy before implementation plan**: You can't plan HOW to build something until you know WHAT success looks like. The ACs constrain the implementation. If you write the plan first, you'll build what's easy, not what's needed.

#### 2c. IMPLEMENTATION-PLAN.md — The Execution Blueprint

NOW you plan the code. Every step maps to an AC. This is what you'll follow during execution.

```markdown
## Chosen Approach
{Which option from RESEARCH.md and why}

## Scope
**In scope**: {what this PR will do}
**Out of scope**: {what it won't — important for avoiding scope creep}

## Files Summary
| File | Action | Purpose |
|------|--------|---------|
| src/api/batch.py | Create | New batch endpoint |
| src/models/batch.py | Create | Request/response schemas |
| tests/test_batch.py | Create | AC1, AC2, AC3 coverage |

## Step-by-Step Implementation
### Step 1: Create batch schema (AC2)
{Code example showing the schema with validation}

### Step 2: Implement endpoint (AC1)
{Code example showing the handler}

### Step 3: Add timeout handling (AC3)
{Code example showing timeout logic}

## Verification Checklist
- [ ] Step 1 complete — schema validates correctly
- [ ] Step 2 complete — endpoint returns results
- [ ] Step 3 complete — timeout returns partial results
- [ ] All tests in TEST-STRATEGY.md pass
```

**The handoff**: Once RESEARCH + TEST-STRATEGY + IMPLEMENTATION-PLAN are solid, you (or another engineer, or the AI) can execute the plan with minimal ambiguity. The thinking is done. The coding is mechanical.

---

### Step 3: `/execute-pr` — Implement the Plan

**What it does**: Reads PLAN.md, creates a task list, implements phase by phase with progress tracking and incremental commits. Updates IMPLEMENTATION.md with changes and deviations.

You're following a plan with clear exit criteria, not discovering requirements while coding.

**Key disciplines**:
- The command reads PLAN.md and works through it step by step
- Run the tests from TEST-STRATEGY.md as you go
- If you discover the plan is wrong, **stop and update the plan first**
- If requirements change, update RESEARCH.md → TEST-STRATEGY.md → PLAN.md in that order, then resume

**The anti-pattern**: "I'll just code this differently and update the docs later." No. The docs lead, the code follows.

---

### Step 4: `/review-pr` — Review + Gate + Merge + Close

**What it does**: This is the exit command. It handles everything from review through merge:

1. Spawns a fresh sub-agent for AI code review (clean context window)
2. Generates `REVIEW.md` with verdict + per-AC coverage
3. Runs docs-gate check (same as CI)
4. **If Approve + gate passes**: merges PR, archives docs, updates ACTIVE_PRS.md
5. **If issues found**: reports what to fix, does NOT merge

**At Run level (Level 3-4), review-pr also automatically runs**:
- `/stakeholder-alignment` → STAKEHOLDER-ALIGNMENT.md (scores PR against digital twins)
- `/compound` → compound_extract.json (extracts episode for self-model)
- Enhanced docs-gate (includes stakeholder scores)

The dev doesn't run extra commands. Same `/review-pr`, richer output at Run level.

**What you get in `REVIEW.md`**:
```markdown
## Review v1

**Verdict**: Approve (or Request Changes)
**Reviewed**: 2026-04-10

### Summary
One paragraph on what the PR does and whether it achieves its stated goals.

### Per-AC Coverage Table
| AC | Description | Test Coverage | Status |
|----|-------------|---------------|--------|
| AC1 | Batch endpoint handles 100+ items | T1, T3 | PASS |
| AC2 | Error on invalid schema | T2 | PASS |

### Risk Assessment
- Risk 1: ...

### Post-Merge Checklist
- [ ] Run migration on staging
```

**Why a sub-agent**: Clean context window. The reviewer hasn't seen your implementation conversations, so it gives an independent read.

### CI — `pr-docs-gate.yml`

The same checks that `/review-pr` runs locally also run in CI on every PR targeting `main`. **Blocks merge on failure.**

**Walk-level checks (blocking)**:
1. PR docs folder exists
2. RESEARCH.md present
3. TEST-STRATEGY.md present
4. PLAN.md present

**Run-level checks (adds)**:
5. REVIEW.md with Approve verdict
6. STAKEHOLDER-ALIGNMENT.md with aggregate score

**Advisory (non-blocking)**: compound_extract.json, stakeholder scores below 0.3, unchecked DoD items.

**Small PR exemption**: 5 or fewer changed lines in docs/config files skip the gate.

---

## Part 3: Architecture Decision Records (ADRs)

### Why ADRs

Code tells you WHAT. Commits tell you WHEN. ADRs tell you WHY.

Six months from now, someone will ask "why did we use Supabase instead of Auth0?" The answer is in `docs/decisions/2026-02-25-supabase-jwt-auth-foundation.md`, not in someone's memory.

### ADR Template

```markdown
# ADR-{NNN}: {Title}

**Date**: YYYY-MM-DD
**Status**: Proposed | Accepted | Deprecated | Superseded by ADR-XXX
**PR**: #{number} (if applicable)

## Context

What is the problem? What forces are at play?

### GTM / Product Context

Why does this matter for the business, not just the code?

## Decision

What did we decide and why?

**Decisions**: {D-XX, D-YY} (links to fine-grained decision IDs in ADR_CONTEXT.md)

## Consequences

### Positive
- ...

### Negative
- ...

## Alternatives Considered

### Alternative A
**Description**: ...
**Pros**: ...
**Cons**: ...
**Why not chosen**: ...

## Related
- ADR-{NNN}: {related decision}
- Brainstorm: docs/brainstorms/YYYY-MM-DD-slug.md
```

### ADR Index

`docs/decisions/_INDEX.md` is the master registry:

```markdown
| ID | Date | Title | Status |
|----|------|-------|--------|
| ADR-001 | 2025-01-01 | Session ID Strategy | Accepted |
| ADR-002 | 2025-12-14 | AI-Native Documentation | Accepted |
| ADR-004 | 2026-02-25 | Supabase JWT Auth | Superseded by ADR-012 |
```

### The `/decision` Command

Creates the ADR file, appends to the index, updates `RECENT_DECISIONS.md` (rolling 10-row window), and adds a row to `ADR_CONTEXT.md` (machine-readable lookup).

---

## Part 4: Context Docs — The Project Brain

### What Are Context Docs?

Files in `docs/.context/` that Claude Code reads at session start. They give the AI (and new team members) instant context on the project without reading the entire codebase.

### The Core Set (Start With These)

| File | What it contains | Update frequency |
|---|---|---|
| `JTBD.md` | Jobs to be done with evidence strength scores | After customer interviews |
| `ICP.md` | Ideal customer profiles with pain points | After customer validation |
| `ROADMAP.md` | Phase-level plan (not sprint-level) | Monthly or after major pivots |
| `ARCHITECTURE-TAXONOMY.md` | System layers, boundaries, what's Engine vs Platform vs App | After architectural decisions |
| `KNOWN_ISSUES.md` | Active bugs, tech debt, acknowledged gaps | Continuously |
| `CURRENT_SPRINT.md` | What's in flight right now | Every sprint start |
| `ACTIVE_PRS.md` | Open and recently merged PRs | Automatically via `/start-pr` and `/close-pr` |

### The Decision Layer (Add When You Have 5+ ADRs)

| File | What it contains | Update frequency |
|---|---|---|
| `ADR_CONTEXT.md` | Machine-readable decision lookup (ADR → technical reason → GTM reason) | Via `/decision` command |
| `RECENT_DECISIONS.md` | Rolling 10-row table of latest decisions with narrative summaries | Via `/decision` command |

### The Intelligence Layer (Add When Doing Customer Research)

| File | What it contains | Update frequency |
|---|---|---|
| `COMPOUND_REPORT.md` | Self-model health report — observation context states + stakeholder alignment | Via `/compound` report |
| `BRAND-GUIDELINES.md` | Voice, tone, naming conventions, visual identity | Rarely |

### Keeping Context Docs Fresh

**The rule**: Context docs should be accurate enough that a new team member (or a fresh Claude session) could understand the project in 5 minutes of reading.

**Maturity stages**:

| Stage | What to do |
|---|---|
| **Week 1-4 (Bootstrap)** | Create JTBD.md, ROADMAP.md, ARCHITECTURE-TAXONOMY.md, KNOWN_ISSUES.md. Stub content is fine. |
| **Month 2-3 (Foundations)** | Add ICP.md after first customer conversations. Start ADR_CONTEXT.md when you hit 3+ decisions. Add CURRENT_SPRINT.md when you have a sprint cadence. |
| **Month 4-6 (Maturity)** | Full context doc set. Run `/context-status` monthly to check for stale docs. COMPOUND_REPORT.md if using the self-model API. |
| **Ongoing** | Every PR that changes architecture should trigger a `/context-update`. Every customer interview should update JTBD.md and ICP.md. |

**Anti-pattern**: Context docs that were written once and never updated. A stale ROADMAP.md is worse than no ROADMAP.md because Claude will plan against outdated goals.

---

## Part 5: Getting Started — The 1-Hour Setup

### For a brand new repo:

```bash
# 1. Create the directory structure
mkdir -p .claude/commands docs/.context docs/decisions docs/brainstorms docs/prs scripts .github/workflows

# 2. Create CLAUDE.md at the root
cat > CLAUDE.md << 'EOF'
# CLAUDE.md

## Git Workflow
Always create feature branches and PRs. Never push directly to main.

## PR Documentation
For non-trivial PRs, create docs in `docs/prs/` before implementation.
See docs/prs/ for examples.

## Context Docs
Read docs/.context/ for project context. These are the source of truth
for project goals, architecture, and known issues.
EOF

# 3. Create the ADR index and template
cat > docs/decisions/_INDEX.md << 'EOF'
# Architecture Decision Records

| ID | Date | Title | Status |
|----|------|-------|--------|
EOF

cat > docs/decisions/_TEMPLATE.md << 'EOF'
# ADR-{NNN}: {Title}

**Date**: YYYY-MM-DD
**Status**: Proposed
**PR**: #

## Context
## Decision
## Consequences
### Positive
### Negative
## Alternatives Considered
EOF

# 4. Create starter context docs
touch docs/.context/JTBD.md
touch docs/.context/ROADMAP.md
touch docs/.context/ARCHITECTURE-TAXONOMY.md
touch docs/.context/KNOWN_ISSUES.md
touch docs/.context/ACTIVE_PRS.md

# 5. Create the docs-gate CI workflow (see Part 6 below for contents)
```

### For an existing repo:

Run this Claude Code prompt to analyze and scaffold:

```
Analyze this repository and create the following:
1. A docs/.context/ARCHITECTURE-TAXONOMY.md describing the current system layers
2. A docs/.context/KNOWN_ISSUES.md listing tech debt and acknowledged gaps
3. A docs/.context/ROADMAP.md with the current high-level plan
4. A CLAUDE.md with project-specific instructions for Claude Code sessions

Read the codebase first. Don't invent — describe what's actually here.
```

---

## Part 6: CI/CD — The Docs Gate

### Minimal `pr-docs-gate.yml`

```yaml
name: PR Docs Gate
on:
  pull_request:
    branches: [main]

jobs:
  docs-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      
      - name: Run docs gate
        env:
          PR_NUMBER: ${{ github.event.pull_request.number }}
        run: python scripts/pr_docs_check.py $PR_NUMBER
      
      - name: Post PR comment
        if: always()
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const summary = fs.existsSync('/tmp/pr-docs-summary.md') 
              ? fs.readFileSync('/tmp/pr-docs-summary.md', 'utf8')
              : 'Docs gate check completed.';
            
            const comments = await github.rest.issues.listComments({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
            });
            
            const existing = comments.data.find(c => 
              c.body.includes('<!-- pr-docs-gate -->'));
            
            const body = `<!-- pr-docs-gate -->\n${summary}`;
            
            if (existing) {
              await github.rest.issues.updateComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                comment_id: existing.id,
                body
              });
            } else {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.issue.number,
                body
              });
            }
```

### Minimal `pr_docs_check.py`

```python
#!/usr/bin/env python3
"""PR docs gate checker. Exit 0=pass, 1=fail, 2=exempt."""
import sys, os, re, json
from pathlib import Path

def main():
    pr_num = sys.argv[1] if len(sys.argv) > 1 else None
    if not pr_num:
        print("Usage: pr_docs_check.py <PR_NUMBER>")
        sys.exit(1)
    
    docs_dir = Path("docs/prs")
    pr_folder = None
    
    # Find matching PR folder
    for folder in sorted(docs_dir.iterdir(), reverse=True):
        if folder.is_dir() and f"PR-{pr_num}" in folder.name:
            pr_folder = folder
            break
    
    if not pr_folder:
        write_summary(pr_num, "FAIL", ["No docs/prs/ folder found for PR"])
        sys.exit(1)
    
    required = {
        "RESEARCH.md": pr_folder / "RESEARCH.md",
        "IMPLEMENTATION-PLAN.md": pr_folder / "IMPLEMENTATION-PLAN.md",
        "TEST-STRATEGY.md": pr_folder / "TEST-STRATEGY.md",
        "REVIEW.md": pr_folder / "REVIEW.md",
        "STAKEHOLDER-ALIGNMENT.md": pr_folder / "STAKEHOLDER-ALIGNMENT.md",
    }
    
    # Also accept PLAN.md as alias for IMPLEMENTATION-PLAN.md
    if not required["IMPLEMENTATION-PLAN.md"].exists():
        alt = pr_folder / "PLAN.md"
        if alt.exists():
            required["IMPLEMENTATION-PLAN.md"] = alt
    
    results = []
    for name, path in required.items():
        exists = path.exists() and path.stat().st_size > 50
        results.append((name, "PASS" if exists else "FAIL"))
    
    # Check REVIEW.md for Approve verdict
    review_path = required["REVIEW.md"]
    if review_path.exists():
        content = review_path.read_text()
        if re.search(r'(?i)verdict.*approve', content):
            results.append(("Review verdict: Approve", "PASS"))
        else:
            results.append(("Review verdict: Approve", "FAIL"))
    
    # Check STAKEHOLDER-ALIGNMENT.md for aggregate score
    sa_path = required["STAKEHOLDER-ALIGNMENT.md"]
    if sa_path.exists():
        content = sa_path.read_text()
        if re.search(r'Aggregate Score', content):
            results.append(("Stakeholder score present", "PASS"))
        else:
            results.append(("Stakeholder score present", "FAIL"))
    
    failed = [r for r in results if r[1] == "FAIL"]
    status = "FAIL" if failed else "PASS"
    write_summary(pr_num, status, [f"{r[0]}: {r[1]}" for r in results])
    sys.exit(1 if failed else 0)

def write_summary(pr_num, status, checks):
    lines = [f"## PR Docs Gate: {status}\n", f"**PR**: #{pr_num}\n"]
    lines.append("| Check | Status |")
    lines.append("|---|---|")
    for check in checks:
        parts = check.split(": ")
        name = parts[0]
        st = parts[1] if len(parts) > 1 else "?"
        emoji = "PASS" if st == "PASS" else "FAIL"
        lines.append(f"| {name} | {emoji} |")
    
    summary = "\n".join(lines)
    Path("/tmp/pr-docs-summary.md").write_text(summary)
    print(summary)

if __name__ == "__main__":
    main()
```

---

## Part 7: Prompts for Repo Analysis and Cleanup

### Prompt 1: Architecture Discovery
```
Read this entire codebase. Create docs/.context/ARCHITECTURE-TAXONOMY.md that describes:
1. The system layers (what runs where, what talks to what)
2. Key abstractions and their boundaries
3. Data flow from input to output
4. External dependencies and integration points

Don't evaluate or recommend. Just describe what's here accurately.
```

### Prompt 2: Tech Debt Audit
```
Scan this codebase for:
1. TODO/FIXME/HACK comments
2. Duplicated logic across files
3. Dead code (unused exports, unreachable branches)
4. Missing error handling on external calls
5. Hardcoded values that should be config

Create docs/.context/KNOWN_ISSUES.md organized by severity (P0/P1/P2).
```

### Prompt 3: Test Gap Analysis
```
Analyze the test coverage of this codebase:
1. What has tests? What doesn't?
2. Which critical paths have no test coverage?
3. Are there integration tests for external API calls?
4. What's the ratio of unit to integration to E2E tests?

Create a TEST-GAPS.md with specific recommendations prioritized by risk.
```

### Prompt 4: CLAUDE.md Bootstrap
```
Read this repository's structure, package.json/pyproject.toml, CI config, and README.
Create a CLAUDE.md that tells future Claude Code sessions:
1. How to run the project locally
2. How to run tests
3. The git workflow (branching, PR process)
4. Key files and their roles
5. Environment variables needed
6. Common gotchas

Be specific. Include actual commands, not placeholders.
```

### Prompt 5: Decision Archaeology
```
Read the git log for the last 3 months. Identify:
1. Major architectural changes (new frameworks, removed dependencies, schema changes)
2. Reverted commits or quick-fix-then-proper-fix patterns
3. Large refactors

For each, create an ADR in docs/decisions/ explaining what was decided and why,
reconstructed from the commit messages and code changes. Mark them as "Accepted (retroactive)".
```

---

## Part 8: Maturity Model

### Level 0: Chaos
- No PR docs, no ADRs, no context docs
- "Why did we do this?" answered by "ask Dave, he was here"
- Claude Code sessions start from zero every time

### Level 1: Paper Trail (Week 1-2 to set up)
- CLAUDE.md exists and is accurate
- PRs have RESEARCH.md and IMPLEMENTATION-PLAN.md
- `docs/.context/` has ARCHITECTURE-TAXONOMY.md and KNOWN_ISSUES.md
- Git workflow enforced (no direct push to main)

### Level 2: Verified (Week 3-4 to set up)
- TEST-STRATEGY.md with AC coverage table per PR
- REVIEW.md with AI code review and verdict
- CI docs-gate blocks merge on missing artifacts
- ADR index with 3+ decisions tracked

### Level 3: Aligned (Month 2-3 to set up)
- STAKEHOLDER-ALIGNMENT.md with scored perspectives per PR
- Full `.context/` doc set (JTBD, ICP, ROADMAP, ADR_CONTEXT)
- `/context-update` run monthly to keep docs fresh
- Brainstorms precede major initiatives

### Level 4: Compounding (Month 4+ to set up)
- Self-model API integration via `/compound`
- Transcript processing for customer interviews
- Prediction-outcome tracking on decisions
- Context docs updated from real customer signal, not guesses

---

## Part 9: FAQ

### Setup & Getting Started

**Q: Do I need Claude Code for this to work?**
A: No. The repo structure, PR docs, ADRs, and CI gate work with any development workflow. Claude Code commands automate the process, but you can create the same artifacts manually. The value is in the structure, not the tooling.

**Q: How long does it take to set up from scratch?**
A: Level 1 (paper trail) takes 1-2 hours. Level 2 (verified with CI gate) takes a day. Level 3-4 require ongoing investment over months as you do customer research and make architectural decisions.

**Q: Can I adopt this incrementally?**
A: Yes. Start with CLAUDE.md + ARCHITECTURE-TAXONOMY.md + KNOWN_ISSUES.md. Add the PR docs folder convention next. Add CI gate when you have 3+ PRs following the pattern. Add ADRs when you make your first contested architectural decision.

**Q: What if my team is just me?**
A: Even better. The paper trail is for future-you. Six months from now you won't remember why you chose Supabase over Auth0. The ADR will.

### PR Workflow

**Q: Do I need all 7 artifacts for every PR?**
A: No. The CI gate exempts PRs with 5 or fewer changed lines in docs/config files. For trivial changes (typo fixes, dependency bumps), skip the docs folder entirely. The gate is for non-trivial PRs where you're making decisions that affect users.

**Q: What if I disagree with the AI code review?**
A: The review is a tool, not a gate. If the AI says "Request Changes" but you disagree, update the REVIEW.md with your reasoning and override the verdict. The point is documented reasoning, not blind obedience.

**Q: How long does the full PR lifecycle take?**
A: For a typical feature PR: `/start-pr` (2 min) → fill docs + `/execute-pr` (hours/days) → `/review-pr` (3 min, handles merge + close). Three commands total. The overhead is ~5 minutes per PR for a complete paper trail.

**Q: What if stakeholder alignment scores are low?**
A: Low scores are signal, not blockers. A score of 0.3 for a stakeholder means the PR doesn't serve their goals well. That might be fine — not every PR serves every stakeholder. The value is knowing whose goals you're NOT serving so you can communicate proactively.

### ADRs & Decisions

**Q: When should I create an ADR vs just making the change?**
A: Create an ADR when (a) you considered alternatives, (b) the decision is hard to reverse, or (c) someone will ask "why?" in 6 months. If you're choosing between Redis and Memcached for caching — ADR. If you're renaming a variable — no ADR.

**Q: What if a decision gets reversed?**
A: Mark the original ADR as "Superseded by ADR-XXX" and create a new ADR explaining why the reversal happened. Don't delete the original. The history of why you went one way and then came back is valuable.

**Q: Should brainstorms be formal?**
A: No. Brainstorms are thinking-out-loud documents. No template required. They exist so you can reference "we explored this in the brainstorm" from a later ADR or PR. Many brainstorms lead to nothing — that's fine.

### Context Docs

**Q: How do I know when a context doc is stale?**
A: Run `/context-status` (if using Claude Code) or manually check: Does the ROADMAP.md describe what you're actually working on? Does KNOWN_ISSUES.md list the bugs you know about? If a new team member read these docs, would they be confused? If yes, update.

**Q: Who updates context docs?**
A: Everyone. After a customer interview, update JTBD.md and ICP.md. After an architectural decision, update ARCHITECTURE-TAXONOMY.md. After a sprint planning, update CURRENT_SPRINT.md. Make it a habit, not a ceremony.

**Q: What if context docs and code disagree?**
A: Code wins. Update the context doc. Context docs describe intent and understanding — if the code diverged, either the code is wrong (fix the code) or understanding evolved (fix the doc). Never leave them in conflict.

**Q: Do context docs replace a wiki?**
A: They replace the "project context" portion of a wiki. They don't replace runbooks, onboarding guides, or API docs. Context docs are specifically optimized for AI consumption at session start — concise, structured, up-to-date.

### Scaling — Enterprise Monorepo with Domain Teams

**Q: Does this work for a 20-person team?**
A: Yes. See Part 13 below — full Dayforce-scale example with domain teams, shared NuGet layers, and 200+ engineers.

**Q: Does this work for monorepos?**
A: Yes — monorepos are actually the BEST fit because cross-domain context docs prevent the tribal knowledge silos that kill large orgs. See Part 13 for the exact directory structure.

**Q: How does this interact with existing CI/CD?**
A: The docs-gate is additive. It's a new GitHub Actions job that runs alongside your existing tests, linting, and build checks. It doesn't replace anything — it adds a documentation quality gate. The CI gate uses CODEOWNERS to route PR doc reviews to the right domain team.

---

## Part 10: Additional CI Gates (Beyond Docs)

The docs-gate is the foundation, but a mature repo adds more:

### OpenAPI Drift Check
Blocks PRs where code changes don't match the committed API spec.
```yaml
# Triggers on changes to: services/*/src/**
- name: Check OpenAPI spec is current
  run: PYTHONPATH=".:src" python scripts/export_openapi.py --check
```
**Why**: Your API spec is a contract. If you change routes but don't regenerate the spec, consumers break silently.

### Regression Gate
Runs a baseline comparison test suite against stored artifacts.
```yaml
# Downloads previous baseline, runs tests, uploads new baseline on success
- name: Download baseline
  uses: actions/download-artifact@v4
  with:
    name: regression-baseline
    continue-on-error: true  # First run has no baseline

- name: Run regression tests
  run: pytest tests/simulation/test_regression.py
```
**Why**: Non-deterministic AI systems need regression baselines, not just pass/fail. This tracks whether quality is improving or degrading over time.

---

## Part 11: Environment Configuration

### Required `.env` Variables
```bash
# Core API credentials (set after running compound.py init)
CLARITY_API_KEY=your-api-key
CLARITY_USER_ID=your-user-uuid
CLARITY_SELF_MODEL_ID=your-model-id
CLARITY_API_URL=https://your-api.onrender.com  # defaults if omitted

# GitHub (for gh CLI)
GITHUB_TOKEN=ghp_...

# Linear (for ticket tracking)
LINEAR_API_KEY=lin_api_...
```

### First-Time Setup
```bash
# 1. Install the compound CLI dependencies
pip install requests python-dotenv

# 2. Initialize your builder self-model
python scripts/compound.py init
# → Creates your user + self-model via API
# → Outputs CLARITY_USER_ID and CLARITY_SELF_MODEL_ID
# → Add these to .env

# 3. Source .env before any compound command
set -a && source .env && set +a
```

### The `compound.py` CLI — Full Subcommand Reference
```
compound.py init                    # Create builder self-model
compound.py extract <folder>        # Extract episode from PR docs → compound_extract.json
compound.py sync <json-file>        # Push episode to API
compound.py report                  # Generate COMPOUND_REPORT.md
compound.py stakeholder-alignment   # Score PR against stakeholder twins
compound.py process-transcript      # Extract structured data from meeting transcript
compound.py enrich-stakeholder      # Push transcript beliefs to stakeholder model
compound.py backfill                # Backfill historical PRs into self-model
compound.py cleanup-beliefs         # Remove duplicate/stale beliefs
```

---

## Part 12: Brainstorms — Pre-ADR Thinking

### When to Write a Brainstorm

Write a brainstorm BEFORE starting a multi-PR initiative. It's the thinking you do before you know what the PRs will be.

### Brainstorm Format (Informal)
```markdown
# {Initiative Name}

**Date**: YYYY-MM-DD
**Status**: Brainstorm
**Builds on**: [link to prior brainstorms if any]

## Problem Statement
What are we trying to solve and why now?

## Current State
What exists today? What works? What doesn't?

## Proposed Approach
Design sketches, object models, data flows — whatever helps think through it.

## Stages (PR-Level Granularity)
### Stage 1: {Foundation}
- PR 1: {what and why}
- PR 2: {what and why}

### Stage 2: {Core Feature}
- PR 3: ...

## Dependency Graph
PR 1 → PR 2 → PR 3
         ↘ PR 4

## Open Questions
- ...

## Validation Criteria
How do we know this worked?
```

### The Brainstorm → ADR → PR Flow
```
Brainstorm (informal thinking)
    ↓ leads to
ADR (formal decision, if contested or significant)
    ↓ referenced by
PR docs (RESEARCH.md links to brainstorm + ADR)
    ↓ validated by
REVIEW.md + STAKEHOLDER-ALIGNMENT.md
    ↓ archived in
compound_extract.json → self-model API
```

---

## Part 13: Scaling to Enterprise Monorepo — Dayforce Example

> This section uses Dayforce (7,000+ customers, 200+ engineers, 15+ year codebase) as a concrete example. Dayforce has domain teams (Payroll, WFM, Benefits, Core HR, Recruiting) with sub-domain teams (Payroll France, WFM Scheduling, WFM Compliance). The codebase is a monorepo with a deep NuGet dependency chain between a monolith and microservices.
> 
> Substitute your own domain/team names. The pattern is the same.

### Monorepo Directory Structure

```
dayforce/
├── CLAUDE.md                              # Root-level: cross-domain instructions
├── .claude/
│   ├── commands/                          # Shared commands all teams use
│   │   ├── start-pr.md
│   │   ├── review-pr.md
│   │   ├── check-pr.md
│   │   └── ...
│   └── settings.json
│
├── .github/
│   ├── workflows/
│   │   ├── pr-docs-gate.yml              # Global gate — runs for ALL PRs
│   │   ├── payroll-tests.yml             # Domain-specific CI (path-filtered)
│   │   ├── wfm-tests.yml
│   │   └── benefits-tests.yml
│   └── CODEOWNERS                         # Routes PR reviews to domain teams
│
├── docs/
│   ├── .context/                          # CROSS-DOMAIN context (the org brain)
│   │   ├── ARCHITECTURE-TAXONOMY.md       # Monolith ↔ services ↔ UI layers
│   │   ├── KNOWN_ISSUES.md               # Cross-domain tech debt (NuGet chains, etc.)
│   │   ├── COMPLIANCE-REQUIREMENTS.md     # Shared compliance constraints (California, etc.)
│   │   ├── ACTIVE_PRS.md
│   │   ├── RECENT_DECISIONS.md
│   │   └── ADR_CONTEXT.md
│   │
│   ├── decisions/                         # Org-level ADRs
│   │   ├── _INDEX.md
│   │   └── ...
│   │
│   ├── brainstorms/                       # Cross-domain initiatives
│   │
│   └── prs/                               # ALL PR docs live here (flat, not nested by domain)
│       ├── 2026-04-10-PR-4521-payroll-france-overtime/
│       ├── 2026-04-10-PR-4522-wfm-scheduling-conflict-detection/
│       └── ...
│
├── domains/                               # Each domain owns its own context
│   ├── payroll/
│   │   ├── CLAUDE.md                      # Payroll-specific: "When working in this domain..."
│   │   ├── docs/
│   │   │   └── .context/                  # DOMAIN-LEVEL context
│   │   │       ├── ARCHITECTURE.md        # Payroll calc engine, tax tables, pay rules
│   │   │       ├── KNOWN_ISSUES.md        # Payroll-specific debt and bugs
│   │   │       ├── COMPLIANCE.md          # Country-specific pay law requirements
│   │   │       ├── DOMAIN_MODEL.md        # Key entities: PayRun, Earning, Deduction, TaxCalc
│   │   │       └── INTEGRATION_POINTS.md  # What other domains call into Payroll
│   │   ├── src/
│   │   │   ├── core/                      # Shared payroll logic
│   │   │   ├── france/                    # Sub-domain: Payroll France
│   │   │   ├── us/                        # Sub-domain: Payroll US
│   │   │   └── canada/                    # Sub-domain: Payroll Canada
│   │   └── tests/
│   │
│   ├── wfm/
│   │   ├── CLAUDE.md                      # WFM-specific instructions
│   │   ├── docs/
│   │   │   └── .context/
│   │   │       ├── ARCHITECTURE.md        # Punch engine, accruals, scheduling
│   │   │       ├── KNOWN_ISSUES.md        # WFM-specific: accrual going negative, etc.
│   │   │       ├── COMPLIANCE.md          # Labor law: overtime, meal breaks, CA rules
│   │   │       ├── DOMAIN_MODEL.md        # Punch, Schedule, Accrual, PayRule, JobStep
│   │   │       └── INTEGRATION_POINTS.md  # Payroll reads WFM data for pay calc
│   │   ├── src/
│   │   │   ├── core/                      # Core 1 + Core 4 (shared WFM compliance)
│   │   │   ├── scheduling/               # Sub-domain: Scheduling
│   │   │   └── accruals/                 # Sub-domain: Accrual engine
│   │   └── tests/
│   │
│   ├── benefits/
│   │   ├── CLAUDE.md
│   │   ├── docs/.context/
│   │   └── src/
│   │
│   ├── core-hr/
│   │   ├── CLAUDE.md
│   │   ├── docs/.context/
│   │   └── src/
│   │
│   └── shared/                            # Cross-domain shared libraries
│       ├── CLAUDE.md                      # "Changes here affect ALL domains"
│       ├── docs/
│       │   └── .context/
│       │       ├── NUGET_DEPENDENCY_MAP.md  # The 30-package interface chain
│       │       └── BREAKING_CHANGE_LOG.md   # History of cross-domain breakages
│       └── src/
│           ├── interfaces/                # The NuGet interfaces 5-6 levels deep
│           ├── dtos/                      # Shared DTOs
│           └── monolith-bridge/           # Monolith ↔ services adapter layer
│
└── services/                              # Microservices layer
    ├── wfm-service/
    ├── payroll-service/
    └── ...
```

### How CLAUDE.md Cascading Works

Claude Code reads CLAUDE.md files from root → domain → sub-domain. Each level adds context:

```
Root CLAUDE.md:
  "This is the Dayforce monorepo. 200+ engineers across 5 domains.
   Never push to main. Always create PR docs.
   Read docs/.context/ for cross-domain architecture.
   When working in a domain, ALSO read domains/{name}/CLAUDE.md."

domains/wfm/CLAUDE.md:
  "This is the WFM (Workforce Management) domain.
   Owner: WFM Core team (Dhirendra, 7 devs + 1 QA).
   Key entities: Punch, Schedule, Accrual, PayRule, JobStep.
   90% of work is compliance-driven (labor law changes).
   Read domains/wfm/docs/.context/ for WFM-specific architecture.
   
   IMPORTANT: Changes to shared/src/interfaces/ require 30+ NuGet
   package updates. See shared/docs/.context/NUGET_DEPENDENCY_MAP.md.
   Consider workarounds (fake overloads) for sprint-scoped work."

domains/payroll/docs/.context/COMPLIANCE.md:
  "## France
   - 35-hour work week, overtime after 35h
   - 13th month salary mandatory
   - Social charges: 45% employer side
   - RTT (Réduction du Temps de Travail) accrual rules
   
   ## California
   - Daily overtime after 8h (not just weekly after 40h)
   - Meal break penalty: 1 hour pay if missed
   - Split shift premium required
   
   ## Canada
   - Provincial minimum wage varies
   - Statutory holiday pay rules per province"
```

### CODEOWNERS for Domain-Routed Reviews

```
# .github/CODEOWNERS

# Cross-domain changes require platform team review
/docs/.context/                  @dayforce/platform-architects
/shared/                         @dayforce/platform-architects
/.github/workflows/              @dayforce/platform-architects

# Domain-specific routing
/domains/payroll/                @dayforce/payroll-team
/domains/payroll/src/france/     @dayforce/payroll-france
/domains/wfm/                    @dayforce/wfm-core
/domains/wfm/src/scheduling/     @dayforce/wfm-scheduling
/domains/benefits/               @dayforce/benefits-team
/domains/core-hr/                @dayforce/core-hr-team

# PR docs — reviewed by the domain team that owns the feature
/docs/prs/*payroll*              @dayforce/payroll-team
/docs/prs/*wfm*                  @dayforce/wfm-core
/docs/prs/*benefit*              @dayforce/benefits-team
```

### Domain-Scoped CI with Path Filtering

```yaml
# .github/workflows/wfm-tests.yml
name: WFM Tests
on:
  pull_request:
    paths:
      - 'domains/wfm/**'
      - 'shared/src/interfaces/**'  # Shared changes trigger domain tests too
      - 'services/wfm-service/**'

jobs:
  wfm-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run WFM unit tests
        run: dotnet test domains/wfm/tests/
      - name: Run WFM selenium suite
        run: dotnet test domains/wfm/tests/e2e/ --filter "Category=Compliance"
```

### Context Doc Ownership Matrix

| Context doc | Owner | Domain | Update trigger |
|---|---|---|---|
| `docs/.context/ARCHITECTURE-TAXONOMY.md` | Platform Architects | Cross-domain | Quarterly or after major refactor |
| `docs/.context/COMPLIANCE-REQUIREMENTS.md` | Compliance Dept liaison | Cross-domain | When new law changes are identified |
| `docs/.context/KNOWN_ISSUES.md` (root) | Platform Architects | Cross-domain | When cross-domain bugs found |
| `domains/wfm/docs/.context/ARCHITECTURE.md` | WFM Tech Lead | WFM | After WFM architectural decisions |
| `domains/wfm/docs/.context/COMPLIANCE.md` | WFM PM + Compliance | WFM | When labor law changes per jurisdiction |
| `domains/wfm/docs/.context/KNOWN_ISSUES.md` | WFM QA Lead | WFM | Sprint retrospectives |
| `domains/wfm/docs/.context/DOMAIN_MODEL.md` | WFM Dev Lead (Dhirendra) | WFM | When entities/relationships change |
| `domains/payroll/docs/.context/COMPLIANCE.md` | Payroll PM + Compliance | Payroll | When tax/pay law changes |
| `shared/docs/.context/NUGET_DEPENDENCY_MAP.md` | Platform Architects | Shared | When dependency chain changes |

### Real Dayforce Scenarios

#### Scenario 1: California Overtime Compliance Change (WFM → Payroll)

**What happens**: California changes overtime rules. Compliance dept raises a MIM (Major Incident Management) call, which generates a Jira ticket linked to the WFM Core team.

**Old world**: PM tells dev in grooming. Dev starts coding. Discovers mid-sprint that the change touches payroll calculations too. Needs NuGet interface update. 30 PRs. Sprint blown.

**New world with this workflow**:

1. `/start-pr CLA-4521 ca-overtime-rule-change`
2. **RESEARCH.md** — AI reads `domains/wfm/docs/.context/COMPLIANCE.md` (California section) + `shared/docs/.context/NUGET_DEPENDENCY_MAP.md`. Immediately surfaces: "This requires a new parameter on the background job. The interface is 5-6 levels deep in the NuGet chain. Options: (A) workaround with fake overload — ships in 1 sprint, (B) full NuGet update — 30 PRs across 2 sprints."
3. **TEST-STRATEGY.md** — ACs defined:
   - AC1: Recalculation respects new CA daily overtime threshold
   - AC2: Historical recalc limited to compliance-safe lookback period
   - AC3: No regression on existing 7,000 client tenants
4. **IMPLEMENTATION-PLAN.md** — "Option A (workaround) for this sprint. Create ADR documenting the NuGet tech debt for next sprint."
5. **Decision surfaces BEFORE code** — PM, compliance, and dev align on scope in research phase, not mid-sprint.

#### Scenario 2: Payroll France New Hire (Subdomain Onboarding)

**What happens**: A new developer joins the Payroll France subdomain. Today: 2-3 years to become productive (Dhirendra's number for WFM Core).

**Old world**: Shadow senior devs for months. Read wiki pages that are 3 years stale. Make mistakes, get corrected, slowly accumulate tribal knowledge.

**New world with this workflow**:

1. New dev opens the repo. Claude Code reads:
   - Root `CLAUDE.md` → overall architecture
   - `domains/payroll/CLAUDE.md` → payroll domain context
   - `domains/payroll/docs/.context/ARCHITECTURE.md` → calc engine, tax tables
   - `domains/payroll/docs/.context/COMPLIANCE.md` → France section (35h week, 13th month, RTT)
   - `domains/payroll/docs/.context/DOMAIN_MODEL.md` → key entities
2. New dev asks Claude: "What are the last 5 PRs that touched Payroll France?"
   - Claude reads `docs/.context/ACTIVE_PRS.md`, finds the PR folders, reads their RESEARCH.md files
   - New dev understands recent changes WITH the reasoning behind them
3. New dev gets their first ticket. `/start-pr` creates the scaffold. They iterate on RESEARCH.md with Claude reading the France-specific compliance context. Claude catches: "Note: RTT accrual rules changed in 2025 — see ADR-047."
4. **Time to productive: weeks, not years.** The context docs + PR paper trail replaces 70% of tribal knowledge.

#### Scenario 3: Cross-Domain NuGet Interface Change

**What happens**: A shared interface needs a new method. Touches payroll, WFM, and core-hr. Historically: 30 PRs, each needing its own review, each touching a NuGet package.

**New world with this workflow**:

1. **Brainstorm first**: `docs/brainstorms/2026-04-15-shared-interface-rate-override.md`
   - Documents: why the change is needed, which domains are affected, dependency graph
   - AI reads `shared/docs/.context/NUGET_DEPENDENCY_MAP.md` and generates the exact PR sequence
2. **Multi-PR initiative** broken into stages:
   - Stage 1 (PR-4530): Add method to shared interface + update shared NuGet packages
   - Stage 2 (PR-4531): WFM service consumes new method
   - Stage 3 (PR-4532): Payroll service consumes new method
   - Stage 4 (PR-4533): Monolith bridge updated
3. Each PR has its own docs folder, but RESEARCH.md links to the brainstorm
4. CI runs domain-specific tests per PR (path-filtered) + cross-domain integration tests on the final PR
5. **BREAKING_CHANGE_LOG.md** updated: "2026-04-15: Added `GetRateOverride()` to `IPayRuleProvider` — all consumers must implement by Stage 4"

#### Scenario 4: PM Musical Chairs (Knowledge Preserved)

**What happens**: PMs rotate between domains (the "musical chairs" Dhirendra described). Old PM knew the SpaceX feature existed. New PM didn't. 3 user stories scrapped after hours of grooming.

**New world**: The new PM reads `domains/wfm/docs/.context/ARCHITECTURE.md` + recent ADRs + PR paper trails. Asks Claude: "What features does WFM currently support for custom scheduling rules?" Claude reads the context docs and PR history, surfaces the existing SpaceX feature. **Hours of wasted grooming prevented.**

### Scaling FAQ

**Q: Who owns the root-level context docs vs domain-level?**
A: Platform architects own root `docs/.context/`. Each domain's tech lead owns `domains/{name}/docs/.context/`. PMs own COMPLIANCE.md jointly with the compliance department. See the ownership matrix above.

**Q: What about the compliance department? They drive 90% of WFM features.**
A: Compliance gets their own section in each domain's COMPLIANCE.md. When a law changes, the compliance liaison updates the relevant domain's COMPLIANCE.md. This becomes input to RESEARCH.md when a dev picks up the ticket. The compliance context is now WRITTEN DOWN, not just in someone's head.

**Q: How do we handle the NuGet dependency chain problem?**
A: `shared/docs/.context/NUGET_DEPENDENCY_MAP.md` documents the full chain. Claude reads this during research and warns: "This change requires N package updates." The RESEARCH.md options analysis always includes "workaround to ship in 1 sprint" vs "full NuGet update." ADRs track the tech debt.

**Q: 200 engineers making PR docs — won't this explode the repo?**
A: PR docs are small (5 files, ~2KB each). 500 PRs/year = ~5MB of docs. That's nothing. And it's searchable, AI-readable context that replaces Slack threads and wiki pages that nobody can find. Archive old PR docs quarterly if size becomes a concern.

**Q: How does this work with 2-week sprints and Kanban+Scrum hybrid?**
A: Scrum stories get the full PR lifecycle (RESEARCH → TEST-STRATEGY → IMPL-PLAN → code → review). Kanban bugs get a lightweight version: RESEARCH.md (root cause analysis) + TEST-STRATEGY.md (regression test that proves the fix). Skip IMPLEMENTATION-PLAN for trivial bugs — the fix IS the plan.

**Q: What about Selenium E2E tests? Those are separate from unit tests.**
A: TEST-STRATEGY.md covers ALL test types. The test matrix has a "File" column — put Selenium tests there alongside unit tests. The AC coverage table doesn't care about test type, it cares about coverage: "Is AC3 tested by at least one test, regardless of whether it's unit, integration, or E2E?"

**Q: How do we get 7 teams to adopt this simultaneously?**
A: Don't. Pick one team (ideally WFM Core — they already have high automation coverage and domain experts). Run the workflow for 2 sprints. Measure: sprint predictability, regression rate, onboarding time for new devs. Then show the results to other teams. Adoption follows demonstrated value, not mandates.

---

## Appendix: Minimal Command Templates

These are simplified versions of the Clarity-API commands. Copy these to `.claude/commands/` and customize for your project.

### `.claude/commands/start-pr.md`
```markdown
Create a new PR with documentation scaffold.

1. Get the next PR number: gh pr list --state all --limit 1 --json number
2. Create branch: git checkout -b feature/{slug}
3. Create docs folder: docs/prs/YYYY-MM-DD-PR-{num}-{slug}/
4. Create RESEARCH.md, TEST-STRATEGY.md, PLAN.md, IMPLEMENTATION.md from templates
5. Update docs/.context/ACTIVE_PRS.md with new entry
6. Commit the scaffold
```

### `.claude/commands/execute-pr.md`
```markdown
Implement the plan with progress tracking.

1. Get PR number from argument or current branch
2. Read PLAN.md for implementation steps
3. Create task list from the plan
4. Implement phase by phase with incremental commits
5. Update IMPLEMENTATION.md with changes and deviations
6. Pause on blockers for human input
```

### `.claude/commands/review-pr.md`
```markdown
Review, gate-check, merge, and close the PR.

1. Get PR number from argument or current branch
2. Spawn sub-agent with clean context for AI code review
3. Generate REVIEW.md with: verdict, per-AC coverage, risk assessment
4. Run docs-gate check (python scripts/pr_docs_check.py)
5. If Approve + gate passes:
   - Merge PR via gh pr merge --squash
   - Archive docs folder to _archive/
   - Update ACTIVE_PRS.md (Open -> Recently Merged)
   - Check for ADR-worthy decisions
6. If Request Changes: report issues, do NOT merge

At Run level (Level 3-4), also runs before step 4:
- /stakeholder-alignment -> STAKEHOLDER-ALIGNMENT.md
- /compound extract -> compound_extract.json
```

---

*Last updated: 2026-04-10. Ships with [ai-native-dev-scaffold-walk](https://github.com/Epistemic-Me/ai-native-dev-scaffold-walk).*
