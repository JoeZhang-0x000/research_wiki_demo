---
title: Sandbox Isolation
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/bytedance-deer-flow-an-open-source-long-horizon-2026-04-04.md
links: []
tags: [ai-agents, security, execution]
---

# Sandbox Isolation

## Definition

Sandbox isolation constrains agent execution inside a limited environment so tool calls, filesystem access, and side effects stay separated from the host or from other tasks.

## Why It Matters

As agents gain shell, browser, and code execution abilities, isolation becomes a core safety and reproducibility control. It also helps different tasks or sub-agents avoid interfering with one another.

## How It Works

The sources describe local, Docker, and Kubernetes execution modes, each trading convenience against containment strength. A harness usually mounts only the necessary working data into the sandbox.

## Key Properties / Tradeoffs

- **Safety**: reduces blast radius for bad commands or untrusted code.
- **Reproducibility**: makes execution environments more uniform.
- **Overhead**: stronger isolation can add setup and orchestration cost.

## Related Concepts

- Used by: [[agent-harness]], [[superagent-harness]]
- Often paired with: [[sub-agent-orchestration]]

## Source Basis

- [[summary-deer-flow]] - explicit multi-mode sandbox support.

## Open Questions

- How much isolation is enough for local developer workflows without destroying usability?
