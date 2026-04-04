---
title: Graph RAG Systems
type: topic
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/raphaelmansuy-edgequake-high-performance-graphrag-inspired-from-2026-04-04.md
  - raw/adoresever-graph-memory-graph-graph-2026-04-04.md
links: []
tags: [ai-infra, ai-agents, graph-rag, retrieval, knowledge-graphs]
---

# Graph RAG Systems

## Scope

This topic covers retrieval systems that combine vector or keyword retrieval with explicit graphs of entities, events, communities, or relationships extracted from source material. It spans document-centric GraphRAG as well as graph-shaped memory systems used by agents.

It excludes plain vector RAG systems that never build or query graph structure and excludes graph databases used only for storage without retrieval-time graph reasoning.

Domain: **AI Infra + AI Agents**

## Subproblems

1. **Graph construction** — extracting entities and relationships from documents or conversations
2. **Seed retrieval** — finding strong starting points for graph expansion using vector or lexical search
3. **Traversal and ranking** — deciding which neighbors, communities, or paths should enter the final context
4. **Hybrid answer assembly** — combining graph-derived structure with faithful source passages
5. **Operational cost** — keeping extraction, indexing, and query latency within production limits

## Key Approaches

The current landscape divides mostly by what the graph represents and where it sits in the retrieval loop.

### Document GraphRAG

This family builds knowledge graphs from document corpora and queries both graph structure and embeddings at answer time. EdgeQuake follows this pattern with multiple retrieval modes, graph extraction, community detection, and a graph-aware query engine around a Rust backend.

### Memory Graphs

This variant builds the graph from conversations and tool traces rather than static documents. The retrieved objects are tasks, skills, failures, or communities of prior experience. In the sources, `graph-memory` uses Personalized PageRank and community summaries to rank relevant memory for the next session.

## Landscape of Systems / Papers

| Name | Year | Key Contribution | Link |
|------|------|------------------|------|
| EdgeQuake | 2026 | Rust GraphRAG system with six query modes, graph extraction, and production-oriented API surface | [[summary-edgequake]] |
| graph-memory | 2026 | Graph-based persistent memory with dual-path recall and episodic traces | [[summary-graph-memory]] |

## Important References

- raphaelmansuy (2026) — "edgequake" — [[summary-edgequake]] — high-performance GraphRAG implementation inspired by LightRAG
- adoresever (2026) — "graph-memory" — [[summary-graph-memory]] — demonstrates graph retrieval in a memory rather than document setting

## Open Problems

- How should teams benchmark GraphRAG quality against strong hybrid retrieval systems without overstating graph benefits?
- Which parts of graph extraction can be made deterministic enough for production data pipelines?
- What graph abstractions remain legible to downstream agents instead of becoming another opaque intermediate layer?

## Related Topics

- [[agent-memory-systems]]
- [[markdown-knowledge-bases]]
