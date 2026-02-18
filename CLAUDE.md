# Claude Code Project Context

This file provides guidance to Claude Code instances when working with projects using this scaffold.

## MANDATORY: PR Workflow Rules

**NEVER commit directly to master/main.** All code changes MUST follow PR workflow.

### Before ANY Code Changes
1. Check current branch: `git branch --show-current`
2. If on master/main → **STOP** and create feature branch
3. Check for PR: `gh pr view`
4. If no PR → suggest creating draft PR

### Blocked Operations on master/main
- `git commit` (any form)
- `git push origin master/main`
- File edits via Edit/Write tools without branch check

See `.claude/commands/shared/branch-safety.md` for enforcement details.

---

## Workflow: Feature to Production

### The Automated Path

For any feature, the master orchestrator handles everything:

```
/project:execute-pr {num}
```

This runs the full lifecycle automatically:

```
start-pr → implement-pr → verify-pr → push → create GH PR → approval gate → close-pr → [compound] → context-update
```

It pauses at the approval gate for human review before merging. If interrupted, re-running detects existing state and resumes.

### The Manual Path (Step by Step)

**1. Start the PR** — creates feature branch and paper trail:
```
/project:start-pr {num} {slug}
```
Creates `feature/pr-{num}-{slug}` branch and `docs/prs/{date}-PR-{num}-{slug}/` with RESEARCH.md, PLAN.md, IMPLEMENTATION.md, REVIEW.md.

**2. Research** — understand the problem before coding:
- Fill in RESEARCH.md with problem statement, options considered, recommendation
- Use `/hl:research_codebase_nt` to explore the codebase
- Record architectural decisions with `/project:decision {slug}`

**3. Plan** — define the implementation approach:
- Fill in PLAN.md with scope, technical design, implementation order
- Or generate one: `/hl:create_plan`
- Revise after feedback: `/hl:iterate_plan {path-to-plan} {feedback}`

**4. Implement** — execute the plan with progress tracking:
```
/project:implement-pr {num}
```
Reads PLAN.md, creates TodoWrite tasks, implements phase by phase, updates IMPLEMENTATION.md.

**5. Verify** — run all available checks:
```
/project:verify-pr {num}
```
Auto-detects lint, typecheck, test, build and reports pass/fail. Must pass before merge.

**6. Commit and push**:
```
/hl:commit
git push -u origin feature/pr-{num}-{slug}
```

**7. Create/update GitHub PR**:
```
/hl:describe_pr {num}
```
Generates PR description from paper trail, analyzes diff, creates/updates PR on GitHub.

**8. Review** — get human approval:
- Have teammate review, or use `/hl:local_review {num}` for local analysis
- Never merge without human approval

**9. Merge and close**:
```
/project:close-pr {num}
```
Merges via `gh pr merge --squash`, completes IMPLEMENTATION.md, updates ACTIVE_PRS.md, checks for ADRs, commits docs.

**10. Update context**:
```
/project:context-update
```
Refreshes all `.context/` files. Check health anytime with `/project:context-status`.

### For Smaller Tasks

| Situation | Use this |
|-----------|----------|
| Medium task (hours) | `/hl:oneshot_plan` — research, plan, implement in one session |
| Quick fix | `/hl:founder_mode` — bias toward action, still uses PRs |
| Need plan only | `/hl:create_plan` then `/project:implement-pr` |
| Continuing work | `/hl:resume_handoff` |
| Debugging | `/hl:debug` |

---

## Project Structure

```
your-project/
├── .claude/
│   └── commands/
│       ├── project/           # PR lifecycle and documentation (11 commands)
│       ├── hl/                # Advanced workflows (22 commands)
│       └── shared/            # Branch safety enforcement
├── docs/
│   ├── .context/              # Living project context
│   │   ├── ACTIVE_PRS.md      # Currently open PRs
│   │   ├── RECENT_DECISIONS.md # Recent architectural decisions
│   │   └── COMPOUND_REPORT.md # Compound loop report (if enabled)
│   ├── decisions/             # Architecture Decision Records (ADRs)
│   │   ├── _INDEX.md          # Decision catalog
│   │   └── _TEMPLATE.md       # ADR template
│   ├── handoffs/              # Session handoff documents
│   ├── plans/                 # Implementation plans
│   ├── prs/                   # PR paper trails
│   │   └── _TEMPLATE/         # RESEARCH.md, PLAN.md, IMPLEMENTATION.md, REVIEW.md
│   └── research/              # Codebase research documents
├── scripts/
│   └── compound_config.py     # Compound loop config (observation contexts, etc.)
├── CLAUDE.md                  # This file
├── GETTING-STARTED.md         # Compound loop setup guide
└── ... your code ...
```

## Available Commands

### PR Lifecycle (`/project:*`)

| Command | Purpose |
|---------|---------|
| `/project:start-pr {num} {slug}` | Create feature branch + paper trail folder |
| `/project:implement-pr {num}` | Execute implementation from PLAN.md with tracking |
| `/project:verify-pr {num}` | Run lint, typecheck, test, build checks |
| `/project:close-pr {num}` | Merge GitHub PR, complete docs, check for ADRs |
| `/project:execute-pr {num}` | Full lifecycle orchestrator (all of the above) |
| `/project:pr-status [num]` | PR progress, phase, and next action |

### Documentation (`/project:*`)

| Command | Purpose |
|---------|---------|
| `/project:decision {slug}` | Create Architecture Decision Record |
| `/project:context-update` | Refresh ACTIVE_PRS.md and RECENT_DECISIONS.md |
| `/project:context-status` | Documentation health report with staleness checks |

### Compound Loop (`/project:*`) — requires Clarity API credentials

| Command | Purpose |
|---------|---------|
| `/project:compound [num]` | Full compound loop: extract, align, sync, report |
| `/project:stakeholder-alignment [num]` | Run stakeholder alignment scoring for a PR |

### Planning (`/hl:*`)

| Command | Purpose |
|---------|---------|
| `/hl:create_plan` | Interactive plan creation with codebase research (opus) |
| `/hl:create_plan_nt` | Lightweight plan, no docs/ required (opus) |
| `/hl:implement_plan` | Execute plan phase by phase with verification |
| `/hl:iterate_plan` | Update existing plan based on feedback (opus) |
| `/hl:iterate_plan_nt` | Lightweight plan iteration (opus) |
| `/hl:validate_plan` | Verify implementation matches plan |
| `/hl:execute_pr` | Implement from PR paper trail (RESEARCH + PLAN) |
| `/hl:oneshot` | Research + plan in one flow |
| `/hl:oneshot_plan` | Research + plan + implement in one session |

### Git & PR (`/hl:*`)

| Command | Purpose |
|---------|---------|
| `/hl:commit` | Commits with branch safety enforcement |
| `/hl:ci_commit` | Non-interactive commit for CI workflows |
| `/hl:describe_pr` | Generate PR description from paper trail |
| `/hl:ci_describe_pr` | Non-interactive PR description for CI |
| `/hl:describe_pr_nt` | Lightweight PR description |

### Research & Debug (`/hl:*`)

| Command | Purpose |
|---------|---------|
| `/hl:research_codebase` | Codebase research + doc generation (opus) |
| `/hl:research_codebase_generic` | Deep research with parallel sub-agents (opus) |
| `/hl:research_codebase_nt` | Lightweight inline research (opus) |
| `/hl:debug` | Investigate logs and code (read-only) |

### Review, Handoffs, and Modes (`/hl:*`)

| Command | Purpose |
|---------|---------|
| `/hl:local_review` | Review a colleague's PR locally |
| `/hl:create_handoff` | Create session handoff document |
| `/hl:resume_handoff` | Resume from handoff document |
| `/hl:founder_mode` | Rapid development with bias toward action |

## Documentation Patterns

### PR Paper Trail

Each PR gets `docs/prs/{date}-PR-{num}-{slug}/` with:
- **RESEARCH.md** — The "why": problem statement, options, recommendation
- **PLAN.md** — The "how": scope, design, implementation order, definition of done
- **IMPLEMENTATION.md** — The "what": changes made, deviations, learnings
- **REVIEW.md** — Structured review notes + compound loop data (observation context changes, beliefs)

### Compound Loop (opt-in)

The compound loop adds self-reflection to the PR lifecycle. It extracts episodes and beliefs from REVIEW.md, scores stakeholder alignment, syncs to the Clarity API, and generates a compound report.

**Setup**: See [GETTING-STARTED.md](./GETTING-STARTED.md) for Clarity API credentials and configuration.

**How it works**:
1. Fill in REVIEW.md's "Compound Loop Data" section during review
2. Run `/project:compound` (or let `close-pr`/`execute-pr` offer it)
3. Check `docs/.context/COMPOUND_REPORT.md` for current project state

**Without credentials**: All PR lifecycle commands work normally. The compound loop is skipped silently.

### Architecture Decision Records

Record significant decisions with `/project:decision {slug}`. Use ADRs when:
- Choosing between competing technologies
- Establishing patterns for the codebase
- Making trade-offs that affect the system
- Decisions that future developers will question

### Best Practices

- **Fill RESEARCH.md before coding** — understand the problem first
- **Update PLAN.md when scope changes** — keep it current, not aspirational
- **Complete IMPLEMENTATION.md with learnings** — future you will thank you
- **Run `/project:context-update` regularly** — keep living docs current
- **Use `/project:context-status` to check health** — catch staleness early
- **One decision per ADR** — supersede rather than delete old decisions
