# Test Strategy: User Registration

## Acceptance Criteria

| AC-ID | Criteria | Priority |
|-------|----------|----------|
| AC1 | POST /api/users creates a user with valid email + password | P0 |
| AC2 | Returns 422 with field-level errors for invalid input | P0 |
| AC3 | Returns 409 if email already registered | P0 |
| AC4 | Password is hashed (never stored in plaintext) | P0 |
| AC5 | Response includes user ID but NOT password hash | P1 |

## Test Matrix

| Test-ID | File | Test Case | AC Covered | Pass Criteria |
|---------|------|-----------|------------|---------------|
| T1 | tests/api/test_users.py | test_register_valid_user | AC1, AC5 | 201 status, user ID in response, no password in response |
| T2 | tests/api/test_users.py | test_register_invalid_email | AC2 | 422 status, "email" in errors array |
| T3 | tests/api/test_users.py | test_register_short_password | AC2 | 422 status, "password" in errors array |
| T4 | tests/api/test_users.py | test_register_duplicate_email | AC3 | 409 status, "already registered" message |
| T5 | tests/api/test_users.py | test_password_is_hashed | AC4 | DB record password != input password, bcrypt verify passes |

## Definition of Done

- [x] All ACs covered by at least one test
- [x] Tests pass locally
- [x] Tests pass in CI
- [x] No P0 regressions
- [x] IMPLEMENTATION-PLAN.md verification checklist complete
