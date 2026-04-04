---
title: "Summary — BAI-LAB/MemoryOS: [EMNLP 2025 Oral] MemoryOS"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/BAI-LABMemoryOS EMNLP 2025 Oral MemoryOS is designed to provide a memory operating system for personalized AI agents..md
  - https://arxiv.org/abs/2506.06326
tags: []
---

# Summary — BAI-LAB/MemoryOS: [EMNLP 2025 Oral] MemoryOS

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | web / github / paper           |
| Author(s)    | BAI-LAB (Beijing AI Lab)       |
| Year         | 2025                           |
| Venue        | EMNLP 2025 (Oral)             |
| Raw file     | `raw/BAI-LABMemoryOS EMNLP 2025 Oral MemoryOS is designed to provide a memory operating system for personalized AI agents..md` |

## Main Idea

MemoryOS provides a hierarchical memory operating system for personalized AI agents, adopting four core modules—Storage, Updating, Retrieval, and Generation—modelled after OS memory management principles, achieving 49.11% F1 and 46.18% BLEU-1 improvement on the LoCoMo benchmark.

## Key Details

- **Architecture**: Four core modules—Storage (hierarchical levels), Updating (dynamic memory refresh), Retrieval (context-aware recall), Generation (memory-informed synthesis)
- **Memory levels**: Short-term, mid-term, and long-term persona memory with automated user profile and knowledge updating
- **Benchmark**: LoCoMo benchmark—49.11% F1 improvement and 46.18% BLEU-1 improvement over baseline
- **Speed**: 5x latency reduction via parallelization optimizations in the PyPI implementation
- **Supported models**: GPT-4/3.5, Claude series, DeepSeek-R1, Qwen/Qwen3, vLLM, Llama_factory (all via OpenAI API interface)
- **Agent clients**: Claude Desktop, Cline, Cursor
- **MCP support**: MemoryOS-MCP server for injecting long-term memory into AI applications
- **Vector DB**: ChromaDB integration for storage backend
- **Deployments**: Docker-supported for containerized deployment
- **Playground**: Interactive platform available at baijia.online/memoryos/

## Method / Approach

MemoryOS draws from operating system memory management principles to design a hierarchical storage architecture for AI agents. The system treats memory as a first-class OS-level primitive with four coordinated modules:

1. **Storage Module**: Organizes memories hierarchically (short/mid/long-term)
2. **Updating Module**: Dynamically refreshes user profiles and knowledge based on interactions
3. **Retrieval Module**: Context-aware memory recall tuned to current conversation state
4. **Generation Module**: Synthesizes responses informed by retrieved memory

The MCP server (MemoryOS-MCP) exposes modular tools for easy integration into existing agent frameworks.

## Results / Evidence

- **LoCoMo benchmark**: +49.11% F1 score, +46.18% BLEU-1 over baseline
- **Speed**: 5x faster PyPI implementation through parallelization
- **OpenViking comparison**: OpenViking's LoCoMo results (52.08% task completion rate) suggest the field is converging on this benchmark for memory system evaluation

## Limitations

- Tightly coupled to the OpenAI API interface for model calls—provider flexibility is achieved through API key configuration but the calling convention is uniform
- Memory updating strategies are automated but not fully transparent to the user; the self-evolution loop may accumulate biased or incorrect memories over time without easy rollback
- Evaluation is primarily on LoCoMo; generalization to other benchmarks is [UNVERIFIED]

## Links to Concepts

- [[Memory Operating System]] — MemoryOS is a concrete realization of OS-inspired memory hierarchy for agents
- [[Hierarchical Memory]] — short/mid/long-term tiers directly map to this concept
- [[EMNLP 2025]] — published at EMNLP 2025 Oral, indicating peer-reviewed acceptance
- [[MCP Server]] — MemoryOS-MCP exposes agent memory via Model Context Protocol

## Links to Topics

- [[AI Agents]]
- [[High-Performance Computing]] (benchmark performance, parallelization)
- [[Memory Management]]

## Quotes Worth Preserving

> MemoryOS is designed to provide a memory operating system for personalized AI agents, enabling more coherent, personalized, and context-aware interactions. Drawing inspiration from memory management principles in operating systems, it adopts a hierarchical storage architecture with four core modules: Storage, Updating, Retrieval, and Generation.
