---
title: GEPA
type: concept
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/Thread by @RajaPatnaik.md
links:
  - https://x.com/RajaPatnaik/status/2041305017781833859
tags: [prompt-engineering, evolutionary-algorithms, self-evolution]
---

# GEPA

## Definition

GEPA (Genetic-Pareto Prompt Evolution) is an evolutionary optimization framework for automatically improving agent prompts, skills, and tool descriptions — without GPU training or weight updates. It treats prompt variants as individuals in a multi-objective genetic algorithm, selecting for quality, size, and compatibility simultaneously.

## Why It Matters

Prompt engineering is typically manual, iterative, and non-scalable. GEPA automates this process by reading execution traces to understand failure modes and proposing targeted fixes via genetic search. Cost per evolution run is ~$2–10 (claimed), making it accessible to individual developers.

## How It Works

1. Read current skill/prompt definition
2. Generate an evaluation dataset from execution traces
3. Run GEPA optimization — genetic algorithm with Pareto selection across multiple objectives
4. Produce candidate variants
5. Evaluate candidates against safety guardrails (test suite, size limits, semantic drift detection)
6. Submit best variant as a PR for human review

## Key Properties / Tradeoffs

- **No weight updates**: Operates at the prompt/harness layer, not the model layer
- **Multi-objective**: Simultaneously optimizes quality, size, and compatibility (Pareto-optimal front)
- **Cost**: ~$2–10 per evolution run [UNVERIFIED]
- **Safety**: Full test suite must pass; semantic drift detection; human PR review required
- **Scope**: Phase 1 covers skill files; planned phases cover tool descriptions, system prompts, code, and continuous loop

## Related Concepts

- Used by: [[self-evolving-memory]], [[agent-harness]]
- Framework: DSPy (external framework; provides the underlying prompt optimization substrate)
- Contrast with: manual prompt engineering; fine-tuning approaches

## Source Basis

- [[summary-thread-by-rajapatnaik-nousresearch-gepa-self-evolving-agents]] — primary source (tweet thread)
- ICLR 2026 Oral paper (full paper not yet reviewed in wiki)

## Open Questions

- Full technical details of the Pareto selection mechanism are not in the tweet thread — need the actual ICLR 2026 paper.
- Cost claim ($2–10) is unverified.
- Comparison to OpenEvolve (similar system) is unresolved.
