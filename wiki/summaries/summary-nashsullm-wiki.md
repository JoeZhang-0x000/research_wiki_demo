---
title: "Summary — nashsu/llm_wiki"
type: summary
status: draft
created: 2026-04-09
updated: 2026-04-09
sources:
  - raw/nashsullm_wiki.md
links:
  - https://github.com/nashsu/llm_wiki
tags:
  - llm-wiki
  - knowledge-base
  - rag
  - desktop-app
  - tauri
---

# Summary — nashsu/llm_wiki

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | web                            |
| Author(s)    | nashsu                         |
| Year         | 2026                           |
| Venue        | https://github.com/nashsu/llm_wiki |
| Raw file     | `raw/nashsullm_wiki.md`       |

## Main Idea

LLM Wiki is a cross-platform desktop application that implements Karpathy's LLM Wiki pattern — turning documents into a persistent, incrementally-built knowledge base rather than re-deriving knowledge on every query. It uses a two-step chain-of-thought ingest pipeline and provides knowledge graph visualization, multi-conversation chat, and deep research capabilities.

## Key Details

- **Three-layer architecture**: Raw Sources (immutable) → Wiki (LLM-generated) → Schema (rules & config)
- **Two-step ingest pipeline**: Analysis step followed by Generation step for better quality
- **4-signal relevance model** for knowledge graph: Direct link (×3.0), Source overlap (×4.0), Adamic-Adar (×1.5), Type affinity (×1.0)
- **4-phase query retrieval**: Tokenized search → Graph expansion → Budget control → Context assembly
- **Configurable context window**: 4K to 1M tokens with 60/20/5/15 split (wiki/history/index/system)
- **Multi-format document support**: PDF, DOCX, PPTX, XLSX, images, video/audio
- **Chrome Extension (Manifest V3)** with Mozilla Readability.js and Turndown.js
- **Tauri v2** desktop with React 19 + TypeScript, shadcn/ui + Tailwind CSS v4
- **Multi-provider LLM**: OpenAI, Anthropic, Google, Ollama, Custom

## Method / Approach

The project implements and extends Karpathy's LLM Wiki pattern with significant enhancements:

1. **Purpose.md** — defines goals, key questions, research scope
2. **Two-step chain-of-thought ingest** — split into Analysis and Generation for better quality
3. **Source traceability** — every wiki page includes `sources:` field linking back to raw sources
4. **Knowledge graph** with sigma.js + graphology + ForceAtlas2
5. **Deep Research** — Tavily API web search + LLM synthesis
6. **Async review queue** — LLM flags items needing human judgment

## Results / Evidence

[UNVERIFIED] No benchmark numbers or performance metrics provided in the README. The evidence is architectural.

## Limitations

- No quantitative performance data
- Relies on proprietary LLM APIs — no local-only option beyond Ollama
- Chrome Extension only
- No mention of data privacy guarantees

## Links to Concepts

- [[graph-rag]] — LLM Wiki is an alternative to traditional RAG
- [[markdown-knowledge-base]] — implements the markdown knowledge base pattern

## Links to Topics

- [[ai-agents]] — wiki maintenance performed by LLM agents in a loop
- [[high-performance-computing]] — [UNVERIFIED] similar desktop app architecture patterns

## Quotes Worth Preserving

> Instead of traditional RAG (retrieve-and-answer from scratch every time), the LLM **incrementally builds and maintains a persistent wiki** from your sources. Knowledge is compiled once and kept current, not re-derived on every query.
