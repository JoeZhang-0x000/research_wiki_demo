---
title: Recursive Retrieval
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/volcengine-openviking-openviking-is-an-open-source-2026-04-04.md
links: []
tags: [retrieval, ai-agents, hierarchy]
---

# Recursive Retrieval

## Definition

Recursive retrieval is a retrieval strategy that first identifies a broad relevant region and then repeatedly drills into more specific subregions until the needed context is found.

## Why It Matters

Hierarchical stores are hard to query well with one flat lookup. Recursive traversal lets the system stay efficient while preserving structure.

## How It Works

The OpenViking description starts from high-relevance directories, explores subdirectories, and keeps descending until the result is specific enough for the current task.

## Key Properties / Tradeoffs

- **Efficiency**: avoids loading fine-grained detail everywhere.
- **Interpretability**: traversal steps can be inspected.
- **Path dependence**: early routing mistakes can hide relevant leaves.

## Related Concepts

- Used in: [[context-database]], [[three-tier-context]]
- Observable through: [[visualized-retrieval]]

## Source Basis

- [[summary-openviking]]

## Open Questions

- How should recursion stop when retrieval confidence is low but not zero?
