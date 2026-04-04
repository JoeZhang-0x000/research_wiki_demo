---
title: GPU Memory Optimization
type: topic
status: draft
created: 2024-01-15
updated: 2026-04-04
sources:
  - raw/paper-flashattention2-2023.md
links: []
tags: [hpc, gpu, memory, ai-infra, optimization]
---

# GPU Memory Optimization

## Scope

This topic covers techniques for reducing GPU memory consumption and improving memory bandwidth utilization in deep learning training and inference workloads. It spans both algorithmic changes (attention tiling, gradient checkpointing) and systems-level techniques (memory pooling, activation offloading).

Explicitly excluded: CPU memory optimization, distributed memory across nodes (see collective communication), and quantization (separate topic).

Domain: **HPC + AI Infra** (cross-cutting)

## Subproblems

1. **HBM bandwidth saturation** — many ops are memory-bound; maximizing bandwidth utilization is the primary lever
2. **Peak memory reduction** — fitting larger batch sizes or longer sequences by reducing intermediate tensor sizes
3. **Activation memory** — activations stored for backward pass often dominate memory during training
4. **KV cache memory** — at inference time, the key-value cache grows with sequence length and batch size
5. **Fragmentation** — memory allocators leave gaps; custom allocators (e.g., PyTorch's caching allocator) help

## Key Approaches

These approaches reduce HBM traffic, lower peak activation storage, or trade extra compute for lower memory pressure.

### Tiled / Fused Kernels
Avoid writing intermediate tensors to HBM by computing within SRAM tiles. The canonical example is [[flash-attention]], which eliminates the O(N²) attention matrix from HBM. Applicable broadly to any elementwise or reduction chain.

### Gradient Checkpointing (Activation Recomputation)
Instead of storing all activations for backward, store only a subset of "checkpoint" activations and recompute the rest during backward. Trades compute for memory. Standard practice in large-model training.

### Mixed Precision Training
Using FP16 or BF16 for forward pass and FP32 for gradient accumulation halves activation memory. Now universal in LLM training. Requires loss scaling or BF16's wider dynamic range.

### KV Cache Compression
At inference, techniques like grouped-query attention (GQA) and multi-query attention (MQA) reduce the KV cache size by sharing keys/values across attention heads. Supported in [[flash-attention]].

### Memory-Efficient Optimizers
Optimizers like Adam store first and second moment estimates (2× model parameters). Alternatives: 8-bit Adam (bitsandbytes), Adafactor (factored second moment), CAME.

## Landscape of Systems / Papers

| Name               | Year | Key Contribution                              |
|--------------------|------|-----------------------------------------------|
| FlashAttention      | 2022 | IO-aware tiled attention, O(N) memory        |
| FlashAttention-2    | 2023 | 2× speedup, better parallelism               |
| FlashAttention-3    | 2024 | Hopper async pipeline support [UNVERIFIED]   |
| DeepSpeed ZeRO      | 2020 | Partition optimizer state/gradients/params   |
| Megatron-LM         | 2019 | Tensor/pipeline parallelism for large models |
| bitsandbytes        | 2022 | 8-bit optimizer states                        |

## Important References

- Dao et al. (2022) — "FlashAttention" — [[summary-flashattention2]] — foundational IO-aware attention
- Rajbhandari et al. (2020) — "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models" — [summary not yet created]
- Shazeer (2019) — "Fast Transformer Decoding: One Write-Head is All You Need" (MQA) — [summary not yet created]

## Open Problems

- Optimal memory-compute tradeoff for very long context (>128K tokens) training [UNVERIFIED]
- Efficient paged KV cache for variable-length batches (vLLM's PagedAttention approach)
- How to best combine activation recomputation with pipeline parallelism without stalls

## Related Topics

- collective communication — cross-node memory movement
