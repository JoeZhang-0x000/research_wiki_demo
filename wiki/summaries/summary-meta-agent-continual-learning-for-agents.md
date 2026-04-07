---
title: "Summary — Meta-Agent: Continual Learning for Agents"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/meta-agent continual learning for agents.md
links:
  - https://x.com/essamsleiman/status/2041224799746428944
tags:
  - ai-agents
  - meta-harness
  - optimization
  - self-evolving
---

# Summary — Meta-Agent: Continual Learning for Agents

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog/tweet thread              |
| Author(s)    | @essamsleiman                 |
| Year         | 2026                           |
| Venue        | X/Twitter                      |
| Raw file     | `raw/meta-agent continual learning for agents.md` |

## Main Idea

Meta-Agent 是一个开源库，从生产轨迹（production traces）中自动、持续地改进 agent harness。指向一个已有 agent + 一串无标签生产轨迹 + 小型有标签 holdout set，LLM judge 评分 + proposer 写改进 + holdout 验证。在 tau-bench v3 airline 任务上，holdout 准确率从 67% 提升到 87%。

GitHub: https://github.com/canvas-org/meta-agent

## Key Details

**背景**：
- TerminalBench-2 上，vanilla Claude Code + Haiku 4.5 得 27.5%，最佳手工工程 harness 同模型得 35.5%（无微调）
- 现有自动改进方法（Autoresearch、Meta-Harness）依赖强评估信号（标签、测试、确定性检查）
- 现实生产环境中标签稀疏或不可得

**Meta-Agent 工作流**：
1. **Read**：从运行 agent 收集轨迹
2. **Judge**：用 LLM judge 对轨迹评分
3. **Propose**：读失败轨迹，识别反复失败模式，写一条针对性 harness 更新
4. **Validate**：在新 harness 上评估 holdout set，只有 holdout 准确率提升才保留
5. **Repeat**：用更新后的 harness 继续循环

**可改变的 harness 部分**：
- System prompt
- 工具使用的 lifecycle hooks
- 停止条件和错误处理
- 自定义工具、权限逻辑和 subagents
- 模型周围的其他控制逻辑

**关键学习**：
- Judge-based search 在无标签轨迹上可行
- 持久 trace memory 帮助 proposer 避免重复失败
- Proposer 倾向于过拟合：早期迭代常修复特定轨迹而非写通用行为规则
- 缓解方法："State your change as a rule about agent behavior. If you can only justify it by pointing to specific traces, it's too narrow."
- Proposer prompt 的小改动对优化质量影响大

## Results / Evidence

**Tau-bench v3 airline（50 tasks，35 search / 15 holdout）**：
- Baseline: 67%
- Labeled-search variant: 80%
- **LLM-judge search: 87%**

**最佳改进路径**（3次迭代到达 87%）：
1. 添加 stop condition → holdout 下降（agent 持续幻觉）
2. 重写 system prompt with tool-use rules → holdout 上升但 prompt 开销过大
3. 将业务规则移入 skill → 80%
4. 修正 skill 中的事实错误 → 87%

最终改进来自三个 harness 组件：stop condition + 重写的 system prompt + 包含领域规则的 skill

## Limitations

- 单次运行结果，小基准分割，计划扩展多运行和方差估计
- 当前仅支持 Claude Agent SDK，计划支持 Codex SDK、OpenCode SDK 等

## Links to Concepts

- [[meta-harness]] — 直接相关，同一领域的工作
- [[model-harness]] — meta-agent 改进的对象
- (autoresearch) — 相关的前身工作

## Links to Topics

- [[ai-agents]] — meta-agent 用于改进 agent 系统

## Quotes Worth Preserving

> "State your change as a rule about agent behavior. If you can only justify it by pointing to specific traces, it's too narrow."

> "The proposer prompt matters. Small changes to the proposer's instructions had a large effect on optimization quality."
