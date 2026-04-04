---
title: Experiential Memory
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/shichun-liu-agent-memory-paper-list-the-paper-list-of-memory-2026-04-04.md
links: []
tags: [ai-agents, memory]
---

# Experiential Memory

## Definition

Experiential memory stores lessons, procedures, failures, and successful patterns gathered from prior agent interactions rather than only factual knowledge.

## Why It Matters

Agents often fail for procedural reasons, not because they lack facts. Preserving what worked before lets the system reuse strategies, edits, and workflows across sessions.

## How It Works

Experiential memory is usually formed by extracting reusable patterns from conversations, task traces, or tool outputs and storing them as documents, graph nodes, or structured records.

## Key Properties / Tradeoffs

- **Actionability**: often more useful than raw factual recall for long tasks.
- **Compression**: can preserve know-how without replaying full transcripts.
- **Noise risk**: weak extraction can store bad habits or one-off fixes.

## Related Concepts

- Part of: [[agent-memory-taxonomy]]
- Contrasts with: [[factual-memory]]
- Often supports: [[sub-agent-orchestration]], [[skills-system]]

## Source Basis

- [[summary-agent-memory-survey]] - names experiential memory as a core function.
- [[summary-graph-memory]] - example of extracting and reusing past experience.

## Open Questions

- What is the right unit of storage for procedural knowledge: trace, summary, or executable skill?
