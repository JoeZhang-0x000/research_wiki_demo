---
title: "Summary — 观摩学习顶级 Agents 如何对 GPT-5.4 进行行为矫正"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/观摩学习顶级 Agents 如何对 GPT-5.4 进行行为矫正.md
links:
  - https://x.com/_kaichen/status/2041199915280507123
tags:
  - ai-agents
  - prompt-engineering
  - gpt-5
  - hermes-agent
  - openclaw
---

# Summary — 观摩学习顶级 Agents 如何对 GPT-5.4 进行行为矫正

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog/tweet thread              |
| Author(s)    | @_kaichen                      |
| Year         | 2026                           |
| Venue        | X/Twitter                      |
| Raw file     | `raw/观摩学习顶级 Agents 如何对 GPT-5.4 进行行为矫正.md` |

## Main Idea

顶级 Agent 框架（Hermes Agent、OpenClaw）花大量工程精力修复 GPT-5.4 在 agentic 场景下的四个顽固行为缺陷：光说不做、半途而废、不做验证、编造而非查询。模型能力足够，但训练目标（单轮对话质量）和 Agent 场景要求（多轮执行纪律）之间存在 gap，Harness 层用 prompt engineering 填这个 gap。

## Key Details

### GPT-5.4 四个顽固行为缺陷

1. **光说不做（Commentary-Only Turns）**：说完计划就结束，没有 tool call。GPT 系列有强烈"先描述计划再行动"倾向，Agent 场景里每一轮空转都浪费上下文
2. **半途而废（Premature Completion）**：工具返回部分结果就当完整答案交付，不继续搜索
3. **不做验证（No Verification）**：生成代码不跑测试，写配置不检查语法，给答案不交叉验证
4. **编造而非查询（Hallucination Over Lookup）**：明明有 search_files、web_search 工具，却选择凭印象编一个

### OpenClaw 方案（三段 Prompt，~1500 tokens）

文件：`extensions/openai/prompt-overlay.ts`

- **执行偏好层（Execution Bias）**：禁止 commentary-only turns，"Start the real work in the same turn when the next step is clear."
- **输出契约层（Output Contract）**：强制精简输出，禁用 em dash（GPT-5 特别爱用），默认简短回答
- **人格层（Friendly Prompt Overlay）**：把执行纪律包装成"好队友"风格

### Hermes Agent 方案（9层 System Prompt）

文件：`agent/prompt_builder.py`

**XML 标签强化指令权重**：
```xml
<tool_persistence>
Do not stop early when another tool call would materially improve the result.
If a tool returns empty or partial results, retry with a different query or strategy before giving up.
</tool_persistence>
```

**四维验证清单**：
- Correctness：输出是否满足所有需求？
- Grounding：事实性声明是否有工具输出支撑？
- Formatting：输出格式是否匹配要求？
- Safety：下一步有没有副作用？需要确认范围？

**反幻觉优先级链**：
工具查询 → 带标签地假设 → 向用户提问

**Developer Role 切换**：OpenAI API 里 developer role 比 system role 指令权重更高。Hermes 调 GPT-5/Codex 时自动把 system prompt 切换成 developer role。

**条件式 prompt 组装**：当前会话没有 web_search 工具时，所有提到 web_search 的引导文本都被自动剥离，防止模型幻想调用不存在的工具。

### 深层洞察

**Prompt 是创可贴，不是手术**。模型厂商卖"通用智能"，但 Agent 框架第一件事是用 prompt 给模型打行为补丁。真正解决方案应在训练阶段就把 agentic behavior 作为优化目标。Hermes 代码里的 `trajectory_compressor.py` 已经在为 RL 训练压缩 Agent 轨迹数据——Prompt 补丁是现在权宜之计，training pipeline 才是终局。

## Limitations

- 分析基于源码阅读，来源为 2026 年 4 月
- Hermes 的 9 层架构和 trajectory_compressor 是前瞻性设计，效果未经验证

## Links to Concepts

- [[model-harness]] — Hermes 和 OpenClaw 都在做 harness 层的行为工程
- [[meta-harness]] — 与 Meta Harness 相关（同一时期的工作）

## Links to Topics

- [[ai-agents]] — 顶级 Agent 框架的实践
- [[coding-agents]] — GPT-5 在 coding agent 场景的问题

## Quotes Worth Preserving

> "模型厂商卖的是'通用智能'，但 Agent 框架在生产环境里做的第一件事，是用 prompt 给模型打行为补丁。"

> "RLHF 优化的是'回答让人满意'，不是'持续正确地调用工具直到任务完成'。"

> "Prompt 终究是创可贴，不是手术。真正的解决方案应该在训练阶段就把 agentic behavior 作为优化目标。"
