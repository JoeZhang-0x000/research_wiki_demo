---
title: Markdown Knowledge Base
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/Thread by @karpathy.md
  - raw/Building a Virtual Filesystem for Mintlify's AI Assistant.md
tags: [ai-agents, markdown, obsidian, knowledge-management]
---

# Markdown Knowledge Base

## Definition

A markdown knowledge base is a corpus of structured `.md` files organized as directories, pages, and links so that both humans and agents can read, search, update, and derive new documents from it. It treats the filesystem itself as the primary knowledge interface instead of hiding content behind a database-only retrieval layer.

## Why It Matters

Markdown is simple, inspectable, versionable, and works with ordinary tools like `grep`, `cat`, and `find`. For agent workflows, that means the same representation can support source ingest, compilation into summaries and concepts, downstream question answering, and further distillation. This pattern underpins [[markdown-knowledge-bases]] and complements [[persistent-agent-memory]] when durable knowledge is stored as files instead of only as database records.

## How It Works

The sources describe a closed-loop workflow:

1. Collect source material into a raw corpus
2. Compile the corpus into summaries, concepts, indexes, and topic pages
3. Query the compiled wiki with an agent using normal file operations
4. Write reports, notes, or visualizations back into the corpus
5. Distill reusable outputs into the wiki so future queries start from a better base

The key operational move is to maintain lightweight structure:

- directories encode broad organization
- index files prevent navigation drift
- backlinks or wiki links preserve relationships
- schemas keep generated pages consistent enough for later automation

## Key Properties / Tradeoffs

- **Human inspectability**: every artifact stays readable without specialized tooling
- **Agent compatibility**: shell-native tools often work well enough at small and medium scales
- **Incremental compilation**: new sources can be folded into the wiki one by one
- **Scale limits**: larger corpora may need derived indexes or search helpers to avoid slow or shallow retrieval
- **Schema discipline**: the format stays flexible, but quality drops quickly if pages drift without linting

## Related Concepts

- Used in: [[markdown-knowledge-bases]]
- Can be exposed through: [[virtual-filesystem-interface]]
- Can act as a substrate for: [[persistent-agent-memory]]

## Source Basis

- [[summary-karpathy-knowledge-base-thread]] — direct description of the raw → compile → query workflow
- [[summary-mintlify-virtual-filesystem]] — argument for filesystem-style interfaces over top-k chunk retrieval

## Open Questions

- What indexing structure keeps markdown corpora navigable once they exceed the size that agents can casually scan?
- Which parts of the wiki should stay persistent versus being rebuilt ephemerally for a given question?
- How much schema rigidity is needed before a markdown knowledge base starts to feel like a fragile database?
