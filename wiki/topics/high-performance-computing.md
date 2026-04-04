---
title: High-Performance Computing
type: topic
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/paper-flashattention2-2023.md
  - raw/bai-lab-memoryos-emnlp-oral-memoryos-is-2026-04-04.md
  - raw/raphaelmansuy-edgequake-high-performance-graphrag-inspired-from-2026-04-04.md
links: []
tags: [hpc, ai-infra, systems]
---

# High-Performance Computing

## Scope

This topic covers systems and algorithmic techniques aimed at maximizing throughput, minimizing latency, and using hardware efficiently in compute-intensive AI workloads. In this repo it appears mainly through GPU memory optimization, low-latency retrieval systems, and fast agent-memory backends.

It excludes general software performance advice that is not tied to hardware-aware or large-scale execution concerns.

Domain: **HPC + AI Infra**

## Subproblems

1. **Memory bandwidth** - reducing movement to and from expensive memory tiers.
2. **Parallelization** - structuring work across threads, devices, or services.
3. **Latency** - keeping interactive systems responsive even with heavy pipelines.
4. **Storage/query efficiency** - retrieving state fast enough for online use.
5. **Benchmarking** - comparing systems with workload-relevant metrics.

## Key Approaches

### Kernel and memory optimization

FlashAttention-style work improves utilization by restructuring the computation itself around hardware constraints such as HBM bandwidth and SRAM locality.

### Runtime and service optimization

Systems like MemoryOS and EdgeQuake pursue performance through backend engineering, parallel pipelines, and storage/runtime choices that keep memory or retrieval on the critical path.

## Landscape of Systems / Papers

| Name | Year | Key Contribution | Link |
|------|------|------------------|------|
| FlashAttention-2 | 2023 | IO-aware attention with improved parallelism | [[summary-flashattention2]] |
| MemoryOS | 2025 | Faster hierarchical memory pipeline with reported 5x latency reduction | [[summary-memoryos-emnlp2025]] |
| EdgeQuake | 2026 | Rust GraphRAG system positioned around high performance | [[summary-edgequake]] |

## Important References

- [[summary-flashattention2]] - canonical GPU memory/bandwidth example.
- [[summary-memoryos-emnlp2025]] - shows HPC concerns in an agent-memory stack.
- [[summary-edgequake]] - production-minded GraphRAG implementation in Rust.

## Open Problems

- Which benchmarks capture both offline throughput and online latency for agent infrastructure?
- How do memory-centric optimizations interact with increasingly long-context models?
- What performance tradeoffs are acceptable when transparency or observability features are added?

## Related Topics

- [[gpu-memory-optimization]]
- [[graph-rag-systems]]
- [[memory-management]]
