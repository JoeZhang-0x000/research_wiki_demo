---
title: "Summary — MaxGfeller/open-harness: Code-first Composable AI Agent SDK"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/MaxGfelleropen-harness A code-first, composable SDK to build powerful AI agents.md
  - https://github.com/MaxGfeller/open-harness
tags: []
---

# Summary — MaxGfeller/open-harness: Code-first Composable AI Agent SDK

## Source Metadata

| Field        | Value                                                       |
|--------------|-------------------------------------------------------------|
| Source type  | web / github / sdk                                          |
| Author(s)    | MaxGfeller                                                  |
| Year         | 2025                                                        |
| Venue        | GitHub (open source)                                        |
| Raw file     | `raw/MaxGfelleropen-harness A code-first, composable SDK to build powerful AI agents.md` |

## Main Idea

OpenHarness is a code-first, composable SDK for building AI agents, built on Vercel's AI SDK, providing a modular architecture of Agents, Sessions, Conversations, and composable middleware (turn tracking, compaction, retry) with first-class TypeScript/React/Vue support.

## Key Details

- **Base**: Built on Vercel's AI SDK (AI SDK 5)
- **Three packages**:
  - `@openharness/core` — Agent, Session, Conversation, middleware, tools, UI stream integration
  - `@openharness/react` — React hooks and provider for AI SDK 5 chat UIs
  - `@openharness/vue` — Vue 3 composables and provider for AI SDK 5 chat UIs
- **Agent class**: Stateless executor configured with model, tools, maxSteps; yields events (text.delta, etc.)
- **Session class**: Multi-turn conversation context with compaction, retry, and persistence; default 128k context window
- **Conversation class**: Stateful wrapper combining a runner with send() API
- **Composable middleware**: `apply()`, `toRunner()`, `withTurnTracking()`, `withCompaction()`, `withRetry()`
- **Built-in tools**: `createFsTools()` (filesystem), `createBashTool()` (shell), custom tool interface
- **Examples**: CLI agent, Next.js chat, Nuxt chat
- **Documentation**: docs.open-harness.dev
- **Advanced features**: Subagents (nested delegation), MCP servers, Skills (on-demand instruction packages)

## Method / Approach

OpenHarness treats agents as pure event iterators. An Agent is configured with a model and tool set, then run over an input message stream. Events are yielded incrementally (including `text.delta` for streaming), making it suitable for both CLI and web UI integration.

Middleware is composable via `apply()`:

```typescript
const runner = apply(
  toRunner(agent),
  withTurnTracking(),       // track turns
  withCompaction({ contextWindow: 200_000, model: agent.model }), // compress context
  withRetry({ maxRetries: 5 })
);
```

Sessions add statefulness on top of stateless agents—managing compaction triggers, retry logic, and persistence across multiple conversation turns.

## Results / Evidence

No benchmark results are provided; OpenHarness is a developer tool / SDK rather than a research contribution.

## Limitations

- Provider-dependent on Vercel AI SDK; not model-agnostic at the core
- No built-in memory system—sessions are the only persistence primitive, and compaction is left to the developer to configure
- Smaller community compared to established frameworks (LangChain, etc.)

## Links to Concepts

- [[Agent Harness]] — OpenHarness is itself a harness framework for building agents
- [[Session Management]] — Session class with compaction and retry
- [[Middleware Pattern]] — Composable middleware via apply()

## Links to Topics

- [[AI Agents]]
- [[Tool Use]]

## Quotes Worth Preserving

> Build capable, general-purpose AI agents in code. Based on Vercel's AI SDK, inspired by Claude Code, Codex, and similar agent harnesses.
