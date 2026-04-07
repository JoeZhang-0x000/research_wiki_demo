---
title: "Summary — vLLM-MetaX MACA Hardware Plugin"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/MetaX-MACAvLLM-metax Community maintained hardware plugin for vLLM on MetaX GPU.md
  - https://github.com/MetaX-MACA/vLLM-metax
links:
  - https://github.com/MetaX-MACA/vLLM-metax
  - https://vllm-metax.readthedocs.io/
tags:
  - vLLM plugin
  - MetaX MACA
  - Chinese AI chip
  - hardware plugin
  - inference optimization
---

# Summary — vLLM-MetaX MACA Hardware Plugin

## Source Metadata

| Field        | Value                                               |
|--------------|-----------------------------------------------------|
| Source type  | GitHub README + technical documentation             |
| Author(s)    | MetaX-MACA (MetaX Technologies)                     |
| Year         | 2025–2026                                           |
| Venue        | https://github.com/MetaX-MACA/vLLM-metax            |
| Raw file     | `raw/MetaX-MACAvLLM-metax Community maintained hardware plugin for vLLM on MetaX GPU.md` |

## Main Idea

vLLM-MetaX is a hardware plugin that ports vLLM to MetaX's MACA (MetaX CUDA-Alike) GPU accelerators, providing near-drop-in CUDA compatibility on MetaX hardware through a layered design: MACA presents itself as a CUDA device to PyTorch, while the plugin supplies MetaX-optimized kernels via `mcoplib` (MetaX Collective Operations Library). The plugin follows RFC #11162 (Hardware Pluggable) and RFC #19161 (Enhancing vLLM Plugin Architecture) for clean upstream integration.

## Key Details

**Plugin Architecture (RFC #11162 Compliant):**
- Registered via `vllm.platform_plugins` entry point → `MacaPlatform`
- Two platform classes: `MxsmlMacaPlatform` (NVML-enabled, real hardware) and `NonMxsmlMacaPlatform` (fallback/testing)
- `device_type: "cuda"` and `dispatch_key: "CUDA"` — vLLM treats MACA as a CUDA device semantically
- Supports `pymxsml` (MetaX's NVML equivalent) for device management

**Attention Backends (8 registered):**
| Backend | Class |
|---------|-------|
| FLASHMLA | `vllm_metax.v1.attention.backends.mla.flashmla.MacaFlashMLABackend` |
| FLASHMLA_SPARSE | `vllm_metax.v1.attention.backends.mla.flashmla_sparse` |
| TRITON_MLA | `vllm_metax.v1.attention.backends.mla.triton_mla` |
| FLASH_ATTN | `vllm_metax.v1.attention.backends.flash_attn.MacaFlashAttentionBackend` |
| FLASHINFER | `vllm_metax.v1.attention.backends.flashinfer.MacaFlashInferBackend` |
| TRITON_ATTN | `vllm_metax.v1.attention.backends.triton_attn` |
| TREE_ATTN | `vllm_metax.v1.attention.backends.tree_attn` |
| FLEX_ATTENTION | `vllm_metax.v1.attention.backends.flex_attention` |

**Custom CUDA Kernels (csrc/):**
- `attention/*.cu` — paged attention, flash attention backends
- `moe/*.cu` — grouped_topk, topk_softmax, moe_align_sum, moe_wna16
- `layernorm_kernels.cu`, `layernorm_quant_kernels.cu` — RMSNorm, fused RMSNorm
- `fused_qknorm_rope_kernel.cu` — fused QK normalization with RoPE
- `cache_kernels.cu`, `cache_kernels_fused.cu` — KV cache management
- `quantization/*.cu` — AWQ, GPTQ, compressed tensors

**Quantization Support:**
- AWQ, GPTQ, compressed-tensors, moe_wna16, gguf
- Weight-only quantization and INT8/INT4 inference

**Distributed Communication:**
- `MacaCommunicator` extends `CudaCommunicator` with MetaX-specific optimizations
- `CoArAll2AllManager` for all-reduce-based MoE dispatch/combine (enabled via `MACA_DP_OPT`)
- NCCL as the distributed backend

**Version Matrix (tight vLLM alignment):**
| Plugin | vLLM | Maca SDK | mcoplib |
|--------|------|----------|---------|
| v0.10.2 | v0.10.2 | maca3.2.1.7 | N/A |
| v0.11.2 | v0.11.2 | maca3.3.0.x | 0.2.0 |
| v0.12.0 | v0.12.0 | maca3.3.0.x | 0.3.0 |
| v0.13.0 | v0.13.0 | maca3.3.0.x | 0.3.1 |
| v0.14.0 | v0.14.0 | maca3.5.3.x | 0.4.0 |
| v0.15.0 | v0.15.0 | maca3.5.3.x | 0.4.1 (Latest) |
| v0.17.0 | v0.17.0 | maca3.5.3.x | 0.4.1+ (WIP) |
| v0.18.0 | v0.18.0 | maca3.5.3.x | 0.4.1+ (WIP) |

**Critical Note:** v0.11.2+ moved kernels to separate `mcoplib` package — always use pre-compiled kernels in production.

**Supported Models (35+ text, 20+ multimodal):**
- Text: Llama 3.1/3/2, Qwen 2/3, DeepSeek V2/V3, GLM-4/4V, InternLM 2/3, Mixtral, Baichuan, ChatGLM, Falcon, GPT-NeoX, MPT
- Multimodal: LLaVA-NeXT, Qwen2.5-VL, InternVL 3.5/3.0, GLM-4V, DeepSeek-VL2, LLaVA-NeXT-Video, InternVideo 2.5, Qwen2.5-Omni

**Key Environment Variables:**
- `USE_PRECOMPILED_KERNEL=1` — use mcoplib vs build from source
- `MACA_DP_OPT=1` — enable all2all optimization
- `VLLM_METAX_ENABLE_FA_SPLIT_FORWARD=1` — split prefill/decode attention
- `MACA_VLLM_ENABLE_MCTLASS_FUSED_MOE=0` — enable Cutlass MoE kernels
- `VLLM_FUSED_MOE_CHUNK_SIZE=16*1024` — MoE chunk size

**Branch Strategy:**
- `master` — tracks vLLM main (no functionality guarantee)
- `releases/vX.Y.Z` — stable release branches
- `vX.Y.Z-dev` — development branches
- `v0.16.0` explicitly skipped

## Method / Approach

MetaX's key design insight is "CUDA compatibility through abstraction": MACA presents itself as a CUDA device to PyTorch, allowing vLLM's CUDA-originated code to run without modification at the framework level. The plugin then supplies MetaX-optimized kernels via `mcoplib` (pre-compiled) or `csrc/` (source). This two-layer approach—framework-level CUDA compatibility + kernel-level hardware optimization—minimizes porting effort while preserving performance.

## Results / Evidence

- v0.15.0 (March 2026) — latest stable release, aligned with vLLM v0.15.0
- Hosted vLLM Beijing Meetup (Nov 2025) and Shanghai Meetup (Aug 2025) with distributed inference focus
- 123 GitHub stars as of research date
- Comprehensive 35+ text model and 20+ multimodal model support

## Limitations

- Requires MetaX C-series hardware
- Docker images only available from MetaX developer community (not publicly downloadable)
- `mcoplib` kernels are proprietary pre-compiled binaries — not open source
- Development from source requires `USE_PRECOMPILED_KERNEL=0` build
- Python >= 3.9, < 3.12 required (Python 3.12 not supported)

## Links to Concepts

- [[vLLM Plugin Architecture]] — RFC #11162 and RFC #19161 compliance
- [[FLASHMLA]] — multi-head latent attention backend
- [[Paged Attention]] — MetaX's KV cache implementation
- [[MoE Quantization]] — grouped_topk, moe_align_sum kernels
- [[Collective Communication]] — NCCL-based distributed on MACA

## Links to Topics

- [[Chinese AI Chips]] — MetaX MACA in the AI accelerator landscape
- [[LLM Inference Engines]] — vLLM hardware plugin ecosystem

## Quotes Worth Preserving

> "MACA is a cuda_alike backend and provided near-native CUDA experiences on MetaX Hardware" — vLLM-MetaX README, describing the CUDA compatibility strategy

> "After v0.11.2, vLLM-MetaX moved its `_C` and `_moe_C` kernel into a separate package named `mcoplib`. Please always use mcoplib for production usage." — installation docs, critical production guidance
