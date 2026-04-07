---
title: "Thread by @RajaPatnaik"
source: "https://x.com/RajaPatnaik/status/2041305017781833859"
author:
  - "[[@RajaPatnaik]]"
published: 2026-04-07
created: 2026-04-07
description: "Very cool stuff out of @NousResearch. They open-sourced a system that lets Hermes agents evolve themselves — no GPU training required. It u"
tags:
  - "clippings"
---
**Raja Patnaik** @RajaPatnaik [2026-04-07](https://x.com/RajaPatnaik/status/2041305017781833859)

Very cool stuff out of @NousResearch. They open-sourced a system that lets Hermes agents evolve themselves — no GPU training required.

It uses GEPA to automatically improve skills, prompts, and tool descriptions. Here's how it works:

![Image](https://pbs.twimg.com/media/HFQsGFJaQAA7mG6?format=jpg&name=large)

---

**Raja Patnaik** @RajaPatnaik [2026-04-07](https://x.com/RajaPatnaik/status/2041305030163419221)

The core idea: instead of manually tuning prompts and skills, let an evolutionary optimizer do it.

It uses DSPy + GEPA (Genetic-Pareto Prompt Evolution) — an ICLR 2026 Oral paper — to read execution traces, understand WHY things fail, and propose targeted fixes.

Cost? ~$2-10

---

**Raja Patnaik** @RajaPatnaik [2026-04-07](https://x.com/RajaPatnaik/status/2041305041697726529)

The pipeline is elegant:

Read current skill/prompt → Generate eval dataset → Run GEPA optimization → Produce candidate variants → Evaluate against guardrails → Submit best variant as a PR.

No weight updates. No fine-tuning. Just better prompts, found through evolution.

---

**Raja Patnaik** @RajaPatnaik [2026-04-07](https://x.com/RajaPatnaik/status/2041305053236285737)

What can it evolve?

Phase 1 (done): Skill files

Phases 2-5 (planned): Tool descriptions, system prompts, implementation code, and eventually a continuous self-improvement loop.

Agents that get better at their job automatically. That's the trajectory.

---

**Raja Patnaik** @RajaPatnaik [2026-04-07](https://x.com/RajaPatnaik/status/2041305064766419107)

The safety guardrails are solid: full test suite must pass, size limits enforced, semantic drift detection, caching compatibility checks, and every change goes through human PR review.

No autonomous self-modification without a human in the loop.

---

**Raja Patnaik** @RajaPatnaik [2026-04-07](https://x.com/RajaPatnaik/status/2041305076460065118)

Also check out DSPy and GEPA:

https://dspy.ai

---

**Thin Signal** @thin\_signal [2026-04-07](https://x.com/thin_signal/status/2041377058744656180)

Did they also try with OpenEvolve?

---

**Raja Patnaik** @RajaPatnaik [2026-04-07](https://x.com/RajaPatnaik/status/2041386682323513437)

Good question, @NousResearch?

---

**suhaas** @0x5uh445 [2026-04-07](https://x.com/0x5uh445/status/2041381520389345677)

gepa ftw

---

**Raja Patnaik** @RajaPatnaik [2026-04-07](https://x.com/RajaPatnaik/status/2041386733405974875)

Indeed!

---

**Brando** @APIdeclare [2026-04-07](https://x.com/APIdeclare/status/2041446197869846558)

Now I don't have to learn how to use GEPA...🥳