---
title: Persistent Agent Memory
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/adoresever-graph-memory-graph-graph-2026-04-04.md
  - raw/danielwanwx-am-memory-persistent-memory-for-claude-code-2026-04-04.md
  - raw/thread-by-karpathy-2026-04-03.md
links: []
tags: [ai-agents, memory, recall, knowledge-management]
---

# Persistent Agent Memory

## Definition

Persistent agent memory is a storage and retrieval layer that preserves knowledge learned during one agent session and makes relevant portions of it available in later sessions. It sits outside the transient prompt context and turns prior conversations, extracted facts, or derived documents into reusable state.

## Why It Matters

Without persistent memory, coding and research agents repeatedly relearn the same constraints, fixes, and domain facts. Persistent memory reduces repeated explanation cost, supports cross-session continuity, and makes agents behave more like systems that accumulate experience over time. It is a core building block in [[agent-memory-systems]] and often interacts with [[markdown-knowledge-base]] workflows.

## How It Works

Most systems in this category combine three steps:

1. Capture new information from conversations, tool use, or edited files
2. Distill that information into a more searchable representation such as summaries, facts, graph nodes, or documents
3. Retrieve and inject only the most relevant memories for the current task

Two common design patterns show up in the sources:

- **Document-centric memory**: systems like `am-memory` store promoted session summaries and searchable documents in SQLite, then use BM25 and optional vector search for recall
- **Graph-centric memory**: systems like `graph-memory` extract typed nodes and edges from conversations, then rank them with query-conditioned graph traversal

Many implementations also separate short-lived working memory from long-term memory. Working memory tracks the current task or scratchpad, while long-term memory stores decisions, solutions, and durable facts.

## Key Properties / Tradeoffs

- **Recall quality**: richer structures such as knowledge graphs can capture relationships, but they cost more to extract and maintain
- **Latency**: retrieval must stay cheap enough to run before answering, which favors local stores and staged recall pipelines
- **Compaction**: summarization or graph extraction reduces token growth, but can lose nuance compared with raw transcripts
- **Durability policy**: TTL, priority tiers, or promotion rules are needed so the memory store does not become noisy
- **Faithfulness**: episodic traces or source links help recover the original context when distilled memories are too abstract

## Related Concepts

- Used in: [[agent-memory-systems]]
- Often built over: [[markdown-knowledge-base]]
- Retrieval-heavy variant: [[graph-rag]]

## Source Basis

- [[summary-graph-memory]] — graph-based persistent memory for OpenClaw
- [[summary-am-memory]] — SQLite-backed persistent memory for Claude Code
- [[summary-karpathy-knowledge-base-thread]] — wiki-style accumulation as a broader memory pattern

## Open Questions

- What promotion rules best balance long-term retention against memory pollution?
- When does graph-based recall outperform document-based recall enough to justify the added extraction cost?
- How should persistent memory systems expose confidence and provenance to avoid replaying stale or wrong conclusions?
