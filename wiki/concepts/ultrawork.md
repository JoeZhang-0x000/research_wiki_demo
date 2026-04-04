---
title: Ultrawork
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/code-yeongyu-oh-my-openagent-omo-the-best-agent-harness-2026-04-04.md
links: []
tags: [ai-agents, orchestration, execution]
---

# Ultrawork

## Definition

Ultrawork is the OmO execution mode that aggressively activates multiple agents and continuation loops to keep work moving until the task is considered fully complete.

## Why It Matters

It captures a design philosophy common in ambitious coding-agent systems: the runtime should fight premature stopping rather than accept the first plausible-looking answer.

## How It Works

The source describes one command that activates all agents and uses continuation mechanisms such as Ralph Loop and a Todo Enforcer to keep the system from idling early.

## Key Properties / Tradeoffs

- **Persistence**: strong push toward completion.
- **Parallelism**: can mobilize more than one agent at once.
- **Cost risk**: aggressive execution can spend more tokens and time.

## Related Concepts

- Uses: [[discipline-agents]], [[sub-agent-orchestration]]
- Lives in: [[coding-agents]]

## Source Basis

- [[summary-oh-my-openagent]]

## Open Questions

- What stopping criteria keep persistent execution from becoming wasteful thrashing?
