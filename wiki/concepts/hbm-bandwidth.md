---
title: HBM Bandwidth
type: concept
status: draft
created: 2024-01-15
updated: 2026-04-04
sources:
  - raw/paper-flashattention2-2023.md
links: []
tags: [hpc, gpu-hardware, memory, hbm, bandwidth]
---

# HBM Bandwidth

## Definition

High Bandwidth Memory (HBM) bandwidth refers to the data transfer rate between a GPU's stacked DRAM (HBM) and its compute units (SMs). It is measured in TB/s and represents the primary memory bottleneck for memory-bound GPU kernels.

## Why It Matters

Many deep learning operations — including attention, layer normalization, and elementwise ops — are memory-bound: they spend more time reading/writing HBM than doing arithmetic. Understanding HBM bandwidth is essential for kernel optimization in [[flash-attention]], all-reduce operations in collective communication, and AI Infra design.

## Key Properties / Tradeoffs

- **A100 SXM**: ~2 TB/s HBM2e bandwidth
- **H100 SXM**: ~3.35 TB/s HBM3 bandwidth
- **Roofline model**: an operation is memory-bound when its arithmetic intensity (FLOPs / bytes read) falls below the hardware's ops:bytes ratio
- SRAM (shared memory / L2 cache) bandwidth is ~10-20× higher than HBM bandwidth, which is the motivation for tiling techniques like [[flash-attention]]

## Related Concepts

- Used in: [[flash-attention]], [[gpu-memory-optimization]]
- Related: roofline model

## Source Basis

- `raw/paper_flashattention2-2023.md` — IO-bound analysis section

## Open Questions

- How does HBM3e (used in H100 NVL) change the optimal tiling strategy for attention kernels? [UNVERIFIED]
