---
title: "Summary — 8 Claude Code Hooks That Automate What You Keep Forgetting"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/8-claude-code-hooks-that-automate-what-you-2026-04-03.md
  - https://x.com/zodchiii/status/2040000216456143002
tags: []
---

# Summary — 8 Claude Code Hooks That Automate What You Keep Forgetting

## Source Metadata

| Field        | Value                                                       |
|--------------|-------------------------------------------------------------|
| Source type  | blog / social media                                         |
| Author(s)    | @zodchiii                                                   |
| Year         | 2026                                                        |
| Venue        | X (Twitter) thread                                          |
| Raw file     | `raw/8-claude-code-hooks-that-automate-what-you-2026-04-03.md` |

## Main Idea

Claude Code Hooks are automatic actions that fire on specific events (PreToolUse, PostToolUse, Stop) to enforce consistent behavior. Unlike CLAUDE.md suggestions (~80% compliance), hooks run 100% automatically, enabling reliable automation of formatting, safety checks, and testing.

## Key Details

- **PreToolUse**: Runs before Claude does something — can block dangerous actions by returning exit code 2
- **PostToolUse**: Runs after Claude does something — for cleanup, formatting, test running
- **Stop**: Runs when Claude finishes a response — for auto-committing changes
- **Hook #1**: Auto-format every file on Write/Edit using Prettier (or black/gofmt/rustfmt)
- **Hook #2**: Block dangerous commands (rm -rf, git reset --hard, DROP TABLE, curl piping to bash)
- **Hook #3**: Protect sensitive files (.env, package-lock.json, *.pem, secrets/*)
- **Hook #4**: Run tests automatically after every Write/Edit — tail -5 keeps output concise
- **Hook #5**: Block PR creation unless tests pass (matcher: mcp__github__create_pull_request)
- **Hook #6**: Auto-lint with ESLint after edits
- **Hook #7**: Log every Bash command to .claude/command-log.txt with timestamps
- **Hook #8**: Auto-commit after Stop using .claude/hooks/auto-commit.sh

## Method / Approach

Hooks are configured in `.claude/settings.json` at project or user level. Exit code 2 blocks the action and returns error message to Claude for safer retry. Exit code 0 allows proceeding. Hooks work via pattern matching on tool names (Write|Edit|Bash) or specific MCP tools.

## Results / Evidence

Boris Cherny (Claude Code creator) cited that giving Claude a feedback loop improves output quality by 2-3x. The auto-format hook eliminates "Claude forgot to format" commits entirely.

## Limitations

- Hooks require chmod +x on shell scripts
- command-log.txt must be added to .gitignore manually
- Exit code handling differences between hook types can be subtle

## Links to Concepts

- [[claude-code]] — the agent this hooks system extends
- [[tool-use]] — hooks intercept and augment tool usage
- [[agent-harness]] — hooks are part of the harness configuration layer

## Links to Topics

- [[coding-agents]]

## Quotes Worth Preserving

> The difference between a good Claude Code setup and a great one isn't the model or the prompts. It's the hooks.
