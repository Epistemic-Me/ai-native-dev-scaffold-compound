# Claude Code Project Context

This project uses the AI-Native Development Lifecycle (Run level) with stakeholder alignment and compound self-model loop.

## The 3-Command Loop

```
/project:start-pr  →  /project:execute-pr  →  /project:review-pr
```

Same 3 commands as Walk level. The difference: **review-pr automatically runs stakeholder alignment and compound extraction** before merging. The dev doesn't run extra commands.

## MANDATORY: PR Workflow Rules

**NEVER commit directly to master/main.** All code changes MUST follow PR workflow.

See `.claude/commands/shared/branch-safety.md` for enforcement details.

## Fill Order

Before running `/project:execute-pr`, fill these docs IN ORDER:

1. **RESEARCH.md** — Understand the problem. Iterate with AI.
2. **TEST-STRATEGY.md** — Define exit criteria BEFORE code.
3. **IMPLEMENTATION-PLAN.md** — Step-by-step plan mapped to ACs.

## What review-pr Does at Run Level

```
/project:review-pr 042
  1. AI code review → REVIEW.md
  2. Stakeholder alignment (auto) → STAKEHOLDER-ALIGNMENT.md
  3. Compound extraction (auto) → compound_extract.json
  4. Enhanced docs-gate check
  5. If approved → merge → compound sync → archive → close
```

Steps 2-3 are automatic. Requires `CLARITY_API_KEY` in `.env`.

## Available Commands

### Core Loop (3 commands)
| Command | Purpose |
|---------|---------|
| `/project:start-pr {num} {slug}` | Create branch + docs scaffold |
| `/project:execute-pr {num}` | Implement from plan with tracking |
| `/project:review-pr {num}` | Review + alignment + compound + merge + close |

### Skills (invoked by review-pr automatically)
| Skill | Purpose |
|-------|---------|
| `/project:stakeholder-alignment` | Score PR against digital twins |
| `/project:compound` | Extract episode + sync to self-model |

### Utilities
| Command | Purpose |
|---------|---------|
| `/project:decision {slug}` | Create ADR |
| `/project:context-update` | Refresh .context/ docs |
| `/project:context-status` | Documentation health report |

### Power-user commands (in .claude/commands/hl/)
Teams at Run level also have access to: create-plan, iterate-plan, describe-pr, founder-mode, create-handoff, resume-handoff, research-codebase, debug, and more.

## Environment Setup

```bash
# Required for stakeholder alignment + compound
cp .env.example .env
# Fill in: CLARITY_API_KEY, CLARITY_USER_ID, CLARITY_API_URL

# Initialize self-model
python scripts/compound.py init
```

## CI Docs Gate (Enhanced)

Blocking: RESEARCH.md, TEST-STRATEGY.md, IMPLEMENTATION-PLAN.md, REVIEW.md (Approve verdict), STAKEHOLDER-ALIGNMENT.md (aggregate score).
Advisory: compound_extract.json, stakeholder scores below 0.3.
