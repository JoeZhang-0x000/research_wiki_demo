---
title: Provider-Agnostic Agents
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/anomalyco-opencode-the-open-source-coding-2026-04-04.md
links: []
tags: [ai-agents, models, portability]
---

# Provider-Agnostic Agents

## Definition

Provider-agnostic agents are agent systems designed to work across multiple model vendors or local backends without coupling the runtime to one proprietary provider.

## Why It Matters

Portability affects cost control, model routing, and long-term maintainability. It also reduces the risk that core agent workflows are blocked by one provider's SDK or policy changes.

## How It Works

The harness uses an abstraction layer or an OpenAI-compatible interface so the same agent workflow can target multiple models with minimal changes.

## Key Properties / Tradeoffs

- **Flexibility**: easier to swap or route models.
- **Operational choice**: can mix hosted and local models.
- **Feature mismatch**: vendor-specific capabilities may be harder to expose cleanly.

## Related Concepts

- Common in: [[coding-agents]]
- Contrasts with: [[claude-code]]

## Source Basis

- [[summary-opencode]]

## Open Questions

- Which agent APIs stay portable once tool use and streaming semantics differ by provider?
