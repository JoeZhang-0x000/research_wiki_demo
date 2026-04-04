---
title: Context Engineering
type: topic
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/shichun-liu-agent-memory-paper-list-the-paper-list-of-memory-2026-04-04.md
  - raw/bytedance-deer-flow-an-open-source-long-horizon-2026-04-04.md
  - raw/building-a-virtual-filesystem-for-mintlifys-2026-04-03.md
links: []
tags: [ai-agents, context, retrieval, prompting]
---

# Context Engineering

## Scope

This topic covers how agent systems decide what information enters the model context, in what format, and at what time. It includes retrieval, summarization, memory recall, filesystem projections, and other mechanisms used to keep the active prompt useful under token constraints.

It excludes prompt-style advice that does not materially change the runtime data flow into the model.

Domain: **AI Agents**

## Subproblems

1. **Selection** - choosing which facts, files, and memories are worth injecting.
2. **Compression** - summarizing or distilling large state into a smaller prompt footprint.
3. **Projection** - exposing external state as files, tools, or structured memory calls.
4. **Freshness** - avoiding stale or conflicting context.
5. **Observability** - understanding why a context assembly produced a given answer.

## Key Approaches

### Retrieval-backed context

The system looks up relevant documents, graph nodes, or memories on demand and injects only the highest-value subset. Agent memory systems and GraphRAG pipelines both operate this way.

### Filesystem-shaped context

Instead of only returning top-k chunks, the runtime exposes knowledge through directories, files, and browseable abstractions. Mintlify's virtual filesystem and several markdown-wiki workflows demonstrate this pattern.

## Landscape of Systems / Papers

| Name | Year | Key Contribution | Link |
|------|------|------------------|------|
| Agent Memory Survey | 2025 | Frames memory as adjacent to, but distinct from, context engineering | [[summary-agent-memory-survey]] |
| DeerFlow | 2026 | Aggressive context summarization and skill-based offloading | [[summary-deer-flow]] |
| Mintlify ChromaFs | 2026 | Virtual filesystem projection for agent browsing | [[summary-mintlify-virtual-filesystem]] |

## Important References

- [[summary-agent-memory-survey]] - useful for distinguishing memory from context assembly.
- [[summary-deer-flow]] - concrete harness example where context is actively managed.
- [[summary-mintlify-virtual-filesystem]] - shows a filesystem-style projection of indexed knowledge.

## Open Problems

- How much retrieved context should remain inspectable to users and operators?
- What makes a context projection browseable for agents rather than just token-efficient?
- How should systems surface uncertainty when retrieved context conflicts?

## Related Topics

- [[ai-agents]]
- [[memory-management]]
- [[markdown-knowledge-bases]]
