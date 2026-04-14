# Claude Code Project Context

This project is the **Run** stage of the Crawl → Walk → Run AI-native maturity model. It adds compounding intelligence — stakeholder alignment, self-model episodes, transcript processing — on top of a Walk-stage PR lifecycle.

## You Are Here: Crawl / Walk / Run

- **Crawl** — Context Foundation: `CLAUDE.md`, `docs/.context/` core set, `docs/.context/MCP_SERVERS.md`, credential policy. No PR workflow. See `ai-native-dev-scaffold-crawl` *(coming soon)*.
- **Walk** — Paper Trail + Gate: Crawl + 5-stage PR lifecycle + docs-gate CI + ADR index. See `ai-native-dev-scaffold-walk`.
- **Run** — Compounding Intelligence *(← you are here)*: Walk + `/project:stakeholder-alignment` + `/project:compound` + `/project:process-transcript` + self-model API integration. This is where the loop closes: decisions feed forward, customer signal reshapes context docs, episodic memory persists across sessions.

**Don't skip Crawl or Walk.** Running without the context foundation means the compounding loop compounds bad assumptions. 95% of enterprise AI pilots fail here (MIT NANDA, 2025).

## The PR Lifecycle — 5 stages + 3 compounding hooks

```
Walk baseline:   /start-pr → develop → /review-pr → /check-pr → /close-pr
Run additions:                          ↑ /stakeholder-alignment
                                        ↑ /compound
                                        ↑ /process-transcript (triggered by research, not PRs)
```

The Walk lifecycle runs unchanged. The Run additions layer on as part of `/review-pr`:
1. **`/stakeholder-alignment`** — Score the PR against each stakeholder perspective; writes STAKEHOLDER-ALIGNMENT.md
2. **`/compound extract`** — Extract the PR episode payload to `compound_extract.json` for the self-model API
3. **`/process-transcript`** — Run out-of-band after customer interviews to update `docs/.context/JTBD.md` and `docs/.context/ICP.md` with evidence

The dev doesn't memorize extra steps — `/project:review-pr` orchestrates them.

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

## Credential Policy (Crawl-stage foundation)

This repo treats tool access and secrets as **context that must be declared**, not tribal knowledge. Agents and new engineers read this policy before touching anything. At the Run stage this matters even more — the self-model API and transcript ingestion handle sensitive customer data.

1. **No secrets in the repo.** `.env` files are gitignored. `.env.example` documents what variables exist without values. Secrets in commits are a blocking issue — rotate immediately and force-push a clean history.
2. **Vault is the source of truth.** Every credential has a canonical path like `vault://engineering/{service}`. `CLAUDE.md`, `docs/.context/MCP_SERVERS.md`, and ticket Context Declarations reference vault paths, never the secret values.
3. **Service accounts, not personal credentials.** AI agents run as a dedicated identity separate from human developers. The Clarity builder, Linear bot, and any third-party APIs use service accounts whose blast radius is bounded.
4. **Least-privilege per task.** Credentials loaded for a ticket grant access only to what that ticket needs. Customer transcripts, for example, are scoped to `/project:process-transcript` runs — not ambient access.
5. **Short-lived where possible.** Prefer dynamic, expiring credentials over long-lived static keys. For customer PII (transcripts, stakeholder data), this is non-negotiable at Run stage.

See `docs/.context/MCP_SERVERS.md` for per-server credential paths and the Context Declaration template.
