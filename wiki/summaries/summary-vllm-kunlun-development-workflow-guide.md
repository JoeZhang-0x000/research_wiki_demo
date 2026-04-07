---
title: "Summary — vLLM-Kunlun Development Workflow Guide"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/vLLM-Kunlun：大模型开发流程指南，像用 GPU 一样用昆仑芯.md
  - https://github.com/baidu/vLLM-Kunlun
links:
  - https://zhuanlan.zhihu.com/p/2017693527853786391
tags:
  - vLLM plugin
  - Kunlun XPU
  - Baidu
  - development workflow
  - model adaptation
  - performance tuning
---

# Summary — vLLM-Kunlun Development Workflow Guide

## Source Metadata

| Field        | Value                                               |
|--------------|-----------------------------------------------------|
| Source type  | Conference talk / meetup transcript                |
| Author(s)    | Baidu (百度百舸 + 昆仑芯团队)                       |
| Year         | 2026                                                |
| Venue        | vLLM-Kunlun Meetup 北京站, 2026-03-15             |
| Raw file     | `raw/vLLM-Kunlun：大模型开发流程指南，像用 GPU 一样用昆仑芯.md` |

## Main Idea

vLLM-Kunlun provides a standardized 5-stage workflow for adapting new models to Kunlun XPU: (1)需求对齐, (2) 接口适配, (3) 算子增强, (4) 集成测试, (5) 性能调优. This workflow enabled the open source community to port Qwen3.5 to Kunlun P800 in just 3 days by leveraging vLLM-Kunlun's three-layer CUDA-like compatibility architecture and purpose-built toolchain (torch_xray for precision validation, xpu_profiler for performance analysis).

## Key Details

**Three-Layer CUDA-like Architecture:**

Layer 1 — Programming Model Consistency:
- Kunlun reports itself as a CUDA device to vLLM framework
- Device type query returns "cuda", allowing CUDA-written upper-layer logic to directly reuse
- Zero source-code changes to vLLM core required

Layer 2 — Interface Alignment:
- Kunlun backend memory management APIs designed to mirror `torch.cuda` exactly
- `torch.cuda.max_memory_allocated()` transparently maps to Kunlun implementation
- Developers use standard PyTorch CUDA APIs without hardware awareness

Layer 3 — Flexible Operator Registration:
- Custom Kunlun operators registered via `torch.library` as CUDA backend ops
- Enables "plug-and-play" operator injection
- Fully compatible with Fake Tensor and Torch.compile optimizations

**MIMO-Flash-V2 Adaptation Case Study (real example):**

Challenge: Community had no official vLLM support for MIMO-Flash-V2 (new attention algorithm where K and V heads are unequal)

Steps:
1. Used `vllm.general_plugins` interface to register model networking
2. Redirected linear dependency locations to vLLM-Kunlun's implementations
3. Aligned with community latest code to support unequal K/V head dimensions

Timeline: Kunlun team delivered new operators within **2 days** of request. Operators packaged in kunlun-ops, pip installable. Community then completed model run-through by calling operator interfaces directly.

**Qwen3.5 Adaptation Case Study (3-day total):**

Day 1-2: Initial run-through, precision issue identification (OCRBench score low)
- Used `torch_xray` + automatic Hook tools to dump module-level data on both NV H-card and Kunlun XPU
- Used Baidu's 牵星平台 (Qianxing Platform) for precision diagnosis

Day 2: Precision diagnosis report
- 99.57% model nodes bit-exact aligned with GPU
- 40-layer Transformer backbone networks identical to GPU output
- Only LogitsProcessor (final output layer) had small deviation

Root cause: FC operator precision issue → Issue submitted to Kunlun operator team

Day 3: Operator fix delivered → Kunlun team fixed FC operator in **1 day**

Result: Qwen3.5 on Kunlun P800 passed precision validation, 3 days total.

**Performance Optimization Case 1 — CPU/GPU Sync Overhead:**
- Problem: `causal_conv1d_fn` op needed `cache_indices_cpu` for load balancing, but code used `cache_indices.cpu()` triggering D2H sync
- Fix: Moved `cache_indices_cpu` creation to pre-forward preparation stage, initialized in GDN attention metadata builder
- Result: Eliminated D2H sync overhead during inference, significant performance improvement

**Performance Optimization Case 2 — XPU Memcopy Bottleneck:**
- Problem: TTFT bottleneck from `initial_state[~has_initial_state,...] = 0` causing multiple memory accesses
- Fix: Replaced with Kunlun-specific reshape-and-cache operator
- Result: 20%+ TTFT improvement on 4K input scenario

**Standardized Development Process (5 stages):**
1. 需求对齐 — Requirements alignment with upstream community
2. 接口适配 — Interface adaptation (torch.library registration)
3. 算子增强 — Operator enhancement (custom kernel development)
4. 集成测试 — Integration testing (end-to-end validation)
5. 性能调优 — Performance tuning (profiling and optimization)

**Supported Attention Types:** 5 common attention types supported across 10+ models

**Future Roadmap:**
- Continue tracking vLLM community versions (each major version adapted quickly)
- Full support for existing and next-generation Kunlun chips
- Active upstream contribution to vLLM community
- Expanded Model Zoo support

## Method / Approach

The workflow is organized around minimizing the friction between upstream vLLM releases and Kunlun-specific adaptations. By intercepting at the Model layer (rather than the operator or runtime layer), vLLM-Kunlun can absorb upstream changes with minimal merge conflict. The 牵星平台 (Qianxing Platform) provides automated precision diagnosis by comparing intermediate outputs between GPU and XPU at the module level, enabling systematic narrowing of precision issues.

## Results / Evidence

- Qwen3.5-35B-A3B: 99.57% nodes bit-exact aligned with GPU, 40 Transformer layers identical
- TTFT improvement: 20%+ on 4K input via reshape-and-cache operator replacement
- MIMO-Flash-V2 new attention algorithm supported within 2 days of operator request
- Qwen3.5 fully validated on P800 in 3 days (vs traditional multi-week porting cycles)

## Limitations

- torch_xray and 牵星平台 are Baidu internal tools — external users rely on open source equivalents
- Multi-LoRA performance at 80%+ of non-LoRA (not yet 100%)
- Requires Kunlun3 P800 specifically
- Early stage project — documentation and community resources still maturing

## Links to Concepts

- [[vLLM Plugin Architecture]] — plugin system and RFC #11162
- [[Fused MoE]] — Split_Norm_Rope and Fused MoE operators for P800
- [[Paged Attention]] — KV cache management on XPU
- [[CUDA Compatibility Layer]] — three-layer CUDA-like design

## Links to Topics

- [[Chinese AI Chips]] — Kunlun XPU adaptation workflow
- [[LLM Inference Engines]] — vLLM adaptation methodology
- [[Baidu AI Infrastructure]] — Baidu's AI stack

## Quotes Worth Preserving

> "我们的核心目标，就是『让开发者在昆仑芯上使用 vLLM，感觉就像在用大家最熟悉的 GPU 一样』" — Baidu team, vLLM-Kunlun Meetup 北京站

> "社区伙伴在跑通 Qwen3.5 后，发现 35B 模型在一些 case 下有精度问题，OCRBench benchmark 跑分偏低" — precision issue discovered during community porting

> "最终，仅仅总用时 3 天，就实现了 Qwen3.5 在昆仑芯 P800 上的跑通、跑对" — 3-day porting achievement
