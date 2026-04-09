---
title: "nashsu/llm_wiki"
source: "https://github.com/nashsu/llm_wiki"
author:
published:
created: 2026-04-09
description: "A personal knowledge base that builds itself. LLM reads your documents, builds a structured wiki, and keeps it current."
tags:
  - clippings
---
## LLM Wiki

**A personal knowledge base that builds itself.**  
LLM reads your documents, builds a structured wiki, and keeps it current.

## What is this?

LLM Wiki is a cross-platform desktop application that turns your documents into an organized, interlinked knowledge base — automatically. Instead of traditional RAG (retrieve-and-answer from scratch every time), the LLM **incrementally builds and maintains a persistent wiki** from your sources. Knowledge is compiled once and kept current, not re-derived on every query.

This project is based on [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — a methodology for building personal knowledge bases using LLMs.

## Credits

The foundational methodology comes from **Andrej Karpathy**'s [llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## What We Kept from the Original

- **Three-layer architecture**: Raw Sources (immutable) → Wiki (LLM-generated) → Schema (rules & config)
- **Three core operations**: Ingest, Query, Lint
- **index.md** as the content catalog and LLM navigation entry point
- **[[wikilink]]** syntax for cross-references
- **YAML frontmatter** on every wiki page
- **Obsidian compatibility**

## What We Changed & Added

### 1. From CLI to Desktop Application

Full cross-platform desktop application with three-column layout, icon sidebar, custom resizable panels, activity panel, all state persisted, scenario templates.

### 2. Purpose.md — The Wiki's Soul

Defines goals, key questions, research scope; LLM reads it during every ingest and query.

### 3. Two-Step Chain-of-Thought Ingest

Split into two sequential LLM calls:
- Step 1 (Analysis): LLM reads source → structured analysis
- Step 2 (Generation): LLM takes analysis → generates wiki files

### 4. Knowledge Graph with Relevance Model

4-Signal Relevance Model:
- Direct link (×3.0)
- Source overlap (×4.0) 
- Adamic-Adar (×1.5)
- Type affinity (×1.0)

Graph visualization with sigma.js + graphology + ForceAtlas2.

### 5. Optimized Query Retrieval Pipeline

4-phase retrieval: Tokenized Search → Graph Expansion → Budget Control → Context Assembly

### 6. Multi-Conversation Chat with Persistence

Independent chat sessions, conversation sidebar, per-conversation persistence.

### 7. Deep Research

Web search (Tavily API) + LLM synthesis when knowledge gaps are identified.

### 8. Browser Extension (Web Clipper)

Chrome Extension (Manifest V3) with Mozilla Readability.js and Turndown.js.

### 9. Multi-format Document Support

PDF (pdf-extract), DOCX (docx-rs), PPTX, XLSX (calamine), images, video/audio.

## Tech Stack

| Layer | Technology |
|---|---|
| Desktop | Tauri v2 (Rust backend) |
| Frontend | React 19 + TypeScript + Vite |
| UI | shadcn/ui + Tailwind CSS v4 |
| Graph | sigma.js + graphology + ForceAtlas2 |
| PDF | pdf-extract |
| Office | docx-rs + calamine |
| i18n | react-i18next |
| State | Zustand |
| LLM | Streaming fetch (OpenAI, Anthropic, Google, Ollama, Custom) |

## Quick Start

1. Launch app → Create new project (choose template)
2. Settings → Configure LLM provider
3. Sources → Import documents
4. Watch Activity Panel — LLM automatically builds wiki pages
5. Chat to query your knowledge base
6. Browse Knowledge Graph to see connections

## License

GNU General Public License v3.0
