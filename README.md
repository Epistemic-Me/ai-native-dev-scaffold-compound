# AI-Native Development Scaffold + Compound Loop

The **Run** level scaffold. Same 3-command loop as [Walk](https://github.com/Epistemic-Me/ai-native-dev-scaffold), but `review-pr` automatically runs stakeholder alignment and compound extraction.

## The 3-Command Loop (Same as Walk)

```
/start-pr  →  /execute-pr  →  /review-pr
```

### What's Different at Run Level

| Step | Walk (Level 1-2) | Run (Level 3-4) |
|------|------------------|-----------------|
| `/start-pr` | Branch + docs scaffold | Same |
| `/execute-pr` | Implement from plan | Same |
| `/review-pr` | Review + gate + merge | **+ stakeholder alignment + compound + enhanced gate** |

The dev runs the same 3 commands. The system does more behind the scenes.

## How review-pr Works at Run Level

```
/project:review-pr 042
  1. AI code review → REVIEW.md
  2. Stakeholder alignment (auto) → STAKEHOLDER-ALIGNMENT.md
  3. Compound extraction (auto) → compound_extract.json
  4. Enhanced docs-gate (checks stakeholder scores)
  5. If approved → merge → compound sync → archive → close
```

Steps 2-3 require `CLARITY_API_KEY`. If not configured, they're skipped gracefully.

## Getting Started

### 1. Clone

```bash
git clone https://github.com/Epistemic-Me/ai-native-dev-scaffold-compound.git my-project
cd my-project
rm -rf .git && git init
```

### 2. Set up Clarity API

```bash
cp .env.example .env
# Fill in CLARITY_API_KEY, CLARITY_USER_ID, CLARITY_API_URL

# Initialize your self-model
python scripts/compound.py init

# Set up stakeholder twins
cp .stakeholders.json.example .stakeholders.json
# Edit with your stakeholder definitions
```

### 3. Start building

```
/project:start-pr 001 initial-feature
```

## Upgrading from Walk

If you've been using the Walk scaffold and want to level up:

1. Copy this repo's `review-pr.md` over your Walk version
2. Add `stakeholder-alignment.md` and `compound.md` to `.claude/commands/project/`
3. Add `scripts/compound_config.py` (or copy from this repo)
4. Set up `.env` with Clarity API credentials
5. Run `compound.py init`
6. Add the additional context docs (JTBD.md, ICP.md, etc.)

## What's Included (Beyond Walk)

```
+ .claude/commands/project/
    stakeholder-alignment.md   # Score against digital twins
    compound.md                # Extract + sync self-model
    context-status.md          # Documentation health report

+ .claude/commands/hl/         # Power-user commands (20+)
    create-plan, iterate-plan, describe-pr, founder-mode, etc.

+ docs/.context/               # Additional context docs
    (Walk docs) + JTBD.md, ICP.md, ADR_CONTEXT.md, COMPOUND_REPORT.md

+ scripts/
    compound_config.py         # Observation contexts + stakeholder defs

+ .env.example                 # API credentials template
+ .stakeholders.json.example   # Stakeholder config template
+ GETTING-STARTED.md           # API setup guide
```

## Example

See `docs/prs/_archive/2026-01-15-PR-001-add-user-registration/` for a filled example.

## License

MIT — Use freely.

---

*Built for AI-native development with Claude Code by [Epistemic Me](https://github.com/Epistemic-Me)*
