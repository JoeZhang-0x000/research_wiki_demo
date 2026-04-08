---
title: "Summary — Optimizing Agentic LM Inference via Speculative Tool Calls"
type: summary
status: draft
created: 2026-04-08
updated: 2026-04-08
sources:
  - raw/2512.15834-optimizing-agentic-lm-inference-speculative-tool-calls.md
links:
  - https://arxiv.org/abs/2512.15834
tags:
  - "AI Agents"
  - "LLM Inference"
  - "Speculative Execution"
---

# Summary — Optimizing Agentic LM Inference via Speculative Tool Calls

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | paper                          |
| Author(s)    | Daniel Nichols, Prajwal Singhania, Charles Jekel, Abhinav Bhatele, Harshitha Menon |
| Year         | 2025                           |
| Venue        | arXiv (cs.PL, cs.AI, cs.DC, cs.PF, cs.SE) |
| Raw file     | `raw/2512.15834-optimizing-agentic-lm-inference-speculative-tool-calls.md` |

## Main Idea

Language model agents suffer severe inference latency because LLM generation and tool execution are strictly serialized—the LLM waits for each tool to complete before generating the next token. This paper introduces **speculative tool calls** (predicting and pre-executing tools before the LLM explicitly requests them) combined with **sequence residency** (keeping frequent tool sequences loaded in memory), achieving throughput improvements of several hundred tokens per second.

## Key Details

- Tool execution accounts for 35%-61% of total agent request time [UNVERIFIED - see PASTE paper for breakdown numbers]
- The paper proposes a **"tool cache" API endpoint** for LM providers to adopt these optimizations without architectural changes
- Speculation must be theoretically analyzed to determine optimal configuration (speculation depth, prediction accuracy thresholds)
- Sequence residency minimizes repeated overhead of loading tool definitions, initializing environments, establishing external connections
- The optimizations are orthogonal to existing LLM serving improvements (batch scheduling, KV cache, etc.)

## Method / Approach

**Speculative Tool Calls:**
1. Predict which tools the LLM will need before it explicitly requests them
2. Pre-execute predicted tools in parallel with continued LLM generation
3. On correct speculation: results are immediately available, no waiting
4. On incorrect speculation: discard results, fall back to normal execution

**Sequence Residency:**
- Keep frequently-used tool sequences resident in the inference engine memory
- Avoids reloading tool definitions, re-initializing environments, re-establishing connections for each request

**Theoretical Analysis:**
- Derive conditions under which speculation is beneficial (based on tool execution time vs. prediction accuracy)
- Analyze optimal speculation depth (how many tools to speculatively execute ahead)

**Tool Cache API (proposed):**
```
POST /v1/tool_cache
{
  "tools": [...],        // Pre-loaded tool definitions
  "sequences": [...],    // Common tool sequences
  "connections": {...}  // Persistent external connections
}
```

## Results / Evidence

- Throughput improvements of **several hundred tokens per second** when hosting inference for LM agents [UNVERIFIED - exact numbers depend on workload characteristics]
- Theoretical analysis provides insights into speculation configurations that yield best performance

## Limitations

- Only abstract/basic details available (TeX source extraction failed); full technical evaluation not reviewed
- Relies on accurate tool prediction—benefit diminishes if prediction accuracy is low
- Does not address parameter prediction challenge (predicting the exact arguments to pass to speculated tools)
- Tool cache API is a proposal; not yet implemented by major LM providers

## Links to Concepts

- [[tool-use]] — speculative execution as an optimization to the standard tool-use loop
- [[llm-serving]] — inference-level optimization for agent workloads
- [[inference-acceleration]] — broader category of techniques to reduce LLM inference latency

## Links to Topics

- [[ai-agents]] — speculative execution as an agent serving optimization
- [[llm-inference-engines]] — tool cache API proposal as a potential extension to serving infrastructure

## Quotes Worth Preserving

> "Language models are becoming increasingly dependent on external tools. While tools greatly improve the capabilities of LMs, they also introduce performance bottlenecks during the inference process." — Abstract
