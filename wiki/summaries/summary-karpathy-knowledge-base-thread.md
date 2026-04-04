---
title: Summary — Karpathy on LLM Knowledge Bases
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/thread-by-karpathy-2026-04-03.md
  - "https://x.com/karpathy/status/2039805659525644595"
links:
  - "https://x.com/karpathy/status/2039805659525644595"
tags: [ai-agents, markdown, obsidian, workflows]
---

# Summary — Karpathy on LLM Knowledge Bases

## Source Metadata

| Field | Value |
|-------|-------|
| Source type | note |
| Author(s) | Andrej Karpathy |
| Year | 2026 |
| Venue | X thread |
| Raw file | `raw/thread-by-karpathy-2026-04-03.md` |

## Main Idea

Karpathy describes a workflow where an LLM incrementally compiles a raw research corpus into a markdown wiki that then becomes the substrate for future queries, reports, and further wiki improvement. The claim is that at moderate scale, organized markdown plus auto-maintained indexes can be good enough without reaching for a complex RAG stack.

## Key Details

- Source materials of many kinds are placed in `raw/`, then incrementally compiled by an LLM into summaries, concepts, backlinks, and category pages
- Obsidian acts as the main interface for inspecting raw inputs, compiled wiki pages, and derived artifacts such as slides or plots
- Query results are often written back as markdown files or visual artifacts and then filed into the wiki, so exploration compounds into a better knowledge base
- Karpathy reports operating at roughly 100 articles and 400K words without needing fancy RAG because the LLM can maintain indexes and read the important related data directly
- Lint-like maintenance tasks include finding inconsistencies, filling in missing data, and generating candidates for new pages
- The workflow keeps the representation deliberately simple: nested directories of markdown, images, CSVs, and scripts plus an `AGENTS.md` schema

## Method / Approach

The workflow treats knowledge work as a compile loop over files. First, collect inputs into a raw corpus. Second, let the LLM organize them into a wiki with summaries and concept pages. Third, ask complex questions against that wiki. Fourth, save useful outputs back into the corpus so later runs begin with more structure and more distilled knowledge than before.

## Results / Evidence

- The thread reports a working knowledge base with about 100 articles and 400K words
- Karpathy states that the organized markdown and indexes were sufficient for his recent research workflows without a more elaborate RAG layer
- The replies and follow-up post point toward an extrapolation where a team of LLMs builds ephemeral or persistent wikis on demand for a query

## Limitations

- The source is an informal workflow description rather than a controlled evaluation
- The threshold where direct file access stops being enough is not specified
- Human-in-the-loop curation still appears important, especially in earlier stages of a wiki

## Links to Concepts

- [[markdown-knowledge-base]] — primary description of the file-based knowledge workflow
- [[persistent-agent-memory]] — frames the wiki as a form of accumulated cross-session memory
- [[virtual-filesystem-interface]] — reinforces the usefulness of filesystem-native agent interaction

## Links to Topics

- [[markdown-knowledge-bases]]
- [[agent-memory-systems]]

## Quotes Worth Preserving

> raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki
