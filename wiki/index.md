---
title: Knowledge Base Index
type: index
updated: 2026-04-04
---

# Research Wiki — Index

Knowledge base covering: **High-Performance Computing**, **AI Infrastructure**, **AI Agents**

---

## Topics

| Topic | Description | Status |
|-------|-------------|--------|
| [[agent-memory-systems]] | Persistent memory layers that let agents retain and recall prior knowledge across sessions | draft |
| [[graph-rag-systems]] | Retrieval systems that combine vector search with explicit graph structure | draft |
| [[gpu-memory-optimization]] | Techniques for reducing GPU memory usage and improving bandwidth utilization | draft |
| [[markdown-knowledge-bases]] | File-native knowledge workflows built from raw markdown sources, summaries, and indexes | draft |

---

## Concepts

This section collects the atomic knowledge units that topic and summary pages build on.

### AI Infra / HPC

| Concept | One-line summary | Status |
|---------|-----------------|--------|
| [[flash-attention]] | IO-aware tiled attention that avoids materializing the N×N attention matrix | stable |
| [[graph-rag]] | Retrieval-augmented generation that uses explicit graph structure during recall | draft |
| [[hbm-bandwidth]] | GPU HBM data transfer rate — primary bottleneck for memory-bound kernels | draft |
| [[markdown-knowledge-base]] | Linked markdown corpus that agents can compile, query, and maintain | draft |
| [[persistent-agent-memory]] | Durable memory layer that preserves useful knowledge across agent sessions | draft |
| [[virtual-filesystem-interface]] | Filesystem-shaped abstraction over indexed or virtualized knowledge stores | draft |

### AI Agents

| Concept | One-line summary | Status |
|---------|-----------------|--------|
| [[mcp-server]] | Model Context Protocol server exposing memory/tools via standard interface | draft |
| [[memory-operating-system]] | OS-inspired hierarchical memory with Storage/Updating/Retrieval/Generation modules | draft |
| [[multi-level-memory]] | Memory architecture with separate user, session, and agent state tiers | draft |

### Candidate Future Pages

The following concepts are useful follow-up pages for expanding the wiki:

- `online-softmax` — linked from [[flash-attention]]
- `sparse-attention` — linked from [[flash-attention]]
- `collective-communication` — linked from [[gpu-memory-optimization]]
- `transformer-training-infrastructure` — linked from [[flash-attention]]
- `roofline-model` — linked from [[hbm-bandwidth]]

---

## Summaries

| Summary | Source | Topic |
|---------|--------|-------|
| [[summary-am-memory]] | am-memory repository (danielwanwx, 2026) | [[agent-memory-systems]] |
| [[summary-claude-code-sourcemap]] | claude-code-sourcemap (leeyeel, 2026) | [[agent-memory-systems]] |
| [[summary-deer-flow]] | DeerFlow repository (bytedance, 2026) | [[agent-memory-systems]] |
| [[summary-edgequake]] | EdgeQuake repository (raphaelmansuy, 2026) | [[graph-rag-systems]] |
| [[summary-flashattention2]] | FlashAttention-2 paper (Dao, ICLR 2024) | [[gpu-memory-optimization]] |
| [[summary-graph-memory]] | graph-memory repository (adoresever, 2026) | [[agent-memory-systems]] |
| [[summary-karpathy-knowledge-base-thread]] | Karpathy thread on LLM knowledge bases (2026) | [[markdown-knowledge-bases]] |
| [[summary-mem0]] | mem0 repository (mem0ai, 2026) | [[agent-memory-systems]] |
| [[summary-memoryos-emnlp2025]] | MemoryOS paper (BAI-LAB, EMNLP 2025) | [[agent-memory-systems]] |
| [[summary-mintlify-virtual-filesystem]] | Mintlify virtual filesystem writeup (2026) | [[markdown-knowledge-bases]] |
| [[summary-oh-my-openagent]] | oh-my-openagent repository (code-yeongyuoh, 2026) | [[agent-memory-systems]] |
| [[summary-open-harness]] | open-harness repository (MaxGfeller, 2026) | [[agent-memory-systems]] |
| [[summary-opencode]] | opencode repository (anomalyco, 2026) | [[agent-memory-systems]] |
| [[summary-openviking]] | OpenViking repository (volcengine, 2026) | [[agent-memory-systems]] |

---

## How to Navigate

- Start from a **topic** page for a broad overview of an area
- Drill into **concept** pages for precise definitions and mechanistic explanations
- Read **summary** pages for per-paper notes with results and limitations
- Use Obsidian's graph view to see link clusters

---

## Recently Updated

- 2024-01-15 — [[flash-attention]] created (stable)
- 2024-01-15 — [[hbm-bandwidth]] created (draft)
- 2024-01-15 — [[gpu-memory-optimization]] created (draft)
- 2024-01-15 — [[summary-flashattention2]] created (stable)
- 2026-04-04 — [[agent-memory-systems]] created (draft)
- 2026-04-04 — [[graph-rag-systems]] created (draft)
- 2026-04-04 — [[markdown-knowledge-bases]] created (draft)
- 2026-04-04 — [[persistent-agent-memory]] created (draft)
- 2026-04-04 — [[markdown-knowledge-base]] created (draft)
- 2026-04-04 — [[virtual-filesystem-interface]] created (draft)
- 2026-04-04 — [[graph-rag]] created (draft)
- 2026-04-04 — [[summary-mintlify-virtual-filesystem]] created (draft)
- 2026-04-04 — [[summary-karpathy-knowledge-base-thread]] created (draft)
- 2026-04-04 — [[summary-graph-memory]] created (draft)
- 2026-04-04 — [[summary-am-memory]] created (draft)
- 2026-04-04 — [[summary-edgequake]] created (draft)
- 2026-04-04 — [[summary-memoryos-emnlp2025]] created (draft)
- 2026-04-04 — [[summary-open-harness]] created (draft)
- 2026-04-04 — [[summary-agent-memory-survey]] created (draft)
- 2026-04-04 — [[summary-opencode]] created (draft)
- 2026-04-04 — [[summary-deer-flow]] created (draft)
- 2026-04-04 — [[summary-oh-my-openagent]] created (draft)
- 2026-04-04 — [[summary-claude-code-sourcemap]] created (draft)
- 2026-04-04 — [[summary-mem0]] created (draft)
- 2026-04-04 — [[summary-openviking]] created (draft)
- 2026-04-04 — [[mcp-server]] created (draft)
- 2026-04-04 — [[memory-operating-system]] created (draft)
- 2026-04-04 — [[multi-level-memory]] created (draft)
