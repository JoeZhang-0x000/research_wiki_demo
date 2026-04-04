---
title: OpenClaw
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/volcengine-openviking-openviking-is-an-open-source-2026-04-04.md
  - raw/adoresever-graph-memory-graph-graph-2026-04-04.md
links: []
tags: [ai-agents, harness, open-source]
---

# OpenClaw

## Definition

OpenClaw is an open-source agent framework that appears in multiple sources here as a host runtime for memory plugins such as graph-memory and OpenViking.

## Why It Matters

It functions as an integration target in this repo's memory-system landscape. Seeing multiple memory systems plug into the same host helps separate harness concerns from memory-layer concerns.

## How It Works

The sources treat OpenClaw primarily as the outer agent runtime while plugins provide alternate memory or context engines.

## Key Properties / Tradeoffs

- **Ecosystem role**: useful as a shared host for plugin-style memory experiments.
- **Comparability**: makes memory-plugin claims easier to compare.
- **Coverage gap**: this wiki does not yet include a dedicated OpenClaw source summary. [UNVERIFIED]

## Related Concepts

- Host for: [[context-database]]
- Related to: [[agent-harness]], [[graph-rag]]

## Source Basis

- [[summary-openviking]]
- [[summary-graph-memory]]

## Open Questions

- Which OpenClaw runtime assumptions shape the performance of its memory plugins?
