---
title: Self-Evolving Memory
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/volcengine-openviking-openviking-is-an-open-source-2026-04-04.md
  - raw/bai-lab-memoryos-emnlp-oral-memoryos-is-2026-04-04.md
links: []
tags: [memory, ai-agents, updating]
---

# Self-Evolving Memory

## Definition

Self-evolving memory is a memory design where stored state is not static: the system keeps summarizing, updating, consolidating, or reorganizing memory as new interactions arrive.

## Why It Matters

Long-lived agent memory decays if it only accumulates raw artifacts. Evolution mechanisms try to keep memory useful and compact without requiring full manual curation.

## How It Works

The sources describe automated updating of user profiles, session-derived summaries, and hierarchical memory levels that are refreshed over time rather than written once and left unchanged.

## Key Properties / Tradeoffs

- **Adaptivity**: memory can track changing users and tasks.
- **Compression**: consolidation reduces storage and token pressure.
- **Error propagation**: mistaken updates can become durable unless rollback exists.

## Related Concepts

- Falls under: [[memory-management]]
- Related to: [[hierarchical-memory]], [[working-memory]]

## Source Basis

- [[summary-openviking]]
- [[summary-memoryos-emnlp2025]]

## Open Questions

- What rollback or audit model is sufficient for self-updating agent memory?
