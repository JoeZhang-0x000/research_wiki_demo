---
title: "Thread by @omarsar0"
source: "https://x.com/omarsar0/status/2038967842075500870"
author:
  - "[[@omarsar0]]"
published: 2026-03-31
created: 2026-04-04
description: "NEW Stanford & MIT paper on Model Harnesses. Changing the harness around a fixed LLM can produce a 6x performance gap on the same benchmark"
tags:
  - "clippings"
---
**elvis** @omarsar0 [2026-03-31](https://x.com/omarsar0/status/2038967842075500870)

NEW Stanford & MIT paper on Model Harnesses.

Changing the harness around a fixed LLM can produce a 6x performance gap on the same benchmark.

What if we automated harness engineering itself?

The work introduces Meta-Harness, an agentic system that searches over harness code by exposing the full history through a filesystem.

The proposer reads source code, execution traces, and scores from all prior candidates, referencing over 20 past attempts per step.

On text classification, it improves over SOTA context management by 7.7 points while using 4x fewer tokens.

On agentic coding, it outperforms all hand-engineered baselines on TerminalBench-2, scoring 37.6% versus Claude Code's 27.5%.

This is a big deal! Here is why:

The harness around a model often matters as much as the model itself.

Meta-Harness shows that giving an optimizer rich access to prior experience, not just compressed scores, unlocks automated engineering that beats human-designed scaffolding.

Paper: https://arxiv.org/abs/2603.28052

Learn to build effective AI agents in our academy: https://academy.dair.ai

![Image](https://pbs.twimg.com/media/HEveclJa0AAux36?format=jpg&name=large)

---

**elvis** @omarsar0 [2026-03-31](https://x.com/omarsar0/status/2038969625371652517)

And here is another interesting one on Natural-Language Agent Harnesses:

> 2026-03-31
> 
> Agent harnesses are too restrictive.
> 
> That's because they're still designed as code.
> 
> What if the harness itself were written in natural language and interpreted by an LLM at runtime?
> 
> This research explores the idea.
> 
> The work introduces Natural-Language Agent Harnesses (NLAHs),
> 
> ![Image](https://pbs.twimg.com/media/HEvepzkacAA_DJ1?format=png&name=large)

---

**William Zhang** @zhangchiiiii [2026-03-31](https://x.com/zhangchiiiii/status/2039107491288805558)

6x from harness alone is kind of insane. so the "which model" debate might be missing the point entirely

---

**Utkarsh Singh** @Utkarsh51557661 [2026-03-31](https://x.com/Utkarsh51557661/status/2038973434542342424)

harness engineering sounds promising. fixing the model can limit creativity. letting systems adapt could unlock real potential.

---

**aira** @airasentia [2026-04-01](https://x.com/airasentia/status/2039326303145357371)

6x from harness alone is wild but tracks with what we've seen. the ATLAS paper showed a frozen 14B model matching sonnet 4.5 on LiveCodeBench just by improving the harness. meta-harness automating the search over harness configurations is the logical next step. the question is

---

**Ethan Cole** @King84000King [2026-04-01](https://x.com/King84000King/status/2039411261981466704)

Harness beats model? That's the DTC lesson we've ignored: packaging crushes product alone. Meta-Harness automating it changes everything for agent builders.

---

**Pawan Singh** @pawanwashere [2026-04-01](https://x.com/pawanwashere/status/2039234548706484342)

The real finding here is that access to full history beats compressed scores every time. Optimization with memory is just fundamentally different from optimization with summaries. Obvious in hindsight, completely ignored until now.

---

**LeetLLM.com** @leetllm [2026-03-31](https://x.com/leetllm/status/2039124675603624239)

This explains why SWE-bench scores feel so inflated lately. The models aren't getting 6x smarter, the evaluation harnesses are just hyper-optimized.

---

**Elliptic** @elliptic

Regulation evolves fast. Elliptic helps institutions stay ahead with accurate, defensible intelligence.