---
title: LOCOMO Benchmark
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/mem0ai-mem0-universal-memory-layer-for-ai-2026-04-04.md
  - raw/bai-lab-memoryos-emnlp-oral-memoryos-is-2026-04-04.md
  - raw/volcengine-openviking-openviking-is-an-open-source-2026-04-04.md
links: []
tags: [ai-agents, benchmark, memory]
---

# LOCOMO Benchmark

## Definition

LOCOMO is a benchmark used by several agent-memory systems in this repo to evaluate whether persistent memory improves downstream task performance.

## Why It Matters

Memory systems often claim better personalization or long-horizon recall, but those claims are hard to compare without a shared evaluation target. LOCOMO appears as a common reference point across Mem0, MemoryOS, and OpenViking-related reporting.

## How It Works

The sources use LOCOMO as an external benchmark and report metrics such as accuracy, F1, BLEU-1, task completion, latency, and token cost reductions. This page treats it as a common evaluation anchor rather than a fully reconstructed benchmark spec.

## Key Properties / Tradeoffs

- **Comparability**: lets otherwise different systems report against one shared target.
- **Field relevance**: has become a recurring benchmark in agent-memory discussions.
- **Spec gap**: this repo does not yet capture the full task design or protocol details. [UNVERIFIED]

## Related Concepts

- Used by: [[mem0]], [[memory-operating-system]], [[context-database]]
- Relevant to: [[memory-management]], [[high-performance-computing]]

## Source Basis

- [[summary-mem0]]
- [[summary-memoryos-emnlp2025]]
- [[summary-openviking]]

## Open Questions

- Which memory behaviors does LOCOMO measure well, and which does it miss?
