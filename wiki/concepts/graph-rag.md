---
title: Graph RAG
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/raphaelmansuy-edgequake-high-performance-graphrag-inspired-from-2026-04-04.md
  - raw/adoresever-graph-memory-graph-graph-2026-04-04.md
links: []
tags: [ai-infra, ai-agents, retrieval, knowledge-graphs, rag]
---

# Graph RAG

## Definition

Graph RAG is a retrieval-augmented generation pattern that supplements vector or keyword retrieval with an explicit graph of entities, relationships, or communities extracted from source data. Instead of retrieving only isolated chunks, it uses graph structure to recover connected context for multi-hop or relationship-heavy questions.

## Why It Matters

Pure vector retrieval is often good at semantic similarity but weak at preserving how concepts relate to one another. Graph RAG addresses that gap by making entities and edges first-class retrieval objects, which can improve thematic exploration, relationship queries, and memory recall across related events. It appears both in [[graph-rag-systems]] and in graph-based variants of [[persistent-agent-memory]].

## How It Works

Most Graph RAG pipelines in the sources follow a common sequence:

1. Split documents or conversations into processable units
2. Use an LLM or extraction pipeline to identify entities, events, skills, or relationships
3. Store those results in a graph structure, often alongside vector and full-text indexes
4. At query time, retrieve seed nodes through vector or keyword search
5. Expand through graph neighbors, communities, or ranked traversals
6. Merge graph-derived context with source passages before generation

The two examples emphasize different variants:

- **Document graph retrieval** in EdgeQuake, which maps documents into entities and relationships for multi-mode querying
- **Conversation memory graphs** in graph-memory, which rank task, skill, and event nodes with Personalized PageRank

## Key Properties / Tradeoffs

- **Relational recall**: helps answer queries that depend on links between concepts rather than one matching chunk
- **Extraction cost**: graph construction can require repeated LLM passes and maintenance jobs
- **Explainability**: explicit entities and edges can make retrieval paths easier to inspect
- **Freshness burden**: graphs drift if source documents or codebases change but extraction artifacts do not
- **Hybrid dependence**: many practical systems still rely on vector or full-text retrieval for good seed selection

## Related Concepts

- System area: [[graph-rag-systems]]
- Applied to memory in: [[persistent-agent-memory]]
- Can be exposed through: [[virtual-filesystem-interface]]

## Source Basis

- [[summary-edgequake]] — LightRAG-inspired Rust system for document retrieval
- [[summary-graph-memory]] — graph-based conversation memory and recall

## Open Questions

- Which graph construction strategies are robust enough for production corpora without excessive LLM cost?
- How should graph retrieval quality be evaluated relative to strong hybrid vector baselines?
- When is community-level retrieval more useful than node-level retrieval for real user questions?
