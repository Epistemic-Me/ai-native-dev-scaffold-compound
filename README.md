# AI-Native Development Scaffold + Compound Loop

A project scaffold for AI-native software development with Claude Code, extended with the Clarity API compound loop for builder self-reflection and stakeholder alignment.

This is a superset of [ai-native-dev-scaffold](https://github.com/Epistemic-Me/ai-native-dev-scaffold) — all scaffold features work standalone. The compound loop activates when Clarity API credentials are configured.

## What's Included

```
ai-native-dev-scaffold-compound/
├── .claude/
│   └── commands/
│       ├── project/           # PR lifecycle and documentation commands (11 commands)
│       │   ├── start-pr.md       # Create branch + paper trail
│       │   ├── implement-pr.md   # Execute from PLAN.md with tracking
│       │   ├── verify-pr.md      # Run lint/test/build checks
│       │   ├── close-pr.md       # Merge PR + complete docs
│       │   ├── execute-pr.md     # Full lifecycle orchestrator
│       │   ├── pr-status.md      # PR progress view
│       │   ├── decision.md       # Create ADR
│       │   ├── context-update.md # Refresh living context
│       │   ├── context-status.md # Documentation health report
│       │   ├── compound.md      # Compound loop (extract/align/sync/report)
│       │   └── stakeholder-alignment.md # Stakeholder alignment scoring
│       ├── hl/                # Advanced workflow commands (22 commands)
│       │   ├── create_plan.md         # Interactive plan creation (opus)
│       │   ├── create_plan_nt.md      # Lightweight plan (no docs/)
│       │   ├── implement_plan.md      # Execute plans phase by phase
│       │   ├── iterate_plan.md        # Update existing plans (opus)
│       │   ├── iterate_plan_nt.md     # Lightweight iteration
│       │   ├── validate_plan.md       # Verify implementation matches plan
│       │   ├── execute_pr.md          # Implement from PR paper trail
│       │   ├── oneshot.md             # Research + plan in one go
│       │   ├── oneshot_plan.md        # Research + plan + implement
│       │   ├── commit.md              # Git commits with branch safety
│       │   ├── ci_commit.md           # Non-interactive commits
│       │   ├── describe_pr.md         # PR descriptions
│       │   ├── ci_describe_pr.md      # Non-interactive PR desc
│       │   ├── describe_pr_nt.md      # Lightweight PR desc
│       │   ├── debug.md               # Debug issues
│       │   ├── research_codebase.md   # Research + doc generation (opus)
│       │   ├── research_codebase_generic.md  # Deep research with sub-agents
│       │   ├── research_codebase_nt.md       # Lightweight inline research
│       │   ├── local_review.md        # Review PRs locally
│       │   ├── founder_mode.md        # Rapid development mode
│       │   ├── create_handoff.md      # Session handoffs
│       │   └── resume_handoff.md      # Resume handoffs
│       └── shared/            # Shared utilities
│           └── branch-safety.md  # PR workflow enforcement
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
│   ├── research/              # Codebase research documents
│   └── prs/                   # PR paper trails
│       └── _TEMPLATE/         # Template PR folder
│           ├── RESEARCH.md    # Problem exploration & options
│           ├── PLAN.md        # Implementation strategy
│           ├── IMPLEMENTATION.md # What was actually built
│           └── REVIEW.md      # Structured review + compound data
├── scripts/
│   └── compound_config.py     # Compound loop config (observation contexts)
├── CLAUDE.md                  # Project instructions for Claude
├── GETTING-STARTED.md         # Compound loop setup guide
├── .env.example               # Clarity API credentials template
└── .stakeholders.json.example # Stakeholder override template
```

## Philosophy

### Paper Trails Over Comments

Instead of inline comments that rot, we maintain living documentation:

- **RESEARCH.md** - Why are we doing this? What options did we consider?
- **PLAN.md** - How will we implement it? What's in/out of scope?
- **IMPLEMENTATION.md** - What did we actually build? What did we learn?
- **REVIEW.md** - Structured review notes + compound loop data

### Decisions Are First-Class

Every significant technical decision gets an ADR that captures context at decision time, documents alternatives considered, explains trade-offs, and is linkable from code and PRs.

### AI as Collaborator

The `.claude/commands/` folder contains slash commands that automate documentation scaffolding, enforce consistent structure, and reduce friction in the development process.

## Getting Started

### 1. Clone this scaffold

```bash
git clone https://github.com/Epistemic-Me/ai-native-dev-scaffold-compound.git my-project
cd my-project
rm -rf .git
git init
```

### 2. Install Claude commands

**Option A: Global install** (available in all projects):

```bash
cp -r .claude/commands/project ~/.claude/commands/
cp -r .claude/commands/hl ~/.claude/commands/
cp -r .claude/commands/shared ~/.claude/commands/
```

**Option B: Project-local** (leave them in `.claude/commands/`).

### 3. Try it out

```bash
# Start your first PR
/project:start-pr 001 initial-setup

# Or jump straight into the full lifecycle
/project:execute-pr 001
```

## Walkthrough: Feature to Production

Here's a concrete example of taking a feature from idea to merged code using the scaffold. We'll add user authentication to a project.

### Step 1: Start the PR

```
/project:start-pr 042 user-authentication
```

This creates:
- Branch: `feature/pr-042-user-authentication`
- Paper trail: `docs/prs/2025-02-07-PR-042-user-authentication/`
  - `RESEARCH.md` (empty template)
  - `PLAN.md` (empty template)
  - `IMPLEMENTATION.md` (empty template)
  - `REVIEW.md` (empty template)
- Updates `ACTIVE_PRS.md`
- Commits the paper trail to the feature branch

### Step 2: Research the problem

Fill in RESEARCH.md yourself, or use Claude to help research the codebase:

```
/hl:research_codebase_nt
> How does our app currently handle sessions? What auth patterns exist?
```

Then fill in RESEARCH.md with the problem statement, options you considered (JWT vs sessions vs OAuth), and your recommendation. This is the "why" behind the work.

If you're making a significant architectural choice, record it:

```
/project:decision jwt-authentication
```

### Step 3: Plan the implementation

Write PLAN.md with the chosen approach, scope, technical design, and implementation order. Or use Claude to generate a plan:

```
/hl:create_plan
> Implement JWT authentication based on docs/prs/2025-02-07-PR-042-user-authentication/RESEARCH.md
```

This researches the codebase, presents design options, and writes a phased plan with success criteria to PLAN.md.

Need to revise the plan after feedback?

```
/hl:iterate_plan docs/prs/2025-02-07-PR-042-user-authentication/PLAN.md
> Add rate limiting to the login endpoint and split into smaller phases
```

### Step 4: Implement

```
/project:implement-pr 042
```

This reads PLAN.md, creates a TodoWrite task list from the implementation order, and works through each task. As it goes, it:
- Tracks progress (`3/7 tasks complete`)
- Makes incremental commits on the feature branch
- Updates IMPLEMENTATION.md with key changes and any deviations from the plan
- Pauses on blockers to ask you how to proceed

### Step 5: Verify

```
/project:verify-pr 042
```

Auto-detects your project's verification tools and runs them:

```
PR-042 Verification Results

| Check     | Status | Notes     |
|-----------|--------|-----------|
| Lint      | PASS   |           |
| TypeCheck | PASS   |           |
| Tests     | PASS   | 87% cov   |
| Build     | PASS   |           |

Overall: PASS
```

If anything fails, fix it and re-run. Verification must pass before moving on.

### Step 6: Push and create the GitHub PR

```
/hl:commit
```

Stages and commits with a conventional commit message. Then push:

```bash
git push -u origin feature/pr-042-user-authentication
```

Create the GitHub PR:

```
/hl:describe_pr 042
```

This generates a PR description from your paper trail (RESEARCH.md + PLAN.md + IMPLEMENTATION.md), analyzes the diff, and creates/updates the PR on GitHub.

### Step 7: Review

Have a teammate review, or review locally:

```
/hl:local_review 042
```

This analyzes the diff, CI status, and presents a structured review with findings. Can post the review to GitHub.

### Step 8: Merge and close

After approval:

```
/project:close-pr 042
```

This:
- Merges the PR via `gh pr merge --squash --delete-branch`
- Checks out main and pulls
- Completes IMPLEMENTATION.md (summary, learnings)
- Moves the PR from "Open" to "Recently Merged" in ACTIVE_PRS.md
- Checks for architectural decisions and prompts ADR creation if needed
- Commits documentation updates to main

### Step 9: Update project context

```
/project:context-update
```

Refreshes all `.context/` files to reflect the new state of the project.

### The Automated Path

Don't want to run each step manually? The master orchestrator does everything:

```
/project:execute-pr 042
```

This chains together all phases automatically:

```
start-pr → implement-pr → verify-pr → push → create GH PR → approval gate → close-pr → [compound] → context-update
```

It pauses at the approval gate to let you review before merging. If interrupted at any point, re-running the same command detects existing state and resumes where it left off.

### For Small Tasks

If the full paper trail feels like overkill:

```
/hl:oneshot_plan
> Add a logout button to the nav bar
```

This does research, planning, and implementation in one session. Still creates a feature branch and PR, just without the full `docs/prs/` paper trail.

Or for rapid prototyping:

```
/hl:founder_mode
```

Bias toward action over planning. Makes assumptions instead of asking questions. Still enforces branch safety and PRs.

## Commands Reference

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
| `/hl:create_plan_nt` | Lightweight plan, no docs/ directory required (opus) |
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

## Choosing the Right Path

| Situation | Use this |
|-----------|----------|
| Complex feature (days of work) | `/project:execute-pr` or manual step-by-step |
| Medium task (hours) | `/hl:oneshot_plan` |
| Quick fix or small feature | `/hl:founder_mode` |
| Need a detailed plan first | `/hl:create_plan` then `/project:implement-pr` |
| Continuing someone else's work | `/hl:resume_handoff` |
| Debugging an issue | `/hl:debug` |
| Understanding the codebase | `/hl:research_codebase` |
| Reviewing a colleague's PR | `/hl:local_review` |

## PR Paper Trail Format

Each PR gets a folder (`docs/prs/{date}-PR-{num}-{slug}/`) with four documents:

**RESEARCH.md** - The "why": Problem statement, context gathered, options considered with pros/cons, recommendation, open questions.

**PLAN.md** - The "how": Chosen approach, scope (in/out), technical design, implementation order, testing strategy, definition of done.

**IMPLEMENTATION.md** - The "what": Summary of what was built, key changes, deviations from plan, learnings, follow-up items.

**REVIEW.md** - Structured code review notes plus compound loop data (observation context changes, beliefs validated/invalidated).

## Compound Loop

The compound loop is an opt-in self-reflection system powered by the [Clarity API](https://epistemicme.ai). It extracts structured data from your PR documentation and builds a self-model that tracks your project's trajectory.

### What it does

After each PR merge, the compound loop:
1. **Extracts** episodes and beliefs from REVIEW.md
2. **Scores** stakeholder alignment (how well the PR serves each stakeholder's goals)
3. **Syncs** to the Clarity API (building your project's self-model over time)
4. **Reports** current state vs target state across 9 observation contexts

### Setup

See [GETTING-STARTED.md](./GETTING-STARTED.md) for full setup instructions. Quick version:

```bash
# 1. Install Python deps
pip install requests pyyaml

# 2. Clone Clarity API
git clone https://github.com/Epistemic-Me/Clarity-API.git
export CLARITY_API_PATH=/path/to/Clarity-API

# 3. Configure credentials
cp .env.example .env
# Edit .env with your API key

# 4. Initialize your self-model
python3 "${CLARITY_API_PATH}/scripts/compound.py" --config-dir ./scripts init --name "Your Name" --email "you@example.com"
```

### Without credentials

All scaffold commands work normally without Clarity API credentials. The compound loop is simply skipped.

## ADR Format

Architecture Decision Records live in `docs/decisions/` and follow this structure:

```markdown
# ADR-XXX: Title

**Date**: YYYY-MM-DD
**Status**: Proposed | Accepted | Deprecated | Superseded
**PR**: #number (if applicable)

## Context
What issue motivates this decision?

## Decision
What are we doing?

## Consequences
### Positive
### Negative

## Alternatives Considered
What else did we evaluate? Why not chosen?

## Related
Links to PRs, other ADRs, external resources
```

## Best Practices

- **Always work on feature branches** - Never commit to master/main
- **Fill in RESEARCH.md before coding** - Understand the problem first
- **Update PLAN.md when scope changes** - Keep it current, not aspirational
- **Complete IMPLEMENTATION.md with learnings** - Future you will thank you
- **Record significant decisions as ADRs** - Especially ones future developers will question
- **Run `/project:context-update` regularly** - Keep living docs current
- **Use `/project:context-status` to check health** - Catch staleness early

## Contributing

This is an open scaffold - please contribute improvements:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

Many of the `/hl:*` commands are adapted from [HumanLayer](https://github.com/humanlayer/humanlayer).

## License

MIT License - Use freely in your projects.

---

*Built for AI-native development with Claude Code + [Clarity API](https://epistemicme.ai)*
