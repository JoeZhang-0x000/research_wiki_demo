---
title: "Summary — Thread by @yoonholeee"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/Thread by @yoonholeee.md
links:
  - https://x.com/yoonholeee/status/2038640635482456118
tags: [meta-harness, model-harness, automated-harness-engineering, llm-evaluation]
---

# Summary — Thread by @yoonholeee

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | web (X/Twitter thread)         |
| Author(s)    | @yoonholeee (Yoonho Lee), commenters |
| Year         | 2026                           |
| Venue        | X/Twitter                      |
| Raw file     | `raw/Thread by @yoonholeee`    |

## Main Idea

Yoonho Lee announces Meta-Harness, a method for autonomously improving LLM evaluation harnesses by using a coding agent with filesystem access to the complete history of prior attempts. The key finding is that unrestricted access to all previous history is essential — previous text optimization loops that only see rewards/summaries/previous attempts discard important information and underperform.

## Key Details

- **Problem**: Autonomously improving LLM harnesses requires solving hard, long-horizon credit-assignment over all prior code, traces, and scores
- **Meta-Harness**: A harness whose purpose is to optimize other harnesses — an instantiation of classic meta-learning with minimal imposed structure
- **Key requirements**:
  1. Let agent inspect any part of prior attempts
  2. Give it a good hill to climb
- **Iterative loop**: Agent tries different ideas, selectively inspecting very long raw history
- **82 median files read** per proposal attempt
- **TerminalBench-2**: Proposer outperforms human-engineered baselines (ACE, Terminus-KIRA)
- **Comparison to DGM (Darwin-Godel Machines)**: DGM focuses on recursive self-improvement from scratch; Meta-Harness starts from SOTA harnesses and pushes the frontier

## Method / Approach (if applicable)

1. **Proposer**: A coding agent that reads source code, execution traces, and scores from all prior candidates
2. **Filesystem access**: Full history exposed as filesystem, allowing selective inspection
3. **Iterative optimization**: Agent tries different ideas, reads ~82 files median, forms targeted hypothesis about why previous attempts failed
4. **Starts from SOTA**: Unlike from-scratch self-improvement, begins with ACE, Terminus-KIRA baselines

## Results / Evidence

- TerminalBench-2: Meta-Harness proposer outperforms all hand-engineered baselines (ACE, Terminus-KIRA)
- 6x performance gap observed from harness changes on fixed models (per @omarsar0 thread)
- Full history consistently outperforms compressed-score optimization

## Limitations

- Harness optimization ceiling is set by model weights
- If LLM cannot reason through the problem, optimizing eval scaffold only gets faster measurement of same ceiling
- Distinguishing harness failure from model failure is unsolved

## Links to Concepts

- [[meta-harness]] — the method being introduced (new concept candidate)
- [[model-harness]] — what is being optimized
- [[terminalbench]] — evaluation benchmark used

## Links to Topics

- [[ai-agents]] — harness optimization for agentic systems

## Quotes Worth Preserving

> "We find that unrestricted access to all previous history is essential in our settings, because the dependencies are so long-horizon. Previous text optimization loops that only see rewards/summaries/previous attempts discard important information and underperform here"
> — @yoonholeee

> "Meta-Harness is itself a harness: one whose purpose is to optimize other harnesses"
> — @yoonholeee
