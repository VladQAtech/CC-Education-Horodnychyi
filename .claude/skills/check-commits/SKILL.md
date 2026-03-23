---
name: check-commits
description: Check git commits in the current repository for a given time range. Use this skill whenever the user asks to find, list, show, or review commits from a specific period (e.g., "last week", "yesterday", "last 3 days", "since Monday"). Also use it when the user wants to see what changed in the repo recently or wants a commit history summary.
argument-hint: <time range, e.g. "7 days" or "yesterday" or "2 weeks">
---

# Skill: Check Commits

## What this skill does

Lists git commits from the current repository within a given time range. Presents them in a readable table and clearly reports if no commits were found.

## How to use

The user invokes this with `/check-commits <time range>`.

- If `$ARGUMENTS` is provided, use it as the time range (e.g., "7 days", "yesterday", "2 weeks", "since 2026-03-01")
- If no argument is given, default to `7 days`

## Steps

1. Run the following command to fetch commits:
   ```bash
   git log --oneline --since="$ARGUMENTS" --format="%h %s"
   ```
   If `$ARGUMENTS` is empty, use `--since="7 days ago"`.

2. If the output is empty, respond with:
   > No commits found in the last **$ARGUMENTS** (or "7 days" if not specified).

3. If commits are found, display them in a Markdown table:

   | Hash | Message |
   |------|---------|
   | `abc1234` | Commit message here |
   | `def5678` | Another commit message |

4. At the end, show the total count: `Total: N commit(s)`

## Notes

- Run this from the root of the git repository
- Time range strings are passed directly to `git log --since=`, so standard git date formats work: `"7 days ago"`, `"yesterday"`, `"2 weeks ago"`, `"2026-03-01"`
- If the user passes just a number like "7", treat it as "7 days ago"
