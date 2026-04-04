---
title: Coding Agents
type: topic
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/anomalyco-opencode-the-open-source-coding-2026-04-04.md
  - raw/leeyeel-claude-code-sourcemap-claude-code-full-original-source-2026-04-04.md
  - raw/code-yeongyu-oh-my-openagent-omo-the-best-agent-harness-2026-04-04.md
links: []
tags: [ai-agents, coding, developer-tools]
---

# Coding Agents

## Scope

This topic covers agents built to understand codebases, edit files, run commands, and complete software-development tasks such as debugging, refactoring, testing, and repository navigation.

It excludes generic chatbots that only answer programming questions without directly operating on a workspace.

Domain: **AI Agents**

## Subproblems

1. **Code navigation** - finding symbols, references, and relevant files quickly.
2. **Editing reliability** - making precise changes without stale-line or merge mistakes.
3. **Execution** - running tests, linters, builds, and shell commands safely.
4. **Delegation** - splitting work across planners, workers, and specialist agents.
5. **Provider/runtime portability** - avoiding lock-in to a single model or SDK.

## Key Approaches

### Integrated terminal agents

Claude Code and OpenCode package code navigation, file editing, and shell execution into a single terminal-native workflow. Their value comes from reducing the gap between reasoning and action.

### Multi-agent coding harnesses

OmO and DeerFlow push beyond a single agent by introducing specialized roles, deeper orchestration, and more opinionated execution loops for larger tasks.

## Landscape of Systems / Papers

| Name | Year | Key Contribution | Link |
|------|------|------------------|------|
| Claude Code | 2025 | Agentic coding workflow in the terminal | [[summary-claude-code-sourcemap]] |
| OpenCode | 2025 | Open-source coding agent with provider-agnostic runtime | [[summary-opencode]] |
| oh-my-openagent | 2025-2026 | Plugin-based multi-agent coding workflow for OpenCode | [[summary-oh-my-openagent]] |

## Important References

- [[summary-claude-code-sourcemap]] - reverse-engineered snapshot of Claude Code's earlier implementation.
- [[summary-opencode]] - open-source alternative emphasizing portability and LSP support.
- [[summary-oh-my-openagent]] - strong example of orchestration-heavy coding-agent design.

## Open Problems

- What edit primitives are robust enough for autonomous code changes under concurrent modification?
- How should coding agents balance speed against verification depth?
- Which capabilities belong in the base harness versus optional plugins and skills?

## Related Topics

- [[ai-agents]]
- [[context-engineering]]
- [[memory-management]]
