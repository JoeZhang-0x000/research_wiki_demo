---
title: Agent Memory Taxonomy
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/shichun-liu-agent-memory-paper-list-the-paper-list-of-memory-2026-04-04.md
links: []
tags: [ai-agents, memory, taxonomy]
---

# Agent Memory Taxonomy

## Definition

Agent Memory Taxonomy is the survey-proposed framework that organizes memory along three lenses: forms (what carries memory), functions (why memory is needed), and dynamics (how memory changes over time).

## Why It Matters

The field uses "memory" to mean many different things. A taxonomy makes it easier to compare systems that store documents, latent state, or long-term profiles without collapsing them into one vague category.

## How It Works

The survey groups memory by:

- **Forms** - token-level, parametric, or latent representations
- **Functions** - [[factual-memory]], [[experiential-memory]], and [[working-memory]]
- **Dynamics** - formation, evolution, and retrieval

## Key Properties / Tradeoffs

- **Comparability**: gives researchers a shared vocabulary.
- **Coverage**: spans both implementation and purpose.
- **Abstraction level**: useful for analysis, but not itself an evaluation metric.

## Related Concepts

- Decomposes into: [[factual-memory]], [[experiential-memory]], [[working-memory]]
- Used in: [[memory-management]]
- Often implemented with: [[hierarchical-memory]]

## Source Basis

- [[summary-agent-memory-survey]] - primary source for the taxonomy.

## Open Questions

- Which taxonomy axis best predicts real-world usefulness for agent systems?
- How should hybrid systems be classified when they span multiple forms at once?
