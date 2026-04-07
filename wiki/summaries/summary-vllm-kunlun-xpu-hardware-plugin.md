---
title: "Summary — vLLM-Kunlun XPU Hardware Plugin"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/baiduvLLM-Kunlun vLLM Kunlun (vllm-kunlun) is a community-maintained hardware plugin designed to seamlessly run vLLM on the Kunlun XPU..md
  - https://github.com/baidu/vLLM-Kunlun
links:
  - https://github.com/baidu/vLLM-Kunlun
  - https://vllm-kunlun.readthedocs.io/
tags:
  - vLLM plugin
  - Kunlun XPU
  - Baidu
  - Chinese AI chip
  - hardware plugin
  - inference optimization
---

# Summary — vLLM-Kunlun XPU Hardware Plugin

## Source Metadata

| Field        | Value                                               |
|--------------|-----------------------------------------------------|
| Source type  | GitHub README + technical documentation             |
| Author(s)    | Baidu (百度百舸 + 昆仑芯团队)                       |
| Year         | 2025                                                |
| Venue        | https://github.com/baidu/vLLM-Kunlun               |
| Raw file     | `raw/baiduvLLM-Kunlun vLLM Kunlun (vllm-kunlun) is a community-maintained hardware plugin designed to seamlessly run vLLM on the Kunlun XPU..md` |

## Main Idea

vLLM-Kunlun is a community-maintained hardware plugin by Baidu that ports vLLM to Kunlun XPU accelerators, achieving transparent CUDA emulation through a three-layer "CUDA-like" design: (1) programming model compatibility (device type reported as CUDA), (2) interface alignment (torch.cuda APIs map to Kunlun), and (3) flexible operator registration via torch.library. The plugin delivers near-native GPU performance on Kunlun3 P800 hardware while maintaining full upstream vLLM compatibility through RFC #11162 plugin architecture.

## Key Details

**Plugin Architecture (RFC #11162 Compliant):**
- Registered via `vllm.platform_plugins` and `vllm.general_plugins` entry points
- `KunlunPlatform` returns `device_type="cuda"` but `is_xpu()=True`
- `module_mappings` dict (12+ redirects) hooks vLLM's model loading to Kunlun-specific implementations
- General plugins: `kunlun_model`, `kunlun_tool_parser`, `kunlun_reasoning_parser`

**Custom Operator Libraries:**
- `kunlun_ops` — Kunlun hardware-optimized kernels
- `xspeedgate_ops` — additional performance kernels
- Kernel categories: FlashMLA, PagedAttention, FusedMoE, DeepGEMM FP8, AWQ/GPTQ/Cutlass kernels

**Attention Kernels:**
- `flash_attention_context_vllm_xpu` — flash attention context
- `xft_multi_head_latent_page_attention_block` — DeepSeek MLA (Multi-head Latent Attention) implementation

**MoE Kernels:**
- `moe_pre_small` — MoE pre-processing
- `moe_fc`, `moe_fc_v3` — MoE fully-connected layers
- `moe_post` — MoE post-processing

**Performance Toolchain:**
- `xpu_profiler` — nsys-like performance profiling (available at klx-sdk-release-public)
- `torch_xray` — operator-level precision debugging, dumps GPU vs XPU intermediate outputs for diff analysis
- `TorchCompileWrapperWithCustomDispatcher` — PyTorch inductor backend with Kunlun dispatch

**Supported Models (20+):**
Generative Models: Qwen2, Qwen2.5, Qwen3, Qwen3-Moe, Qwen3-Next, MiMo-V2-Flash, Llama2, Llama3, Llama3.1, gpt-oss, GLM4.5, GLM4.5Air, GLM4.7, GLM5, DeepSeek-R1, DeepSeek-V3, DeepSeek-V3.2

Multimodal: Qwen2-VL, Qwen2.5-VL, Qwen3-VL, Qwen3-VL-MoE, Qwen3-Omni-MoE, InternVL-2.5, InternVL-3.5, InternS1

**Quantization Support:**
- compressed-tensors W4A16
- AWQ MoE W4A16
- DeepSeek-V3.2 W8A8
- GPTQ, INT8/INT4 weight-only quantization

**Performance Benchmarks:**
- 16-way concurrency, input/output size 2048
- DeepSeek-V3.2, Qwen3-35B, Qwen3-Moe tested on P800
- Fused MoE + Split_Norm_Rope operators address Attention and MoE bottlenecks

**Version:** v0.11.0 (latest stable), opened source December 8, 2025
**GitHub Stars:** 388 (as of research date)

**Quick Start:**
```bash
python -m vllm.entrypoints.openai.api_server \
    --host 0.0.0.0 --port 8356 \
    --model <model-path> \
    --gpu-memory-utilization 0.9 \
    --trust-remote-code \
    --max-model-len 32768 \
    --tensor-parallel-size 1 \
    --dtype float16 \
    --max_num_seqs 128 \
    --max_num_batched_tokens 32768 \
    --block-size 128 \
    --distributed-executor-backend mp \
    --served-model-name <model-name>
```

**Architecture (from GitHub README):**
```
vllm-kunlun/
├── vllm_kunlun/
│   ├── platforms/          # Kunlun XPU platform implementation
│   ├── models/              # Model implementations (DeepSeek, Qwen, Llama, etc.)
│   ├── ops/                # Custom operators
│   │   ├── attention/      # FlashMLA, paged attention, merge attention states
│   │   ├── fla/            # Flash linear attention
│   │   └── sample/         # Sampling operators
│   ├── v1/                 # vLLM V1 engine adaptations
│   ├── compilation/         # Torch compile wrapper for Kunlun Graph
│   ├── csrc/               # C++ extensions (custom CUDA-compatible kernels)
│   └── config/             # Model configuration overrides
├── tests/
├── docs/
├── ci/
├── setup.py
└── pyproject.toml
```

## Method / Approach

vLLM-Kunlun's architecture is built on three "disguise" layers that make vLLM believe it is running on CUDA while actually targeting Kunlun XPU. First, device type reporting is spoofed — `torch.cuda.is_available()` returns true and device type is "cuda". Second, memory management and core compute APIs mirror `torch.cuda` exactly, so existing CUDA-originated code in vLLM transparently maps to Kunlun. Third, custom kernels are registered via `torch.library` as CUDA backend ops, enabling Fake Tensor and compilation optimizations. The `module_mappings` import hook redirects 12+ vLLM core modules to Kunlun-specific implementations at load time, providing zero-modification integration with upstream vLLM.

## Results / Evidence

- Qwen3.5-35B adapted on Kunlun P800 in 3 days total (2 days for initial run-through + 1 day for precision fix)
- 99.57% model nodes bit-exact对齐 (bit-exact aligned) with GPU reference implementation
- TTFT (Time To First Token) optimization: 20%+ improvement via reshape-and-cache operator replacement
- 16-way concurrency benchmark on P800 with input/output 2048 tokens

## Limitations

- Requires Kunlun3 P800 hardware (previous generation not supported)
- Ubuntu 22.04 only, Python >= 3.10
- Initial open source (Dec 2025) — relatively early stage (v0.11.0)
- Some advanced features still in development (Multi-LoRA at 80%+ of non-LoRA performance, not 100%)

## Links to Concepts

- [[vLLM Plugin Architecture]] — RFC #11162 hardware plugin standard
- [[FLASHMLA]] — DeepSeek multi-head latent attention implementation
- [[Fused MoE]] — fused mixture-of-experts kernels
- [[Paged Attention]] — vLLM's KV cache management on XPU
- [[PyTorch Compilation]] — TorchCompileWrapper for Kunlun Graph

## Links to Topics

- [[Chinese AI Chips]] — Kunlun XPU in Baidu's AI infrastructure
- [[LLM Inference Engines]] — vLLM hardware plugin ecosystem
- [[Baidu AI Infrastructure]] — Baidu's broader AI stack

## Quotes Worth Preserving

> "让开发者在昆仑芯上使用 vLLM，感觉就像在用大家最熟悉的 GPU 一样" — Baidu team, describing the core design goal of vLLM-Kunlun

> "Plugin 重构推理调度流程，实现社区版本升级零侵入" — vLLM-Kunlun launch article, describing the zero-intrusion upgrade path
