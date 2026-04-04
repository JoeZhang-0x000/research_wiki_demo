---
title: Memory Management
type: topic
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/shichun-liu-agent-memory-paper-list-the-paper-list-of-memory-2026-04-04.md
  - raw/mem0ai-mem0-universal-memory-layer-for-ai-2026-04-04.md
  - raw/bai-lab-memoryos-emnlp-oral-memoryos-is-2026-04-04.md
links: []
tags: [ai-agents, memory, retrieval]
---

# Memory Management

## Scope

This topic covers how AI systems store, update, retrieve, compress, and retire information over time. In this wiki it is centered on agent memory rather than hardware memory allocation, though the ideas sometimes borrow language from operating systems.

It excludes transient prompt-only context that is never persisted and excludes GPU/CPU allocator design, which belongs under infrastructure topics.

Domain: **AI Agents**

## Subproblems

1. **Storage layout** - choosing document, graph, hierarchical, or hybrid memory structures.
2. **Promotion and updating** - deciding what becomes durable memory and when it changes.
3. **Retrieval** - finding the right memory fast enough for live interaction.
4. **Lifecycle control** - deduplication, forgetting, consolidation, and rollback.
5. **Evaluation** - measuring whether memory improves outcomes rather than just increasing state.

## Key Approaches

### Document and vector memory

Systems like `am-memory` and Mem0 store promoted artifacts in searchable stores backed by lexical or vector retrieval. This makes memory easy to integrate into existing agent loops.

### Hierarchical and OS-inspired memory

MemoryOS and related work structure memory into tiers with explicit policies for updating and retrieval, borrowing concepts from operating-system memory design.

## Landscape of Systems / Papers

| Name | Year | Key Contribution | Link |
|------|------|------------------|------|
| Agent Memory Survey | 2025 | Taxonomy of memory forms, functions, and dynamics | [[summary-agent-memory-survey]] |
| Mem0 | 2025 | Universal memory layer with multi-level state and search | [[summary-mem0]] |
| MemoryOS | 2025 | Hierarchical memory operating system for personalized agents | [[summary-memoryos-emnlp2025]] |
| am-memory | 2026 | SQLite-backed local persistent memory for Claude Code | [[summary-am-memory]] |

## Important References

- [[summary-agent-memory-survey]] - broad conceptual framing for the area.
- [[summary-mem0]] - production-oriented multi-level memory system.
- [[summary-memoryos-emnlp2025]] - OS-inspired hierarchical design.
- [[summary-am-memory]] - pragmatic local-first implementation.

## Open Problems

- What evaluation setup best measures long-term utility rather than retrieval quality alone?
- How should systems expose stale, conflicting, or low-confidence memories?
- Which memories should stay editable by users versus fully automated?

## Related Topics

- [[agent-memory-systems]]
- [[context-engineering]]
- [[ai-agents]]
