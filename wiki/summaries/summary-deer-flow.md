---
title: "Summary — bytedance/deer-flow: SuperAgent Harness with Memory and Sandboxes"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/bytedance-deer-flow-an-open-source-long-horizon-2026-04-04.md
  - "https://github.com/bytedance/deer-flow"
links:
  - "https://github.com/bytedance/deer-flow"
tags: []
---

# Summary — bytedance/deer-flow: SuperAgent Harness with Memory and Sandboxes

## Source Metadata

| Field        | Value                                                                                         |
|--------------|----------------------------------------------------------------------------------------------|
| Source type  | web / github / open source project                                                          |
| Author(s)    | ByteDance (Daniel Walnut, Henry Li as key contributors)                                       |
| Year         | 2025 (v1); 2026 (v2.0 ground-up rewrite)                                                   |
| Venue        | GitHub Trending #1 (Feb 28, 2026)                                                            |
| Raw file     | `raw/bytedance-deer-flow-an-open-source-long-horizon-2026-04-04.md` |

## Main Idea

DeerFlow 2.0 is a ground-up rewritten super agent harness that orchestrates sub-agents, memory, and sandboxes through extensible skills to handle long-horizon tasks (minutes to hours). Built on LangGraph and LangChain, it provides filesystem access, long-term memory, context engineering, IM channel integrations (Telegram, Slack, Feishu, WeCom), and an embedded Python client.

## Key Details

**Architecture**:
- Built on **LangGraph** and **LangChain**
- Lead agent spawns sub-agents with isolated contexts; sub-agents run in parallel where possible
- Per-thread sandboxed filesystem with `/mnt/user-data/{uploads,workspace,outputs}`

**Skills System**:
- Structured Markdown files defining workflows, best practices, and resources
- Built-in skills: research, report-generation, slide-creation, web-page, image-generation, video-generation
- Skill-embedded MCP servers (on-demand, scoped, self-cleanup)
- Custom skills installable via Gateway

**Sandbox Modes**:
- Local execution (on host)
- Docker execution (isolated containers)
- Kubernetes execution (via provisioner service)

**Long-Term Memory**:
- Persistent memory of user profile, preferences, accumulated knowledge across sessions
- Stored locally under user control
- Memory updates skip duplicate fact entries

**IM Channels** (auto-start when configured, no public IP required):
- Telegram (bot API, long-polling)
- Slack (Socket Mode)
- Feishu/Lark (WebSocket)
- WeCom (WebSocket)

**Observability**:
- LangSmith integration
- LangFuse integration
- Both can run simultaneously

**Recommended Models**:
- Doubao-Seed-2.0-Code, DeepSeek v3.2, Kimi 2.5 (recommended by ByteDance)
- Model-agnostic via OpenAI-compatible API

**Embedded Python Client** (`DeerFlowClient`):
```python
from deerflow.client import DeerFlowClient
client = DeerFlowClient()
response = client.chat("Analyze this paper", thread_id="my-thread")
for event in client.stream("hello"): ...
```

**Key Contributors**: Daniel Walnut (hetaoBackend), Henry Li (magiccube)

## Method / Approach

DeerFlow 2.0 evolved from a Deep Research framework into a "super agent harness" by recognizing that users wanted infrastructure to get work done, not just research. The architecture uses LangGraph for agent orchestration and LangChain for LLM integrations. Skills are loaded progressively (only when needed) to keep context lean. Sub-agents are spawned dynamically for complex task decomposition.

## Results / Evidence

- GitHub Trending #1 on Feb 28, 2026 after v2 launch
- InfoQuest (BytePlus intelligent search tool) integration for enhanced web search
- OpenClaw Context Plugin evaluation showed 52.08% task completion on LoCoMo (vs 35.65% baseline)

## Limitations

- Ground-up v2 rewrite shares no code with v1—ecosystem tools may be fragmented
- Security notice explicitly warns: designed for local trusted environments (127.0.0.1); deployment in LAN/public cloud without strict ACLs introduces risk
- IM channel integrations require API keys/tokens for each platform

## Links to Concepts

- [[superagent-harness]] — DeerFlow positions itself as a super agent harness
- [[sub-agent-orchestration]] — lead agent spawning parallel sub-agents
- [[sandbox-isolation]] — Docker/Kubernetes execution modes
- [[long-term-memory]] — persistent cross-session memory
- [[skills-system]] — Markdown-based extensible capabilities
- [[context-engineering]] — aggressive context summarization and offloading

## Links to Topics

- [[ai-agents]]
- [[context-engineering]]

## Quotes Worth Preserving

> DeerFlow (Deep Exploration and Efficient Research Flow) is an open-source super agent harness that orchestrates sub-agents, memory, and sandboxes to do almost anything — powered by extensible skills.

> Built on LangGraph and LangChain, it ships with everything an agent needs out of the box: a filesystem, memory, skills, sandbox-aware execution, and the ability to plan and spawn sub-agents for complex, multi-step tasks.
