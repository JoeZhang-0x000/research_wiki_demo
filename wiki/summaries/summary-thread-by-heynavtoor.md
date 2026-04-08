---
title: "Summary — Andrej Karpathy's LLM Wiki Pattern"
type: summary
status: draft
created: 2026-04-08
updated: 2026-04-08
sources:
  - raw/Thread by @heynavtoor.md
links:
  - https://x.com/heynavtoor/status/2041140052949090417
tags:
  - "Knowledge Management"
  - "RAG"
  - "LLM"
---

# Summary — Andrej Karpathy's LLM Wiki Pattern

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | tweet thread                   |
| Author(s)    | @heynavtoor (Nav Toor), Andrej Karpathy (original author) |
| Year         | 2026                           |
| Venue        | X/Twitter                     |
| Raw file     | `raw/Thread by @heynavtoor`    |

## Main Idea

Andrej Karpathy published **LLM Wiki** (5,000+ stars in 48 hours, 100% open source), a knowledge management pattern where the AI doesn't retrieve information from scratch on every question. Instead, it builds and maintains a persistent, compounding knowledge base that grows smarter with every source added—fundamentally different from RAG which re-derives knowledge on every query.

## Key Details

**RAG vs LLM Wiki:**

| | RAG | LLM Wiki |
|--|-----|---------|
| Knowledge state | Re-derived on every question | Compiled once, persistent |
| Per-query cost | High (full retrieval + synthesis) | Low after initial compilation |
| Knowledge growth | None (forgets after query) | Compounds (every source adds to wiki) |
| Cross-references | Manual | Automatic |
| Contradiction detection | None | Flagged |

**How LLM Wiki works:**
1. Drop a source (article, paper, transcript, notes) into raw collection
2. AI reads it, writes a summary, updates the index
3. Updates every relevant entity and concept page across the wiki (1 source → 10-15 wiki pages simultaneously)
4. Cross-references built automatically
5. Contradictions between sources flagged
6. Ask questions against the wiki; good answers get filed back as new pages
7. Explorations compound in the knowledge base—nochat history disappears

**Karpathy's use cases:**
- **Personal**: track goals, health, psychology; file journal entries; build structured self-picture over time
- **Research**: read papers for months; build comprehensive wiki with evolving thesis
- **Books**: build fan wiki as you read; characters, themes, plot threads, all cross-referenced
- **Business**: feed Slack threads, meeting transcripts, customer calls; wiki stays current because AI does the maintenance

**Github**: 5,000+ stars, 1,294 forks, published 2 days before the thread (2026-04-04)

**Key quote from Karpathy:**
> "Obsidian is the IDE. The LLM is the programmer. The wiki is the codebase. You never write the wiki yourself. You source, explore, and ask questions. The AI does all the grunt work."

## Method / Approach

LLM Wiki applies a compile-once model to knowledge management:
- **raw/** = source materials (append-only, never edited)
- **wiki/** = compiled, structured knowledge (AI maintains)
- **Ingest**: raw → wiki (AI compiles sources into entity + concept pages)
- **Query**: ask questions against the compiled wiki (not re-reading raw each time)
- Contrast with RAG which re-reads raw on every query

## Results / Evidence

- 5,000+ stars on GitHub in 48 hours
- 1,294 forks
- Viral reception in the AI engineering community

## Limitations

- LLM Wiki and RAG may solve different problems (raised in thread: "RAG for 'find the relevant piece and answer,' LLM Wiki for 'synthesize everything I know over time'")
- No mechanism described for handling wiki bloat or conflicting information beyond "flagging contradictions"
- Depends on AI reliably maintaining wiki consistency as it grows
- Storage and retrieval at scale not addressed

## Links to Concepts

- [[markdown-knowledge-base]] — LLM Wiki as a specific implementation of the markdown knowledge base pattern
- [[graph-rag]] — automatic cross-reference building similar to graph-structured knowledge
- [[long-term-memory]] — wiki as persistent, compounding memory for AI systems
- [[factual-memory]] — wiki pages as structured storage of declarative facts

## Links to Topics

- [[markdown-knowledge-bases]] — LLM Wiki is a concrete instantiation of the wiki compile workflow described in this topic
- [[ai-agents]] — the AI as active maintainer of the knowledge base (not just a passive retriever)

## Quotes Worth Preserving

> "RAG re-discovers knowledge on every question. LLM Wiki compiles it once and keeps it current."

> "Obsidian is the IDE. The LLM is the programmer. The wiki is the codebase. You never write the wiki yourself. You source, explore, and ask questions. The AI does all the grunt work." — Karpathy

> "5k stars in 48h is wild. gonna go check this out tonight" — reply sentiment

> "they might work best together rather than one replacing the other" — Nav Toor on RAG + LLM Wiki
