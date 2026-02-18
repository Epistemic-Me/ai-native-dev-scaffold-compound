# Getting Started with the Compound Loop

This scaffold works in two modes:

1. **Standalone** — PR lifecycle, paper trails, and ADRs work out of the box. No setup needed.
2. **With Compound Loop** — Adds self-reflection, stakeholder alignment, and compound reports. Requires Clarity API credentials.

This guide covers setting up the compound loop. For basic scaffold usage, see [README.md](./README.md).

## What is the Compound Loop?

The compound loop extracts structured data from your PR documentation and feeds it into a self-model via the [Clarity API](https://epistemicme.ai). It answers questions like:

- How is our architecture quality trending?
- Are we aligned with stakeholder goals?
- What beliefs are we validating or invalidating with each PR?

The loop runs after each PR merge:

```
REVIEW.md → extract episodes/beliefs → stakeholder alignment → sync to API → compound report
```

## Prerequisites

- Python 3.8+
- The [Clarity API](https://github.com/Epistemic-Me/Clarity-API) repo cloned locally
- A Clarity API key (contact the [Epistemic Me](https://epistemicme.ai) team)

## Step 1: Install Python Dependencies

```bash
pip install requests pyyaml
```

These are the only Python dependencies. They are not managed by the scaffold.

## Step 2: Clone the Clarity API

The compound loop uses `compound.py` from the Clarity API repo. Clone it alongside your project:

```bash
git clone https://github.com/Epistemic-Me/Clarity-API.git
```

Set the path as an environment variable:

```bash
export CLARITY_API_PATH=/path/to/Clarity-API
```

Add this to your shell profile (`.bashrc`, `.zshrc`, etc.) so it persists.

## Step 3: Configure Credentials

Copy the example env file and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```bash
CLARITY_API_URL=https://clarity-self-learning-agent.onrender.com
CLARITY_API_KEY=your_api_key_here
```

## Step 4: Initialize Your Builder Self-Model

Run the init command to register yourself with the Clarity API:

```bash
python3 "${CLARITY_API_PATH}/scripts/compound.py" \
  --config-dir ./scripts \
  init --name "Your Name" --email "you@example.com"
```

This returns a `user_id` and `self_model_id`. Add them to your `.env`:

```bash
CLARITY_USER_ID=12345
CLARITY_SELF_MODEL_ID=12346
```

## Step 5: Customize Observation Contexts (Optional)

Edit `scripts/compound_config.py` to match your project's domain. The defaults cover 9 generic software project dimensions:

| Context | Pillar | What it measures |
|---------|--------|------------------|
| `architecture_quality` | Technical | Codebase health, pattern consistency |
| `test_coverage` | Technical | Test infrastructure maturity |
| `technical_debt` | Technical | Accumulated shortcuts and deferred cleanup |
| `feature_completeness` | Product | How complete the product is |
| `user_experience` | Product | Quality of end-user experience |
| `developer_velocity` | Process | Speed and ease of shipping |
| `knowledge_distribution` | Team | How well knowledge is shared |
| `customer_alignment` | Business | How well product serves customers |
| `documentation_quality` | Team | Documentation completeness |

Customize `possible_states`, add new contexts, or remove ones that don't apply.

## Step 6: Configure Stakeholders (Optional)

Stakeholders are the people whose goals your PRs should align with. Configure them in one of two ways:

### Option A: Edit compound_config.py directly

Uncomment and fill in the `STAKEHOLDER_DEFINITIONS` and `STAKEHOLDER_WEIGHTS` sections.

### Option B: Use .stakeholders.json override

Copy the example and customize:

```bash
cp .stakeholders.json.example .stakeholders.json
```

Edit `.stakeholders.json` with your team's stakeholders. This file is gitignored so each builder can have their own set.

### Register Stakeholder Self-Models

After defining stakeholders, register them with the API:

```bash
python3 "${CLARITY_API_PATH}/scripts/stakeholder_setup.py"
```

Update `self_model_id` values in your config with the returned IDs.

## Step 7: Map PRs to Contexts

As you merge PRs, update `SPRINT_CONTEXT_MAP` in `compound_config.py` to record which observation contexts each PR advanced:

```python
SPRINT_CONTEXT_MAP = {
    0: {
        "primary": "architecture_quality",
        "secondary": ["test_coverage"],
        "transition": ("fragile", "functional"),
        "title": "Initial Architecture Setup",
        "pr": 1,
    },
}
```

## Using the Compound Loop

### Automatic (during PR lifecycle)

If credentials are configured, the PR lifecycle commands will offer to run the compound loop:

- `/project:close-pr` asks before finalizing
- `/project:execute-pr` includes it as Phase 7

### Manual

Run the compound loop for any PR:

```
/project:compound 042
```

Or just the stakeholder alignment:

```
/project:stakeholder-alignment 042
```

Or just regenerate the report:

```
/project:compound --report-only
```

### Writing Good REVIEW.md

The compound loop extracts data from REVIEW.md. For best results, fill in the "Compound Loop Data" section:

1. **Observation Context Changes** — Which dimensions did this PR advance?
2. **Beliefs** — What assumptions were validated or invalidated?

Even without the compound loop, REVIEW.md provides structured code review notes that improve your paper trail.

## Compound Report

After running the loop, check `docs/.context/COMPOUND_REPORT.md` for:

- Current state vs target state for each observation context
- Gap analysis showing what to focus on next
- Stakeholder alignment trends
- Builder trajectory over time

## Troubleshooting

### "compound.py not found"

Set `CLARITY_API_PATH` to the directory containing the Clarity-API repo:

```bash
export CLARITY_API_PATH=/path/to/Clarity-API
```

### "requests package required"

```bash
pip install requests pyyaml
```

### "CLARITY_API_KEY not set"

Copy `.env.example` to `.env` and fill in your API key. Contact the Epistemic Me team to get one.

### "self_model_id is None"

Run `stakeholder_setup.py` to register your stakeholders, then update the IDs in your config.
