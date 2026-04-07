---
title: "Summary — vLLM-Kunlun Plugin Baidu Kunlun Launch Announcement"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/百度百舸 X 昆仑芯  开源 vLLM-Kunlun Plugin，快速适配新模型、跑出极致性能.md
  - https://github.com/baidu/vLLM-Kunlun
links:
  - https://zhuanlan.zhihu.com/p/1982406667376272869
tags:
  - vLLM plugin
  - Kunlun XPU
  - Baidu
  - Chinese AI chip
  - hardware plugin
  - launch announcement
---

# Summary — vLLM-Kunlun Plugin Baidu Kunlun Launch Announcement

## Source Metadata

| Field        | Value                                               |
|--------------|-----------------------------------------------------|
| Source type  | Blog / product launch announcement                 |
| Author(s)    | Baidu (百度智能云, 百度百舸, 昆仑芯)                |
| Year         | 2025                                                |
| Venue        | https://zhuanlan.zhihu.com/p/1982406667376272869   |
| Raw file     | `raw/百度百舸 X 昆仑芯  开源 vLLM-Kunlun Plugin，快速适配新模型、跑出极致性能.md` |

## Main Idea

Baidu's vLLM-Kunlun Plugin is a production-grade vLLM hardware plugin for Kunlun XPU that solves the core problem of lengthy (3–4 week) invasive custom development cycles whenever vLLM adds new model support. By following RFC #11162 hardware plugin standard, the plugin decouples vLLM's inference engine from the Kunlun XPU backend entirely — new models can be deployed in days, not weeks, with no modification to vLLM core code. The plugin ships with high-performance fused operators, 20+ model support, and Baidu's internal toolchain (torch_xray, xpu_profiler).

## Key Details

**Core Problem Solved:**

Traditional approach: For each new vLLM community model, developers needed 3–4 weeks of invasive source-code modification, leading to code conflicts, upgrade difficulties, and production instability.

vLLM-Kunlun solution: Plugin layers between vLLM engine and Kunlun XPU hardware. New model or new vLLM version → only Plugin layer needs updating → deployment in days.

**Plugin Architecture — Engine Initialization Flow:**

Without plugin: vLLM Engine → Worker (GPU ModelRunner) → Model class (Qwen3MoeForCausalLM) → FlashAttention → CUDA kernels

With vLLM-Kunlun plugin: vLLM Engine → Kunlun Plugin auto-registers → Worker (XPU ModelRunner) → Custom Model class (Qwen3MoeForCausalLM_Kunlun) → Kunlun fused ops → XPU kernels

**Two Adaptation Scenarios:**

Scenario A — vLLM engine upgrade (e.g., V0 → V1):
- Only need to align Plugin to new ModelRunner interface specs
- No changes to Model class or operator layer needed

Scenario B — New model architecture (e.g., DeepSeek-V3.2):
- Only need to update model networking logic inside Plugin
- Reuse existing high-performance operators and scheduling framework
- Incremental development for new operators only

Result: Both scenarios achieve zero intrusion to vLLM core, week→day adaptation cycle.

**High-Performance Fused Operators for P800:**

- `Split_Norm_Rope` — fused normalization + rotary embedding (addresses Attention bottleneck)
- `Fused MoE` — fused mixture-of-experts computation (addresses MoE bottleneck)
- Integrated into `xtorch_ops` (Kunlun operator library), pip-installable

These operators are called seamlessly by vLLM-Kunlun Plugin — no manual invocation required.

**Toolchain (2 key tools):**

torch_xray:
- Operator-level precision debugging
- Automatically compares GPU vs P800 outputs layer by layer
- Rapidly locates numerical deviations
- Available at: `su.bcebos.com/klx-sdk-release-public/xpytorch/dev_kl3/torch_xray/`

xpu_profiler:
- nsys-like performance profiling
- Generates clear operator call timing diagrams
- Identifies performance bottlenecks and compute bubbles
- Available at: `klx-sdk-release-public.su.bcebos.com/v1/xre/xprofiler/release/`

Both tools validated at Baidu scale across multiple business lines.

**20+ Supported Models:**

Generative: Qwen series, DeepSeek series, Llama series, GLM, InternVL multimodal models, GPT OSS

All mainstream open-source models supported. Both community open-source and self-developed private models can be deployed via vLLM-Kunlun.

**Performance Claim:**

DeepSeek, Qwen, Llama, GLM inference throughput and latency on Kunlun P800 "全面对标主流 AI 加速卡" (fully comparable to mainstream AI accelerator cards) — attributed to high-performance fused operators unlocking P800's theoretical compute potential.

**Open Collaboration:**

- GitHub Issues for technical Q&A
- Slack community (vllm-kunlun.slack.com) for experience sharing and version updates
- Welcoming upstream contributions to vLLM main repository
- Transparent planning via GitHub

**Resources:**
| Resource | URL |
|----------|-----|
| vLLM-Kunlun Plugin | github.com/baidu/vLLM-Kunlun |
| torch_xray | su.bcebos.com/klx-sdk-release-public/xpytorch/dev_kl3/torch_xray/latest/ |
| xpu_profiler | klx-sdk-release-public.su.bcebos.com/v1/xre/xprofiler/release/ |

## Method / Approach

The plugin-based architecture is fundamentally an dependency inversion solution: instead of vLLM depending on hardware-specific implementations, the plugin inverts this by having the hardware backend implement a standardized plugin interface that vLLM's engine calls. This is formalized in RFC #11162, which defines the plugin discovery, registration, and execution contract. By building on this standard, Baidu ensures that vLLM-Kunlun tracks upstream vLLM with minimal merge effort.

## Results / Evidence

- Model deployment cycle reduced from 3–4 weeks to days
- 20+ mainstream models supported at launch (December 2025)
- P800 performance "全面对标主流 AI 加速卡" (fully comparable to mainstream AI accelerators)
- Tools (torch_xray, xpu_profiler) already validated at Baidu production scale

## Limitations

- Hardware locked to Kunlun P800 (Kunlun3 generation)
- Requires Ubuntu 22.04, Python >= 3.10
- Early open source (December 2025) — community size and third-party support still building
- torch_xray wheel distribution is a private Baidu URL (not on PyPI) — installation friction for external users

## Links to Concepts

- [[vLLM Plugin Architecture]] — RFC #11162 hardware plugin standard
- [[Fused MoE]] — Split_Norm_Rope and Fused MoE operator design
- [[Paged Attention]] — KV cache on Kunlun XPU
- [[LLM Quantization]] — INT8 quantization support on P800
- [[PyTorch Profiling]] — xpu_profiler as nsys alternative

## Links to Topics

- [[Chinese AI Chips]] — Kunlun XPU in Baidu's AI infrastructure
- [[LLM Inference Engines]] — vLLM plugin ecosystem
- [[Baidu AI Infrastructure]] — Baidu's AI stack

## Quotes Worth Preserving

> "用户只需安装标准 vLLM，再同步安装 vLLM-Kunlun 插件，即可在昆仑芯 XPU 上第一时间部署任意主流大模型，无需修改 vLLM 核心代码，真正实现即插即用" — launch announcement, describing the zero-modification deployment promise

> "新模型或新版本的支持周期从数周缩短至数天，同时确保与社区主干长期兼容，真正实现一次开发，持续演进" — from the launch announcement, contrasting with traditional invasive porting

> "助力开发者高效推进业务落地" — Baidu's stated goal for the toolchain
