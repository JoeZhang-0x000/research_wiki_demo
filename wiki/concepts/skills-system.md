---
title: Skills System
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/bytedance-deer-flow-an-open-source-long-horizon-2026-04-04.md
  - raw/code-yeongyu-oh-my-openagent-omo-the-best-agent-harness-2026-04-04.md
links: []
tags: [ai-agents, skills, extensibility]
---

# Skills System

## Definition

A skills system packages reusable instructions, workflows, and sometimes attached tools so an agent can load task-specific capability on demand instead of carrying all behavior in its base prompt.

## Why It Matters

Large agent runtimes become brittle when everything lives in one monolithic system prompt. Skills make capability more modular and can reduce unnecessary context use.

## How It Works

The sources describe markdown-defined skills, selective loading, and cases where a skill also brings along scoped MCP servers or other execution resources.

## Key Properties / Tradeoffs

- **Modularity**: separates durable workflow knowledge from the harness core.
- **Context efficiency**: only relevant skills need to be loaded.
- **Governance**: poor skill quality can become a hidden source of behavior drift.

## Related Concepts

- Extended by: [[skill-embedded-mcps]]
- Used in: [[superagent-harness]], [[agent-harness]]
- Related to: [[experiential-memory]]

## Source Basis

- [[summary-deer-flow]]
- [[summary-oh-my-openagent]]

## Open Questions

- What metadata and selection policy make skills discoverable without loading too many of them?
