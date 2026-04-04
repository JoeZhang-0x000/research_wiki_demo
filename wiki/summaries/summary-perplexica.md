---
title: "Summary — Perplexica: AI-Powered Open Source Search Engine"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/bunsdev-perplexica-search-engine-ai-perplexica-is-an-ai-powered-2026-04-04.md
  - "https://github.com/BunsDev/Perplexica-Search-Engine-AI"
links:
  - "https://github.com/BunsDev/Perplexica-Search-Engine-AI"
tags: []
---

# Summary — Perplexica: AI-Powered Open Source Search Engine

## Source Metadata

| Field        | Value                                                       |
|--------------|-------------------------------------------------------------|
| Source type  | web / github / open source project                         |
| Author(s)    | BunsDev / ItzCrazyKns                                       |
| Year         | 2024-2026                                                   |
| Venue        | GitHub (open source)                                        |
| Raw file     | `raw/bunsdev-perplexica-search-engine-ai-perplexica-is-an-ai-powered-2026-04-04.md` |

## Main Idea

Perplexica is an open-source AI-powered search engine that understands user questions and provides answers with cited sources, using SearxNG for live web results and supporting local LLMs via Ollama. It offers multiple "focus modes" for different query types (academic, YouTube, Wolfram Alpha, Reddit, etc.).

## Key Details

- **Local LLM support**: Use local models (Llama3, Mixtral) via Ollama
- **Two main modes**:
  - **Copilot Mode** (in development): generates different queries, visits top matches directly
  - **Normal Mode**: processes query and performs web search
- **Six focus modes**: All, Writing Assistant, Academic Search, YouTube Search, Wolfram Alpha, Reddit Search
- **Current information**: uses SearxNG metasearch engine, avoids embedding/staleness issues of vector-db approaches
- **API**: available for integration into other applications
- **Installation**: Docker (recommended) or manual with SearxNG + npm build
- **Privacy**: SearxNG is self-hostable; no data sent to third parties

## Method / Approach

Perplexica uses SearxNG to get live web results, then reranks and extracts most relevant sources. Uses embeddings and similarity searching to refine results. Architecture docs available separately.

## Results / Evidence

No benchmark results provided — this is an open-source engineering project, not a research contribution.

## Limitations

- Docker recommended but not required (manual install is complex)
- Copilot Mode still in development
- Requires SearxNG instance with JSON format enabled

## Links to Concepts

- [[context-database]] — Perplexica can serve as a context retrieval system
- [[agent-harness]] — could be integrated as a tool within agent workflows

## Links to Topics

- [[ai-agents]]
- [[context-engineering]]

## Quotes Worth Preserving

> Perplexica is an open-source AI-powered searching tool that goes deep into the internet to find answers. Inspired by Perplexity AI, it's an open-source option that not just searches the web but understands your questions.
