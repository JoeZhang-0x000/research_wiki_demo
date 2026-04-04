---
title: AI Agents
type: topic
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/bytedance-deer-flow-an-open-source-long-horizon-2026-04-04.md
  - raw/maxgfeller-open-harness-a-code-first-composable-sdk-2026-04-04.md
  - raw/anomalyco-opencode-the-open-source-coding-2026-04-04.md
links: []
tags: [ai-agents, agent-systems, orchestration]
---

# AI Agents

## Scope

This topic covers software systems that plan, use tools, read and modify external state, and pursue multi-step goals with some autonomy. In this wiki, it includes both general-purpose agent harnesses and narrower agent capabilities such as memory, tool use, and delegation.

It excludes one-shot prompt patterns that do not preserve state or interact with tools beyond a single completion.

Domain: **AI Agents**

## Subproblems

1. **Planning and control** - choosing the next action under long-horizon task constraints.
2. **Tool use** - calling filesystems, shells, browsers, MCP servers, and app APIs safely.
3. **Memory** - preserving useful information across turns and sessions.
4. **Delegation** - splitting work across sub-agents or specialized roles.
5. **Runtime safety** - constraining execution through permissions, sandboxes, and review loops.

## Key Approaches

### Harness-first agents

These systems expose a reusable runtime around models, tools, and execution policy. OpenHarness, OpenCode, and DeerFlow all fit this pattern, but differ in how much orchestration, UI, and memory they ship by default.

### Workflow-specific agents

Some projects focus on a narrower slice such as coding, research, or memory-backed assistance. They still rely on the same core primitives, but package them for a specific task family.

## Landscape of Systems / Papers

| Name | Year | Key Contribution | Link |
|------|------|------------------|------|
| DeerFlow | 2026 | Long-horizon super-agent harness with skills, sandboxes, and delegation | [[summary-deer-flow]] |
| OpenHarness | 2025 | Composable agent SDK centered on sessions and middleware | [[summary-open-harness]] |
| OpenCode | 2025 | Provider-agnostic coding agent with TUI and client/server runtime | [[summary-opencode]] |
| MemoryOS | 2025 | OS-inspired hierarchical memory stack for personalized agents | [[summary-memoryos-emnlp2025]] |

## Important References

- [[summary-deer-flow]] - example of a full-stack agent runtime with memory and sandbox support.
- [[summary-open-harness]] - shows a lightweight, composable SDK approach.
- [[summary-opencode]] - highlights provider-agnostic coding-agent design.

## Open Problems

- Which runtime abstractions remain stable as models, tools, and safety policies change?
- How much autonomy should live in the harness versus in higher-level workflows or skills?
- What observability is sufficient for debugging agent behavior without flooding operators with traces?

## Related Topics

- [[coding-agents]]
- [[memory-management]]
- [[context-engineering]]
