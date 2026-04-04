---
title: Middleware Pattern
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/maxgfeller-open-harness-a-code-first-composable-sdk-2026-04-04.md
links: []
tags: [ai-agents, architecture, composition]
---

# Middleware Pattern

## Definition

The middleware pattern composes reusable processing layers around an agent runner so concerns such as retries, compaction, or turn tracking can be added without rewriting the agent core.

## Why It Matters

Harnesses quickly accumulate cross-cutting concerns. Middleware keeps those behaviors composable and easier to test or swap than if they were fused into one monolith.

## How It Works

An agent runner is wrapped by one middleware layer after another, with each layer intercepting or augmenting execution events, inputs, or outputs.

## Key Properties / Tradeoffs

- **Composability**: easy to add orthogonal behaviors.
- **Separation of concerns**: runtime policy stays outside the core agent.
- **Debuggability**: stacked wrappers can obscure the final control flow.

## Related Concepts

- Used in: [[agent-harness]], [[session-management]]

## Source Basis

- [[summary-open-harness]]

## Open Questions

- Which agent runtime concerns should be middleware and which should remain first-class primitives?
