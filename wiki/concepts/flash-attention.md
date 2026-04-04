---
title: Flash Attention
type: concept
status: stable
created: 2024-01-15
updated: 2026-04-04
sources:
  - raw/paper-flashattention2-2023.md
  - "https://arxiv.org/abs/2307.08691"
links: []
tags: [attention, cuda, memory-efficiency, kernels, transformer]
---

# Flash Attention

## Definition

Flash Attention is a family of IO-aware exact attention algorithms that compute the standard scaled dot-product attention while avoiding materializing the full N×N attention matrix in high-bandwidth memory (HBM). It achieves this through tiled computation and online softmax normalization performed entirely in SRAM.

## Why It Matters

Transformer self-attention has O(N²) memory and compute complexity with respect to sequence length. For long sequences, the N×N attention matrix dominates GPU memory consumption and HBM bandwidth becomes the primary bottleneck—not arithmetic throughput. Flash Attention reorders the computation to be IO-optimal, enabling training of models on significantly longer sequences without memory overflow and with wall-clock speedups. It is now a standard component of production LLM training stacks. See also: [[gpu-memory-optimization]].

## How It Works

Flash Attention splits Q, K, and V into tiles that fit in SRAM. For each tile:

1. Load a block of Q from HBM into SRAM
2. Loop over blocks of K and V, loading each into SRAM
3. Compute partial attention scores and maintain a running softmax normalization (the "online softmax" trick)
4. Accumulate the weighted V sum
5. Write only the final output back to HBM

**FlashAttention-2 improvements** over v1:
- Reduces non-matmul FLOPs (non-matmul ops are ~4× slower on Tensor Cores)
- Outer loop parallelized across sequence blocks AND attention heads AND batch dimension → better GPU occupancy
- Backward pass recomputes attention on-chip instead of storing it → avoids large intermediate writes

**Causal masking**: lower-triangular blocks are entirely skipped, yielding ~2× speedup for decoder-only attention.

## Key Properties / Tradeoffs

- **Memory complexity**: O(N) vs O(N²) for naive attention — the N×N matrix is never fully materialized in HBM
- **Compute**: exact (no approximation) — output is numerically identical to standard attention
- **Throughput (A100)**: FlashAttention-2 achieves ~73% of A100 theoretical FLOP/s on forward pass; naive PyTorch reaches ~35%
- **Backward pass**: requires recomputation of attention during backward (extra FLOPs traded for reduced HBM reads)
- **Sequence length limit**: bounded by SRAM size per SM — very long sequences require careful block size tuning
- **Variants supported**: MHA, GQA (grouped-query attention), MQA (multi-query attention)

## Related Concepts

- Builds on: online softmax
- Contrasts with: sparse attention (approximate vs exact)
- Used in: [[gpu-memory-optimization]], transformer training infrastructure
- Related hardware concept: [[hbm-bandwidth]]

## Source Basis

- [[summary-flashattention2]] — primary source
- `raw/paper_flashattention2-2023.md` — full extracted notes

## Open Questions

- What is the optimal block size for H100 NVL (HBM3e bandwidth profile differs from A100)?
- How does FlashAttention-3 compare quantitatively on Hopper-class GPUs?
- Does the recomputation cost in backward become prohibitive for very deep models?
