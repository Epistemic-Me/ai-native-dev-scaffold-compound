# AI-Native Development Scaffold — Sprint Stage

> **AI-native with the customer voice baked into every PR.** Run baseline + digital twins of external stakeholders + stakeholder-alignment scoring + transcript processing + self-model API integration.

```
Walk:   /start-pr  →  develop  →  /review-pr  →  /check-pr  →  /close-pr
Run:    + docs/specs/ + product slop filter + /compound (internal)
Sprint: + /stakeholder-alignment (external twins) + /process-transcript + self-model API
```

This is the **Sprint** stage of a Walk → Run → Sprint AI-native maturity staircase. It extends the Run scaffold with digital twins of external stakeholders (customers, user personas, architects, domain experts), so every PR is scored against the actual voice of the people it's supposed to serve.

This is where AI-native stops being a productivity tool and becomes a structural advantage.

## You Are Here: Walk / Run / Sprint

| Stage | What it is | Scaffold repo |
|---|---|---|
| **Walk** | Context foundation + 5-stage PR lifecycle + docs-gate CI. The operational baseline. | [`ai-native-dev-scaffold-walk`](https://github.com/Epistemic-Me/ai-native-dev-scaffold-walk) |
| **Run** | Walk + authoritative feature specs + product slop filter + `/compound` from internal PR history. | [`ai-native-dev-scaffold-run`](https://github.com/Epistemic-Me/ai-native-dev-scaffold-run) |
| **Sprint** *(← you are here)* | Run + external stakeholder digital twins + `/stakeholder-alignment` + `/process-transcript` + self-model API. Customer voice scored into every PR. | `ai-native-dev-scaffold-sprint` (this repo) |

**Don't start here.** Sprint's compounding value is only unlockable if Walk and Run are solid. Running the compound loop on a broken foundation compounds bad assumptions.

## What Sprint adds beyond Run

### Digital twins of external stakeholders

A **digital twin** is a persistent, queryable model of a person built from real interactions — meeting transcripts, emails, decision history — not a made-up persona.

At Sprint stage, you maintain twins for:
- **Customers** (especially enterprise customers with evolving requirements)
- **Product strategists** (VPs, architects who weigh in on cross-team decisions)
- **Domain experts** (compliance, accessibility, security, performance)
- **Key developers** whose time is hard to get (senior ICs, busy architects)

Twins are stored as structured belief statements with evidence (transcript excerpts, email links, decision logs). They update as new interactions happen.

### `/project:stakeholder-alignment`

On every PR before merge, score the change against relevant stakeholder twins:

```bash
/project:stakeholder-alignment 142
# For each stakeholder twin relevant to this PR:
#   - Compute alignment score (0.0-1.0)
#   - Generate per-stakeholder rationale from their belief statements
#   - Flag conflicts (e.g., "accessibility twin scores 0.3 — this PR lacks keyboard nav")
# Writes STAKEHOLDER-ALIGNMENT.md to the PR docs folder
```

Aggregate score below threshold blocks merge. Per-stakeholder below 0.3 is advisory but triggers a conversation. **This is also the product slop filter mechanism** — a feature that scores low against the product strategy twin gets rejected before code is written.

### `/project:compound`

Extracts PR episodes to the Clarity self-model API (not just local). Enables:
- Cross-repo episode queries ("have we solved this in any other repo?")
- Prediction-outcome tracking on ADRs
- Longitudinal alignment trends per stakeholder
- Monthly `COMPOUND_REPORT.md` with observation context states

### `/project:process-transcript`

Ingest a customer interview or stakeholder meeting transcript:

```bash
/project:process-transcript path/to/transcript.txt --twin customer-acme
# Extracts belief statements with evidence
# Updates the twin's belief database
# Generates proposed diffs to docs/.context/JTBD.md and docs/.context/ICP.md
# Team reviews and merges the updates
```

This is the loop that keeps context docs evidence-backed, not PM-guessed.

### Customer twin for implementation handoff (Services Transformation use case)

For customer-facing engagements where requirements evolve across sales → implementation → config validation → production, a **customer twin** captures:
- Stated requirements from the sales conversation
- Decisions made during implementation
- Audit trail of changes of mind (with reasons)
- Post-implementation feedback

Every handoff step references the twin. 80% of the context that gets lost in emails and Slack now lives in a queryable structure.

This use case applies to any configuration-driven implementation (not just code). Same workflow, different deliverable.

## You Are Here: Walk / Run / Sprint

This scaffold ships everything in Walk + everything in Run + the Sprint additions above.

## Quick Start

```bash
# 1. Clone and reinitialize
git clone https://github.com/Epistemic-Me/ai-native-dev-scaffold-sprint.git my-project
cd my-project
rm -rf .git && git init && git add -A && git commit -m "init: sprint scaffold"

# 2. Set up Clarity API (required for Sprint features)
cp .env.example .env
# Fill in: CLARITY_API_KEY, CLARITY_USER_ID, CLARITY_API_URL

# 3. Initialize your self-model
python scripts/compound.py init

# 4. Define stakeholders for this repo
cp .stakeholders.json.example .stakeholders.json
# Add twin IDs for the people whose voice matters

# 5. Start your first PR — stakeholder-alignment runs automatically in /review-pr
/project:start-pr 001 my-first-feature
```

## Design Principle: Walker Floor, Sprinter Ceiling

Sprint is the ceiling, not the floor. Most engineers at your org will live in Walk. A subset will graduate to Run when institutional memory becomes the constraint. Only the teams doing the highest-leverage work (executive-visible initiatives, customer-facing services, cross-domain migrations) need to be at Sprint.

Don't push everyone here. Let the capability emerge where it's needed.

## GitHub Copilot Compatibility

The `.claude/commands/` markdown files work with any AI harness that reads command definitions. The Clarity self-model API is tool-agnostic — it's an HTTP API. You can call it from Copilot CLI, Copilot Cloud Agents, Claude Code, or a custom tool.

## References

- **MIT NANDA — GenAI Divide 2025**: 95% pilot failure root cause is the learning gap. https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
- **Clarity self-model**: Epistemic Me's backend for stakeholder twins + episodic memory
- **GitHub — Continuous AI**: https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/

## License

MIT
