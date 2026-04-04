---
title: "Summary — Anthropic Diff Tool: Finding Behavioral Differences in New Models"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/a-diff-tool-for-ai-finding-behavioral-2026-04-04.md
  - https://www.anthropic.com/research/diff-tool
  - https://arxiv.org/abs/2602.11729
tags: []
---

# Summary — Anthropic Diff Tool: Finding Behavioral Differences in New Models

## Source Metadata

| Field        | Value                                                       |
|--------------|-------------------------------------------------------------|
| Source type  | research paper / blog post                                  |
| Author(s)    | Thomas Jiralerspong, Trenton Bricken (Anthropic Fellows)   |
| Year         | 2026                                                        |
| Venue        | Anthropic Research / arXiv:2602.11729                      |
| Raw file     | raw/a-diff-tool-for-ai-finding-behavioral-2026-04-04.md |

## Main Idea

Model diffing applies the software engineering concept of "diff" to neural networks, comparing models to automatically surface behavioral differences rather than manually auditing millions of weights. The Dedicated Feature Crosscoder (DFC) extends this to cross-architecture model comparison, identifying features unique to one model that may represent safety-relevant behaviors.

## Key Details

- **Traditional benchmarks** are reactive — only catch known problems, miss "unknown unknowns"
- **Model diffing** principle: focus on the ~50 lines that changed rather than million-line audit
- **Base-vs-finetune diffing**: compare modified model to trusted previous version
- **Cross-architecture diffing**: compare models with different origins and internal representations
- **Standard crosscoder** problem: forces imperfect translations, misses model-unique features
- **Dedicated Feature Crosscoder (DFC)** solution: three-section "bilingual dictionary" — shared dictionary, French-only section, English-only section
- **Steering**: suppress or amplify identified features to validate causal relationship to behavior

## Method / Approach

The DFC is architecturally designed with three distinct sections:
1. Shared dictionary: concepts both models understand
2. "Model-A-only" section: features unique to model A  
3. "Model-B-only" section: features unique to model B

This avoids the standard crosscoder's flaw of forcing imperfect matches that mask novel features.

## Results / Evidence

Validated findings across open-weight models:
- **"Chinese Communist Party Alignment" feature**: found in Qwen3-8B and DeepSeek-R1-0528-Qwen3-8B — controls pro-government censorship; absent in American models. Suppressing it enables discussion of Tiananmen Square.
- **"American Exceptionalism" feature**: found in Llama-3.1-8B-Instruct — controls US superiority assertions; absent in Chinese models compared
- **"Copyright Refusal Mechanism"**: found in OpenAI's GPT-OSS-20B — controls refusal to provide copyrighted material; absent in DeepSeek model

Reproducibility: CCP alignment feature rediscovered 5/5 times; American Exceptionalism 4/5 times.

## Limitations

- DFC surfaces thousands of features; only small fraction correspond to meaningful behavioral risks
- Method is a high-recall screening tool, not a definitive safety verdict
- Does not determine origin of behaviors (deliberate training vs. emergent from data)
- Analyzed only open-source models (Anthropic Fellows project)
- Not yet applied to frontier models

## Links to Concepts

- [[agent-harness]] — the coding agent this research aims to audit

## Links to Topics

- [[ai-agents]] — safety auditing for deployed agents

## Quotes Worth Preserving

> It's not enough to know how well they perform on existing tests — we also need to understand how they are changing and what new risks they might introduce.
