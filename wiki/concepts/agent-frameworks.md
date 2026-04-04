---
title: Agent Frameworks
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/Thread by @lijigang.md
links: []
tags: [agent-architecture, llm]
---

# Agent Frameworks

## Definition

Agent frameworks are runtime architectures that combine a language model with tools, state management, and execution policies to enable autonomous behavior. They provide the scaffolding that transforms a pure next-token predictor into an agent capable of planning, using tools, and maintaining state across multiple turns.

## Why It Matters

The debate in the community centers on whether agent frameworks are fundamental to intelligence or merely compensatory scaffolding for current model limitations. Some argue frameworks will dissolve into model capabilities as models improve; others contend that closed-loop control and persistent state are inherently separate from the model's core function.

## How It Works

Typical agent frameworks include:
- **Model**: The core LLM that generates actions
- **Tools**: Functions the model can call (shell, search, code execution)
- **State**: Memory of prior actions, observations, and intermediate results
- **Policy/Orchestration**: How the framework selects actions, handles errors, and loops

Frameworks range from minimal (single tool like shell access) to complex (hierarchical multi-agent orchestration with dedicated memory systems).

## Key Properties / Tradeoffs

- **Complexity vs capability**: More complex frameworks enable harder tasks but introduce maintenance burden
- **Model dependence**: Framework effectiveness often depends on underlying model capabilities
- **Closed-loop vs open-loop**: Closed-loop frameworks maintain state and iterate; open-loop frameworks execute fixed plans
- **Context utilization**: Frameworks must efficiently use context window to maintain coherent agent state

## Related Concepts

- Builds on: [[model-harness]], [[tool-use]], [[session-management]]
- Used in: [[ai-agents]]
- Related: [[closed-loop-control]]

## Source Basis

- [[summary-thread-by-lijigang]] — primary source; community debate on framework necessity

## Open Questions

- [UNVERIFIED] Whether strong enough models eliminate framework need
- [UNVERIFIED] Optimal framework complexity for different task types
