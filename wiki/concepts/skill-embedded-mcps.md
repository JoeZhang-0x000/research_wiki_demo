---
title: Skill-Embedded MCPs
type: concept
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/code-yeongyu-oh-my-openagent-omo-the-best-agent-harness-2026-04-04.md
  - raw/bytedance-deer-flow-an-open-source-long-horizon-2026-04-04.md
links: []
tags: [ai-agents, mcp, skills]
---

# Skill-Embedded MCPs

## Definition

Skill-embedded MCPs are MCP servers bundled with a skill so the extra tool surface is started only when that skill is invoked.

## Why It Matters

This pattern keeps the base runtime simpler and can reduce idle context or operational overhead by loading specialized tools only when needed.

## How It Works

The skill definition declares or implies the MCP resources it needs. When the skill is activated, the harness starts those servers in scoped fashion and tears them down afterward.

## Key Properties / Tradeoffs

- **On-demand capability**: tool surface follows task need.
- **Context cleanliness**: avoids always-on tool clutter.
- **Operational coupling**: skill and MCP lifecycle become tied together.

## Related Concepts

- Extension of: [[skills-system]]
- Built on: [[mcp-server]]

## Source Basis

- [[summary-oh-my-openagent]]
- [[summary-deer-flow]]

## Open Questions

- How should skill packages declare permissions and lifecycle for embedded MCP servers?
