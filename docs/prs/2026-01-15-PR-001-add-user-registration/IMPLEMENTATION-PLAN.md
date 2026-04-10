# Implementation Plan: User Registration

## Chosen Approach
Option A from RESEARCH.md — simple email/password registration.

## Scope
**In scope**: POST /api/users, input validation, password hashing, duplicate detection
**Out of scope**: OAuth, email verification, password reset (future PRs)

## Files Summary

| File | Action | Purpose |
|------|--------|---------|
| prisma/schema.prisma | Modify | Add User model |
| src/api/users.ts | Create | Registration endpoint |
| src/validators/user.ts | Create | Input validation schema |
| tests/api/test_users.py | Create | All test cases from TEST-STRATEGY |

## Step-by-Step

### Step 1: Add User model to Prisma schema (AC4)
Add User model with id, email (unique), passwordHash, createdAt. Run `prisma migrate dev`.

### Step 2: Create input validation (AC2)
Zod schema: email must be valid format, password >= 8 chars. Returns field-level errors.

### Step 3: Create POST /api/users endpoint (AC1, AC3, AC5)
- Validate input (step 2)
- Check for duplicate email -> 409
- Hash password with bcrypt
- Create user in DB
- Return user ID + email (NOT password hash)

### Step 4: Write tests (all ACs)
Implement T1-T5 from TEST-STRATEGY.md.

## Verification Checklist
- [x] Step 1: User model migrated
- [x] Step 2: Validation rejects bad input
- [x] Step 3: Endpoint creates users, handles duplicates
- [x] Step 4: All 5 tests pass
