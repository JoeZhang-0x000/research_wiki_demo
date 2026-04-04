---
title: "Summary — Shichun-Liu/Agent-Memory-Paper-List: Memory in the Age of AI Agents Survey"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/shichun-liu-agent-memory-paper-list-the-paper-list-of-memory-2026-04-04.md
  - "https://arxiv.org/abs/2512.13564"
links:
  - "https://github.com/Shichun-Liu/Agent-Memory-Paper-List"
tags: []
---

# Summary — Shichun-Liu/Agent-Memory-Paper-List: Memory in the Age of AI Agents Survey

## Source Metadata

| Field        | Value                                                                           |
|--------------|---------------------------------------------------------------------------------|
| Source type  | paper / github repository                                                       |
| Author(s)    | Yuyang Hu, Shichun Liu, Yanwei Yue, et al. (large author list)                |
| Year         | 2025                                                                            |
| Venue        | arXiv (2512.13564); Huggingface Daily Paper #1 on 2025-12-16                  |
| Raw file     | `raw/shichun-liu-agent-memory-paper-list-the-paper-list-of-memory-2026-04-04.md` |

## Main Idea

This repository compiles "Memory in the Age of AI Agents: A Survey"—a comprehensive taxonomy of agent memory organized through three unified lenses: **Forms** (what carries memory: token-level, parametric, latent), **Functions** (why agents need memory: factual, experiential, working), and **Dynamics** (how memory evolves: formation, evolution, retrieval). It also maintains an extensive paper list categorizing 200+ works under this taxonomy.

## Key Details

**Core Taxonomy**:

- **Forms** (What Carries Memory?):
  - Token-level (explicit & discrete) — memories stored as text tokens
  - Parametric (implicit weights) — memories encoded in model parameters
  - Latent (hidden states) — memories in activation space

- **Functions** (Why Agents Need Memory?):
  - Factual — knowledge storage and retrieval
  - Experiential — insights, skills, and learned procedures
  - Working Memory — active context management for ongoing tasks

- **Dynamics** (How Memory Evolves?):
  - Formation (extraction from interactions)
  - Evolution (consolidation and forgetting)
  - Retrieval (access strategies)

**Notable Related Work Catalogued**:
- Mem0 (mem0ai) — production-ready scalable long-term memory
- MemGPT (2023) — "LLMs as Operating Systems"
- HippoRAG (2024) — neurobiologically inspired long-term memory
- A-MEM (2025) — agentic memory for LLM agents
- Zep (2025) — temporal knowledge graph for agent memory
- O-Mem (2025) — omni memory system for personalized self-evolving agents
- EverMemOS (2026) — self-organizing memory OS for structured long-horizon reasoning

**Survey stats**: 1k+ GitHub stars; featured on Huggingface Daily Paper #1 (Dec 2025).

## Method / Approach

The survey distinguishes Agent Memory from related concepts (RAG, Context Engineering) and provides a conceptual foundation for treating memory as a first-class primitive in agentic intelligence. The paper list is organized by the taxonomy and maintained as a living repository updated with new works.

## Results / Evidence

The survey itself is a literature synthesis; no novel empirical results are reported. The paper list provides quantitative evidence of the field's growth (200+ papers as of early 2026).

## Limitations

- The taxonomy, while comprehensive, is a organizational choice rather than a formal evaluation framework
- Many papers are preprints; quality varies
- The rapid pace of new work (2026 papers already included) means the survey will require continuous updates

## Links to Concepts

- [[agent-memory-taxonomy]] — the three-axis taxonomy (Forms × Functions × Dynamics) is the central conceptual contribution
- [[factual-memory]] — token-level memory for knowledge
- [[experiential-memory]] — memory of insights and skills
- [[working-memory]] — active context management
- [[mem0]] — listed as a key related system
- [[memgpt]] — cited as foundational work ("LLMs as Operating Systems")
- [[hierarchical-memory]] — multiple memory tiers appear throughout the taxonomy

## Links to Topics

- [[ai-agents]]
- [[memory-management]]

## Quotes Worth Preserving

> Memory serves as the cornerstone of foundation model-based agents, underpinning their ability to perform long-horizon reasoning, adapt continually, and interact effectively with complex environments.

> We distinguish Agent Memory from related concepts like RAG and Context Engineering, and provide a comprehensive overview through three unified lenses: Forms, Functions, and Dynamics.
