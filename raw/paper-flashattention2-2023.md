# [RAW SOURCE — DO NOT EDIT]
# Source: FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning
# Authors: Tri Dao
# Venue: ICLR 2024
# URL: https://arxiv.org/abs/2307.08691
# Added: 2024-01-15
# Note: This is a manually captured excerpt for demonstration. Not verbatim paper text.

---

FlashAttention-2 is an improved version of FlashAttention that achieves better GPU utilization
through two main changes: (1) reducing non-matmul FLOPs, and (2) better parallelism across
the sequence length dimension.

Key observations from the paper:

- Standard attention requires O(N²) memory. FlashAttention reduces this to O(N) by tiling
  the attention computation and using online softmax normalization.

- FlashAttention-2 achieves ~2x speedup over FlashAttention-1 on A100 GPUs.

- The main bottleneck in FlashAttention-1 was suboptimal work partitioning between warps,
  leading to unnecessary shared memory reads/writes.

- FlashAttention-2 partitions work differently: the outer loop over sequence blocks is
  parallelized across attention heads AND batch dimensions, maximizing occupancy.

- For the backward pass, FlashAttention-2 does not store the full N×N attention matrix;
  instead it recomputes attention on-chip during backward to save HBM bandwidth.

- Benchmarks on A100 (80GB SXM): forward pass reaches ~73% of theoretical FLOP/s of A100,
  compared to ~35% for standard PyTorch attention.

- causal masking is handled by skipping computation on the lower-triangular blocks, giving
  roughly 2x speedup for causal vs. non-causal attention.

- The technique is IO-bound, not compute-bound. The key insight: HBM bandwidth is the
  bottleneck, not arithmetic throughput.

Implementation notes:
- Written in CUDA/Triton
- Fused kernel: QKV projections, attention, and output projection in one kernel call reduces
  memory reads/writes to HBM
- Supports multi-head attention, grouped-query attention (GQA), and multi-query attention (MQA)
