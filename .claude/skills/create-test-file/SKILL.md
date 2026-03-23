---
name: create-test-file
description: Scaffold a new pytest test file for the Promova project following team naming conventions. Use this skill when the user asks to create a new test file, start writing tests for a feature, or scaffold a test module.
argument-hint: <feature-name> [platform: web|api|ios|android]
disable-model-invocation: true
---

# Skill: Create Test File

Scaffold a new pytest test file following the project's naming conventions and structure.

## Arguments

`$ARGUMENTS` contains the feature name and optionally the platform:
- `/create-test-file login web` → `tests/web/test_login.py`
- `/create-test-file daily_goal api` → `tests/api/test_daily_goal.py`
- `/create-test-file usyk_mode` → ask the user which platform

Parse `$ARGUMENTS`:
1. First word = feature name (use as-is, e.g. `usyk_mode`, `login`)
2. Second word = platform (`web`, `api`, `ios`, `android`) — if missing, ask before proceeding

## Steps

1. **Determine the target path**
   - File goes at: `tests/<platform>/test_<feature>.py`
   - Create the directory if it doesn't exist

2. **Generate the file** with this structure:

```python
import pytest
from playwright.sync_api import Page


def test_<feature>_<action_1>(page: Page):
    # TODO: implement
    pass


def test_<feature>_<action_2>(page: Page):
    # TODO: implement
    pass
```

   - Include 2 placeholder test functions
   - Name them `test_<feature>_<what_is_being_verified>` — make the action descriptive, not generic
   - Each function gets a `# TODO: implement` comment and `pass`
   - Function-based only — no test classes

3. **Report** what was created:
   - Full file path
   - List of generated function names
   - Reminder to fill in the TODO bodies

## Naming conventions (always apply)

- **File**: `test_<feature>.py` — lowercase, underscores
- **Functions**: `test_<feature>_<action>` — action describes what is verified, often including expected outcome (e.g., `test_login_invalid_password_shows_error`, `test_usyk_mode_toggle_appears_on_my_plan_tab`)
- **No classes** — all tests are top-level functions
- **Imports**: always include `pytest` and `from playwright.sync_api import Page`

## Example

`/create-test-file onboarding web` produces `tests/web/test_onboarding.py`:

```python
import pytest
from playwright.sync_api import Page


def test_onboarding_first_screen_displays_welcome_message(page: Page):
    # TODO: implement
    pass


def test_onboarding_skip_button_navigates_to_home(page: Page):
    # TODO: implement
    pass
```
