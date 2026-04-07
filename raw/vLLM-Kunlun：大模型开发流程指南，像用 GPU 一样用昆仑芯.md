---
title: "vLLM-Kunlun：大模型开发流程指南，像用 GPU 一样用昆仑芯"
source: "https://zhuanlan.zhihu.com/p/2017693527853786391"
author:
  - "[[百度智能云适合跑AI的云]]"
published:
created: 2026-04-07
description: "本文整理自 26 年 3 月 15 日 vLLM-Kunlun Meetup 北京站活动的同名主题演讲。 在微信公众号百度智能云技术站回复「vLLM-Kunlun」，可以获得此次 Meetup 上半场的 6 个演讲主题材料。 OpenClaw 全民养龙虾的火爆，…"
tags:
  - "clippings"
---
本文整理自 26 年 3 月 15 日 vLLM-Kunlun Meetup 北京站活动的同名主题演讲。

在微信公众号百度智能云技术站回复「vLLM-Kunlun」，可以获得此次 Meetup 上半场的 6 个演讲主题材料。

---

OpenClaw 全民养龙虾的火爆，引发了对算力需求的爆发，云服务厂商以及个人开发者都在寻找高效的异构推理引擎，尽可能发挥硬件算力。其中 vLLM 就是异构计算推理框架中的佼佼者，凭借出色的性能、高兼容性，大幅提升了推理效率。

当我们将目光转向国产 AI 算力，一个现实的难题便摆在了眼前：怎样才能让 vLLM 这样优秀的框架，在全新的、架构不同的硬件上，同样高效、稳定地运行呢？

这正是我们团队过去一段时间里全力以赴在做的事情。简单来说，我们的核心目标，就是「让开发者在 [昆仑芯](https://zhida.zhihu.com/search?content_id=271679481&content_type=Article&match_order=1&q=%E6%98%86%E4%BB%91%E8%8A%AF&zhida_source=entity) 上使用 vLLM，感觉就像在用大家最熟悉的 GPU 一样」。

今天，我将从 vLLM-Kunlun 的平台介绍、模型适配的实践、强大的工具链、性能优化的案例，以及对未来的展望等五个方面，和大家分享我们的探索与实践成果。

![](https://pic1.zhimg.com/v2-1f17f6877d638c10c6b3e00e0d3cb0be_1440w.jpg)

首先，让我们聊聊这个项目的起点。

我们的目标很明确：要让所有使用昆仑芯的开发者，都可以拥有类 [CUDA](https://zhida.zhihu.com/search?content_id=271679481&content_type=Article&match_order=1&q=CUDA&zhida_source=entity) 的推理引擎开发社区，这味着我们不能简单地把代码 复制粘贴过来；算子库的接口不同，需要我们做大量的「翻译」和「衔接」工作。

因此百度百舸在和昆仑芯团队充分商讨和对接后，我们决定打造 vLLM-Kunlun 这个开源项目，为所有昆仑芯使用者提供高效、易用的大模型推理解决方案。

![](https://pic2.zhimg.com/v2-9d33b3759630353fd2bd9cea6a8f1795_1440w.jpg)

让我再来带大家看一下 vLLM-Kunlun 的架构设计思路：

- 本图中上层是 vLLM-Kunlun Plugin，它负责处理模型注册、Attention 机制的分发等上层逻辑。
- 中间是我们的高性能算子库，这里面包含了大量针对昆仑芯硬件特性优化的核心计算单元。
- 再往下，是工具链和昆仑芯 XPU 驱动，它们为整个系统提供了强大的调试、优化能力和坚实的算力底座。

说到这里，其实大家应该发现了，我们是从 Model 这一层劫持的。而这套架构的灵魂，就是 CUDA-like 特性。

![](https://pic4.zhimg.com/v2-14745cf0e255c911ba0a1efc4b97b04b_1440w.jpg)

其实作为一个插件系统来说，对社区代码尽可能少的修改是我们秉持的目标和理想。这可以说是我们实现「无缝衔接」的魔法。我们主要做了三件事：

- 第一，编程模型的一致性。我们和昆仑芯片团队协商，巧妙地进行了一些伪装，让 vLLM 框架层认为自己正运行在一个标准的 CUDA 环境中。比如，当框架查询设备类型时，我们自信地告诉它：我就是 CUDA。这样一来，大量为 CUDA 编写的上层逻辑就可以直接复用，省去了大量的修改工作。
- 第二，接口的高度对齐。昆仑芯后端的内存管理等核心接口，设计得和 torch.cuda 几乎一模一样。开发者调用 torch.cuda.max\_memory\_allocated () 这样的标准接口时，底层会自动映射到我们昆仑芯的实现上，完全不需要关心底层的差异。
- 第三，灵活的算子注册机制。我们利用 torch.library 这个强大的工具，将我们的昆仑算子注册到 [PyTorch](https://zhida.zhihu.com/search?content_id=271679481&content_type=Article&match_order=1&q=PyTorch&zhida_source=entity) 的算子体系中，并且标记为 CUDA 后端。这样，不仅能实现即插即用，还能完美兼容 Fake Tensor 等高级编译优化特性。

通过这三层伪装和对齐，我们成功地在软件层面抹平了硬件差异，为 vLLM 生态向国产算力的无缝迁移铺平了道路。

![](https://pic4.zhimg.com/v2-f2ce1aa4d0ec229fd3647114f2cecded_1440w.jpg)

说了这么多，在这里我也给大家带来两个实战案例分享，一个是小米 MIMO-Flash-V2 模型，一个是最新的 [Qwen3.5](https://zhida.zhihu.com/search?content_id=271679481&content_type=Article&match_order=1&q=Qwen3.5&zhida_source=entity) 模型。看看我们如何基于 vLLM-Kunlun 实现快速适配与性能优化。

第一个是关于 MIMO-Flash-V2 的适配。

当时社区还没有正式发布支持 MIMO-Flash-V2 的正式版本，因此对于 plugin 来说，我们需要做的是两步：首先利用社区提供的 vllm.general\_plugins 接口注册组网，然后重定向 linear 依赖的位置到 vLLM-Kunlun 当中，对齐社区最新代码，支持部署 K 和 V 的 head 不相等的模型。

![](https://pic1.zhimg.com/v2-1892f58b9a6ceba53bfd8da92cfee434_1440w.jpg)

对于这种 Attention 新算法的支持，昆仑芯团队在 2 天内给了我们新算子支持。这些支持的算子会统一打包到 kunlun-ops 中，我们只要重新 pip install kunlun\_ops 即可，然后打开 site package 中的 init 文件查看 python 端调用接口。

在拿到新算子后，我们直接按照接口参数调用算子，即完成了模型跑通的全流程。

![](https://pic4.zhimg.com/v2-841b532f5d325ce8ac9f22d539c8c4a5_1440w.jpg)

随着 vLLM-Kunlun 项目的完善，目前我们已经支持绝大多数的 Attention 计算类型，并支持多数前沿模型。

在此展示 5 种常见的 Attention 类型，以及 10 余款已经支持的模型。

![](https://picx.zhimg.com/v2-6401575d9fdcbb83bc4bec789d861d69_1440w.jpg)

因此，在 Qwen3.5 问世以后，开源社区的小伙伴，在 vLLM-Kunlun 升级对应的 v0.15.1 版本以后，2 天内完成了跑通、精度问题定位以及性能分析的全流程操作。

![](https://pic4.zhimg.com/v2-9db061a325dbc0f8712314c4da85aecd_1440w.jpg)

社区伙伴在跑通 Qwen3.5 后，发现 35B 模型在一些 case 下有精度问题，OCRBench benchmark 跑分偏低。

在这个背景下，先使用 torch\_xray 工具、自动 Hook 工具，分别在 NV 的 H 卡以及昆仑芯上按照模块 Dump 数据，并联合百度内部工具链同学开发的 [牵星平台](https://zhida.zhihu.com/search?content_id=271679481&content_type=Article&match_order=1&q=%E7%89%B5%E6%98%9F%E5%B9%B3%E5%8F%B0&zhida_source=entity) ，快速得到精度诊断。

- 关于 torch\_xray： [vllm-kunlun.readthedocs.io](https://vllm-kunlun.readthedocs.io/en/latest/developer_guide/evaluation/accuracy/accuracy_kernel.html)
![](https://pic1.zhimg.com/v2-9b023c8ef9a5b45ebd1a02b795626d00_1440w.jpg)

首先我们将 torch\_xray 的输出提供给牵星平台 AI 分析，得到精度诊断报告。这份报告可以清晰的展示有问题的模块精度，实现快速定位。

报告显示，Qwen3.5-35B-A3B 模型 99.57% 的节点实现完全对齐，40 层 Transformer 主干网络与 GPU 表现一致，仅 LogitsProcessor 最终输出层存在微小偏差。

我们发现这种偏差是 FC 算子问题导致的。然后通过 issue 提交昆仑芯算子团队，仅用 1 天就得到了该模型精度修复的算子产出。

最终，仅仅总用时 3 天，就实现了 Qwen3.5 在昆仑芯 P800 上的跑通、跑对。

![](https://picx.zhimg.com/v2-6ad5b707793434933ae895ba91158c85_1440w.jpg)

在解决精度问题后，我们直接使用 vLLM 内置的 [Pytorch Profiler](https://zhida.zhihu.com/search?content_id=271679481&content_type=Article&match_order=1&q=Pytorch+Profiler&zhida_source=entity) 进行性能分析，完全按照 vLLM 主社区的使用说明操作，无需做任何修改即可完成全流程 profiling。

- 关于 Pytorch Profiler： [docs.vllm.ai/en/stable/](https://docs.vllm.ai/en/stable/contributing/profiling/#example-commands-and-usage)

这边我用两个例子，给大家展示开源社区伙伴利用 Pytorch Profiler 工具提升 Qwen3.5 模型推理性能。

一个是 CPU 和 GPU 同步开销的问题。由于在 GPU 操作中进行.cpu () 转换会触发隐式的 cudaStreamSynchronize 调用，从而导致 GPU 必须等待所有待处理的 CUDA 操作完成，在 Trace 图中形成明显的 Bubble。

![](https://picx.zhimg.com/v2-f6230c98429caccdfdf1986b1accfb87_1440w.jpg)

产生这个问题的原因是昆仑芯 GDN attention 专属优化算子 causal\_conv1d\_fn：由于这个算子需要额外的 cache\_indices\_cpu 做更高效的负载均衡，而最初的代码实现方式是直接使用了 cache\_indices.cpu() 的语法，这会频繁触发 D2H 同步操作。

针对这一问题，我们将 cache\_indices\_cpu 创建，迁移至模型前向推理前的准备阶段，并在 GDN attention metadata builder 中完成初始化，彻底避免了推理过程中的 D2H 同步开销，大幅提升了模型性能。

![](https://picx.zhimg.com/v2-f977b1663b65297f6f0a3735f4f4e53f_1440w.jpg)

第二个案例，是 XPU 中 mem copy 耗时过高的优化。我们发现，Qwen3.5 算子总耗时里，mem copy 耗时占比严重偏高。

![](https://pic3.zhimg.com/v2-67cddf9ad2c30b1ed84bb9e21ab9cb42_1440w.jpg)

经排查，发现是 vLLM 代码中 GDN Cache 的一个布尔索引赋值操作带来的问题，即 initial\_state \[~has\_initial\_state,...\] = 0。该操作会引发多次内存访问，成为 TTFT 的核心瓶颈。

后来我们复用昆仑芯专属的 reshape and cache 算子来替代社区的代码，大幅优化 Cache 写入效率。经测试，在 4K 输入场景，把 TTFT 优化了 20% 多。

最终完成了 Qwen 3.5 在昆仑芯 P800 上的跑好，极致释放硬件性能。

![](https://pica.zhimg.com/v2-2b753e698b9c2ecfe220f0ec40d7d542_1440w.jpg)

通过这些实践，我们沉淀出了一套基于新硬件开发新 Feature 的标准化流程：从需求对齐、接口适配，到算子增强、集成测试，再到性能调优。这套标准化流程，确保我们能高效、稳定地紧跟上游社区的发展节奏。

![](https://pica.zhimg.com/v2-cf39f38517448d0ac84a6e1b98e3c3c4_1440w.jpg)

最后，和大家聊聊 vLLM-Kunlun 的未来展望。

我们将继续紧跟社区的步伐，确保对 vLLM 的每一个大版本都能快速跟进适配，并充分挖掘、利用社区 GPU Runner 的核心能力。

在硬件上，我们会持续跟进昆仑芯的迭代。全面支持现有及新一代昆仑芯芯片，充分释放国产硬件的算力潜力。

同时，我们也会更积极地拥抱开源，回馈社区，将我们在通用优化、异构硬件 CI/CD 方面的经验同步至上游社区，并进一步丰富 Model Zoo 的支持。

![](https://pic2.zhimg.com/v2-56403e880d2e8ea1a9c9e482d5da998d_1440w.jpg)

我们相信，随着国产算力的不断成熟和开源社区的共同努力，未来的 AI 应用将拥有更加坚实和多元化的基石。

我的分享就到这里。大家如果对我们的项目感兴趣，欢迎访问我们在 GitHub 上的开源项目。

- 项目地址： [github.com/baidu/vLLM-K](https://github.com/baidu/vLLM-Kunlun)

编辑于 2026-03-18 20:10・北京[国内首个AI短剧创作大模型现已免费开源，个人就能轻松拍摄短剧，最重要的是完全免费！](https://zhuanlan.zhihu.com/p/1954605359525263099)

[

这题我会，朋友是AI短剧编剧大佬 她刚开始创作短剧的时候，以为随便用几个模型就能月入过万，结果现实狠狠教训了一顿！一来对工具理解不透，二来作品被批“毫无灵魂，剧情太生硬”，搞得她差点放弃。 之所...

](https://zhuanlan.zhihu.com/p/1954605359525263099)