---
title: Working Memory
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/shichun-liu-agent-memory-paper-list-the-paper-list-of-memory-2026-04-04.md
  - raw/danielwanwx-am-memory-persistent-memory-for-claude-code-2026-04-04.md
links: []
tags: [ai-agents, memory]
---

# Working Memory

## Definition

Working memory is the actively maintained state an agent uses to carry the current task forward, such as short-lived plans, selected context, or intermediate task state.

## Why It Matters

Agents need a space for "what matters right now" that is narrower than long-term memory but more durable than a single token stream. This layer keeps ongoing tasks coherent without constantly re-deriving state.

## How It Works

Working memory can appear as compact task state, session variables, scratchpads, or small retrieved memory sets that are refreshed as the conversation evolves.

## Key Properties / Tradeoffs

- **Focus**: reduces distraction from unrelated long-term knowledge.
- **Volatility**: should change quickly as the task changes.
- **Boundary management**: weak separation from long-term memory creates clutter.

## Related Concepts

- Part of: [[agent-memory-taxonomy]]
- Often fed by: [[memory-search]]
- Supported by: [[hierarchical-memory]], [[persistent-agent-memory]]

## Source Basis

- [[summary-agent-memory-survey]]
- [[summary-am-memory]]

## Open Questions

- What should trigger promotion from working memory into durable memory?
