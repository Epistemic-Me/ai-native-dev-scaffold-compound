# RESEARCH: Reposition scaffold as Run stage of Walk/Run/Sprint

**Linear**: [DAY-46](https://linear.app/epistemicme/issue/DAY-46)
**Predecessor**: DAY-32 (AI-Native PR Workflow Slide Deck v1 for an enterprise software company stakeholders)
**Sibling PR**: `ai-native-dev-scaffold-run` PR #8

## Requirements Analysis

DAY-32 framed the maturity model as Walk/Run and collapsed the real Clarity-API lifecycle into a fictional "3-command loop". Feedback from stakeholder prep: this skips the context engineering foundation that's the #1 differentiator for AI-native vs AI-augmented. MIT NANDA 2025 found 95% of enterprise AI pilots fail due to the "learning gap" (missing organizational context), not model quality.

The v2 deck reframes the maturity model as **Walk → Run → Sprint**, dimensioned across **People / Process / Tools**. This PR repositions `ai-native-dev-scaffold-sprint` as the **Run** stage — the compounding intelligence layer that adds stakeholder alignment, self-model episodes, and transcript processing on top of a Walk foundation.

## Current State Analysis

The Run scaffold already has:
- `CLAUDE.md` describing "Run level" with stakeholder-alignment + compound
- `docs/.context/` with ARCHITECTURE-TAXONOMY, CURRENT_SPRINT, KNOWN_ISSUES, ROADMAP, ACTIVE_PRS, RECENT_DECISIONS
- `.claude/commands/project/` with start-pr, review-pr, stakeholder-alignment, compound, decision, context-update, context-status, close-pr
- `pr-docs-gate.yml` + `pr_docs_check.py` enforcing RESEARCH/TEST-STRATEGY/IMPLEMENTATION-PLAN
- GETTING-STARTED.md, scripts/compound.py

What's missing:
- `docs/.context/MCP_SERVERS.md` including Run-specific servers (Self-Model API, transcript ingestion)
- Credential policy section in CLAUDE.md (with extra emphasis on customer PII at Run)
- "You Are Here" Walk/Run/Sprint positioning
- Explicit warning that users should not start here without Walk maturity first

## Implementation Gap Analysis

| Gap | Impact | Fix |
|---|---|---|
| No MCP_SERVERS.md | No pattern for declaring Run-stage tools (Self-Model API, transcript ingest) | Create with Walk baseline + Run additions + Context Declaration template |
| No credential policy | Customer-PII handling is tribal; a Run-stage leak has bigger blast radius | Add 5-point abstract policy section with customer-PII emphasis |
| "3-command loop" framing | Contradicts real Clarity-API 5-stage lifecycle | Rewrite CLAUDE.md header to show 5-stage Walk baseline + 3 Run additions |
| No staircase positioning | Users might start here without Walk maturity and compound bad assumptions | Add "You Are Here" table + explicit "don't start here" warning |

## Dependencies and Risks

- **Dependency**: DAY-46 v2 deck revision
- **Dependency**: `ai-native-dev-scaffold-run` (Walk) sibling PR #8
- **Dependency**: `ai-native-dev-scaffold-walk` repo creation (tracked in DAY-46)
- **Risk**: Existing Run users may find the "don't start here" warning discouraging — mitigated by framing it as a sequencing recommendation, not a restriction
- **Risk**: Credential policy's customer-PII emphasis could invite questions about specific compliance frameworks — kept deliberately abstract so orgs can map to their own (SOC2, HIPAA, GDPR)

## Open Questions

None — scope is narrow and doc-only.
