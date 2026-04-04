---
title: Three-Tier Context
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/volcengine-openviking-openviking-is-an-open-source-2026-04-04.md
links: []
tags: [context, hierarchy, ai-agents]
---

# Three-Tier Context

## Definition

Three-tier context is a hierarchical organization where context is stored and retrieved across three abstraction levels rather than as one flat store.

## Why It Matters

A coarse-to-fine layout lets systems cheaply locate relevant regions before loading detailed items, which is especially useful when context includes memories, resources, and skills together.

## How It Works

The OpenViking material describes L0/L1/L2 levels, where higher levels summarize or organize lower-level detail and retrieval can descend as needed.

## Key Properties / Tradeoffs

- **Hierarchy**: strong support for structured retrieval.
- **Scalability**: avoids treating every record as equal.
- **Maintenance**: summaries and lower levels must stay aligned.

## Related Concepts

- Example of: [[hierarchical-memory]]
- Used by: [[context-database]], [[recursive-retrieval]]

## Source Basis

- [[summary-openviking]]

## Open Questions

- What is the best policy for promoting or compressing content across the three levels?
