---
title: Hierarchical Memory
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/shichun-liu-agent-memory-paper-list-the-paper-list-of-memory-2026-04-04.md
  - raw/bai-lab-memoryos-emnlp-oral-memoryos-is-2026-04-04.md
links: []
tags: [ai-agents, memory, hierarchy]
---

# Hierarchical Memory

## Definition

Hierarchical memory organizes agent memory into multiple levels or tiers that differ in lifetime, granularity, and retrieval cost.

## Why It Matters

Not all context should be stored or retrieved the same way. Tiering lets systems keep short-lived active state close to the current task while moving broader or older knowledge into slower, longer-lived layers.

## How It Works

Common patterns include separating short-term, session, and long-term memory, or using directory-like levels that move from coarse summaries to detailed records.

## Key Properties / Tradeoffs

- **Efficiency**: reduces the need to search everything at full fidelity.
- **Policy complexity**: promotion, consolidation, and eviction rules matter.
- **Interpretability**: tiered systems are often easier to reason about than a flat memory pool.

## Related Concepts

- Related: [[multi-level-memory]], [[memory-operating-system]]
- Used in: [[memory-management]]
- Can support: [[working-memory]]

## Source Basis

- [[summary-agent-memory-survey]] - survey framing.
- [[summary-memoryos-emnlp2025]] - concrete short/mid/long-term design.
- [[summary-openviking]] - L0/L1/L2 context hierarchy example.

## Open Questions

- What is the right retrieval policy between tiers for live agent use?
