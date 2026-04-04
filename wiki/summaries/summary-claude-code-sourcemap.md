---
title: "Summary — leeyeel/claude-code-sourcemap: Claude Code Source Maps"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/leeyeel-claude-code-sourcemap-claude-code-full-original-source-2026-04-04.md
  - "https://github.com/leeyeel/claude-code-sourcemap"
links:
  - "https://github.com/leeyeel/claude-code-sourcemap"
tags: []
---

# Summary — leeyeel/claude-code-sourcemap: Claude Code Source Maps

## Source Metadata

| Field        | Value                                                                       |
|--------------|-----------------------------------------------------------------------------|
| Source type  | web / github / source code archive                                         |
| Author(s)    | leeyeel (forked from original Claude Code); original by Anthropic          |
| Year         | 2025                                                                        |
| Venue        | GitHub (source map extraction project)                                     |
| Raw file     | `raw/leeyeel-claude-code-sourcemap-claude-code-full-original-source-2026-04-04.md` |

## Main Idea

This repository hosts the full original source code of Claude Code (Research Preview version 0.2.8) extracted from source maps. The original source was not publicly available; leeyeel extracted it from the distributed Claude Code package for research and transparency purposes.

## Key Details

- **Version**: Claude Code Research Preview 0.2.8
- **Extraction method**: Source map reverse engineering
- **Fork**: https://github.com/dnakov/anon-kode (active fork)
- **Note**: The maintainer explicitly states "I'm not working on this repo, this is the original source"
- **Status**: leeyeel's repo is archival; active development on the fork

**Claude Code capabilities described**:
- Edit files and fix bugs across codebase
- Answer questions about architecture and logic
- Execute and fix tests, lint, and other commands
- Search git history, resolve merge conflicts, create commits and PRs

**Research Preview specifics**:
- Beta product launched to learn from developer experiences
- Feedback collected (usage data, conversation data, user feedback via `/bug`)
- NOT used for training generative models
- Feedback transcripts stored max 30 days for sensitive data
- OAuth one-time setup via Anthropic Console account

## Method / Approach

The source code was obtained by downloading the Claude Code npm package and using the embedded source maps to reconstruct the original TypeScript/JavaScript source files. This is a legitimate reverse-engineering approach for a tool whose source was not publicly distributed.

## Results / Evidence

This is an informational/research artifact, not a research contribution with results.

## Limitations

- Version 0.2.8 is outdated—Claude Code has evolved significantly since
- No documentation beyond extracted source
- Authorship and legal status of the extracted source is ambiguous

## Links to Concepts

- [[claude-code]] — the subject of this source map extraction
- [[source-map-reverse-engineering]] — extraction technique used

## Links to Topics

- [[ai-agents]]
- [[coding-agents]]

## Quotes Worth Preserving

> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows — all through natural language commands.
