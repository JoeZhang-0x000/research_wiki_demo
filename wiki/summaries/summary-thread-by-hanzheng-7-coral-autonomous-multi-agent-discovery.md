---
title: "Summary — Thread by @hanzheng_7: CORAL Autonomous Multi-Agent Discovery"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/Thread by @hanzheng_7.md
links:
  - https://x.com/hanzheng_7/status/2041291008378343707
tags:
  - ai-agents
  - multi-agent
  - autoresearch
  - self-evolving
---

# Summary — Thread by @hanzheng_7: CORAL Autonomous Multi-Agent Discovery

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog/tweet thread              |
| Author(s)    | @hanzheng_7                   |
| Year         | 2026                           |
| Venue        | X/Twitter                      |
| Raw file     | `raw/Thread by @hanzheng_7.md` |

## Main Idea

CORAL 是真正的自主多 Agent 发现系统：Agent 自主决定探索什么、存储什么知识、复用哪些想法、何时测试假设。50%以上的突破来自 Agent 之间互相借鉴他人的发现，证明知识复用和协作是规模化自动发现的核心。

Paper: https://arxiv.org/abs/2603.28052
Code: https://github.com/Human-Agent-Society/CORAL

## Key Details

**核心问题**：当前很多"自进化"框架的 Agent 仍在严格约束的循环内运作——它们改动解，但并不真正决定如何探索。

**CORAL 的真正自主性**：
- 🔍 **what to explore**（探索什么）
- 🧠 **what knowledge to store**（存储什么知识）
- ♻️ **which ideas to reuse**（复用哪些想法）
- 🧪 **when to test hypotheses**（何时测试假设）

**关键发现**：
- 单个自主 Agent 已超越固定进化搜索
- 最大收益来自多 Agent 形成研究社区
- **50%以上**的突破来自在他人发现基础上继续工作
- 在 10+ 困难任务（算法发现、系统优化）上达到 SOTA，同时将效率提升 3-10 倍

**Multi-Agent vs Single-Agent**：
单一自主 Agent 已优于固定进化搜索，但最大收益来自多 Agent 形成研究社区

## Links to Concepts

- (autoresearch) — CORAL 是 Autoresearch 的多 Agent 扩展版本
- [[meta-harness]] — 与 Meta Harness 相关（同一时期的工作）
- (multi-agent-orchestration) — 多 Agent 协作机制

## Links to Topics

- [[ai-agents]] — 属于自主 Agent 系统

## Quotes Worth Preserving

> "A single autonomous agent already outperforms fixed evolutionary search, but the biggest gains emerge when multiple agents form a research community."

> "Over 50% of breakthroughs in multi-agent runs come from building on other agents' discoveries."
