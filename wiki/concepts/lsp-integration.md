---
title: LSP Integration
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/anomalyco-opencode-the-open-source-coding-2026-04-04.md
  - raw/code-yeongyu-oh-my-openagent-omo-the-best-agent-harness-2026-04-04.md
links: []
tags: [coding, ai-agents, tooling]
---

# LSP Integration

## Definition

LSP integration means an agent runtime can call Language Server Protocol features such as go-to-definition, references, rename, and diagnostics while working in a codebase.

## Why It Matters

Text search alone misses semantic structure. LSP calls give coding agents a better navigation and refactoring substrate, especially in large typed codebases.

## How It Works

The harness connects to language servers for the current project and exposes semantic navigation or edit actions as tools the agent can call during analysis and code change workflows.

## Key Properties / Tradeoffs

- **Semantic precision**: better than plain grep for many tasks.
- **Language dependence**: quality depends on server support and workspace setup.
- **Operational overhead**: starting and maintaining language servers adds complexity.

## Related Concepts

- Common in: [[coding-agents]]
- Complements: [[tool-use]], [[agent-harness]]

## Source Basis

- [[summary-opencode]]
- [[summary-oh-my-openagent]]

## Open Questions

- Which LSP actions should agents use directly versus through higher-level abstractions?
