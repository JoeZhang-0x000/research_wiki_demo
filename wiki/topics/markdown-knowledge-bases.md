---
title: Markdown Knowledge Bases
type: topic
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/Thread by @karpathy.md
  - raw/Building a Virtual Filesystem for Mintlify's AI Assistant.md
tags: [ai-agents, markdown, obsidian, research, knowledge-management]
---

# Markdown Knowledge Bases

## Scope

This topic covers workflows where raw source material is collected into files and then incrementally compiled into a linked markdown wiki for later research, question answering, and derived outputs. It includes file layout, indexing, agent editing patterns, and shell-style navigation over the corpus.

It excludes opaque retrieval systems that expose only chunk search APIs and excludes general note-taking advice that is not aimed at agent-operated knowledge workflows.

Domain: **AI Agents**

## Subproblems

1. **Ingest** — converting web pages, papers, repos, and notes into durable markdown artifacts
2. **Compilation** — turning raw sources into summaries, concepts, and indexes
3. **Navigation** — helping agents find relevant pages through links, indexes, grep, and directory structure
4. **Derived output** — writing reports, slides, plots, or analyses back into the same workspace
5. **Maintenance** — linting for missing links, inconsistent metadata, or stale pages

## Key Approaches

The sources point to two closely related ways of making markdown corpora usable by agents.

### Direct Filesystem Wikis

This approach uses ordinary directories and markdown files as the core representation. Agents read and write pages directly, while index pages and schemas keep the structure legible enough for autonomous maintenance. The Karpathy thread frames this as a simple but effective alternative to heavier retrieval stacks at moderate corpus sizes.

### Virtualized Filesystem Projections

This approach exposes an indexed or chunked documentation store as a shell-navigable filesystem rather than as top-k retrieval only. The Mintlify writeup shows how a virtual filesystem can preserve agent ergonomics while avoiding the latency of provisioning full sandboxes. This is where [[virtual-filesystem-interface]] becomes operationally important.

## Landscape of Systems / Papers

| Name | Year | Key Contribution | Link |
|------|------|------------------|------|
| Karpathy knowledge-base workflow | 2026 | Raw → wiki → query → output loop built around markdown and Obsidian | [[summary-karpathy-knowledge-base-thread]] |
| Mintlify ChromaFs | 2026 | Virtual filesystem over indexed docs to support shell-native agent browsing | [[summary-mintlify-virtual-filesystem]] |

## Important References

- Andrej Karpathy (2026) — "Thread by @karpathy" — [[summary-karpathy-knowledge-base-thread]] — practical workflow for research knowledge bases
- Densumesh (2026) — "Building a Virtual Filesystem for Mintlify's AI Assistant" — [[summary-mintlify-virtual-filesystem]] — filesystem illusion over a doc index for low-latency agent use

## Open Problems

- How much explicit indexing is needed before a markdown corpus stops degrading into directory sprawl?
- When should a workflow move from direct file access to helper indexes or virtualized views?
- What maintenance loop best keeps a generated wiki coherent as the number of pages grows?

## Related Topics

- [[agent-memory-systems]]
- [[graph-rag-systems]]
