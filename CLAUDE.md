# CLAUDE.md
This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview
This is a test project with Python autotests for the language learning app Promova. The autotests are written for API, iOS, Android and Web


## Context

This is a course repository for the Claude Code Education program. Modules are started with `/cc-course:start <module-number>` (modules 1–5) and submitted with `/cc-course:submit`.

## Useful Course Commands

- `/cc-course:start <N>` — begin module N
- `/cc-course:status` — view course progress
- `/cc-course:hint` — get contextual help for the current task
- `/cc-course:validate` — check if current module requirements are complete
- `/cc-course:submit` — package completed work for review
- `/cc-course:continue` — signal readiness to proceed to the next step

## Tech Stack
  - Language: Python
  - Framework: Playwright
  - Testing: Playwright (e2e), pytest
  - Build: (test automation project)

## Conventions
  - Тести лежать у папці `tests/`
  - Page Objects у папці `pages/`
  - Fixtures у `conftest.py`
  - Назви тестів: `test_daily_goal.py, test_learning_map.py`

## Commands
  - Run tests: `pytest`
  - Run specific test: `pytest tests/test_login.py`
  - Run with report: `pytest --html=report.html`
  - Start dev: <no command>