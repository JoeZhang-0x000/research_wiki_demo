---
title: "Summary — 搞懂缓存机制，从Gemma4到Claude Code省80%Token"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/搞懂缓存机制，从Gemma4到Claude Code省80%Token.md
links:
  - https://x.com/MinLiBuilds/status/2041178722230030384
tags:
  - llm
  - caching
  - claude-code
  - optimization
---

# Summary — 搞懂缓存机制，从Gemma4到Claude Code省80%Token

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog                           |
| Author(s)    | @MinLiBuilds                   |
| Year         | 2026                           |
| Venue        | X/Twitter                      |
| Raw file     | `raw/搞懂缓存机制，从Gemma4到Claude Code省80%Token.md` |

## Main Idea

KV cache 是大模型推理优化的核心：历史 token 的 Key-Value 张量算完就固定，可以缓存复用。Claude Code 对缓存做了精密工程——分层前缀匹配、两档 TTL（5分钟/1小时）、断裂检测。理解这套机制，才能有意识地保护缓存、省 3-5 倍 token。

## Key Details

- **Gemma 4 实验**：Turn 2→3 prompt 处理从 31 秒降到 0.25 秒，100 倍加速，瓶颈从 GPU 计算变为内存读取
- **Qwen3.5 小模型无感**：0.8B 参数，算 KV 本来只要 200ms，缓存收益微乎其微
- **Decoder-only 架构**：因果注意力，历史 KV 算完就固定，可复用；BERT 这种双向注意力加新 token 会改变所有表示，缓存全废
- **Claude Code 缓存分层**：
  - Block 1-2：不缓存（计费归因头、CLI 前缀）
  - Block 3：global 缓存（所有用户共享的静态指令）
  - Block 4：org 缓存（CLAUDE.md 等动态内容）
  - tools + messages：session 级缓存
- **两档 TTL**：默认 5 分钟；Pro/Max 订阅用户（未超额）1 小时
- **缓存断裂检测**：cache_read_input_tokens 比上次下降 >5% 且绝对值 >2000 tokens → 判定断裂
- **Sub-agent 几乎不能复用主线程缓存**：工具集不同、消息历史独立、可能用不同模型

## Method / Approach

作者用 Ollama 本地跑 Gemma 4 (8B) 和 Qwen3.5 (0.8B)，做多轮对话实验，测 prompt 处理时间。对比缓存命中/未命中的速度差异，揭示 KV 缓存机制。再逆向 Claude Code 源码，分析 Anthropic 的缓存工程实现。

## Results / Evidence

**10 轮对话节省测算**（系统提示 20K tokens）：
- 无缓存：10 轮全价 = 10 份
- 有缓存：1 次全价 + 9 次 1/10 ≈ 1.9 份
- **节省 76%，实际 3-5 倍差距**

**Claude Code 缓存结构**：
```
┌────────────────────────────────────────────────┐
│ system（~20K tokens）                            │
│   Block 1: 计费归因头              → 不缓存     │
│   Block 2: CLI 前缀               → 不缓存     │
│   Block 3: 静态指令（行为规则等）   → global 缓存│
│   ──── DYNAMIC_BOUNDARY ────                    │
│   Block 4: 动态内容（CLAUDE.md 等）→ org 缓存   │
├─────────────────────────────────────────────────┤
│ tools（工具 schema，session 内冻结）               │
├─────────────────────────────────────────────────│
│ messages（对话历史，最后一条上 cache_control）   │
└─────────────────────────────────────────────────┘
```

**缓存保护行为（绿灯）**：
- 连续对话，前缀不变，增量缓存
- btw 共享 session
- Claude.md 配好后不乱动

**缓存破坏行为（红灯）**：
- 开新 session（~20K tokens 全价重算）
- 改 CLAUDE.md（Block 4 起全失效）
- 加减 MCP 工具（schema 变化）
- 切换模型（完全失效）
- /compact（消息历史变化）
- 发呆超过 TTL

## Limitations

- Ollama 缓存是概率性的，不可靠（内存压力导致 KV 被淘汰）
- Sub-agent 每次几乎冷启动，不适合高频并行使用
- Cache Keep-Alive 续命方案只是设想，未实测

## Links to Concepts

- [[kv-cache]] — KV 缓存的技术基础
- [[claude-code]] — Claude Code 的缓存实现
- [[llm-quantization]] — 相关推理优化方向

## Links to Topics

- [[llm-quantization]] — 同属 LLM 推理优化话题
- [[ai-agents]] — Claude Code 作为 agent 工具

## Quotes Worth Preserving

> "理解了这套机制，你就知道怎么让同样的套餐多撑 3-5 倍。"

> "这就是为什么'一个 session 持续对话'比'频繁开新 session'省钱的根本原因。"

> "每启动一个 sub-agent，基本等于一次'迷你冷启动'。"
