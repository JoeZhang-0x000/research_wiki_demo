---
title: Agent Harness
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/maxgfeller-open-harness-a-code-first-composable-sdk-2026-04-04.md
  - raw/anomalyco-opencode-the-open-source-coding-2026-04-04.md
  - raw/bytedance-deer-flow-an-open-source-long-horizon-2026-04-04.md
links: []
tags: [ai-agents, runtime, harness]
---

# Agent Harness

## Definition

An agent harness is the runtime layer that wraps a model with tools, state, permissions, execution policy, and often UI or session control so the overall system can act as an autonomous or semi-autonomous agent.

## Why It Matters

Most practical agent behavior is determined by the harness, not just the model. The harness decides what tools exist, how context is assembled, whether edits are safe, and how long-running tasks are driven to completion.

## How It Works

Typical harness responsibilities include:

- building the model/tool/session abstraction boundary
- exposing files, shell, web, or MCP capabilities
- managing retries, compaction, and delegation
- enforcing permission and sandbox policy

## Key Properties / Tradeoffs

- **Capability surface**: richer harnesses can do more, but are harder to reason about.
- **Reliability**: edit tools and execution controls often dominate real-world success rates.
- **Extensibility**: plugin, middleware, and skill systems reduce core complexity when well-factored.

## Related Concepts

- Specialized form: [[superagent-harness]]
- Often used by: [[coding-agents]]
- Common concerns: [[tool-use]], [[session-management]], [[sandbox-isolation]]

## Source Basis

- [[summary-open-harness]] - composable SDK framing.
- [[summary-opencode]] - open-source coding harness framing.
- [[summary-deer-flow]] - long-horizon orchestration-heavy harness.

## Open Questions

- Which responsibilities should stay in the harness versus external skills or agents?
- How opinionated can a harness become before it stops being reusable?
