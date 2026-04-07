---
title: "Summary — Karpathy's Second Brain: How to Build It"
type: summary
status: draft
created: 2026-04-07
updated: 2026-04-07
sources:
  - raw/karpathy's second brain how to build it.md
links:
  - https://x.com/godofprompt/status/2041265656893489419
tags:
  - knowledge-base
  - llm
  - productivity
  - research
---

# Summary — Karpathy's Second Brain: How to Build It

## Source Metadata

| Field        | Value                          |
|--------------|--------------------------------|
| Source type  | blog/tutorial                   |
| Author(s)    | @godofprompt (summary of Karpathy's gist) |
| Year         | 2026                           |
| Venue        | X/Twitter → GitHub Gist        |
| Raw file     | `raw/karpathy's second brain how to build it.md` |

## Main Idea

Karpathy 的 Second Brain 方案：用 LLM 构建和维护个人知识库，替代传统的 RAG 或文件搜索。核心是三个文件夹（raw/、wiki/、outputs/）+ 一个 CLAUDE.md schema 文件。LLM 负责读源文件、编译 wiki、维护链接、更新索引。人负责筛选来源、提问、思考。知识随时间积累而非每次归零。

## Key Details

**架构**：
```
my-knowledge-base/
├── raw/           # 源材料。AI 只读，不修改。
│   └── assets/    # 图片、截图、图表
├── wiki/          # AI 维护的 wiki。人读，AI 写。
├── outputs/       # 报告、分析、查询答案
└── CLAUDE.md      # Schema 文件，整个系统的心脏
```

**CLAUDE.md Schema 核心要素**：
- YAML frontmatter：title, created, last_updated, source_count, status
- wiki 规范：每个 topic 一个 .md 文件，双括号链接内部页面，每条事实引用来源
- 矛盾标记：新信息与旧内容矛盾时显式标记
- 索引和日志：wiki/index.md 列表所有页面，wiki/log.md 追加记录

**工作流**：
1. **Ingest**：读源文件 → 讨论要点 → 创建 summary page → 更新 index → 更新所有相关概念页 → 添加反链 → 标记矛盾 → 追加日志
2. **Query**：读 index → 读相关 wiki 页 → 综合答案并引用 → 如果有新洞察→ 存回 wiki → 保存到 outputs/
3. **Lint**：每月健康检查，输出 lint-report-[date].md

**Prompt 模板**（从文章提取）：
- INGEST: "Read CLAUDE.md. Process [FILENAME] from raw/. Read fully, discuss takeaways, create summary, update index, update pages, add backlinks, flag contradictions, log."
- QUERY: "Read wiki/index.md. Answer: [QUESTION]. Cite wiki pages. If worth preserving, file as new wiki page."
- LINT: "Run full health check on wiki/ per CLAUDE.md. Output to wiki/lint-report-[date].md with severity levels."

## Method / Approach

Karpathy 的核心洞察：AI 写 wiki 比人更勤快——它们不会厌倦，不会忘记更新交叉引用，一次可以处理 15 个文件而不抱怨。Lex Fridman 确认他运行类似设置，生成交互 HTML 可视化并在跑步时用 voice mode 加载"mini-knowledge-bases"。

## Results / Evidence

Karpathy 的成果：约 100 篇文章、约 40 万词的单话题研究内容，他没有写一个字，全部由 AI 编写、链接、分类、维护。

关键倍增效应：好的答案应该存回 wiki。每次问题使下一次答案更好。

## Limitations

- **Context Window Ceiling**：~100 篇文章、~400K 词是上限。128K 上下文窗口只能容纳 ~96K 词，AI 选择性读取会漏掉内容（"lost in the middle"效应）
- **Error Compounding**：AI 写的 wiki 页面有细微错误，你基于它回答，错误进入答案，答案再存回 wiki。两个页面强化同一个错误。每月 lint 有帮助，但 linting AI 和犯错的 AI 有相同的盲点
- **Hallucination Doesn't Disappear**：wiki 方法减少幻觉因为 AI 锚定在源材料上，但不消除。AI 可以综合出不存在的连接，且因为 wiki 看起来很权威（干净 markdown、交叉引用、引用），更容易信任错误信息
- **Cost Isn't Zero**：每个 ingest、query、lint 都消耗 tokens。触及 10-15 页的单源可能花费 $2-5（前沿模型），50 源 = $100-250
- **Doesn't Scale to Enterprise**：~100 文章时有效。10,000+ 源时系统崩溃
- **Single-Model Blind Spots**：整个 wiki 是一个模型的解释，有偏差和高成本决策的建议用 4+ 模型独立运行再比较一致性

## Links to Concepts

- [[markdown-knowledge-base]] — 核心方法论相关
- [[persistent-agent-memory]] — 涉及持久记忆机制
- [[context-engineering]] — 涉及上下文工程

## Links to Topics

- [[markdown-knowledge-bases]] — 直接相关
- [[ai-agents]] — 涉及 AI agent 作为知识管理系统

## Quotes Worth Preserving

> "The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."

> "Knowledge compounds instead of resetting."

> "When outputs get filed back, errors compound too."
