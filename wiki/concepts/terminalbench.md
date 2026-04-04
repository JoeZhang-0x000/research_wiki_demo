---
title: TerminalBench
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/Thread by @omarsar0.md
  - raw/Thread by @yoonholeee.md
links: []
tags: [benchmark, llm-evaluation, terminal]
---

# TerminalBench

## Definition

TerminalBench is an evaluation benchmark for agentic coding tasks in terminal/shell environments. It measures how well AI systems can complete software development tasks using command-line interfaces, file manipulation, and code execution.

## Why It Matters

TerminalBench-2 is referenced in Meta-Harness research as the primary benchmark for agentic coding tasks. The benchmark tests agents' ability to navigate complex development environments, execute shell commands, and complete multi-step software tasks — representing a realistic proxy for developer assistance scenarios.

## Key Results from Meta-Harness Paper

| System | TerminalBench-2 Score |
|--------|---------------------|
| Meta-Harness | 37.6% |
| Claude Code | 27.5% |
| Human baseline (ACE) | [UNVERIFIED] |
| Terminus-KIRA | [UNVERIFIED] |

Meta-Harness outperformed all hand-engineered baselines including ACE and Terminus-KIRA.

## Related Concepts

- Used in: [[meta-harness]], [[model-harness]]
- Related: [[tool-use]]

## Source Basis

- [[summary-thread-by-yoonholeee]] — primary source; benchmark used in Meta-Harness evaluation
- [[summary-thread-by-omarsar0]] — secondary source; benchmark results cited

## Open Questions

- [UNVERIFIED] Full details of benchmark construction and task types
- [UNVERIFIED] How TerminalBench-2 differs from version 1
