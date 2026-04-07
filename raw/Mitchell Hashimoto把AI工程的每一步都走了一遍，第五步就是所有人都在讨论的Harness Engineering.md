---
title: "Mitchell Hashimoto把AI工程的每一步都走了一遍，第五步就是所有人都在讨论的Harness Engineering"
source: "https://x.com/GoSailGlobal/status/2041385440826245287"
author:
  - "[[@GoSailGlobal]]"
published: 2026-04-07
created: 2026-04-07
description: "Terraform 之父 Mitchell Hashimoto 写了一篇长文，完整复盘了他从\"AI 没什么用\"到\"永远有一个 Agent 在后台跑\"的六个阶段。最关键的转折点在第五阶段，他给这个阶段起的名字正好是最近整个 AI 工程社区都在讨论的概念：Engineer the H..."
tags:
  - "clippings"
---
Terraform 之父 Mitchell Hashimoto 写了一篇长文，完整复盘了他从"AI 没什么用"到"永远有一个 Agent 在后台跑"的六个阶段。最关键的转折点在第五阶段，他给这个阶段起的名字正好是最近整个 AI 工程社区都在讨论的概念：Engineer the Harness

## 第一阶段：扔掉聊天窗口

![Image](https://pbs.twimg.com/media/HFNyBiJakAAZPqT?format=jpg&name=large)

Hashimoto 最早也是从 ChatGPT 和 Gemini 的网页界面开始的。他用 Gemini 还原了一个 macOS 的 SwiftUI 命令面板，效果不错，稍微改改就能用。但他很快发现了聊天模式的根本问题：纠错成本太高，你得反复告诉模型哪里错了，来回几轮之后上下文就乱了

他的结论是：聊天机器人做不了真正的工程任务，你需要的是 Agent。能读文件、能执行命令、能发 HTTP 请求的 Agent

## 第二阶段：重做自己的工作

![Image](https://pbs.twimg.com/media/HFNyDYjaYAAg15s?format=jpg&name=large)

这个阶段是最反直觉的。Hashimoto 没有在 Agent 不好用的时候放弃，反而逼自己把所有手动完成的 commit 用 Agent 重做一遍。等于同样的工作做两次，手动一次，Agent 一次

这个笨办法让他发现了三个关键原则

**把大任务拆成独立的小动作**。不要给 Agent 一个模糊的大目标，要拆成一个个可验证的小步骤

**把模糊的请求拆成规划和执行两个阶段**。先让 Agent 做计划，确认计划合理之后再让它执行

**给 Agent 提供自我验证的手段**。Agent 写完代码之后应该能自己跑测试，自己截图确认效果，而不是等你来检查

## 第三阶段：下班前 30 分钟交给 Agent

![Image](https://pbs.twimg.com/media/HFNyFHaboAA2juZ?format=jpg&name=large)

有了前两个阶段的经验，Hashimoto 开始在每天工作结束前的 30 分钟启动 Agent 任务。这个时间窗口特别适合三类工作

深度调研，比如调研某个库的生态和替代方案。Agent 可以系统性地搜索、阅读文档、整理对比表格

模糊想法的并行探索。你有一个不太确定的方向，让 Agent 先跑一版看看可行性

GitHub issue 分拣。用 gh CLI 让 Agent 自动归类和标记 issue

## 第四阶段：把确定能做好的活外包出去

![Image](https://pbs.twimg.com/media/HFNyGy3bAAAYyTW?format=jpg&name=large)

到这个阶段 Hashimoto 已经知道哪些任务 Agent 能稳定完成了。关键操作是：把任务交出去之后，关掉 Agent 的通知

这个细节很重要。如果你每次 Agent 有输出都去看一眼，上下文切换的成本会把省下的时间全部吃掉。正确的做法是把 Agent 当成一个异步的协作者，你去做别的事，它在后台跑，跑完了你再来看结果

他还提了一个让很多人不舒服的观点：把任务交给 Agent 意味着你自己不会在那个领域积累技能。但他认为这个取舍是值得的，只要你在其他地方保持手动编码的习惯

## 第五阶段：设计 Harness

![Image](https://pbs.twimg.com/media/HFNyIxoaYAAIjl6?format=jpg&name=large)

这是整篇文章最核心的部分。Hashimoto 对 Harness Engineering 给了一个极简的定义：**每次发现 Agent 犯了一个错误，你就花时间设计一个方案，确保它永远不会再犯同样的错误**

具体实践有两种形式

第一种是 AGENTS.md 文件。在他的 Ghostty 项目里，AGENTS.md 记录了所有 Agent 已知的失败模式和对应的纠正指令。比如"编译 Zig 的时候不要用 zig build，要用 nix develop"，比如"修改这个模块的时候必须同时更新对应的测试"

第二种是编写验证工具。给 Agent 写截图脚本让它能看到自己的 UI 输出，写过滤测试脚本让它能只跑相关的测试用例。这些工具让 Agent 有了自我验证的能力，不需要人来检查每一步

这个定义跟我们之前介绍过的 Anthropic 和 OpenAI 的 Harness Engineering 实践高度一致。Anthropic 的方案是生成器加评估器分离，OpenAI 的方案是用 Linter 和 CI 机械化执行架构约束。三者的共同点是：不靠更好的 Prompt，靠系统性的工程约束

王树义老师在他的文章（[Harness Engineering 详解](https://wangshuyi.substack.com/p/harness-engineering)）里给了一个更理论化的框架。他把 Harness 的控制机制分成两类：**Guides（前馈控制）** 和 **Sensors（反馈控制）**。Guides 是在 Agent 行动之前给方向，比如代码规范、架构约束。Sensors 是在 Agent 行动之后做观测和纠正，比如测试、监控

Hashimoto 的 AGENTS.md 属于 Guides，他的验证工具属于 Sensors。两者结合就是完整的 Harness

王树义老师还分享了一个特别有代表性的实战案例。他让 Agent 处理 30 张 PPT，串行处理到后面几张的时候质量明显下降，因为设计规范被挤出了上下文窗口。解决方案是给每张 PPT 分配一个独立的 Agent，隔离上下文。这就是 Harness 层面的架构设计，跟 Prompt 写得好不好完全无关

## 第六阶段：永远有一个 Agent 在跑

![Image](https://pbs.twimg.com/media/HFNyKsdbEAAOuHw?format=jpg&name=large)

Hashimoto 的目标状态是工作日的任何时刻都有至少一个 Agent 在后台运行。他目前做到了 10% 到 20% 的工作时间有 Agent 在跑

一个有趣的偏好：他更喜欢用慢模型跑单个 Agent，而不是用快模型跑多个并行 Agent。他用的是 Amp 的 deep mode，一个任务可能跑 30 分钟以上。他的逻辑是更深的思考比更快的响应更有价值

## 从个人实践到行业共识

![Image](https://pbs.twimg.com/media/HFNyMo6bsAAKP3r?format=jpg&name=large)

把 Hashimoto 的六个阶段和行业里其他声音放在一起看，一条清晰的演进路径浮现出来

Anthropic 的工程师 Prithvi Rajasekaran 搭了一个多 Agent 系统做前端开发，核心发现跟 Hashimoto 一样：Agent 自己评估自己的工作永远是自我表扬，必须把生成和评估拆开。OpenAI 用 3 个工程师 5 个月写了 100 万行代码，没有一行是人手写的，工程师的全部时间花在设计 Agent 的运行约束上

Karpathy 说他 12 月之后就没手写过一行代码。Every CEO 分享了 90% 用 AI 和 100% 用 AI 之间差了 10 倍的经验。OpenAI 对齐研究员说代码只占你工作价值的 10%，剩下 90% 是写规格说明书

所有这些声音指向同一个结论：工程师的核心技能正在从写代码转向设计 Agent 的运行环境。Hashimoto 的六阶段提供了一条具体的路径，让你知道怎么一步一步走到那里

王树义老师的完整分析见他的 [Substack 文章](https://wangshuyi.substack.com/p/harness-engineering)，推荐配合 Hashimoto 的[原文](https://mitchellh.com/writing/my-ai-adoption-journey)一起看，一个讲理论框架，一个讲实操路径