---
title: "Thread by @yoonholeee"
source: "https://x.com/yoonholeee/status/2038640635482456118"
author:
  - "[[@yoonholeee]]"
published: 2026-03-30
created: 2026-04-04
description: "How can we autonomously improve LLM harnesses on problems humans are actively working on? Doing so requires solving a hard, long-horizon cr"
tags:
  - "clippings"
---
**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038640635482456118)

How can we autonomously improve LLM harnesses on problems humans are actively working on?

Doing so requires solving a hard, long-horizon credit-assignment problem over all prior code, traces, and scores.

Announcing Meta-Harness: a method for optimizing harnesses end-to-end

![Image](https://pbs.twimg.com/media/HEq02pQakAERs85?format=jpg&name=large)

---

**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038640660815937856)

The key idea is simple:

\- Use a coding agent as the proposer

\- Give it filesystem access to the full history of prior experience (this directory gets very big)

Our iterative loop lets the agent try different ideas while selectively inspecting a very long raw history.

![Image](https://pbs.twimg.com/media/HEq029taEAEKQxo?format=jpg&name=large)

---

**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038640665647837451)

We find that unrestricted access to all previous history is essential in our settings, because the dependencies are so long-horizon.

Previous text optimization loops that only see rewards/summaries/previous attempts discard important information and underperform here.

![Image](https://pbs.twimg.com/media/HEq04bAbUAAwQhT?format=jpg&name=large)

---

**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038640670714581375)

We make progress on optimizing harnesses for TerminalBench-2.

The proposer, after reading dozens of files (82 median), reasons through why its previous attempts failed to form a targeted hypothesis. It's surprisingly similar to how a human engineer might approach this problem

![Image](https://pbs.twimg.com/media/HEq04soasAAyafg?format=png&name=large)

---

**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038640672950173943)

Meta-Harness is itself a harness: one whose purpose is to optimize other harnesses.

It's a new instantiation of classic meta-learning ideas, with even less imposed structure:

1\. Let an agent inspect any part of prior attempts

2\. Give it a good hill to climb

---

**Gregor** @bygregorr [2026-03-30](https://x.com/bygregorr/status/2038681568173027646)

The framing assumes better harnesses are the bottleneck. But if the LLM can't reason through the problem yet, optimizing the eval scaffold just gets you a faster way to measure the same ceiling. What signals are you using to distinguish harness failure from model failure?

---

**Yoonho Lee** @yoonholeee [2026-03-30](https://x.com/yoonholeee/status/2038687734697701582)

Agreed; harness optimization has a ceiling set by the model weights.

The way I view this is that LLM systems have two components: (1) the model, (2) the harness. The harness definitely matters for hard problems; look at, e.g., the amount of prompt/agent engineering people do

1/2

---

**Graham Neubig** @gneubig [2026-03-31](https://x.com/gneubig/status/2038789475057213714)

Very nice work, I'm excited to dig in further!

This seems very similar conceptually to Darwin-Godel machines and other similar papers: https://arxiv.org/abs/2505.22954

Could you give a quick summary about how this relates to previous work like this?

---

**Yoonho Lee** @yoonholeee [2026-03-31](https://x.com/yoonholeee/status/2038822240259895626)

Thank you!

I just read DGM, so I may be missing some details, but two differences stand out to me:

1\. DGM's focus is on recursive self-improvement from scratch, whereas we start from ~SOTA harnesses (ACE, Terminus-KIRA) and try to push the frontier

2\. A key finding for us is

---

**Temoor Tanveer** @ttanvali [2026-03-30](https://x.com/ttanvali/status/2038653641100304614)

Very cool work Yoonho!

Any intuitions behind on why full history outperforms other evolutionary systems?

If the evals are fast enough I would imagine running 100s of AlphaEvolve style iterations would outperform a single trajectory no?