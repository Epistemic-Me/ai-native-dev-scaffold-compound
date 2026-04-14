# AI-Native Development Scaffold — Run Stage

> The compounding loop: decisions feed forward, customer signal reshapes context, episodic memory persists across sessions.

```
Walk:  /start-pr  →  develop  →  /review-pr  →  /check-pr  →  /close-pr
Run:                              ↳ /stakeholder-alignment + /compound (automatic)
                                  ↳ /process-transcript (out-of-band after research)
```

This is the **Run** stage of the Crawl → Walk → Run AI-native maturity staircase. It extends the Walk scaffold with stakeholder alignment scoring, compound self-model integration via the Clarity API, and transcript processing that feeds customer signal back into `docs/.context/`.

## You Are Here: Crawl / Walk / Run

AI-native development is a three-stage maturity staircase. The compounding value at Run is only unlockable if Crawl and Walk are solid.

| Stage | What it is | Scaffold repo |
|---|---|---|
| **Crawl** | Context Foundation: `CLAUDE.md`, `docs/.context/` core set, `MCP_SERVERS.md`, credential policy. No PR workflow yet. | `ai-native-dev-scaffold-crawl` *(coming soon)* |
| **Walk** | Paper Trail + Gate: Crawl + 5-stage PR lifecycle + docs-gate CI + ADR index. | [`ai-native-dev-scaffold`](https://github.com/Epistemic-Me/ai-native-dev-scaffold) |
| **Run** *(← you are here)* | Compounding Intelligence: Walk + `/stakeholder-alignment` + `/compound` + `/process-transcript` + self-model API. | `ai-native-dev-scaffold-compound` (this repo) |

**Don't start here.** Clone the Walk scaffold first, run it for 2 sprints until the PR lifecycle and docs-gate feel native, then graduate to this repo when you're ready to close the compounding loop. Running without a real context foundation means the loop compounds bad assumptions.

---

## Quick Start

```bash
# 1. Clone and reinitialize
git clone https://github.com/Epistemic-Me/ai-native-dev-scaffold-compound.git my-project
cd my-project
rm -rf .git && git init && git add -A && git commit -m "init: scaffold"

# 2. Set up Clarity API (optional — graceful skip if missing)
cp .env.example .env
# Fill in: CLARITY_API_KEY, CLARITY_USER_ID, CLARITY_API_URL

# 3. Start your first PR
/project:start-pr 001 my-first-feature
```

---

## Walk vs Run: What's Different

| | Walk (Level 1-2) | Run (Level 3-4) |
|---|---|---|
| **Commands** | Same 3 | Same 3 |
| **review-pr** | AI review → gate → merge | AI review → **stakeholder alignment** → **compound** → gate → merge |
| **Artifacts per PR** | 5 | 7 (+STAKEHOLDER-ALIGNMENT.md, +compound_extract.json) |
| **CI gate** | Docs exist | Docs exist + review verdict + stakeholder score |
| **API required** | No | Yes (Clarity API) — graceful skip if missing |
| **Learning** | Paper trail | Paper trail + **compounding organizational knowledge** |

The dev experience is identical. The system does more behind the scenes.

---

## The 3 Commands

### `/project:start-pr {num} {slug}`
Same as Walk. Creates branch + docs folder with templates.

### `/project:execute-pr {num}`
Same as Walk. Reads IMPLEMENTATION-PLAN.md, implements step by step.

**Before running**, fill docs in order:
1. **RESEARCH.md** — Understand the problem
2. **TEST-STRATEGY.md** — Define acceptance criteria
3. **IMPLEMENTATION-PLAN.md** — Plan mapped to ACs

### `/project:review-pr {num}` (Enhanced)

```
1. AI code review → REVIEW.md (same as Walk)
2. Stakeholder alignment (auto) → STAKEHOLDER-ALIGNMENT.md
3. Compound extraction (auto) → compound_extract.json
4. Enhanced docs-gate check
5. If approved → merge → compound sync → archive → close
```

Steps 2-3 happen automatically. If `CLARITY_API_KEY` is not set, they're skipped gracefully and you get Walk-level behavior.

---

## What Run Adds

### Stakeholder Alignment
Every PR is scored against digital twin stakeholders via the Clarity API. Each twin "observes" the PR from their role's perspective and scores alignment to their goals.

### Compound Self-Model
Every merged PR becomes an episode in your team's self-model — organizational learning that compounds over time. The system tracks what was decided, what changed, and what was learned.

### Additional Commands

| Command | Purpose |
|---------|---------|
| `/project:stakeholder-alignment` | Run alignment scoring manually |
| `/project:compound` | Run extraction/sync manually |
| `/project:context-status` | Documentation health report |

### Power-User Commands (in `.claude/commands/hl/`)
20+ additional commands: `create-plan`, `iterate-plan`, `describe-pr`, `founder-mode`, `research-codebase`, `debug`, `create-handoff`, `resume-handoff`, and more.

---

## Upgrading from Walk

If you've been using the Walk scaffold:

1. Copy `review-pr.md` from this repo → `.claude/commands/project/`
2. Copy `stakeholder-alignment.md` and `compound.md` → `.claude/commands/project/`
3. Copy `scripts/compound_config.py`
4. Set up `.env` with Clarity API credentials
5. Add the extra context docs (JTBD.md, ICP.md, etc.) to `docs/.context/`

---

## Example

See `docs/prs/_archive/2026-01-15-PR-001-add-user-registration/` for a complete filled example.

---

## Environment

```bash
# .env (copy from .env.example)
CLARITY_API_KEY=your-key
CLARITY_USER_ID=your-uuid
CLARITY_API_URL=https://your-api.onrender.com
```

See `GETTING-STARTED.md` for full API setup guide.

---

MIT License. Built by [Epistemic Me](https://github.com/Epistemic-Me).
