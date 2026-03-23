---
name: pytest-naming-conventions
description: Naming conventions for pytest tests in this project. Apply these rules automatically whenever writing, creating, or reviewing any pytest test files, test functions, or test structure. Use this skill any time tests are being written or discussed — even if the user doesn't explicitly mention naming.
user-invocable: false
---

# Pytest Naming Conventions

These are the team's agreed naming standards for the Promova test automation project (Python + Playwright + pytest).

## File naming

Test files follow the pattern `test_<feature>.py`, where `<feature>` is the area being tested.

```
test_login.py
test_daily_goal.py
test_learning_map.py
test_onboarding.py
```

One feature per file keeps tests easy to find and run selectively.

## Function naming

Test functions follow `test_<feature>_<action>`, where `<action>` typically describes what happens or what the expected result is. This makes the test's intent clear just from the name.

```python
def test_login_valid_credentials():
def test_login_invalid_password():
def test_create_solid_order_returns_200():
def test_daily_goal_completion_updates_streak():
def test_learning_map_loads_correct_lessons():
```

The name should answer: *what is being tested and what should happen?*

## Platform separation

Tests for different platforms (Web, iOS, Android, API) are separated by **directory**, not by name prefix.

```
tests/
├── web/
│   └── test_login.py
├── api/
│   └── test_login.py
├── ios/
│   └── test_login.py
└── android/
    └── test_login.py
```

Do not add platform prefixes to file or function names (e.g., avoid `test_web_login.py` or `def test_api_login()`).

## Test style

Use **function-based tests** — no test classes.

```python
# Correct
def test_login_valid_credentials():
    ...

# Avoid
class TestLogin:
    def test_valid_credentials(self):
        ...
```

Function-based tests are simpler to read, easier to run individually, and match the project's existing style.
