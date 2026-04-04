---
title: "Summary — GPU Memory Math for LLMs (2026 Edition)"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/GPU Memory Math for LLMs (2026 Edition).md
links:
  - https://x.com/TheAhmadOsman/status/2040103488714068245
tags: [gpu-memory, quantization, llm-inference, local-llm]
---

# Summary — GPU Memory Math for LLMs (2026 Edition)

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | web (X/Twitter thread)         |
| Author(s)    | @TheAhmadOsman                 |
| Year         | 2026                           |
| Venue        | X/Twitter                      |
| Raw file     | `raw/GPU Memory Math for LLMs (2026 Edition).md` |

## Main Idea

The core formula for estimating VRAM needed to run LLMs locally is: **VRAM (GB) ≈ Parameters (billions) × (effective bits per weight ÷ 8)**. This single formula governs all quantization formats from FP16 to GGUF variants, and the real challenge is not weight storage but the "VRAM tax" from KV cache, activations, batching, and framework overhead.

## Key Details

### Quantization Format Reference

| Format | Bits/Weight | GB per 1B Params | Example: 7B |
|--------|-------------|------------------|-------------|
| FP16/BF16 | 16 | ~2 GB | ~14 GB |
| FP8/INT8 | 8 | ~1 GB | ~7 GB |
| Q6_K | ~6.5 | ~0.82 GB | ~5.7 GB |
| Q5_K | ~5.5 | ~0.69 GB | ~4.8 GB |
| Q4_K | ~4.5 | ~0.56 GB | ~3.9 GB |
| Q3_K | ~3.5 | ~0.43 GB | ~3 GB |
| Q2_K | ~2.5 | ~0.33 GB | ~2.3 GB |
| 4-bit (NF4/etc) | 4 | ~0.5 GB | ~3.5–4 GB |

### Quick Rule of Thumb
- FP16 = 2x model size
- FP8 = 1x model size
- 4-bit = 0.5x model size

### GPU Fit Guide (weights only)

| GPU VRAM | FP16 | FP8 | 4-bit |
|----------|------|-----|-------|
| 8 GB | ~3B | ~6–7B | ~12–13B |
| 16 GB | ~7B | ~13B | ~25B |
| 24 GB | ~10–12B | ~20B | ~35–40B |
| 48 GB | ~20–24B | ~40B | ~70–80B |
| 80 GB (A100) | ~35–40B | ~70B | ~140B-class |

### The VRAM Tax (often ignored)
- **KV cache**: explodes with long context (32K, 128K+)
- **Activations**: vary by runtime, can spike under certain execution paths
- **Batching/concurrency**: multiply memory usage fast, especially in agent workloads
- **Framework overhead**: Transformers, vLLM, TensorRT-LLM, llama.cpp all have different overhead
- **CUDA Graphs**: trade extra reserved memory for better latency/throughput

Rule of thumb: Add 10–30% extra VRAM for a safe run; more for long context and agent workflows.

### MoE Clarification
- "8x7B" sounds like 56B but only a subset of experts run per token
- Compute cost ≠ memory cost
- Total parameters → affects memory footprint
- Active parameters → affects speed
- May still need memory for all experts depending on loading strategy

### GGUF Caveat
Memory numbers for GGUF only apply in llama.cpp-style inference. Move to other frameworks and weights may be dequantized, causing memory usage to jump dramatically.

## Method / Approach (if applicable)

This is an educational thread providing a practical mental model for local LLM deployment. The approach is to reduce all quantization complexity to one formula and practical GPU fit tables.

## Results / Evidence

Practical VRAM calculations for common model sizes:
- 7B: FP16 ~14 GB, FP8 ~7 GB, 4-bit ~3.5–4 GB
- 13B: FP16 ~26 GB, FP8 ~13 GB, 4-bit ~6–7 GB
- 70B: FP16 ~140 GB, FP8 ~70 GB, 4-bit ~35–40 GB
- 405B: FP16 ~810 GB, FP8 ~405 GB, 4-bit ~200+ GB

## Limitations

- Weights-only calculations; actual VRAM needs are significantly higher due to KV cache, activations, and overhead
- GGUF numbers are runtime-specific (llama.cpp); other runtimes may differ substantially
- No empirical benchmarking data — these are rules of thumb
- MoE expert loading strategies vary by implementation

## Links to Concepts

- [[hbm-bandwidth]] — related to GPU memory constraints this guide addresses
- [[gpu-memory-optimization]] — the broader topic of fitting LLMs in GPU memory

## Links to Topics

- [[gpu-memory-optimization]] — this content belongs under GPU memory optimization
- [[high-performance-computing]] — related to HPC memory management

## Quotes Worth Preserving

> "VRAM (in GB) ≈ Parameters (in billions) × (effective bits per weight ÷ 8)"
