---
title: Meta-Harness
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/Thread by @omarsar0.md
  - raw/Thread by @yoonholeee.md
links: []
tags: [automated-harness-engineering, llm-optimization]
---

# Meta-Harness

## Definition

Meta-Harness is a system that optimizes evaluation harnesses end-to-end by using a coding agent with filesystem access to the complete history of prior harness attempts. It is itself a harness — one whose purpose is to optimize other harnesses.

## Why It Matters

This work demonstrates that automated harness engineering can outperform human-designed scaffolding. By giving an optimizer rich access to full history (not just compressed scores), Meta-Harness achieves 37.6% on TerminalBench-2 vs Claude Code's 27.5%, and improves text classification by 7.7 points over SOTA while using 4x fewer tokens.

## How It Works

1. **Proposer**: A coding agent that reads source code, execution traces, and scores from all prior candidates
2. **Filesystem access**: Full history of prior attempts exposed as filesystem, allowing selective inspection
3. **Iterative loop**: Agent tries different ideas, selectively inspecting long raw history
4. **Reference to >20 past attempts per step**: Exploits accumulated experience

Key finding: Unrestricted access to all previous history is essential — previous text optimization loops that only see rewards/summaries discard important information and underperform.

## Key Properties / Tradeoffs

- **Full history vs compressed scores**: Full history consistently outperforms summary-based optimization
- **82 median files read per proposal**: Agents inspect extensive prior attempts
- **Meta-learning instantiation**: Classic meta-learning with minimal imposed structure
- **Ceiling set by model weights**: Harness optimization cannot exceed model capability

## Results

- TerminalBench-2: 37.6% vs Claude Code 27.5% (+10.1 points)
- Text classification: +7.7 points over SOTA context management, 4x fewer tokens

## Related Concepts

- Builds on: [[model-harness]]
- Related: [[terminalbench]]
- Parent concept: [[model-harness]]

## Source Basis

- [[summary-thread-by-yoonholeee]] — primary source; author announcement
- [[summary-thread-by-omarsar0]] — secondary source; community discussion

## Open Questions

- [UNVERIFIED] How to distinguish harness failure from model failure
- [UNVERIFIED] Generalization to other benchmark types beyond TerminalBench
