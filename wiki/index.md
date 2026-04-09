---
title: Knowledge Base Index
type: index
updated: 2026-04-07
---

# Research Wiki — Index

Knowledge base covering: **High-Performance Computing**, **AI Infrastructure**, **AI Agents**

---

## Topics

| Topic | Description | Status |
|-------|-------------|--------|
| [[agent-memory-systems]] | Persistent memory layers that let agents retain and recall prior knowledge across sessions | draft |
| [[ai-agents]] | Runtime and workflow patterns for autonomous systems that plan, use tools, and manage state | draft |
| [[coding-agents]] | Agent systems specialized for navigating, editing, and executing against codebases | draft |
| [[context-engineering]] | Techniques for selecting, compressing, and projecting context into model prompts | draft |
| [[graph-rag-systems]] | Retrieval systems that combine vector search with explicit graph structure | draft |
| [[gpu-memory-optimization]] | Techniques for reducing GPU memory usage and improving bandwidth utilization | draft |
| [[high-performance-computing]] | Hardware-aware performance work across AI infrastructure and memory-heavy systems | draft |
| [[llm-inference-engines]] | vLLM and hardware plugins for LLM inference on diverse accelerators including Chinese AI chips | draft |
| [[llm-quantization]] | Methods for quantizing LLM weights, activations, and KV cache to reduce memory and accelerate inference | draft |
| [[markdown-knowledge-bases]] | File-native knowledge workflows built from raw markdown sources, summaries, and indexes | draft |
| [[memory-management]] | Storage, updating, retrieval, and lifecycle control for agent memory systems | draft |
| [[fundamental-physics]] | Deep questions about spacetime, gravity, particle physics, and the nature of reality | draft |

---

## Concepts

This section collects the atomic knowledge units that topic and summary pages build on.

### AI Infra / HPC

| Concept | One-line summary | Status |
|---------|-----------------|--------|
| [[flash-attention]] | IO-aware tiled attention that avoids materializing the N×N attention matrix | stable |
| [[graph-rag]] | Retrieval-augmented generation that uses explicit graph structure during recall | draft |
| [[hbm-bandwidth]] | GPU HBM data transfer rate — primary bottleneck for memory-bound kernels | draft |
| [[markdown-knowledge-base]] | Linked markdown corpus that agents can compile, query, and maintain | draft |
| [[persistent-agent-memory]] | Durable memory layer that preserves useful knowledge across agent sessions | draft |
| [[virtual-filesystem-interface]] | Filesystem-shaped abstraction over indexed or virtualized knowledge stores | draft |

### AI Agents

| Concept | One-line summary | Status |
|---------|-----------------|--------|
| [[agent-frameworks]] | Runtime architectures combining LLM with tools, state, and execution policies | draft |
| [[agent-harness]] | Runtime layer that combines model, tools, state, and execution policy into an agent | draft |
| [[closed-loop-control]] | Control architecture where agents continuously observe and update based on feedback | draft |
| [[meta-harness]] | Harness that optimizes other harnesses via full-history filesystem access | draft |
| [[model-harness]] | Evaluation scaffolding (prompting, tools, context) surrounding a fixed LLM | draft |
| [[terminalbench]] | Benchmark for agentic coding tasks in terminal/shell environments | draft |
| [[claude-code]] | Terminal-native coding agent used as a reference point by several open-source projects | draft |
| [[gepa]] | Genetic-Pareto Prompt Evolution: evolutionary prompt optimization without weight updates | draft |
| [[agent-trust-protocol]] | HTTPS-equivalent trust infrastructure for AI agents: cryptographic identity, signed messages, tamper-evident memory | draft |
| [[context-database]] | Context store built around agent browseability rather than flat retrieval only | draft |
| [[discipline-agents]] | Specialized agent roles used inside a coordinated multi-agent workflow | draft |
| [[hashline-edit-tool]] | Content-addressed editing approach that guards against stale-line changes | draft |
| [[hierarchical-memory]] | Multi-tier memory layout that separates state by lifetime and retrieval cost | draft |
| [[locomo-benchmark]] | Shared benchmark reference used by several agent-memory systems in this repo | draft |
| [[long-term-memory]] | Durable memory that persists useful knowledge across sessions | draft |
| [[lsp-integration]] | Language Server Protocol support for semantic code navigation and refactoring | draft |
| [[mem0]] | Productized agent-memory system with multi-level memory and search APIs | draft |
| [[memgpt]] | Foundational literature reference for OS-style memory thinking in agents | draft |
| [[memory-search]] | Retrieval step that finds relevant stored memories for the current task | draft |
| [[mcp-server]] | Model Context Protocol server exposing memory/tools via standard interface | draft |
| [[middleware-pattern]] | Composable runtime layers for retries, compaction, and related concerns | draft |
| [[memory-operating-system]] | OS-inspired hierarchical memory with Storage/Updating/Retrieval/Generation modules | draft |
| [[multi-level-memory]] | Memory architecture with separate user, session, and agent state tiers | draft |
| [[openclaw]] | Agent framework used as a host runtime for memory plugins in several sources | draft |
| [[provider-agnostic-agents]] | Agents designed to work across multiple model providers or local backends | draft |
| [[recursive-retrieval]] | Retrieval strategy that drills from coarse context regions to finer detail | draft |
| [[self-evolving-memory]] | Memory that is continuously updated, consolidated, or reorganized over time | draft |
| [[session-management]] | Handling multi-turn state, compaction, and persistence boundaries | draft |
| [[skill-embedded-mcps]] | MCP servers loaded on demand as part of a skill package | draft |
| [[skills-system]] | Modular task-specific instruction and capability packages for agents | draft |
| [[source-map-reverse-engineering]] | Recovering source trees from shipped bundles and source maps | draft |
| [[sub-agent-orchestration]] | Delegating bounded work to multiple narrower agents | draft |
| [[superagent-harness]] | Orchestration-heavy harness for long-horizon, multi-stage tasks | draft |
| [[sandbox-isolation]] | Constraining agent execution inside limited environments | draft |
| [[three-tier-context]] | Three-level context hierarchy for coarse-to-fine retrieval | draft |
| [[tool-use]] | Calling external tools such as shell, files, search, or MCP servers | draft |
| [[ultrawork]] | Aggressive multi-agent completion mode aimed at preventing premature stopping | draft |
| [[universal-memory-layer]] | Shared memory abstraction between applications and model calls | draft |
| [[visualized-retrieval]] | Inspectable view of the path a retrieval system took | draft |

### Agent Memory

| Concept | One-line summary | Status |
|---------|-----------------|--------|
| [[agent-memory-taxonomy]] | Survey taxonomy organizing memory by forms, functions, and dynamics | draft |
| [[experiential-memory]] | Stored lessons, procedures, and reusable know-how from prior work | draft |
| [[factual-memory]] | Durable store of preferences, constraints, and other declarative facts | draft |
| [[working-memory]] | Actively maintained task state used in the current interaction | draft |

### Physics / Foundations

| Concept | One-line summary | Status |
|---------|-----------------|--------|
| [[holographic-principle]] | Information encoded on boundary scaling with area, not volume | draft |
| [[gauge-theory]] | Field theory with redundancy under symmetry transformations | draft |
| [[quantum-gravity]] | Unifying quantum mechanics with general relativity | draft |
| [[standard-model]] | Particle physics model: SU(3)×SU(2)×U(1)/Z₆ with quarks, leptons, gauge bosons | draft |
| [[measurement-problem]] | Why quantum measurement yields definite outcomes | draft |

### Candidate Future Pages

The following concepts are useful follow-up pages for expanding the wiki:

- `online-softmax` — linked from [[flash-attention]]
- `sparse-attention` — linked from [[flash-attention]]
- `collective-communication` — linked from [[gpu-memory-optimization]]
- `transformer-training-infrastructure` — linked from [[flash-attention]]
- `roofline-model` — linked from [[hbm-bandwidth]]

---

## Summaries

| Summary | Source | Topic |
|---------|--------|-------|
| [[summary-am-memory]] | am-memory repository (danielwanwx, 2026) | [[agent-memory-systems]] |
| [[summary-agent-memory-survey]] | "Memory in the Age of AI Agents" survey repo (Shichun-Liu, 2025) | [[memory-management]] |
| [[summary-claude-code-sourcemap]] | claude-code-sourcemap (leeyeel, 2026) | [[agent-memory-systems]] |
| [[summary-deer-flow]] | DeerFlow repository (bytedance, 2026) | [[agent-memory-systems]] |
| [[summary-edgequake]] | EdgeQuake repository (raphaelmansuy, 2026) | [[graph-rag-systems]] |
| [[summary-flashattention2]] | FlashAttention-2 paper (Dao, ICLR 2024) | [[gpu-memory-optimization]] |
| [[summary-gpu-memory-math-for-llms-2026-edition]] | VRAM formula guide for running LLMs locally (2026) | [[gpu-memory-optimization]] |
| [[summary-graph-memory]] | graph-memory repository (adoresever, 2026) | [[agent-memory-systems]] |
| [[summary-karpathy-knowledge-base-thread]] | Karpathy thread on LLM knowledge bases (2026) | [[markdown-knowledge-bases]] |
| [[summary-thread-by-lijigang]] | Thread on whether agent frameworks are necessary (2026) | [[ai-agents]] |
| [[summary-thread-by-gittrend0x]] | GitHub trending agent projects analysis (2026) | [[ai-agents]] |
| [[summary-thread-by-indigox]] | Anthropic diff tool: model behavioral alignment features (2026) | [[ai-agents]] |
| [[summary-mem0]] | mem0 repository (mem0ai, 2026) | [[agent-memory-systems]] |
| [[summary-memoryos-emnlp2025]] | MemoryOS paper (BAI-LAB, EMNLP 2025) | [[agent-memory-systems]] |
| [[summary-mintlify-virtual-filesystem]] | Mintlify virtual filesystem writeup (2026) | [[markdown-knowledge-bases]] |
| [[summary-oh-my-openagent]] | oh-my-openagent repository (code-yeongyuoh, 2026) | [[agent-memory-systems]] |
| [[summary-open-harness]] | open-harness repository (MaxGfeller, 2026) | [[agent-memory-systems]] |
| [[summary-opencode]] | opencode repository (anomalyco, 2026) | [[agent-memory-systems]] |
| [[summary-openviking]] | OpenViking repository (volcengine, 2026) | [[agent-memory-systems]] |
| [[summary-thread-by-omarsar0]] | Stanford/MIT paper on Meta-Harness automated harness engineering (2026) | [[ai-agents]] |
| [[summary-claude-code-hooks]] | Claude Code hooks thread (zodchiii, 2026) | [[coding-agents]] |
| [[summary-anthropic-diff-tool]] | Anthropic model diffing research (2026) | [[ai-agents]] |
| [[summary-thread-by-yoonholeee]] | Meta-Harness author announcement thread (2026) | [[ai-agents]] |
| [[summary-perplexica]] | Perplexica search engine (BunsDev, 2026) | [[ai-agents]] |
| [[summary-how-to-build-your-second-brain]] | Karpathy-inspired second brain: three folders + schema file + AI compilation (2026) | [[markdown-knowledge-bases]] |
| [[summary-nvidia-llm-router]] | NVIDIA LLM Router blueprint (2026) | [[ai-agents]] |
| [[summary-kvmix-gradient-based-layer-importance-kv-cache-2025]] | Gradient-based layer importance mixed-precision KV cache quantization (2025) | [[llm-quantization]] |
| [[summary-bitdecoding-tensor-cores-long-context-2025]] | Low-bit KV cache with tensor core optimization for long-context decoding (2025) | [[llm-quantization]] |
| [[summary-kvtuner-sensitivity-aware-kv-cache-2025]] | Auto-tuning per-layer precision for KV cache quantization (2025) | [[llm-quantization]] |
| [[summary-sageattention-8bit-attention-2024]] | Accurate 8-bit attention for plug-and-play inference acceleration (2024) | [[llm-quantization]] |
| [[summary-flexq-int6-llm-serving-2025]] | INT6 quantization via algorithm-system co-design for LLM serving (2025) | [[llm-quantization]] |
| [[summary-abq-llm-arbitrary-bit-quantization-2024]] | Arbitrary bit-width quantization for LLM inference (2024) | [[llm-quantization]] |
| [[summary-hcattention-extreme-kv-cache-compression-2025]] | Extreme KV cache compression via heterogeneous attention (2025) | [[llm-quantization]] |
| [[summary-binary-weight-activation-llm-ptq-2025]] | Binary weight and activation quantization post-training (2025) | [[llm-quantization]] |
| [[summary-bitnet-v2-4bit-activations-hadamard-2025]] | Native 4-bit activations for 1-bit LLMs via Hadamard transformation (2025) | [[llm-quantization]] |
| [[summary-kvquant-10m-context-2024]] | 3-bit KV cache quantization enabling 10M context length (NeurIPS 2024) | [[llm-quantization]] |
| [[summary-qserv-w4a8kv4-llm-serving-2024]] | W4A8KV4 system co-design: 3x dollar cost reduction for LLM serving (2024) | [[llm-quantization]] |
| [[summary-compression-scaling-laws-unifying-2025]] | Unified scaling laws for sparsity and quantization compression (2025) | [[llm-quantization]] |
| [[summary-channel-wise-mixed-precision-quantization-2024]] | Channel-wise mixed-precision weight quantization (2024) | [[llm-quantization]] |
| [[summary-bitnet-cpu-inference-2024]] | bitnet.cpp: fast BitNet b1.58 inference on CPUs (2024) | [[llm-quantization]] |
| [[summary-daq-density-aware-weight-only-2024]] | Density-aware weight-only quantization with 22.8% less perplexity loss (2024) | [[llm-quantization]] |
| [[summary-stbllm-structured-binary-2024]] | Structured binary LLMs breaking the 1-bit barrier (2024) | [[llm-quantization]] |
| [[summary-kivi-2bit-kv-cache-2024]] | Tuning-free 2-bit KV cache: per-channel Key, per-token Value (ICML 2024) | [[llm-quantization]] |
| [[summary-smoothquant-8bit-llm-2022]] | W8A8 quantization via outlier migration: 530B on single node (ICML 2023) | [[llm-quantization]] |
| [[summary-wkvquant-weight-kv-cache-2024]] | Joint weight and KV cache quantization (2024) | [[llm-quantization]] |
| [[summary-finequant-fine-grained-weight-only-2023]] | Adaptive fine-grained granularity for weight-only quantization (2023) | [[llm-quantization]] |
| [[summary-gptq-accurate-post-training-2022]] | GPTQ: 175B in 4 GPU hours to 4-bit, ICLR 2023 | [[llm-quantization]] |
| [[summary-atom-lowbit-quantization-2023]] | W4A4 serving: 7.7x throughput vs FP16 (2023) | [[llm-quantization]] |
| [[summary-neural-machine-translation-4bit-2019]] | Early 4-bit NMT quantization with log quantization and error feedback (2019) | [[llm-quantization]] |
| [[summary-observers-are-all-you-need]] | Observer Patch Holography: physics from observer-overlap consistency on holographic screens (2026) | [[fundamental-physics]] |
| [[summary-搞懂缓存机制从gemma4到claude-code省80token]] | KV cache原理 + Claude Code缓存工程：省3-5倍token (2026) | [[llm-quantization]] |
| [[summary-苏格拉底追问维特根斯坦拆解波兰尼兜底我的系统再次升级]] | 苏格拉底+维特根斯坦+波兰尼：模糊念头→清晰想法的三层系统 (2026) | [[ai-agents]] |
| [[summary-thread-by-deedydas-meta-harnesses]] | Meta Harness: harness的自我优化版本，大幅超越传统harness (2026) | [[ai-agents]] |
| [[summary-thread-by-gittrend0x-github-trending-self-evolving-agents]] | GitHub 5个自我进化记忆Agent爆火：从记忆进化到多Agent辩论到自动科研 (2026) | [[ai-agents]] |
| [[summary-thread-by-hanzheng-7-coral-autonomous-multi-agent-discovery]] | CORAL: 多Agent形成研究社区，50%以上突破来自互相借鉴 (2026) | [[ai-agents]] |
| [[summary-karpathy-second-brain-how-to-build-it]] | Karpathy第二大脑方案：三个文件夹+CLAUDE.md，AI维护wiki积累知识 (2026) | [[markdown-knowledge-bases]] |
| [[summary-karpathy-llm-wiki-pattern-2026]] | LLM Wiki：compile-only知识库，Raw→Wiki→Schema三层，Ingest/Query/Lint三种操作，knowledge compounding (2026) | [[markdown-knowledge-bases]] |
| [[summary-meta-agent-continual-learning-for-agents]] | Meta-Agent: 从生产轨迹持续改进harness，holdout准确率67%→87% (2026) | [[ai-agents]] |
| [[summary-观摩学习顶级agents如何对gpt进行行为矫正]] | Hermes Agent和OpenClaw修复GPT-5.4行为缺陷：光说不做/半途而废/不验证/编造 (2026) | [[ai-agents]] |
| [[summary-mcp-vs-cli-debate-speed]] | MCP vs CLI争议核心：速度问题 + Cerebras推理加速 + Monty安全代码执行 (2026) | [[ai-agents]] |
| [[summary-molab-notebook-competition-alphaxiv-marimo]] | alphaXiv x marimo竞赛：选论文做成交互notebook，截止4月26日 (2026) | [[markdown-knowledge-bases]] |
| [[summary-raca-research-assistant-coding-agent-for-phd-students]] | RACA: PhD学生的Claude Code harness，SSH连Slurm+HuggingFace可视化，只说话不写代码 (2026) | [[ai-agents]] |
| [[summary-asi-evolve-automated-ai-research-self-improvement]] | ASI-Evolve: AI运行完整科学循环自我改进，发现100+新架构，超越人类3x (2026) | [[ai-agents]] |
| [[summary-feynman-open-source-ai-research-agent]] | Feynman: 四agent研究系统(Researcher/Reviewer/Writer/Verifier)，MIT协议 (2026) | [[ai-agents]] |
| [[summary-thread-by-mitchell-hashimoto-ai-engineering-six-stages]] | Hashimoto六阶段AI工程演进：Harness Engineering是核心，AGENTS.md+验证工具=完整Harness (2026) | [[ai-agents]] |
| [[summary-thread-by-rajapatnaik-nousresearch-gepa-self-evolving-agents]] | NousResearch GEPA：DSPy+遗传Pareto优化，$2-10进化Agent提示词，无需GPU训练 (2026) | [[ai-agents]] |
| [[summary-thread-by-xiao-zcloak-agent-trust-protocol-atp-zcloak]] | DeepMind报告：网页隐藏指令86%成功率攻破Agent，ATP=Agent版HTTPS，密码学身份+签名消息+防篡改账本 (2026) | [[ai-agents]] |
| [[summary-google-deepmind-ai-agent-traps-ssrn-2026]] | DeepMind "AI Agent Traps"：六类攻击 taxonomy，感知/推理/记忆/行为/多Agent/人机协同，86% injection成功率，所有类别均有PoC (2026) | [[ai-agents]] |
| [[summary-251215834-optimizing-agentic-lm-inference-speculative-tool-calls]] | Speculative tool calls + sequence residency for agentic LM inference：几百 tokens/秒 throughput 提升 (2025) | [[ai-agents]] |
| [[summary-260318897-act-while-thinking-paste]] | PASTE: Pattern-Aware Speculative Tool Execution，Pattern Tuple (C,T,f,p) + opportunistic scheduling，task completion time -48.5%，tool throughput 1.8x (2026) | [[ai-agents]] |
| [[summary-thread-by-hitw93]] | Tw93's Waza: 8个AI时代工程师技能集(/think, /design, /hunt, /check, /read, /write, /learn, /health)，全markdown，100%开源 (2026) | [[ai-agents]] |
| [[summary-thread-by-heynavtoor]] | Karpathy's LLM Wiki: compile-once vs RAG re-derive，5k stars 48h，自动compound knowledge，Obsidian=IDE, LLM=programmer (2026) | [[markdown-knowledge-bases]] |
| [[summary-nashsullm-wiki]] | nashsu/llm_wiki: Desktop app implementing Karpathy's LLM Wiki pattern with two-step ingest, knowledge graph, and deep research (2026) | [[markdown-knowledge-bases]] |
| [[summary-cambricon-vllm-mlu-hardware-plugin]] | Cambricon vLLM-MLU: MLU370+插件，CNCL通信，CnMemAllocator，DeepSeek-V3.2-Exp首发 (2025) | [[llm-inference-engines]] |
| [[summary-vllm-metax-maca-hardware-plugin]] | vLLM-MetaX MACA: RFC #11162兼容，8种Attention后端，mcoplib生产内核，v0.15.0 (2026) | [[llm-inference-engines]] |
| [[summary-vllm-kunlun-xpu-hardware-plugin]] | vLLM-Kunlun XPU: 昆仑芯P800插件，三层CUDA兼容，FlashMLA/FusedMoE，388 stars (2025) | [[llm-inference-engines]] |
| [[summary-vllm-kunlun-development-workflow-guide]] | vLLM-Kunlun开发流程：5阶段标准化流程，Qwen3.5三天适配案例，torch_xray精度诊断 (2026) | [[llm-inference-engines]] |
| [[summary-vllm-kunlun-plugin-baidu-kunlun-xin-launch]] | vLLM-Kunlun正式发布：百度百舸+昆仑芯，RFC #11162插件，20+模型支持，xpu_profiler工具链 (2025) | [[llm-inference-engines]] |

---

## How to Navigate

- Start from a **topic** page for a broad overview of an area
- Drill into **concept** pages for precise definitions and mechanistic explanations
- Read **summary** pages for per-paper notes with results and limitations
- Use Obsidian's graph view to see link clusters

---

## Recently Updated

- 2024-01-15 — [[flash-attention]] created (stable)
- 2024-01-15 — [[hbm-bandwidth]] created (draft)
- 2024-01-15 — [[gpu-memory-optimization]] created (draft)
- 2024-01-15 — [[summary-flashattention2]] created (stable)
- 2026-04-04 — [[agent-memory-systems]] created (draft)
- 2026-04-04 — [[ai-agents]] created (draft)
- 2026-04-04 — [[coding-agents]] created (draft)
- 2026-04-04 — [[context-engineering]] created (draft)
- 2026-04-04 — [[graph-rag-systems]] created (draft)
- 2026-04-04 — [[high-performance-computing]] created (draft)
- 2026-04-04 — [[markdown-knowledge-bases]] created (draft)
- 2026-04-04 — [[memory-management]] created (draft)
- 2026-04-04 — [[agent-harness]] created (draft)
- 2026-04-04 — [[agent-memory-taxonomy]] created (draft)
- 2026-04-04 — [[claude-code]] created (draft)
- 2026-04-04 — [[context-database]] created (draft)
- 2026-04-04 — [[discipline-agents]] created (draft)
- 2026-04-04 — [[experiential-memory]] created (draft)
- 2026-04-04 — [[factual-memory]] created (draft)
- 2026-04-04 — [[filesystem-paradigm]] created (draft)
- 2026-04-04 — [[hashline-edit-tool]] created (draft)
- 2026-04-04 — [[hierarchical-memory]] created (draft)
- 2026-04-04 — [[locomo-benchmark]] created (draft)
- 2026-04-04 — [[long-term-memory]] created (draft)
- 2026-04-04 — [[lsp-integration]] created (draft)
- 2026-04-04 — [[mem0]] created (draft)
- 2026-04-04 — [[memgpt]] created (draft)
- 2026-04-04 — [[memory-search]] created (draft)
- 2026-04-04 — [[middleware-pattern]] created (draft)
- 2026-04-04 — [[persistent-agent-memory]] created (draft)
- 2026-04-04 — [[openclaw]] created (draft)
- 2026-04-04 — [[provider-agnostic-agents]] created (draft)
- 2026-04-04 — [[recursive-retrieval]] created (draft)
- 2026-04-04 — [[sandbox-isolation]] created (draft)
- 2026-04-04 — [[self-evolving-memory]] created (draft)
- 2026-04-04 — [[session-management]] created (draft)
- 2026-04-04 — [[skill-embedded-mcps]] created (draft)
- 2026-04-04 — [[skills-system]] created (draft)
- 2026-04-04 — [[source-map-reverse-engineering]] created (draft)
- 2026-04-04 — [[sub-agent-orchestration]] created (draft)
- 2026-04-04 — [[superagent-harness]] created (draft)
- 2026-04-04 — [[three-tier-context]] created (draft)
- 2026-04-04 — [[tool-use]] created (draft)
- 2026-04-04 — [[ultrawork]] created (draft)
- 2026-04-04 — [[universal-memory-layer]] created (draft)
- 2026-04-04 — [[visualized-retrieval]] created (draft)
- 2026-04-04 — [[working-memory]] created (draft)
- 2026-04-04 — [[markdown-knowledge-base]] created (draft)
- 2026-04-04 — [[virtual-filesystem-interface]] created (draft)
- 2026-04-04 — [[graph-rag]] created (draft)
- 2026-04-04 — [[summary-mintlify-virtual-filesystem]] created (draft)
- 2026-04-04 — [[summary-karpathy-knowledge-base-thread]] created (draft)
- 2026-04-04 — [[summary-graph-memory]] created (draft)
- 2026-04-04 — [[summary-am-memory]] created (draft)
- 2026-04-04 — [[summary-edgequake]] created (draft)
- 2026-04-04 — [[summary-memoryos-emnlp2025]] created (draft)
- 2026-04-04 — [[summary-open-harness]] created (draft)
- 2026-04-04 — [[summary-agent-memory-survey]] created (draft)
- 2026-04-04 — [[summary-opencode]] created (draft)
- 2026-04-04 — [[summary-deer-flow]] created (draft)
- 2026-04-04 — [[summary-oh-my-openagent]] created (draft)
- 2026-04-04 — [[summary-claude-code-sourcemap]] created (draft)
- 2026-04-04 — [[summary-mem0]] created (draft)
- 2026-04-04 — [[summary-openviking]] created (draft)
- 2026-04-04 — [[mcp-server]] created (draft)
- 2026-04-04 — [[memory-operating-system]] created (draft)
- 2026-04-04 — [[multi-level-memory]] created (draft)
- 2026-04-07 — [[fundamental-physics]] created (draft)
- 2026-04-07 — [[summary-observers-are-all-you-need]] created (draft)
- 2026-04-07 — [[holographic-principle]] created (draft)
- 2026-04-07 — [[gauge-theory]] created (draft)
- 2026-04-07 — [[quantum-gravity]] created (draft)
- 2026-04-07 — [[standard-model]] created (draft)
- 2026-04-07 — [[measurement-problem]] created (draft)
- 2026-04-07 — [[summary-搞懂缓存机制从gemma4到claude-code省80token]] created (draft)
- 2026-04-07 — [[summary-苏格拉底追问维特根斯坦拆解波兰尼兜底我的系统再次升级]] created (draft)
- 2026-04-07 — [[summary-thread-by-deedydas-meta-harnesses]] created (draft)
- 2026-04-07 — [[summary-thread-by-gittrend0x-github-trending-self-evolving-agents]] created (draft)
- 2026-04-07 — [[summary-thread-by-hanzheng-7-coral-autonomous-multi-agent-discovery]] created (draft)
- 2026-04-07 — [[summary-karpathy-second-brain-how-to-build-it]] created (draft)
- 2026-04-07 — [[summary-meta-agent-continual-learning-for-agents]] created (draft)
- 2026-04-07 — [[summary-观摩学习顶级agents如何对gpt进行行为矫正]] created (draft)
- 2026-04-07 — [[summary-mcp-vs-cli-debate-speed]] created (draft)
- 2026-04-07 — [[summary-molab-notebook-competition-alphaxiv-marimo]] created (draft)
- 2026-04-07 — [[summary-raca-research-assistant-coding-agent-for-phd-students]] created (draft)
- 2026-04-07 — [[summary-asi-evolve-automated-ai-research-self-improvement]] created (draft)
- 2026-04-07 — [[summary-feynman-open-source-ai-research-agent]] created (draft)
- 2026-04-07 — [[summary-cambricon-vllm-mlu-hardware-plugin]] created (draft)
- 2026-04-07 — [[summary-vllm-metax-maca-hardware-plugin]] created (draft)
- 2026-04-07 — [[summary-vllm-kunlun-xpu-hardware-plugin]] created (draft)
- 2026-04-07 — [[summary-vllm-kunlun-development-workflow-guide]] created (draft)
- 2026-04-07 — [[summary-vllm-kunlun-plugin-baidu-kunlun-xin-launch]] created (draft)
- 2026-04-07 — [[llm-inference-engines]] created (draft)
- 2026-04-07 — [[summary-thread-by-mitchell-hashimoto-ai-engineering-six-stages]] created (draft)
- 2026-04-07 — [[summary-thread-by-rajapatnaik-nousresearch-gepa-self-evolving-agents]] created (draft)
- 2026-04-07 — [[gepa]] created (draft)
- 2026-04-07 — [[agent-trust-protocol]] created (draft)
- 2026-04-07 — [[summary-thread-by-xiao-zcloak-agent-trust-protocol-atp-zcloak]] created (draft)
- 2026-04-07 — [[summary-google-deepmind-ai-agent-traps-ssrn-2026]] created (draft)
- 2026-04-07 — [[summary-karpathy-llm-wiki-pattern-2026]] created (draft)
- 2026-04-07 — [[markdown-knowledge-base]] updated (added LLM Wiki gist source)
- 2026-04-08 — [[summary-251215834-optimizing-agentic-lm-inference-speculative-tool-calls]] created (draft)
- 2026-04-08 — [[summary-260318897-act-while-thinking-paste]] created (draft)
- 2026-04-08 — [[summary-thread-by-hitw93]] created (draft)
- 2026-04-08 — [[summary-thread-by-heynavtoor]] created (draft)
- 2026-04-09 — [[summary-nashsullm-wiki]] created (draft)
