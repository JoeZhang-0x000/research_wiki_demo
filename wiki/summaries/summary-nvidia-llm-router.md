---
title: "Summary — NVIDIA LLM Router: Route LLM Requests to the Best Model"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/nvidia-ai-blueprints-llm-router-route-llm-requests-to-the-2026-04-04.md
  - https://github.com/NVIDIA-AI-Blueprints/llm-router
tags: []
---

# Summary — NVIDIA LLM Router: Route LLM Requests to the Best Model

## Source Metadata

| Field        | Value                                                       |
|--------------|-------------------------------------------------------------|
| Source type  | web / github / AI blueprint (experimental)                 |
| Author(s)    | NVIDIA AI Blueprints                                       |
| Year         | 2025-2026                                                   |
| Venue        | GitHub (NVIDIA AI Blueprints)                              |
| Raw file     | `raw/nvidia-ai-blueprints-llm-router-route-llm-requests-to-the-2026-04-04.md` |

## Main Idea

LLM Router v2 (experimental) automatically routes user prompts to the optimal LLM or VLM by analyzing content (text + images) and applying either intent-based classification or a trained neural network. The goal is optimizing cost-quality-latency tradeoffs without manual model selection.

## Key Details

- **Two routing strategies**:
  - **Intent-based routing**: uses Qwen 1.7B to classify intents (hard_question, chit_chat, image_understanding, etc.) and map to recommended models
  - **Auto-routing (CLIP + NN)**: uses CLIP embeddings + trained neural network to predict optimal model based on quality/latency/cost metrics
- **Multimodal support**: handles both text and images via base64 data URLs
- **OpenAI API compatible**: returns model recommendations via chat completions endpoint (does NOT proxy — just returns model name)
- **Default model set**:
  | Model | Type | Provider | Use Case |
  |-------|------|----------|----------|
  | gpt-5-chat | Frontier LLM | Azure OpenAI | Complex reasoning |
  | nvidia/nemotron-nano-12b-v2-vl | Open VLM | NVIDIA Build API | Multimodal/image understanding |
  | nvidia/nvidia-nemotron-nano-9b-v2 | Small Open LLM | NVIDIA Build API | Simple text, chit chat |
- **Configurable**: route to any models by updating intent router config or retraining auto-router
- **v1 vs v2 differences**: v1 uses Rust proxy + BERT + Triton; v2 uses NeMo Agent Toolkit + FastAPI + Qwen 1.7B or CLIP+NN

## Method / Approach

Intent-based routing maps user intents to model capabilities via Qwen 1.7B classification. Auto-routing uses CLIP to generate embeddings from text/images, then a trained neural network predicts the best model. Both return model name only — actual API calls are made by the calling application.

## Results / Evidence

No benchmark results provided in the source material — this is a reference blueprint/architecture, not a research paper.

## Limitations

- **Experimental**: v2 not yet backwards compatible with v1
- **Does not proxy**: v2 only returns model recommendations; caller must make actual API call
- **Requires API keys**: NVIDIA Build API, Azure OpenAI (or standard OpenAI)
- **Hardware requirements**: T4+ GPU with 16GB for Qwen 1.7B; CLIP server needs 8GB+ GPU for auto-router training

## Links to Concepts

- [[provider-agnostic-agents]] — router enables transparent model selection
- [[tool-use]] — the router is a tool for model selection in agent workflows

## Links to Topics

- [[ai-agents]]
- [[context-engineering]]

## Quotes Worth Preserving

> In an ideal world the most accurate model would also be the cheapest and fastest, but in practice modern agentic AI systems have to make trade-offs between accuracy, speed, and cost.
