# Research: User Registration Endpoint

## Problem Statement
Users currently cannot create accounts. The app has no registration flow. We need a POST /api/users endpoint that creates accounts with email/password.

## Current State
- No user model exists
- No auth middleware
- Database is PostgreSQL via Prisma ORM
- Existing endpoints follow REST conventions in `src/api/`

## Options Considered

### Option A: Simple email/password registration
- Pros: Fast to build, covers MVP needs
- Cons: No OAuth, no email verification
- Effort: 1 day

### Option B: Full auth system with OAuth + email verification
- Pros: Production-grade, supports Google/GitHub login
- Cons: 3-5 days, scope creep risk for an MVP
- Effort: 3-5 days

## Recommendation
Option A for this PR. Email verification and OAuth are separate PRs (tracked as future work in ROADMAP.md).

## Dependencies
- Prisma ORM (already installed)
- bcrypt for password hashing (needs install)

## Open Questions
- ~~Password minimum length?~~ Resolved: 8 characters minimum (per team discussion)
