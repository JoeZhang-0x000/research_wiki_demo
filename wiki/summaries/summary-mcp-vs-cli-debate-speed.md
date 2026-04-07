---
title: "Summary — The Debate of MCP vs. CLI Centers on Speed"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/The Debate of MCP vs. CLI Centers on Speed..md
links:
  - https://x.com/cerebras/status/2041300697258590590
tags:
  - ai-agents
  - mcp
  - infrastructure
  - latency
---

# Summary — The Debate of MCP vs. CLI Centers on Speed

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog                           |
| Author(s)    | @zhennydez (via @cerebras)     |
| Year         | 2026                           |
| Venue        | X/Twitter → cerebras.ai        |
| Raw file     | `raw/The Debate of MCP vs. CLI Centers on Speed..md` |

## Main Idea

MCP vs CLI 的争议核心是速度：Perplexity CTO 宣布放弃 MCP 回到 API/CLI，因为 MCP 的 token 开销和多步延迟在生产环境中不可接受。但更深层的两个问题——推理基础设施和代码执行环境——才是真正的瓶颈，解决它们对 MCP 和 CLI 都有价值。

## Key Details

**MCP 的代价**：
- MCP 工作方式：每个 tool call 携带完整 schema 定义，每个 auth handshake 端到端运行，每步等待前一步完成
- 3个服务（GitHub、Slack、Sentry）的 tool definitions 在 agent 读到用户消息之前就占 55,000 tokens
- Token 开销比 CLI 高 3-42x

**Perplexity 的选择**：
- CLI 轻量快速，但静态——调用显式编程的工具，auth 需要为每个服务单独管理，无共享协议层的可观测性或调试能力

**两个深层考量**：

1. **更快推理**（Cerebras Wafer-Scale Engine）：
   - 3,000 tokens/秒
   - 约 15x 快于传统 GPU 推理
   - 推理够快时，MCP 的 tool call 延迟成本相对缩小

2. **安全代码执行**（Pydantic Monty）：
   - Rust 写的最小 Python 解释器
   - 启动时间 <0.06ms vs Docker 195ms vs sandboxing 服务 >1000ms
   - 无文件系统/网络/环境变量访问（除非显式授权）
   - 攻击面积极小
   - 当前仅支持部分 Python 子集，无第三方库，生产不可用

## Links to Concepts

- [[mcp-server]] — MCP 服务器相关
- [[agent-harness]] — 涉及 agent 的执行环境和基础设施

## Links to Topics

- [[ai-agents]] — MCP vs CLI 是 agent 部署的核心工程决策

## Quotes Worth Preserving

> "The frustrations driving the MCP vs. CLI debate are real. But a significant part of how to speed up the experience also sits in the inference infrastructure and execution environment, not just the protocol itself."

> "These improvements don't belong to MCP alone — CLI workflows, in a similar vein, can get faster too."
