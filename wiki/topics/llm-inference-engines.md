---
title: "LLM Inference Engines"
type: topic
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - https://github.com/Cambricon/vllm-mlu
  - https://github.com/MetaX-MACA/vLLM-metax
  - https://github.com/baidu/vLLM-Kunlun
links:
  - https://github.com/vllm-project/vllm
tags:
  - vLLM
  - hardware plugin
  - inference optimization
  - Chinese AI chips
---

# LLM Inference Engines

## Scope

This topic covers inference engines and hardware plugins for running Large Language Models (LLMs) efficiently on diverse hardware platforms. It focuses on vLLM's plugin architecture and the ecosystem of hardware-specific backends for AI accelerators, including Chinese AI chips (Cambricon MLU, MetaX MACA, Kunlun XPU). Domain: AI Infrastructure.

## Subproblems

1. **Hardware Plugin Architecture** — Standardized plugin interfaces (RFC #11162) for adding new hardware backends to vLLM without modifying core code
2. **Custom Kernel Development** — Hardware-specific CUDA kernels for attention, layer normalization, rotary embedding, and MoE computation
3. **Distributed Communication** — Collective communication backends (CNCL, NCCL) for multi-device tensor parallelism and expert parallelism
4. **Quantization Support** — Weight-only, INT8, and FP8 quantization on non-NVIDIA hardware
5. **CUDA Compatibility Layers** — Techniques for running CUDA-originated code on non-CUDA accelerators (CUDA-like backends, Fake Tensor)

## Key Approaches

### Approach 1: vLLM Hardware Plugin (RFC #11162)

vLLM's plugin system allows hardware vendors to provide backend implementations without forking vLLM. Plugins register via Python entry points, hijack module loading via import hooks, and supply custom operators via `torch.library`. This approach enables day-0 support for new models and zero-modification upstream upgrades.

### Approach 2: CUDA-like Abstraction

Chinese AI chip vendors (MetaX MACA, Kunlun XPU) implement CUDA-compatible backends that report as "cuda" to PyTorch, allowing vLLM's CUDA-originated code to run without modification. Custom kernels are registered as CUDA backend ops via `torch.library`.

## Landscape of Systems / Papers

| System | Hardware | Plugin Type | Key Feature |
|--------|----------|-------------|-------------|
| [[summary-cambricon-vllm-mlu-hardware-plugin]] | Cambricon MLU370+ | CNCL collective, CnMemAllocator | DeepSeek-V3.2-Exp day-0 |
| [[summary-vllm-metax-maca-hardware-plugin]] | MetaX MACA C-series | RFC #11162, mcoplib kernels | 8 attention backends, 35+ models |
| [[summary-vllm-kunlun-xpu-hardware-plugin]] | Kunlun3 P800 | CUDA-like, torch.library | FlashMLA, Fused MoE, 20+ models |
| [[summary-vllm-kunlun-development-workflow-guide]] | Kunlun3 P800 | 5-stage workflow | torch_xray precision, xpu_profiler |
| [[summary-vllm-kunlun-plugin-baidu-kunlun-xin-launch]] | Kunlun3 P800 | RFC #11162 | Zero-intrusion upgrades, toolchain |

## Open Problems

- Most Chinese AI chip vLLM plugins still require proprietary SDKs not publicly available
- mcoplib (MetaX) kernels are pre-compiled binaries, not open source
- Fragmentation: each chip vendor maintains separate plugin repositories
- Performance parity with NVIDIA A/H100 GPUs not yet comprehensively benchmarked against

## Related Topics

[[gpu-memory-optimization]] — KV cache and memory management techniques shared across inference engines
[[llm-quantization]] — quantization methods supported by vLLM plugins
[[high-performance-computing]] — HPC context for accelerator architecture
[[ai-agents]] — inference engines as backends for AI agent runtimes
