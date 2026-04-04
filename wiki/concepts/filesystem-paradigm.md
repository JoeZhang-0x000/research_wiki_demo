---
title: Filesystem Paradigm
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/volcengine-openviking-openviking-is-an-open-source-2026-04-04.md
  - raw/building-a-virtual-filesystem-for-mintlifys-2026-04-03.md
links: []
tags: [ai-agents, filesystem, context]
---

# Filesystem Paradigm

## Definition

The filesystem paradigm treats context as something agents can browse through directory and file abstractions instead of only through opaque search results.

## Why It Matters

Agents already know how to navigate files. Reusing that interaction style can make retrieval more inspectable and can preserve hierarchy that flat chunk search discards.

## How It Works

Systems expose virtual or physical files, directories, and sometimes URIs so the agent can drill from broad structure into specific detail with ordinary browse-and-read actions.

## Key Properties / Tradeoffs

- **Browseability**: easier to inspect than hidden ranking pipelines.
- **Hierarchy**: directories preserve coarse-to-fine organization.
- **Implementation cost**: requires mapping indexes or memories into a stable file model.

## Related Concepts

- Used by: [[context-database]], [[virtual-filesystem-interface]]
- Relevant to: [[context-engineering]], [[markdown-knowledge-base]]

## Source Basis

- [[summary-openviking]]
- [[summary-mintlify-virtual-filesystem]]

## Open Questions

- What makes a virtual filesystem feel native enough for agents to rely on it?
