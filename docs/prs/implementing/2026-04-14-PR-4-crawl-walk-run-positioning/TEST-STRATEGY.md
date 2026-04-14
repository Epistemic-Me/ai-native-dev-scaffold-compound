# TEST-STRATEGY: Reposition scaffold as Run stage

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | `docs/.context/MCP_SERVERS.md` exists with Walk baseline (Linear, Playwright, GitHub) + Run additions (Self-Model API, transcript ingestion) |
| AC2 | `CLAUDE.md` shows Walk 5-stage lifecycle + Run 3-command additions (`/stakeholder-alignment`, `/compound`, `/process-transcript`) |
| AC3 | `CLAUDE.md` includes Credential Policy section with customer-PII emphasis |
| AC4 | `CLAUDE.md` top contains "You Are Here" Crawl/Walk/Run staircase |
| AC5 | `README.md` title includes "Run Stage", "You Are Here" table with sibling scaffold links, and explicit "don't start here without Walk maturity" warning |
| AC6 | Docs-gate CI continues to pass (this PR's own docs folder satisfies RESEARCH/TEST-STRATEGY/IMPLEMENTATION-PLAN) |

## Test Matrix

| Test ID | File | Test Case | AC Covered | Pass Criteria |
|---|---|---|---|---|
| T1 | docs/.context/MCP_SERVERS.md | File exists, non-empty | AC1 | `test -s` |
| T2 | docs/.context/MCP_SERVERS.md | Contains Walk baseline servers | AC1 | grep Linear, Playwright, GitHub MCP |
| T3 | docs/.context/MCP_SERVERS.md | Contains Run additions | AC1 | grep "Self-Model API" and "Transcript ingestion" |
| T4 | docs/.context/MCP_SERVERS.md | Context Declaration template present | AC1 | grep "Context Declaration" |
| T5 | CLAUDE.md | Walk lifecycle + Run additions | AC2 | grep "/start-pr" AND "/stakeholder-alignment" AND "/compound" AND "/process-transcript" |
| T6 | CLAUDE.md | Credential Policy section | AC3 | grep "Credential Policy" |
| T7 | CLAUDE.md | Customer PII reference | AC3 | grep -i "customer" in policy section |
| T8 | CLAUDE.md | You Are Here staircase | AC4 | grep "You Are Here" |
| T9 | README.md | Title contains Run Stage | AC5 | `head -1 README.md | grep -q "Run"` |
| T10 | README.md | Don't-start-here warning | AC5 | grep "Don't start here" |
| T11 | README.md | Links to sibling scaffolds | AC5 | grep "ai-native-dev-scaffold" (non-compound) |
| T12 | CI | Docs-gate passes | AC6 | GitHub Actions green check |

## Definition of Done

- [ ] All 6 acceptance criteria verified
- [ ] CI docs-gate green
- [ ] Sibling PR #8 in `ai-native-dev-scaffold` merged first (recommended, not blocking)
- [ ] No behavior changes — only documentation
