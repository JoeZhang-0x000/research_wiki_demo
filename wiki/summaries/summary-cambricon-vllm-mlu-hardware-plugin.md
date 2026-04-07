---
title: "Summary — Cambricon vLLM-MLU Hardware Plugin"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/Cambriconvllm-mlu.md
  - https://github.com/Cambricon/vllm-mlu
links:
  - https://github.com/Cambricon/vllm-mlu
tags:
  - vLLM plugin
  - Cambricon MLU
  - Chinese AI chip
  - hardware plugin
  - inference optimization
---

# Summary — Cambricon vLLM-MLU Hardware Plugin

## Source Metadata

| Field        | Value                                               |
|--------------|-----------------------------------------------------|
| Source type  | GitHub README + technical documentation             |
| Author(s)    | Cambricon (寒武纪)                                  |
| Year         | 2025                                                |
| Venue        | https://github.com/Cambricon/vllm-mlu              |
| Raw file     | `raw/Cambriconvllm-mlu.md`                          |

## Main Idea

Cambricon vLLM (vllm-mlu) is a community-developed hardware plugin that ports vLLM to Cambricon's MLU (Machine Learning Unit) AI accelerators, enabling native vLLM features—Chunk Prefill, Prefix Caching, Spec Decode, Graph Mode, Sleep Mode, LoRA, Expert Parallel, KV Transfer—on MLU370+ hardware through a plugin architecture compliant with vLLM's RFC #11162 hardware plugin standard.

## Key Details

**Plugin Architecture:**
- Registered via `vllm.platform_plugins` and `vllm.general_plugins` entry points (`mlu_hijack`)
- `MLUPlatform` class registered as `PlatformEnum.OOT`, dispatching to `torch.mlu`
- `module_mappings` dict redirects 12+ vLLM core modules to Kunlun equivalents (import hook pattern)
- No source-code modification to vLLM required — pure plugin model

**Custom Operators:**
- `apply_rotary` — rotary embedding kernel
- `fused_rms_norm` — fused RMS normalization
- `fused_layer_norm` — fused layer normalization
- `flash_attention` — flash attention implementation
- `split_head_nums` — multi-head attention splitting
- All ops registered via `torch.library` as CUDA backend ops for Fake Tensor compatibility

**Distributed Communication:**
- `MLUCommunicator` extends `BaseCommunicator` via CNCL (Cambricon Collective Communication Library) — not NCCL
- `MLUNCCLCommunicator` provides multi-device tensor parallelism

**Memory Management:**
- `CnMemAllocator` singleton with tag-based memory pooling
- Sleep/wake mode support for memory power management
- Manages MLU device memory explicitly, separate from CUDA memory

**Supported Models:**
- Currently registers `DeepseekV32ForCausalLM` (DeepSeek-V3.2-Exp)
- Day-0 support for DeepSeek-V3.2-Exp (added 2025.09.29)
- Architecture is extensible for additional models via model registry

**Features Supported:**
- Chunk Prefill, Prefix Caching, Spec Decode, Graph Mode, Sleep Mode
- LoRA support
- Expert Parallel (MoE models)
- KV Transfer across devices
- Quantization: weightonly, smoothquant, awq_mlu, gptq_mlu, fp8

**Environment Variables:**
- `VLLM_V1_USE_FULL_GRAPH` — enable full graph capture
- `MLU_GRAPH_CAPTURE_LIST` — specify ops for graph capture
- `MLU_NOSYNCH` — control synchronization behavior

**Hardware Requirement:** MLU370 or above

**Software Stack:**
- Cambricon SDK 25.08
- PyTorch container (torch2.7.1, torchmlu1.28.0)
- Ubuntu 22.04
- Ray 2.43.0 (with MLU-specific patches for distributed execution)

**Installation:**
```bash
# Install vLLM from source (developer mode)
cd vllm-v{version}/
VLLM_TARGET_DEVICE=empty pip install -e .

# Install MLU plugin on top
git clone https://github.com/Cambricon/vllm-mlu
cd vllm-mlu
pip install -e .

# Patch Ray for MLU support
pip install --no-cache-dir --force-reinstall ray==2.43.0
cp __init__.py ${PIP_INSTALL_LOC}/ray/_private/accelerators/
cp mlu.py ${PIP_INSTALL_LOC}/ray/_private/accelerators/
# ... additional Ray MLU patches
```

**Multi-Instance Inference Example:**
```bash
vllm serve ${MODEL_PATH} \
    --port 8100 \
    --max-model-len 40000 \
    --distributed-executor-backend ray \
    --trust-remote-code \
    --tensor-parallel-size 32 \
    --enable-expert-parallel \
    --no-enable-prefix-caching \
    --disable-log-requests \
    --enforce-eager
```

## Method / Approach

Cambricon vLLM follows the plugin architecture defined by vLLM RFC #11162, which standardizes hardware backend registration through Python entry points. The plugin hijacks vLLM's module loading via an import hook system, redirecting core computational modules (attention, layer norm, rotary embedding) to MLU-optimized implementations while presenting a CUDA-compatible interface to the vLLM framework. The key design choice is registering custom ops through `torch.library` as CUDA backend ops, which allows seamless integration with PyTorch's Fake Tensor and compilation infrastructure without requiring changes to upstream vLLM code.

## Results / Evidence

- DeepSeek-V3.2-Exp achieved day-0 support (2025.09.29) — first model to run on vllm-mlu
- 32-device tensor parallel inference demonstrated via offline example
- Supports up to 40,000 max model length
- Expert Parallel mode enables MoE model distribution across MLU devices

## Limitations

- Only one model (`DeepseekV32ForCausalLM`) is explicitly registered; other models require manual extension
- Requires Cambricon SDK 25.08 (not publicly available — must contact ecosystem@cambricon.com)
- Ray integration requires manual patching of 7+ Ray internal files for MLU support
- Only MLU370+ supported (MLU300 series and below not compatible)
- CNCL is a proprietary collective communication library — not as widely documented as NCCL

## Links to Concepts

- [[vLLM Plugin Architecture]] — RFC #11162 hardware plugin standard
- [[Collective Communication]] — CNCL vs NCCL for distributed training
- [[Flash Attention]] — flash_attention custom op implementation
- [[Paged Attention]] — KV cache management on MLU hardware
- [[MoE Expert Parallel]] — expert parallelism for mixture-of-experts models

## Links to Topics

- [[Chinese AI Chips]] — Cambricon MLU in the landscape of Chinese AI accelerators
- [[LLM Inference Engines]] — vLLM and its hardware plugin ecosystem

## Quotes Worth Preserving

> "vllm_mlu支持包括但不限于Chunk Prefill、Prefix Caching、Spec Decode、Graph Mode、Sleep Mode等vLLM原生特性" — vllm-mlu README, describing feature parity with upstream vLLM

> "本镜像仅支持MLU370以上的设备" — hardware requirement limitation stated in README
