---
title: "观摩学习顶级 Agents 如何对 GPT-5.4 进行行为矫正"
source: "https://x.com/_kaichen/status/2041199915280507123"
author:
  - "[[@_kaichen]]"
published: 2026-04-07
created: 2026-04-07
description: "最近翻了两个开源 Agent 框架的源码——Hermes Agent 和 OpenClaw。发现一件有意思的事：它们花了大量工程精力，专门修 GPT-5 在 agentic 场景下的行为缺陷。不是模型能力不够，是模型\"不听话\"。问题出在哪GPT-5 做单轮对话很强。但一旦进入 A..."
tags:
  - "clippings"
---
最近翻了两个开源 Agent 框架的源码——Hermes Agent 和 OpenClaw。发现一件有意思的事：**它们花了大量工程精力，专门修 GPT-5 在 agentic 场景下的行为缺陷。**

不是模型能力不够，是模型"不听话"。

## 问题出在哪

GPT-5 做单轮对话很强。但一旦进入 Agent 循环——需要连续调用工具、自主决策、持续推进任务——它就暴露出四个顽固的坏毛病：

**1\. 光说不做（Commentary-Only Turns）**

你让它改个文件，它回复"我会先读取文件内容，然后定位问题，接着修改……"。说完就结束了。没有任何 tool call。

这不是偶发。GPT 系列模型有很强的"先描述计划再行动"的倾向。在聊天场景里这是好习惯，在 Agent 场景里这是致命的——每一轮空转都浪费上下文窗口和时间。

**2\. 半途而废（Premature Completion）**

工具返回了部分结果，模型就把它当成完整答案交付了。比如搜索只返回了 3 条结果，明明可以换个关键词再搜一轮，它却直接总结"根据以上结果……"。

**3\. 不做验证（No Verification）**

生成了代码不跑测试，写了配置不检查语法，给了答案不交叉验证。直接输出，交付，下一个。

**4\. 编造而非查询（Hallucination Over Lookup）**

手边明明有 search\_files、web\_search 这些工具，遇到不确定的信息却选择"凭印象编一个"。这在长任务里尤其危险——一个错误的文件路径或 API 参数，后面全部白做。

这四个问题不是 GPT-5 独有的，但 GPT 系列表现最突出。Hermes 的代码注释里写得很直白：Claude 不需要这套矫正（"Claude's instruction-following is strong by default"）。

## OpenClaw 的做法：三段 Prompt，简洁有效

[https://github.com/openclaw/openclaw/blob/e7fe087677a659004d805c8ccd947db4ebfc0fed/extensions/openai/index.test.ts](https://github.com/openclaw/openclaw/blob/e7fe087677a659004d805c8ccd947db4ebfc0fed/extensions/openai/index.test.ts)

OpenClaw 的修复方案藏在一个 90 行的 TypeScript 文件里（extensions/openai/prompt-overlay.ts）。核心是三段 prompt overlay，只对 GPT-5 模型生效。

**执行偏好层（Execution Bias）**——解决"说了不做"：

> Start the real work in the same turn when the next step is clear.

翻译成人话：别废话，直接干。

它还加了一条针对性极强的规则：如果用户最后一条消息是"ok do it"或"go ahead"，跳过所有复述，直接开始 tool call。

**输出契约层（Output Contract）**——解决啰嗦和格式问题：

强制精简输出，禁用 em dash（GPT-5 特别爱用破折号），默认简短回答。

**人格层（Friendly Prompt Overlay）**——把执行纪律包装成"好队友"风格：

这一层很聪明。它不是单纯的性格设定，而是把执行规则嵌进了交互风格里。"Commentary-only turns are incomplete when the next action is clear"——这句话既是性格描述，也是行为约束。

整套方案大约 1,500 tokens。小、准、狠。

## Hermes 的做法：系统工程级的行为控制

[https://github.com/NousResearch/hermes-agent/blob/6f1cb46df9825e693e33069626444b9a1bd0d344/agent/prompt\_builder.py#L196](https://github.com/NousResearch/hermes-agent/blob/6f1cb46df9825e693e33069626444b9a1bd0d344/agent/prompt_builder.py#L196)

Hermes 走了一条完全不同的路。它承认受 OpenClaw 启发（代码注释提到了 "OpenClaw PR #38953"），但把问题升级成了一套完整的行为工程体系。

XML 标签强化指令权重

Hermes 发现纯文本指令对 GPT 的约束力不够，于是用 XML 标签包裹关键规则：

<tool\_persistence> Do not stop early when another tool call would materially improve the result. If a tool returns empty or partial results, retry with a different query or strategy before giving up. </tool\_persistence>

XML 标签不是装饰。在 transformer 的注意力机制里，结构化标记比平铺直叙的文本更容易被模型"注意到"。这是一个实践中被反复验证的 prompting 技巧。

四维验证清单

OpenClaw 的验证是一句话："verify correctness, coverage, formatting, and obvious side effects"。Hermes 把它展开成四个维度：

- **Correctness**：输出是否满足所有需求？
- **Grounding**：事实性声明是否有工具输出支撑？
- **Formatting**：输出格式是否匹配要求？
- **Safety**：下一步有没有副作用（写文件、执行命令、调 API）？需要确认范围。

多出的 Grounding 和 Safety 两个维度，直接对应"编造"和"不验证"两个坏毛病。

反幻觉优先级链

遇到缺失信息时，Hermes 规定了明确的行动优先级：

**工具查询 → 带标签地假设 → 向用户提问**

"Ask a clarifying question only when the information cannot be retrieved by tools." 先自己查，查不到再问人。这比 OpenClaw 的隐含规则（"Do prerequisite lookup or discovery before dependent actions"）更具操作性。

Developer Role 切换

这是一个 API 层面的 trick。OpenAI 的 API 里，developer role 比 system role 的指令权重更高。Hermes 在调 GPT-5/Codex 时，自动把 system prompt 切换成 developer role。不改内容，只改信封，指令遵循率就上去了。

9 层系统提示词架构

Hermes 最核心的设计是条件式组装的 9 层 system prompt：

层内容关键设计1人格（SOUL.md）与执行规则解耦2工具感知指导只注入已有工具的规则3云服务能力声明—4**执行纪律 + 模型补丁核心修复层**5自定义 system message运行时覆盖6持久记忆快照会话开始时冻结7Skills 索引每次回复前扫描8项目上下文文件带注入扫描9时间戳与元数据—

第 2 层的设计值得注意：如果当前会话没有 web\_search 工具，所有提到 web\_search 的引导文本都会被自动剥离。这防止模型幻想调用一个不存在的工具——又是一个反幻觉措施。

## 一个更深的观察

这件事真正有意思的地方不在技术细节，而在它揭示的行业现实：

**模型厂商卖的是"通用智能"，但 Agent 框架在生产环境里做的第一件事，是用 prompt 给模型打行为补丁。**

GPT-5.4 的 benchmark 分数很高。它能写论文、能做数学推理、能处理复杂指令。但在 Agent 循环里连续跑 50 轮 tool call？它会走神，会偷懒，会编造，会虎头蛇尾。

这不是模型"笨"。这是模型的训练目标（单轮对话质量）和 Agent 场景的要求（多轮执行纪律）之间存在 gap。RLHF 优化的是"回答让人满意"，不是"持续正确地调用工具直到任务完成"。

Hermes 和 OpenClaw 正在用 prompt engineering 填这个 gap。但 prompt 终究是创可贴，不是手术。真正的解决方案应该在训练阶段就把 agentic behavior 作为优化目标。

Hermes 的代码里其实已经有了这个方向的伏笔——trajectory\_compressor.py 文件专门为 RL 训练压缩 Agent 轨迹数据，强化"理解 → 执行 → 验证"的行为模式。Prompt 补丁是现在的权宜之计，training pipeline 才是终局。

## 对构建 Agent 的实践启示

如果你正在用 GPT-5.4/Codex 构建 Agent，这两个项目的源码值得细读。几个可以直接拿走的做法：

1. **"说了就要做"规则**：在 system prompt 里明确禁止 commentary-only turns。这一条规则的 ROI 最高。
2. **空结果重试**：工具返回空或部分结果时，要求模型换策略重试，而非直接放弃。
3. **条件式 prompt 组装**：只注入当前可用工具的引导。多余的工具提及会诱导幻觉。
4. **XML 标签包裹关键规则**：对 GPT 系列效果显著。
5. **验证清单**：至少要求 Correctness 和 Grounding 两个维度。

模型在变强，但 Agent 框架的行为工程不会消失。只要模型的训练目标和 Agent 的执行需求之间还有 gap，Harness 层就有存在价值。

本文基于 Hermes Agent 和 OpenClaw 的开源代码分析，研究日期 2026 年 4 月。