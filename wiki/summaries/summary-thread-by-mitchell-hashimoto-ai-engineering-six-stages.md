---
title: "Thread by Mitchell Hashimoto — AI Engineering Six Stages"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/Mitchell Hashimoto把AI工程的每一步都走了一遍，第五步就是所有人都在讨论的Harness Engineering.md
links:
  - https://x.com/GoSailGlobal/status/2041385440826245287
tags: [ai-agents, harness-engineering, self-evolution]
---

# Summary — Thread by Mitchell Hashimoto — AI Engineering Six Stages

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog                           |
| Author(s)    | Mitchell Hashimoto (via @GoSailGlobal) |
| Year         | 2026                           |
| Venue        | x.com / mitchellh.com          |
| Raw file     | `raw/Mitchell Hashimoto把AI工程的每一步都走了一遍，第五步就是所有人都在讨论的Harness Engineering.md` |

## Main Idea

Mitchell Hashimoto (Terraform author) documents his six-stage evolution from "AI is useless" to "always have an Agent running." The pivotal Stage 5—**Harness Engineering**—defines the current frontier: 每次发现 Agent 犯了一个错误，你就花时间设计一个方案，确保它永远不会再犯同样的错误. This converges with Anthropic's and OpenAI's Harness Engineering definitions: systematic engineering constraints, not better prompts.

## Key Details

- **Stage 1 – Ditch the chat window**: Chat mode has high correction cost (反复纠错上下文乱). Need agents that read files, execute commands, send HTTP requests.
- **Stage 2 – Redo your own work**: Manually redo every commit with an Agent, discovering three principles: (1) break big tasks into independent verifiable steps, (2) split vague requests into plan + execute phases, (3) give agents self-verification means.
- **Stage 3 – 30 minutes before knock-off**: Agent-suited for deep research, parallel exploration of uncertain ideas, GitHub issue triage via gh CLI.
- **Stage 4 – Outsource confirmed good work**: Turn off Agent notifications after delegation. Treat Agent as async collaborator to avoid context-switching cost.
- **Stage 5 – Design the Harness** (core): Two forms — (1) **AGENTS.md files** recording known failure modes and corrective instructions (e.g., "when compiling Zig, use `nix develop` not `zig build`"), (2) **verification tools** (screenshot scripts, test filtering) giving agents self-verification capability.
- **Stage 6 – Always one Agent running**: Target state: at least one Agent running at all times during work hours. Currently achieves 10–20% of work hours with an Agent running. Prefers slow deep-mode models (e.g., Amp's deep mode, 30+ min per task) over fast models in parallel.
- **Harness control types** (from 王树义老师): **Guides** (feedforward: code standards, architecture constraints) and **Sensors** (feedback: tests, monitoring). AGENTS.md = Guides; verification tools = Sensors.
- **Architecture-level Harness solution**: Example — 30 PPTs processed serially degrade in quality as design spec gets evicted from context window. Fix: assign each PPT an isolated Agent context. This is Harness-level architecture design, completely orthogonal to prompt quality.

## Method / Approach (if applicable)

Hashimoto's methodology is empirical and iterative: force-use Agents on real work, document every failure mode, then engineer systematic constraints (Harness) to prevent recurrence. This contrasts with prompt optimization approaches.

## Results / Evidence

- Industry convergence: Anthropic's Prithvi Rajasekaran's multi-agent frontend system found that agents cannot self-evaluate — generation and evaluation must be separated.
- OpenAI: 3 engineers, 5 months, 1M lines of code written, zero handwritten. Engineers spent all time designing Agent run constraints.
- Karpathy: has not handwritten code since December.
- Every CEO: 10x experience gap between 90% AI usage and 100% AI usage.
- OpenAI alignment researcher: code is only 10% of work value; remaining 90% is writing specifications.

## Limitations

- Hashimoto notes: delegating to Agent means you don't accumulate skill in that domain — he considers this acceptable trade-off if you maintain manual coding elsewhere.
- Single-person anecdotal evidence; no controlled comparisons.
- "Always one Agent running" at 10–20% of work hours is far from the aspirational "100%" — gap suggests practical bottlenecks.

## Links to Concepts

- [[agent-harness]] — core concept; Hashimoto's Stage 5 is the practical articulation
- [[self-evolving-memory]] — related; Hashimoto's Harness engineering is a form of self-improvement without weight updates
- [[meta-harness]] — related; OpenAI/Anthropic also pursuing harness self-optimization
- [[discipline-agents]] — specialized agent roles, relevant to Stage 2's task decomposition

## Links to Topics

- [[ai-agents]] — primary topic

## Quotes Worth Preserving

> Harness Engineering 极简定义：每次发现 Agent 犯了一个错误，你就花时间设计一个方案，确保它永远不会再犯同样的错误。

> 不要给 Agent 一个模糊的大目标，要拆成一个个可验证的小步骤.

> Karpathy 说他 12 月之后就没手写过一行代码。代码只占你工作价值的 10%，剩下 90% 是写规格说明书.
