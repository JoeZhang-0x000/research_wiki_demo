---
title: MemGPT
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/shichun-liu-agent-memory-paper-list-the-paper-list-of-memory-2026-04-04.md
links: []
tags: [ai-agents, memory]
---

# MemGPT

## Definition

MemGPT is a memory-oriented agent system cited in the survey as foundational work for treating large language models through an operating-system-like memory lens.

## Why It Matters

It appears in the survey as an anchor point for later memory systems that separate active context from larger stores and reason explicitly about memory management.

## How It Works

This repo currently references MemGPT through the survey rather than a direct source summary, so this page records its role in the surrounding literature rather than reconstructing its full architecture.

## Key Properties / Tradeoffs

- **Influence**: helps motivate OS-style memory thinking for agents.
- **Literature role**: often cited as a bridge between LLM runtime design and memory systems.
- **Coverage gap**: implementation specifics in this wiki remain incomplete. [UNVERIFIED]

## Related Concepts

- Related to: [[memory-operating-system]], [[hierarchical-memory]]
- Mentioned by: [[agent-memory-taxonomy]]

## Source Basis

- [[summary-agent-memory-survey]]

## Open Questions

- Which MemGPT ideas survived into newer production memory systems versus remaining conceptual?
