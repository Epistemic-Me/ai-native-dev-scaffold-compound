# MCP Servers — Tool Context Registry

Every MCP (Model Context Protocol) server this repo uses, why it's here, which ticket types need it, and where its credentials live.

This file is part of the **Walk** stage of the Walk/Run/Sprint maturity model. Before a team can run the PR lifecycle reliably, tool access must be declared and consistent across developers and agent sessions. See `CLAUDE.md` → "Credential Policy" for the companion secret-handling rules.

## How to use this file

1. **Before starting a ticket**: scan the registry to see which servers you need. Declare them in the ticket's **Context Declaration** block (see template below).
2. **When adding a new MCP server**: open a PR that edits this file. Include purpose, needed-for, scope, credential path, and fallback.
3. **When deprecating a server**: mark it deprecated here first, migrate callers, then remove.

## Registry

### Linear MCP
- **Purpose**: Read and update Linear tickets from Claude Code during `/start-pr`, `/review-pr`, `/close-pr`
- **Needed for**: Every PR — ticket sync is a Walk-stage baseline
- **Scope**: Read tickets, update status and description, add comments. Read-only on projects/milestones.
- **Credential**: `LINEAR_API_KEY` — **service account**, not personal. Vault path: `vault://engineering/linear-bot`
- **Fallback**: `gh issue` commands against a GitHub Issues mirror, or manual Linear web UI
- **Docs**: https://linear.app/developers/mcp

### Playwright MCP
- **Purpose**: Browser automation for E2E testing, UI validation, visual regression checks
- **Needed for**: Frontend PRs, regression verification steps in TEST-STRATEGY.md
- **Scope**: Local Chrome instance only. Allowed targets: `localhost:*`, staging URLs listed in `.playwright-allowed.json`. **No production URLs.**
- **Credential**: none (local runner)
- **Fallback**: Manual browser testing with test plan from TEST-STRATEGY.md
- **Docs**: https://github.com/microsoft/playwright-mcp

### GitHub MCP (optional — if not using `gh` CLI)
- **Purpose**: Read PRs, issues, CI status, and review comments from Claude Code
- **Needed for**: `/check-pr`, `/review-pr` when running docs-gate locally
- **Scope**: This repo + org-public repos. Read-only on org membership.
- **Credential**: GitHub App installation token. Vault path: `vault://engineering/github-app-scaffold`
- **Fallback**: `gh` CLI commands (already available in most dev environments)
- **Docs**: https://github.com/github/github-mcp-server

## Per-Ticket Context Declaration template

Every ticket description includes a **Context Declaration** block alongside acceptance criteria. Copy this template:

```markdown
## Context Declaration

**Docs needed**:
- docs/.context/ARCHITECTURE-TAXONOMY.md
- docs/.context/KNOWN_ISSUES.md
- [other relevant context docs]

**MCP servers**: Linear, Playwright
**Credentials**: vault://engineering/linear-bot, [others as needed]
**Related ADRs**: ADR-NNNN (short title)
**Related PRs**: #123, #145
```

This is the Walk-stage contract: you declare context requirements **before** work starts, not mid-PR when something breaks.

## Run-stage additions (compounding intelligence)

This scaffold is the **Run** stage of the Walk/Run/Sprint staircase. It adds servers beyond the Walk baseline for the compounding loop — self-model API, transcript processing, stakeholder alignment.

### Self-Model API (Clarity backend)
- **Purpose**: Persist episodes extracted by `/compound`, query alignment data, track prediction→outcome on decisions
- **Needed for**: `/stakeholder-alignment`, `/compound`, `/process-transcript`, monthly COMPOUND_REPORT.md refresh
- **Scope**: Write episodes for this repo's `self_model_id`; read alignment across all repos sharing the self-model
- **Credential**: `CLARITY_API_KEY` — builder identity, not personal. Vault path: `vault://engineering/clarity-builder-{repo}`
- **Fallback**: Manual JSON export via `scripts/compound.py extract` (no cross-session memory)
- **Setup**: `cp .clarity.json.example .clarity.json` then `~/.claude/scripts/fetch-self-context.sh`

### Transcript ingestion (Otter, Fireflies, or equivalent)
- **Purpose**: Pull customer interview transcripts into `/process-transcript` to update JTBD.md and ICP.md with evidence
- **Needed for**: Quarterly context-doc refresh, JTBD evidence updates after research sessions
- **Scope**: Read-only on meeting transcripts tagged for this project
- **Credential**: Provider-specific API key. Vault path: `vault://research/transcript-ingest`
- **Fallback**: Manual transcript paste into `/process-transcript`

## Deprecated / Removed servers

None yet.

## References

- **Model Context Protocol spec**: https://modelcontextprotocol.io/
- **Anthropic MCP announcement**: https://www.anthropic.com/news/model-context-protocol
- **Astrix Security — State of MCP Server Security 2025** (88% require credentials, 53% long-lived static secrets, only 8.5% OAuth): https://astrix.security/learn/blog/state-of-mcp-server-security-2025/
- **Model Context Protocol donation to Linux Foundation (Dec 2025)**: part of the Agentic AI Foundation alongside AGENTS.md
