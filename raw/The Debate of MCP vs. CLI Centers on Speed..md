---
title: "The Debate of MCP vs. CLI Centers on Speed."
source: "https://x.com/cerebras/status/2041300697258590590"
author:
  - "[[@cerebras]]"
published: 2026-04-07
created: 2026-04-07
description: "Written by @zhennydez MCP had a formative year. Then it had a turbulent week.Source: Morgan Linton (@morganlinton), post on X. Retrieved Mar..."
tags:
  - "clippings"
---
Written by [@zhennydez](https://x.com/@zhennydez)

MCP had a formative year. Then it had a turbulent week.

![Image](https://pbs.twimg.com/media/HFQjWg7bEAA49q9?format=jpg&name=large)

Source: Morgan Linton ([@morganlinton](https://x.com/@morganlinton)), post on X. Retrieved March 2026, from [https://x.com/morganlinton/status/2031795683897077965](https://x.com/morganlinton/status/2031795683897077965)

Perplexity CTO Denis Yarats walked on stage at Ask 2026 and announced that Perplexity was moving away from MCPs… and back to APIs and CLIs.

Immediately, Twitter split into two camps.

Not surprising, given MCP grew from an Anthropic open standard in November 2024 to industry-wide adoptions with [over 97 million monthly downloads in just thirteen months](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) across a range of companies and platforms.

Yet Perplexity, a prominent AI company, chose to walk away from it.

![Image](https://pbs.twimg.com/media/HFQjyYGbwAAZcDz?format=jpg&name=large)

Source: Anthropic (2025). Donating the Model Context Protocol and Establishing the Agentic AI Foundation. Retrieved April 2026, from [https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)

MCP's overhead isn't arbitrary. The protocol [works by](https://modelcontextprotocol.io/docs/getting-started/intro) guiding model interactions down specific, auditable paths: every tool call carries its full schema definition, every auth handshake runs end to end, and every step waits for the previous one to complete before the next begins. That predictability is exactly what enterprise deployments need.

But it comes at a cost: in a multi-step workflow, each structured step adds latency, and those costs accumulate across a long chain of tool calls.

**The Case Against MCP**

Those who cheered the move argued MCPs' token overhead is a harmful constraint, slowing down runtime and worsening as more tools are connected. To put it into perspective, Samir Amzani from DevCommunity [noted that](https://dev.to/amzani/your-mcp-server-is-eating-your-context-window-theres-a-simpler-way-3ja2) connecting just three services, GitHub, Slack, and Sentry, can put over 55,000 tokens of tool definitions in the MCP context window before the agent reads a single user message, ranging anywhere from [3-42x](https://www.scalekit.com/blog/mcp-vs-cli-use) higher token usage than CLIs.

**The Case For MCP**

However, while acknowledging MCPs' latency issues, supporters pointed to what developers would be giving up switching to CLIs. CLIs are lightweight and fast, but they're also static, calling tools they've been explicitly programmed to use, requiring developers to manage auth separately for every service, and offering no shared protocol layer for observability or debugging.

![Image](https://pbs.twimg.com/media/HFQj8_uaYAAwBYx?format=jpg&name=large)

No official explanation from Perplexity followed, but the divide reflected real development needs: teams with faster latency requirements may find CLIs more practical, while teams prioritizing observability and production safety may find MCPs' structure worth the overhead.

**Looking Beyond the Protocol Choice**

Switching to CLIs and APIs does solve some problems: the token overhead drops and the per-step latency improves. However, it doesn't fix everything. Some fundamental constraints, compounding latency at scale and unsafe code execution, are not fully resolved by swapping interfaces.

And these deeper constraints point to two areas worth examining: inference infrastructure and code execution environments.

![Image](https://pbs.twimg.com/media/HFQkCIUbMAAcUug?format=png&name=large)

**Consideration #1: Faster Inference**

One consideration is in the inference infrastructure, where faster inference targets the latency problem directly. Newer chip architectures designed for low latency AI workflows, such as [Cerebras's Wafer-Scale Engine](https://www.cerebras.ai/chip), keep model weights in on-chip memory across wafers rather than relying on off-chip memory, eliminating the memory bottleneck of conventional GPU inference. The result is up to [3,000 tokens per second](https://inference-docs.cerebras.ai/models/overview), or roughly up to [15x faster](https://www.cerebras.ai/blog/speedandaccuracyblog) than conventional GPU-based solutions, depending on the model.

That speed changes the calculus on MCP. Pair faster inference with real MCP servers, GitHub for code context, Slack for team data, Atlassian for project state, and the latency cost of each tool call shrinks significantly. The overhead that made MCP feel impractical becomes more manageable when the underlying inference is fast enough.

For enterprises that have prioritized MCP's auditable structure, this matters: faster inference doesn't require trading away the safety layer. It just makes the full stack, tool calls and all, more viable in production.

![Source: Artificial Analysis. GLM-4.7 API provider benchmarking data. Snapshot as of 1:34 PM, March 15, 2026. Retrieved March 2026, from https://artificialanalysis.ai/models/glm-4-7/providers](https://pbs.twimg.com/media/HFQuMndaAAECLh4?format=jpg&name=large)

read image description

Source: Artificial Analysis. GLM-4.7 API provider benchmarking data. Snapshot as of 1:34 PM, March 15, 2026. Retrieved March 2026, from [https://artificialanalysis.ai/models/glm-4-7/providers](https://artificialanalysis.ai/models/glm-4-7/providers)

**Consideration #2: Safe Code Execution**

Another consideration is in secure code execution. Running agent-generated code presents a tradeoff between safety and speed.

[Monty](https://github.com/pydantic/monty), a minimal Python interpreter written in Rust shipped by Pydantic, takes a different approach by keeping scope small. Rather than spinning up a container or exposing a full runtime, Monty runs only what the agent needs, no filesystem access, no network calls, no environment variables unless explicitly granted, and pausing only when an external call requires authorization. Because the interpreter is minimal, the attack surface for prompt injection is correspondingly small.

Startup time is [under 0.06ms, compared to 195ms for Docker and over 1,000ms for sandboxing services.](https://github.com/pydantic/monty) Although, Monty is still experimental, supports only a partial Python subset, and has no third-party library support, so it is not yet production-ready. But the blueprint is there for further iteration and development.

![Image](https://pbs.twimg.com/media/HFQkfnMa0AA20th?format=jpg&name=large)

Source: Model Context Protocol docs. Retrieved March 2026, from [https://modelcontextprotocol.io/docs/getting-started/intro](https://modelcontextprotocol.io/docs/getting-started/intro); Pydantic (Monty). Retrieved March 2026, from [https://github.com/pydantic/monty](https://github.com/pydantic/monty)

**These Considerations Benefit Both MCPs and CLIs**

The frustrations driving the MCP vs. CLI debate are real. The token overhead, the sluggish workflows, the risks of running agent-generated code— none of that is in dispute. But a significant part of how to speed up the experience also sits in the inference infrastructure and execution environment, not just the protocol itself. And these improvements don't belong to MCP alone, CLI workflows, in a similar vein, can get faster too.

**Contextualizing the Constraints**

Perplexity made a pragmatic call against real constraints, and so did the many teams quietly reaching for CLIs: because MCPs felt too slow. Many others are equally sticking with MCP. Both are reasonable decisions given their specific development needs.

And as the MCP vs. CLI debate continues, protocols aside, inference infrastructure and execution environments are equally worth the attention.

Full blog: [https://www.cerebras.ai/blog/MCPvsCLI](https://www.cerebras.ai/blog/MCPvsCLI)

In partnership with [@pydantic](https://x.com/@pydantic)