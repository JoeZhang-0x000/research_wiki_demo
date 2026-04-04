---
title: "Summary — Thread by @lijigang"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/Thread by @lijigang.md
links:
  - https://x.com/lijigang/status/2039361579595272339
tags: [agent-frameworks, llm-architecture, closed-loop-control]
---

# Summary — Thread by @lijigang

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | web (X/Twitter thread)         |
| Author(s)    | @lijigang (李继刚), multiple commenters |
| Year         | 2026                           |
| Venue        | X/Twitter                      |
| Raw file     | `raw/Thread by @lijigang`      |

## Main Idea

A debate on whether AI agent frameworks are fundamentally necessary or merely temporary scaffolding that will become redundant as base models improve. Contributors argue both sides: some believe closed-loop control is intrinsic to intelligence and frameworks will simply move inside the model, while others contend that strong base models eliminate the need for complex orchestration.

## Key Details

- **@lijigang** (originator): Questions whether agent frameworks become redundant if models are strong enough, or if closed-loop control is essential to intelligence itself
- **@tui_te_da_wang**: Removed all multi-tool orchestration in a project, keeping only shell access — model creates/reads notes, queries DB, edits its own responses without "program compression"
- **@578120036X**: Model has "walls" — engineering is needed to harness it
- **@RanRan113080440**: Agent frameworks grow stronger with model capability; model capabilities have plateaued
- **@bydu88c3**: Base model strength sets the ceiling; SFT/RL use human preferences to constrain models; COT/context should not be human-defined; RAG using human guidance is flawed
- **@ShidongKe**: Strong model is still a pure function; needs framework for persistent state and "hands"
- **@YuAnReL**: Model only does next-token prediction; frameworks won't disappear, they'll become part of the model
- **@wsiwsii**: Intelligence本质 is predict-act-update loop; agent framework outside = agent, inside = advanced reasoning
- **@jsyqrt**: "Strength" is multi-dimensional — generative ability vs. execution control are parallel, not causal
- **@mapsnking**: Agent architecture is anthropomorphic workflow; needs explicit trust mechanism; closed-loop is required for commercialization

## Method / Approach (if applicable)

This is a discussion thread, not a research paper. The conversation explores the philosophical and engineering question of whether agent scaffolding is a fundamental requirement or a workaround for model limitations.

## Results / Evidence

No formal results; the thread is a debate synthesizing practitioner perspectives. Key observations:
- Reducing frameworks to minimal shell access can work for certain use cases
- The "6x harness gap" mentioned in other threads suggests framework engineering is currently significant
- Consensus is not reached; perspectives split between "model-centric" and "framework-essential" camps

## Limitations

- This is a social media discussion, not peer-reviewed research
- Claims about model capabilities and framework necessity are anecdotal
- No controlled experiments or systematic evaluation

## Links to Concepts

- [[agent-frameworks]] — core topic of discussion
- [[closed-loop-control]] — central to the debate on whether it's essential to intelligence
- [[model-harness]] — related to the engineering perspective on scaffolding

## Links to Topics

- [[ai-agents]] — the broader topic this thread addresses

## Quotes Worth Preserving

> "智能的本质是预测-行动-更新的闭环，放在模型外叫agent框架，放在模型里面就是高级推理"
> — @wsiwsii

> "模型只能做next token prediction. 框架不会消失/多余，只会变成模型的一部分"
> — @YuAnReL

> "再强的模型也只是纯函数 需要框架去搭建持久化状态和手脚"
> — @ShidongKe
