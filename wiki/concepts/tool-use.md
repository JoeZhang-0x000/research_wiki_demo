---
title: Tool Use
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/maxgfeller-open-harness-a-code-first-composable-sdk-2026-04-04.md
  - raw/anomalyco-opencode-the-open-source-coding-2026-04-04.md
links: []
tags: [ai-agents, tools, execution]
---

# Tool Use

## Definition

Tool use is the ability of an agent to call external capabilities such as filesystems, shells, search systems, browsers, or APIs as part of solving a task.

## Why It Matters

Without tools, agents are limited to reasoning over whatever text is already in context. Tool use is what makes them operational rather than purely conversational.

## How It Works

The harness exposes discrete callable tools with schemas or other interfaces, the model chooses when to call them, and the runtime feeds tool results back into the agent loop.

## Key Properties / Tradeoffs

- **Actionability**: enables real work in the environment.
- **Safety**: every new tool expands the failure surface.
- **Composition**: strong tool APIs simplify planning and recovery.

## Related Concepts

- Central to: [[agent-harness]], [[coding-agents]]
- Often mediated by: [[mcp-server]]

## Source Basis

- [[summary-open-harness]]
- [[summary-opencode]]

## Open Questions

- Which tool affordances are robust enough for autonomous use across many repositories?
