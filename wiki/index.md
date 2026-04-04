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
| [[ai-agents]] | Runtime and workflow patterns for autonomous systems that plan, use tools, and manage state | draft |
| [[coding-agents]] | Agent systems specialized for navigating, editing, and executing against codebases | draft |
| [[context-engineering]] | Techniques for selecting, compressing, and projecting context into model prompts | draft |
| [[graph-rag-systems]] | Retrieval systems that combine vector search with explicit graph structure | draft |
| [[gpu-memory-optimization]] | Techniques for reducing GPU memory usage and improving bandwidth utilization | draft |
| [[high-performance-computing]] | Hardware-aware performance work across AI infrastructure and memory-heavy systems | draft |
| [[markdown-knowledge-bases]] | File-native knowledge workflows built from raw markdown sources, summaries, and indexes | draft |
| [[memory-management]] | Storage, updating, retrieval, and lifecycle control for agent memory systems | draft |

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
| [[agent-frameworks]] | Runtime architectures combining LLM with tools, state, and execution policies | draft |
| [[agent-harness]] | Runtime layer that combines model, tools, state, and execution policy into an agent | draft |
| [[closed-loop-control]] | Control architecture where agents continuously observe and update based on feedback | draft |
| [[meta-harness]] | Harness that optimizes other harnesses via full-history filesystem access | draft |
| [[model-harness]] | Evaluation scaffolding (prompting, tools, context) surrounding a fixed LLM | draft |
| [[terminalbench]] | Benchmark for agentic coding tasks in terminal/shell environments | draft |
| [[claude-code]] | Terminal-native coding agent used as a reference point by several open-source projects | draft |
| [[context-database]] | Context store built around agent browseability rather than flat retrieval only | draft |
| [[discipline-agents]] | Specialized agent roles used inside a coordinated multi-agent workflow | draft |
| [[hashline-edit-tool]] | Content-addressed editing approach that guards against stale-line changes | draft |
| [[hierarchical-memory]] | Multi-tier memory layout that separates state by lifetime and retrieval cost | draft |
| [[locomo-benchmark]] | Shared benchmark reference used by several agent-memory systems in this repo | draft |
| [[long-term-memory]] | Durable memory that persists useful knowledge across sessions | draft |
| [[lsp-integration]] | Language Server Protocol support for semantic code navigation and refactoring | draft |
| [[mem0]] | Productized agent-memory system with multi-level memory and search APIs | draft |
| [[memgpt]] | Foundational literature reference for OS-style memory thinking in agents | draft |
| [[memory-search]] | Retrieval step that finds relevant stored memories for the current task | draft |
| [[mcp-server]] | Model Context Protocol server exposing memory/tools via standard interface | draft |
| [[middleware-pattern]] | Composable runtime layers for retries, compaction, and related concerns | draft |
| [[memory-operating-system]] | OS-inspired hierarchical memory with Storage/Updating/Retrieval/Generation modules | draft |
| [[multi-level-memory]] | Memory architecture with separate user, session, and agent state tiers | draft |
| [[openclaw]] | Agent framework used as a host runtime for memory plugins in several sources | draft |
| [[provider-agnostic-agents]] | Agents designed to work across multiple model providers or local backends | draft |
| [[recursive-retrieval]] | Retrieval strategy that drills from coarse context regions to finer detail | draft |
| [[self-evolving-memory]] | Memory that is continuously updated, consolidated, or reorganized over time | draft |
| [[session-management]] | Handling multi-turn state, compaction, and persistence boundaries | draft |
| [[skill-embedded-mcps]] | MCP servers loaded on demand as part of a skill package | draft |
| [[skills-system]] | Modular task-specific instruction and capability packages for agents | draft |
| [[source-map-reverse-engineering]] | Recovering source trees from shipped bundles and source maps | draft |
| [[sub-agent-orchestration]] | Delegating bounded work to multiple narrower agents | draft |
| [[superagent-harness]] | Orchestration-heavy harness for long-horizon, multi-stage tasks | draft |
| [[sandbox-isolation]] | Constraining agent execution inside limited environments | draft |
| [[three-tier-context]] | Three-level context hierarchy for coarse-to-fine retrieval | draft |
| [[tool-use]] | Calling external tools such as shell, files, search, or MCP servers | draft |
| [[ultrawork]] | Aggressive multi-agent completion mode aimed at preventing premature stopping | draft |
| [[universal-memory-layer]] | Shared memory abstraction between applications and model calls | draft |
| [[visualized-retrieval]] | Inspectable view of the path a retrieval system took | draft |

### Agent Memory

| Concept | One-line summary | Status |
|---------|-----------------|--------|
| [[agent-memory-taxonomy]] | Survey taxonomy organizing memory by forms, functions, and dynamics | draft |
| [[experiential-memory]] | Stored lessons, procedures, and reusable know-how from prior work | draft |
| [[factual-memory]] | Durable store of preferences, constraints, and other declarative facts | draft |
| [[working-memory]] | Actively maintained task state used in the current interaction | draft |

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
| [[summary-agent-memory-survey]] | "Memory in the Age of AI Agents" survey repo (Shichun-Liu, 2025) | [[memory-management]] |
| [[summary-claude-code-sourcemap]] | claude-code-sourcemap (leeyeel, 2026) | [[agent-memory-systems]] |
| [[summary-deer-flow]] | DeerFlow repository (bytedance, 2026) | [[agent-memory-systems]] |
| [[summary-edgequake]] | EdgeQuake repository (raphaelmansuy, 2026) | [[graph-rag-systems]] |
| [[summary-flashattention2]] | FlashAttention-2 paper (Dao, ICLR 2024) | [[gpu-memory-optimization]] |
| [[summary-graph-memory]] | graph-memory repository (adoresever, 2026) | [[agent-memory-systems]] |
| [[summary-karpathy-knowledge-base-thread]] | Karpathy thread on LLM knowledge bases (2026) | [[markdown-knowledge-bases]] |
| [[summary-thread-by-lijigang]] | Thread on whether agent frameworks are necessary (2026) | [[ai-agents]] |
| [[summary-mem0]] | mem0 repository (mem0ai, 2026) | [[agent-memory-systems]] |
| [[summary-memoryos-emnlp2025]] | MemoryOS paper (BAI-LAB, EMNLP 2025) | [[agent-memory-systems]] |
| [[summary-mintlify-virtual-filesystem]] | Mintlify virtual filesystem writeup (2026) | [[markdown-knowledge-bases]] |
| [[summary-oh-my-openagent]] | oh-my-openagent repository (code-yeongyuoh, 2026) | [[agent-memory-systems]] |
| [[summary-open-harness]] | open-harness repository (MaxGfeller, 2026) | [[agent-memory-systems]] |
| [[summary-opencode]] | opencode repository (anomalyco, 2026) | [[agent-memory-systems]] |
| [[summary-openviking]] | OpenViking repository (volcengine, 2026) | [[agent-memory-systems]] |
| [[summary-thread-by-omarsar0]] | Stanford/MIT paper on Meta-Harness automated harness engineering (2026) | [[ai-agents]] |
| [[summary-claude-code-hooks]] | Claude Code hooks thread (zodchiii, 2026) | [[coding-agents]] |
| [[summary-anthropic-diff-tool]] | Anthropic model diffing research (2026) | [[ai-agents]] |
| [[summary-thread-by-yoonholeee]] | Meta-Harness author announcement thread (2026) | [[ai-agents]] |
| [[summary-perplexica]] | Perplexica search engine (BunsDev, 2026) | [[ai-agents]] |
| [[summary-nvidia-llm-router]] | NVIDIA LLM Router blueprint (2026) | [[ai-agents]] |

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
- 2026-04-04 — [[ai-agents]] created (draft)
- 2026-04-04 — [[coding-agents]] created (draft)
- 2026-04-04 — [[context-engineering]] created (draft)
- 2026-04-04 — [[graph-rag-systems]] created (draft)
- 2026-04-04 — [[high-performance-computing]] created (draft)
- 2026-04-04 — [[markdown-knowledge-bases]] created (draft)
- 2026-04-04 — [[memory-management]] created (draft)
- 2026-04-04 — [[agent-harness]] created (draft)
- 2026-04-04 — [[agent-memory-taxonomy]] created (draft)
- 2026-04-04 — [[claude-code]] created (draft)
- 2026-04-04 — [[context-database]] created (draft)
- 2026-04-04 — [[discipline-agents]] created (draft)
- 2026-04-04 — [[experiential-memory]] created (draft)
- 2026-04-04 — [[factual-memory]] created (draft)
- 2026-04-04 — [[filesystem-paradigm]] created (draft)
- 2026-04-04 — [[hashline-edit-tool]] created (draft)
- 2026-04-04 — [[hierarchical-memory]] created (draft)
- 2026-04-04 — [[locomo-benchmark]] created (draft)
- 2026-04-04 — [[long-term-memory]] created (draft)
- 2026-04-04 — [[lsp-integration]] created (draft)
- 2026-04-04 — [[mem0]] created (draft)
- 2026-04-04 — [[memgpt]] created (draft)
- 2026-04-04 — [[memory-search]] created (draft)
- 2026-04-04 — [[middleware-pattern]] created (draft)
- 2026-04-04 — [[persistent-agent-memory]] created (draft)
- 2026-04-04 — [[openclaw]] created (draft)
- 2026-04-04 — [[provider-agnostic-agents]] created (draft)
- 2026-04-04 — [[recursive-retrieval]] created (draft)
- 2026-04-04 — [[sandbox-isolation]] created (draft)
- 2026-04-04 — [[self-evolving-memory]] created (draft)
- 2026-04-04 — [[session-management]] created (draft)
- 2026-04-04 — [[skill-embedded-mcps]] created (draft)
- 2026-04-04 — [[skills-system]] created (draft)
- 2026-04-04 — [[source-map-reverse-engineering]] created (draft)
- 2026-04-04 — [[sub-agent-orchestration]] created (draft)
- 2026-04-04 — [[superagent-harness]] created (draft)
- 2026-04-04 — [[three-tier-context]] created (draft)
- 2026-04-04 — [[tool-use]] created (draft)
- 2026-04-04 — [[ultrawork]] created (draft)
- 2026-04-04 — [[universal-memory-layer]] created (draft)
- 2026-04-04 — [[visualized-retrieval]] created (draft)
- 2026-04-04 — [[working-memory]] created (draft)
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
