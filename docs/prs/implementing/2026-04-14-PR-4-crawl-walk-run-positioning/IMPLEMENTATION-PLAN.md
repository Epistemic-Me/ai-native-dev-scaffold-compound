# IMPLEMENTATION-PLAN: Reposition scaffold as Run stage

## Chosen Approach

Docs-only edit. Three files, one new.

## Scope

In scope:
- New `docs/.context/MCP_SERVERS.md` with Walk baseline + Run additions
- Edit `CLAUDE.md`: header reframe, 5-stage Walk + Run additions, Credential Policy
- Edit `README.md`: title + "You Are Here" + don't-start-here warning

Out of scope:
- Any command file changes
- pr_docs_check.py or CI workflow
- `ai-native-dev-scaffold-crawl` creation (tracked in DAY-46)

## Files Summary

| File | Action | Purpose |
|---|---|---|
| `docs/.context/MCP_SERVERS.md` | Create | Tool registry (Walk baseline + Run additions) + Context Declaration |
| `CLAUDE.md` | Edit | Reframe as Run stage, show Walk + Run command layering, Credential Policy |
| `README.md` | Edit | Title + "You Are Here" + explicit sequencing warning |

## Step-by-Step Implementation

### Step 1: MCP_SERVERS.md (AC1)
- Copy the Walk-stage registry template (Linear, Playwright, GitHub)
- Append "Run-stage additions" section with Self-Model API and transcript ingestion entries
- Include Context Declaration template

### Step 2: CLAUDE.md (AC2, AC4)
- Replace header with "Run stage of Crawl → Walk → Run" framing
- Add "You Are Here" staircase table
- Rewrite lifecycle section to show Walk 5 stages + Run 3 additions layering onto `/review-pr`

### Step 3: CLAUDE.md Credential Policy (AC3)
- Append section with 5 abstract principles
- Emphasize customer-PII handling in principles 3-5

### Step 4: README.md (AC5)
- Change title to "AI-Native Development Scaffold — Run Stage"
- Add "You Are Here" table linking to `ai-native-dev-scaffold-crawl` and `ai-native-dev-scaffold-walk`
- Include explicit "Don't start here. Clone the Walk scaffold first..." warning

## Verification Checklist

- [x] T1-T4: MCP_SERVERS.md created with all required content
- [x] T5: CLAUDE.md shows Walk + Run command layering
- [x] T6-T7: Credential Policy with PII emphasis
- [x] T8: You Are Here staircase in CLAUDE.md
- [x] T9-T11: README.md title, warning, and links
- [ ] T12: CI docs-gate green (verified on draft PR)
