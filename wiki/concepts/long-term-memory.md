---
title: Long-Term Memory
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/bytedance-deer-flow-an-open-source-long-horizon-2026-04-04.md
  - raw/mem0ai-mem0-universal-memory-layer-for-ai-2026-04-04.md
links: []
tags: [ai-agents, memory]
---

# Long-Term Memory

## Definition

Long-term memory is the durable memory layer that persists useful knowledge across sessions rather than only within the current interaction.

## Why It Matters

It is what lets agents accumulate user preferences, recurring solutions, and reusable knowledge over time instead of restarting from zero every session.

## How It Works

Long-term memory is usually built by promoting selected session artifacts into a durable store and retrieving a small subset back into context when relevant.

## Key Properties / Tradeoffs

- **Persistence**: survives beyond one conversation.
- **Personalization**: enables cumulative adaptation.
- **Staleness risk**: old memories can become wrong or irrelevant.

## Related Concepts

- More specific implementation: [[persistent-agent-memory]]
- Often organized as: [[hierarchical-memory]]
- Falls under: [[memory-management]]

## Source Basis

- [[summary-deer-flow]]
- [[summary-mem0]]

## Open Questions

- What promotion rules preserve useful long-term memory without flooding the store?
