---
title: Summary — EdgeQuake
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/raphaelmansuy-edgequake-high-performance-graphrag-inspired-from-2026-04-04.md
  - "https://github.com/raphaelmansuy/edgequake"
links:
  - "https://github.com/raphaelmansuy/edgequake"
tags: [ai-infra, graph-rag, rust, retrieval]
---

# Summary — EdgeQuake

## Source Metadata

| Field | Value |
|-------|-------|
| Source type | web |
| Author(s) | raphaelmansuy |
| Year | 2026 |
| Venue | GitHub repository |
| Raw file | `raw/raphaelmansuy-edgequake-high-performance-graphrag-inspired-from-2026-04-04.md` |

## Main Idea

EdgeQuake is a Rust implementation of a LightRAG-style GraphRAG system that combines entity and relationship extraction, graph traversal, and vector retrieval in a production-oriented service stack. Its main claim is that graph structure improves retrieval for relationship-heavy and multi-hop questions while Rust and a modular backend keep the system fast and operationally tractable.

## Key Details

- The system extracts entities and relationships from documents and supports six query modes: naive, local, global, hybrid, mix, and bypass
- The backend is described as async-first and built around Rust crates for API serving, pipeline orchestration, storage, querying, PDF extraction, auth, audit, and task processing
- Storage combines PostgreSQL AGE for graph data and `pgvector` for embeddings, with metadata pre-filtering pushed into SQL
- Community detection, multi-pass gleaning, and configurable entity types are used to improve graph quality and domain adaptation
- A production-focused PDF pipeline supports both text extraction and multimodal vision-based page reading for scanned or layout-heavy PDFs
- The frontend exposes graph visualization, document upload, and query interfaces, and the project also ships an MCP integration surface for agents
- The README reports benchmark-style claims such as sub-200 ms hybrid query latency and 2-3x more entity extraction than traditional RAG baselines

## Method / Approach

Documents are ingested, chunked, embedded, and passed through LLM-powered entity and relationship extraction to populate a graph-backed retrieval layer. Query handling can then combine vector similarity, local neighborhood expansion, community-level retrieval, and hybrid ranking depending on the selected mode. The architecture is presented as a full-stack GraphRAG product rather than a narrow research prototype.

## Results / Evidence

- The source reports hybrid query latency below 200 ms and document processing around 25 seconds for a 10K-token document
- It claims support for 1000+ concurrent users and around 4x lower memory usage per document than the named traditional baseline
- The repository emphasizes production packaging features such as OpenAPI docs, SSE streaming, health endpoints, and tenant/workspace isolation

## Limitations

- The README-level performance numbers are not accompanied in the raw note by detailed benchmark methodology
- The system depends on multiple heavyweight components, including PostgreSQL, graph extensions, embeddings, and LLM extraction
- The breadth of features means the operational simplicity is lower than in local-first or file-native approaches

## Links to Concepts

- [[graph-rag]] — primary document-centric example
- [[persistent-agent-memory]] — related because graph retrieval patterns overlap with memory systems

## Links to Topics

- [[graph-rag-systems]]

## Quotes Worth Preserving

> vectors capture semantic similarity but lose structural relationships between concepts
