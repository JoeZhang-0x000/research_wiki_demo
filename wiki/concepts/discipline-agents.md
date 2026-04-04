---
title: Discipline Agents
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/code-yeongyu-oh-my-openagent-omo-the-best-agent-harness-2026-04-04.md
links: []
tags: [ai-agents, orchestration, specialization]
---

# Discipline Agents

## Definition

Discipline agents are specialized agent roles with distinct prompts, models, or responsibilities that collaborate within one larger orchestration loop.

## Why It Matters

The pattern separates planning, execution, architecture, and research work instead of forcing one agent persona to do everything. That can improve clarity and delegation quality on larger tasks.

## How It Works

The OmO source describes named roles such as orchestrator, deep worker, planner, and search-oriented specialists, each invoked for different parts of the workflow.

## Key Properties / Tradeoffs

- **Specialization**: clearer division of labor.
- **Prompt isolation**: each role can carry narrower instructions.
- **Coordination burden**: more roles mean more opportunities for drift or redundancy.

## Related Concepts

- Used in: [[sub-agent-orchestration]], [[ultrawork]]
- Part of: [[coding-agents]]

## Source Basis

- [[summary-oh-my-openagent]]

## Open Questions

- Which specializations consistently outperform a strong general worker?
