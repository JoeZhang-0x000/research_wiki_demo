---
title: Summary — FlashAttention-2 (Dao, 2023)
type: summary
status: stable
created: 2024-01-15
updated: 2026-04-04
sources:
  - raw/paper-flashattention2-2023.md
  - https://arxiv.org/abs/2307.08691
tags: [attention, cuda, memory-efficiency, kernels, iclr2024]
---

# Summary — FlashAttention-2 (Dao, 2023)

## Source Metadata

| Field       | Value                                              |
|-------------|----------------------------------------------------|
| Source type | paper                                              |
| Author(s)   | Tri Dao                                            |
| Year        | 2023 (ICLR 2024)                                  |
| Venue       | ICLR 2024                                          |
| Raw file    | `raw/paper-flashattention2-2023.md`                |

## Main Idea

FlashAttention-2 achieves ~2× speedup over FlashAttention-1 by reducing non-matmul FLOPs and improving parallelism across the sequence length dimension, reaching ~73% of A100 theoretical FLOP/s on the attention forward pass.

## Key Details

- Tiled attention computation avoids materializing the N×N attention matrix in HBM — memory is O(N) instead of O(N²)
- Online softmax normalization maintains numerical correctness without storing intermediate attention weights
- Outer loop (over sequence blocks) is now parallelized across heads AND batch dimensions, not just batch — better GPU occupancy
- Backward pass recomputes attention on-chip to avoid HBM writes; trades FLOPs for bandwidth
- Causal masking skips lower-triangular blocks → ~2× compute reduction for decoder attention
- Forward: ~73% A100 FLOP/s utilization vs ~35% for standard PyTorch attention
- Supports MHA, GQA, MQA variants

## Method / Approach

The kernel is a fused CUDA/Triton implementation. Key algorithmic move: instead of storing the softmax denominator per row (which requires a full row of K), FlashAttention maintains running max and running sum statistics per tile (the Milakov & Gimelshein online softmax), allowing correct normalization without ever seeing the full row simultaneously.

Work partitioning fix: FA-1 assigned one thread block per (batch, head) pair. FA-2 also splits along the sequence dimension, allowing the attention computation to spread across more SMs when batch size or head count is small.

## Results / Evidence

- A100 80GB SXM benchmark, sequence length 2048, head dim 64
- Forward: ~73% FLOP/s vs ~35% (PyTorch), ~50% (FA-1)
- End-to-end GPT-3 training: ~2.2× speedup over baseline attention
- Memory: fits 10× longer sequences than naive attention at same GPU memory budget

## Limitations

- **Acknowledged**: Performance depends heavily on block size; tuning required per GPU architecture
- **Acknowledged**: Recomputation in backward adds FLOPs (~33% overhead)
- **Scope**: The reported benchmarks focus on the kernels and hardware configurations evaluated in the paper rather than exhaustive cross-hardware comparisons

## Links to Concepts

- [[flash-attention]] — this paper is the primary source for the concept page
- [[hbm-bandwidth]] — the IO-bound analysis underpins why FlashAttention works
- online softmax — core algorithmic primitive used in the algorithm

## Links to Topics

- [[gpu-memory-optimization]]

## Quotes Worth Preserving

> "The key insight is that attention is IO-bound, not compute-bound, on modern GPUs."
> — paraphrased from paper introduction (not verbatim)
