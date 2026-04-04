---
title: Agent Memory Systems
type: topic
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/adoresever-graph-memory-graph-graph-2026-04-04.md
  - raw/danielwanwx-am-memory-persistent-memory-for-claude-code-2026-04-04.md
  - raw/thread-by-karpathy-2026-04-03.md
links: []
tags: [ai-agents, memory, persistence, retrieval]
---

# Agent Memory Systems

## Scope

This topic covers systems that let agents retain, retrieve, and reuse knowledge across sessions instead of relying only on the current context window. It includes conversation-derived memory, memory promotion policies, retrieval layers, and durable knowledge artifacts such as generated wiki pages.

It excludes short-lived prompt engineering tricks that do not survive beyond a session and large-scale pretraining or finetuning approaches that move knowledge into model weights.

Domain: **AI Agents**

## Subproblems

1. **Capture** — deciding what agent output, user input, or tool traces are worth preserving
2. **Distillation** — compressing raw transcripts into summaries, facts, graph nodes, or documents
3. **Recall** — surfacing relevant memory fast enough to sit in the critical path of an answer
4. **Lifecycle management** — expiring, merging, or promoting memories so the store stays useful
5. **Provenance and trust** — showing where a memory came from and how stale it might be

## Key Approaches

Current systems split mainly by the representation they preserve and the mechanism they use to retrieve it.

### SQLite Document Memory

This approach stores distilled documents in a local database with full-text search and optional embeddings. It favors low operational overhead, quick setup, and simple deployment in local agent environments. [[persistent-agent-memory]] in `am-memory` is a representative example.

### Knowledge Graph Memory

This approach turns conversations into entities, tasks, events, and edges, then ranks them with graph traversal. It aims to preserve relationships between learned facts and past fixes instead of flattening everything into standalone notes. The `graph-memory` source pushes this design toward community-aware and episodic recall.

### Wiki-Backed Memory

Here, memory is maintained as markdown files, summaries, indexes, and concepts that agents can edit and query with normal file tools. This is less specialized than a memory database, but it keeps the representation transparent and reusable. [[markdown-knowledge-base]] describes this substrate.

## Landscape of Systems / Papers

| Name | Year | Key Contribution | Link |
|------|------|------------------|------|
| graph-memory | 2026 | Conversation memory graph with PPR ranking, community-aware recall, and episodic traces | [[summary-graph-memory]] |
| am-memory | 2026 | SQLite-backed persistent memory for Claude Code with BM25, optional vector search, and session promotion | [[summary-am-memory]] |
| Karpathy knowledge-base workflow | 2026 | Markdown wiki compilation loop for research and QA | [[summary-karpathy-knowledge-base-thread]] |

## Important References

- adoresever (2026) — "graph-memory" — [[summary-graph-memory]] — graph-based cross-session recall for OpenClaw
- danielwanwx (2026) — "am-memory" — [[summary-am-memory]] — pragmatic local persistent memory for Claude Code
- Andrej Karpathy (2026) — "Thread by @karpathy" — [[summary-karpathy-knowledge-base-thread]] — outlines the markdown knowledge-base loop that memory systems can build on

## Open Problems

- How should memory systems decide what to preserve automatically without flooding the store with low-signal artifacts?
- How can a system expose stale or conflicting memories before the agent treats them as facts?
- What is the right split between structured memory stores and file-based knowledge bases in coding workflows?

## Related Topics

- [[markdown-knowledge-bases]]
- [[graph-rag-systems]]
