---
title: Summary — am-memory
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/danielwanwx-am-memory-persistent-memory-for-claude-code-2026-04-04.md
  - https://github.com/danielwanwx/am-memory
tags: [ai-agents, memory, sqlite, claude-code]
---

# Summary — am-memory

## Source Metadata

| Field | Value |
|-------|-------|
| Source type | web |
| Author(s) | danielwanwx |
| Year | 2026 |
| Venue | GitHub repository |
| Raw file | `raw/danielwanwx-am-memory-persistent-memory-for-claude-code-2026-04-04.md` |

## Main Idea

`am-memory` provides Claude Code with local persistent memory by storing promoted session knowledge in a single SQLite database and exposing search and save operations through MCP tools and hooks. The design emphasizes minimal setup, local-first operation, and automatic promotion of useful session data into a long-term searchable store.

## Key Details

- Setup is designed as `pip install am-memory` followed by `am init`, which creates the database, registers the MCP server, installs hooks, and appends instructions to `~/.claude/CLAUDE.md`
- The architecture separates search, long-term documents, raw session records, message storage, and working-memory state inside one SQLite file
- Full-text search uses FTS5 with a trigram tokenizer; optional vector search uses `sqlite-vec`
- Search follows a staged cascade that stops at the first retrieval layer returning results
- Session-end promotion assigns priority tiers such as P0, P1, and P2 based on the extracted quality of the session
- `am dream` performs background consolidation, including staleness detection, contradiction scanning, redundancy merges, and generation of concept-index documents
- TTL and LRU policies are used to keep the search index useful without deleting the underlying files or source artifacts

## Method / Approach

The system hooks into Claude Code session start and stop events, records sessions and raw messages, and then promotes the most useful artifacts into a long-term `documents` table. At query time, Claude is expected to call `am_search` before answering questions that might benefit from prior architectural decisions, debugging results, or technical constraints. Separate state tools provide lightweight working memory for active tasks.

## Results / Evidence

- The source claims BM25-only search latency around 50 ms and vector-backed latency around 500 ms when using Ollama
- The repository presents a one-file deployment model with no external database or cloud service
- The design includes automated health checks that operate across the whole memory base rather than only on new sessions

## Limitations

- The source describes architecture and intended behavior but does not provide a broad empirical evaluation of recall quality
- Vector search is optional and may introduce materially different latency depending on the embedding backend
- Much of the value depends on good extraction and promotion rules, which can be a source of noise if they are poorly tuned

## Links to Concepts

- [[persistent-agent-memory]] — document-centric memory implementation
- [[markdown-knowledge-base]] — related file-centric substrate discussed in the broader workflow sources

## Links to Topics

- [[agent-memory-systems]]

## Quotes Worth Preserving

> Every Claude Code session starts from zero.
