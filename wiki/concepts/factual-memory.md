---
title: Factual Memory
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/shichun-liu-agent-memory-paper-list-the-paper-list-of-memory-2026-04-04.md
  - raw/mem0ai-mem0-universal-memory-layer-for-ai-2026-04-04.md
links: []
tags: [ai-agents, memory]
---

# Factual Memory

## Definition

Factual memory stores declarative knowledge such as user preferences, stable facts, project constraints, or reference information that an agent may need to retrieve later.

## Why It Matters

Many useful agent interactions depend on remembering facts that outlive a single turn. Without a durable factual layer, the system either repeats discovery work or relies on fragile prompt injection.

## How It Works

Facts are extracted from interactions or documents, normalized into a durable representation, and later recovered through keyword, vector, or structured retrieval.

## Key Properties / Tradeoffs

- **Precision**: factual stores should prefer correctness over breadth.
- **Longevity**: facts often persist longer than transient working state.
- **Conflict handling**: stale or contradictory facts require explicit resolution.

## Related Concepts

- Part of: [[agent-memory-taxonomy]]
- Contrasts with: [[experiential-memory]]
- Often retrieved by: [[memory-search]]

## Source Basis

- [[summary-agent-memory-survey]] - taxonomy source.
- [[summary-mem0]] - concrete factual memory system.

## Open Questions

- How should agents represent uncertainty when a remembered fact is old or weakly sourced?
