---
title: Summary — graph-memory
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/adoresever-graph-memory-graph-graph-2026-04-04.md
  - https://github.com/adoresever/graph-memory
tags: [ai-agents, memory, knowledge-graphs, openclaw]
---

# Summary — graph-memory

## Source Metadata

| Field | Value |
|-------|-------|
| Source type | web |
| Author(s) | adoresever |
| Year | 2026 |
| Venue | GitHub repository |
| Raw file | `raw/adoresever-graph-memory-graph-graph-2026-04-04.md` |

## Main Idea

`graph-memory` adds a graph-based context engine to OpenClaw that converts conversations into typed nodes and edges, then recalls relevant prior knowledge through a dual-path retrieval pipeline. The system positions this graph as a way to compress growing histories, preserve cross-session learning, and connect isolated task-specific learnings.

## Key Details

- The graph uses three node types (`TASK`, `SKILL`, `EVENT`) and five edge types (`USED_SKILL`, `SOLVED_BY`, `REQUIRES`, `PATCHES`, `CONFLICTS_WITH`)
- The retrieval pipeline has a precise path that starts from vector or FTS5 matches and a generalized path that starts from community-summary embeddings
- Personalized PageRank ranks nodes relative to the current query instead of using a static global importance score
- Community detection runs periodically and produces summary embeddings so recall can operate at both node and community levels
- The top-ranked nodes can contribute episodic traces, which pull the original conversation snippets that produced them back into context
- The project claims a 7-round conversation drops from 95,187 tokens to 23,977 tokens with graph-memory enabled, roughly 75% compression
- Embeddings are fetched through a raw OpenAI-compatible API path rather than an SDK, broadening provider support

## Method / Approach

The system ingests every message, extracts triples asynchronously after each turn, and periodically runs maintenance jobs such as PageRank, community detection, and deduplication. On the next session, it retrieves candidate nodes through keyword or vector paths, expands through community and graph structure, ranks them with Personalized PageRank, and injects a compact XML-like representation plus selected episodic traces into the prompt.

## Results / Evidence

- The README reports 75% token compression in a seven-round example workflow
- It claims real-time Personalized PageRank runs in about 5 ms for graphs with thousands of nodes
- The system includes a Windows installer and OpenAI-compatible embedding path aimed at reducing deployment friction

## Limitations

- The benchmark evidence is repository-level and example-driven rather than independently reproduced
- Graph extraction and maintenance depend on background LLM calls, so quality and cost depend on model behavior
- The source emphasizes OpenClaw integration; portability to other agent runtimes is suggested but not demonstrated in the raw note

## Links to Concepts

- [[persistent-agent-memory]] — primary example of graph-shaped agent memory
- [[graph-rag]] — retrieval is graph-aware and query-conditioned

## Links to Topics

- [[agent-memory-systems]]
- [[graph-rag-systems]]

## Quotes Worth Preserving

> It feels like talking to an agent that learns from experience.
