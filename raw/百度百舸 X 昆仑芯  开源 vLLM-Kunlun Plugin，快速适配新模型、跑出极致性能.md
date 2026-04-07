---
title: "百度百舸 X 昆仑芯 | 开源 vLLM-Kunlun Plugin，快速适配新模型、跑出极致性能"
source: "https://zhuanlan.zhihu.com/p/1982406667376272869"
author:
  - "[[百度智能云适合跑AI的云]]"
published:
created: 2026-04-07
description: "为解决国产芯片部署开源大模型的效率与性能瓶颈，百度百舸联合昆仑芯正式推出 vLLM-Kunlun Plugin —— 一款面向百度昆仑芯 XPU 的高性能 vLLM 平台插件，该 Plugin 现已全面开源。 同时，项目同步开放了配套工具…"
tags:
  - "clippings"
---
为解决国产芯片部署开源大模型的效率与性能瓶颈， [百度百舸](https://zhida.zhihu.com/search?content_id=267503110&content_type=Article&match_order=1&q=%E7%99%BE%E5%BA%A6%E7%99%BE%E8%88%B8&zhida_source=entity) 联合 [昆仑芯](https://zhida.zhihu.com/search?content_id=267503110&content_type=Article&match_order=1&q=%E6%98%86%E4%BB%91%E8%8A%AF&zhida_source=entity) 正式推出 [vLLM-Kunlun Plugin](https://zhida.zhihu.com/search?content_id=267503110&content_type=Article&match_order=1&q=vLLM-Kunlun+Plugin&zhida_source=entity) —— 一款面向百度昆仑芯 XPU 的高性能 vLLM 平台插件，该 Plugin 现已全面开源。  

同时，项目同步开放了配套工具链，包括用于算子精度验证的torch\_xray 与支持性能剖析的 [xpu\_profiler](https://zhida.zhihu.com/search?content_id=267503110&content_type=Article&match_order=1&q=xpu_profiler&zhida_source=entity) ，助力开发者高效完成模型迁移、调试与优化。  

欢迎访问以下地址获取资源：

| vLLM-Kunlun Plugin | [github.com/baidu/vLLM-K](https://github.com/baidu/vLLM-Kunlun) |
| --- | --- |
| torch\_xray | [su.bcebos.com/klx-sdk-r](https://su.bcebos.com/klx-sdk-release-public/xpytorch/dev_kl3/torch_xray/latest/torch_xray-999.9.9-cp310-cp310-linux_x86_64.whl) |
| xpu\_profiler | [klx-sdk-release-public.su.bcebos.com](https://klx-sdk-release-public.su.bcebos.com/v1/xre/xprofiler/release/xprofiler-Linux_x86_64-2.0.2.0.tar.gz) |

---

## 1\. 基于 vLLM 社区标准推出 Plugin，让新模型部署从数周缩短至数天

过去，每当 vLLM 社区发布对新模型的支持，若希望在国产芯片上同步部署，开发者往往需要对 vLLM 源码进行侵入式二次开发。这一过程不仅耗时长达三到四周，还容易因代码冲突导致后续社区版本升级困难，甚至影响已有业务的稳定性。

为破解这一难题，vLLM 社区推出了 RFC #11162 硬件插件标准。百度百舸联合昆仑芯基于该标准开发了 vLLM-Kunlun Plugin，实现 vLLM 社区版与昆仑芯 XPU 后端的完全解耦。

用户只需安装标准 vLLM，再同步安装 vLLM-Kunlun 插件，即可在昆仑芯 XPU 上第一时间部署任意主流大模型，无需修改 vLLM 核心代码，真正实现即插即用。

![](https://picx.zhimg.com/v2-df688b516413b487192d8004958896e1_1440w.jpg)

## 2\. Plugin 重构推理调度流程，实现社区版本升级零侵入

在传统 vLLM 架构中，推理请求由 Engine 接收并调度，Worker 在 GPU 上创建 ModelRunner，进而实例化如 [Qwen3MoeForCausalLM](https://zhida.zhihu.com/search?content_id=267503110&content_type=Article&match_order=1&q=Qwen3MoeForCausalLM&zhida_source=entity) 等模型类，并依赖 FlashAttention 等算子完成计算。整个流程深度绑定 CUDA 生态，一旦目标硬件平台变更，几乎每个环节都需要定制修改。

启用 vLLM-Kunlun Plugin 后，以昆仑芯 [P800](https://zhida.zhihu.com/search?content_id=267503110&content_type=Article&match_order=1&q=P800&zhida_source=entity) 为例，推理流程发生了关键转变：在 Engine 初始化阶段，系统会依据 RFC #11162 自动发现并注册 Kunlun Plugin。随后，Worker 创建专为昆仑芯 P800 优化的 ModelRunner，并加载 Plugin 提供的定制化模型类 Model Class（如 Qwen3MoeForCausalLM\_Kunlun），该模型类进一步调用高性能昆仑芯算子，执行底层 Kernel 计算。

这一架构革新带来了显著业务价值：

- 当 vLLM 社区发布新引擎版本，例如从 V0 升级至 V1，开发者只需在 Plugin 层面对齐新的 ModelRunner 接口规范；
- 当社区推出新模型架构，如 [DeepSeek-V3.2](https://zhida.zhihu.com/search?content_id=267503110&content_type=Article&match_order=1&q=DeepSeek-V3.2&zhida_source=entity) ，则仅需在 Plugin 内部更新模型组网逻辑，复用已有高性能算子和调度框架。同时，针对新增算子进行增量开发。

两种场景下，均无需侵入 vLLM 核心，大幅降低适配成本。新模型或新版本的支持周期从数周缩短至数天，同时确保与社区主干长期兼容，真正实现一次开发，持续演进。

## 3\. 深度定制融合算子，让 P800 推理吞吐和时延全面对齐主流 AI 加速卡

针对 P800 芯片的计算特性，百度百舸联合昆仑芯，专门为各类模型设计了高性能融合算子，例如 Split\_Norm\_Rope 和 Fused MoE，有效缓解 Attention 与 MoE 模块的计算瓶颈。这些算子已集成至高性能昆仑芯算子库（比如 [xtorch\_ops](https://zhida.zhihu.com/search?content_id=267503110&content_type=Article&match_order=1&q=xtorch_ops&zhida_source=entity) ）中，可被 vLLM-Kunlun Plugin 无缝调用。

在 DeepSeek、Qwen、Llama、GLM 等主流模型的实测中，这些高性能算子使得 P800 的推理服务吞吐与时延表现全面对标主流 AI 加速卡，真正释放国产芯片的理论算力潜力。

## 4\. 开放百度内部工具 torch\_xray 与 xpu\_profiler，让精度验证与性能调优开箱即用

为确保模型在 P800 上稳定高效运行，本项目同步开放 2 套关键工具：

- torch\_xray：用于算子精度调试，可自动比对 GPU 与 P800 的逐层输出，快速定位数值偏差；
- xpu\_profiler：提供类 nsys 的性能剖析能力，生成清晰的算子调用时序图，帮助开发者精准识别性能瓶颈与计算气泡。

这两套工具链已在百度大规模业务中反复验证，显著提升了大模型向国产芯片迁移与调优的效率，有效保障精度与性能的一致性，具备低门槛、高可靠、快迭代的特点，助力开发者高效推进业务落地。

## 5\. 覆盖 20+ 主流及多模态模型，私有模型也能快速适配上线

目前，vLLM 推理引擎在 P800 已支持超过 20+ 主流及多模态模型系列，涵盖 Qwen 系列、DeepSeek 系列、Llama 系列、GLM、InternVL 多模态模型、GPT OSS 等。无论您使用的是社区开源模型还是自研私有模型，均可通过 vLLM-Kunlun Plugin 快速完成部署与优化，大幅降低迁移成本。

## 6\. 建立开放协作机制，让社区贡献直通主干生态

vLLM-Kunlun Plugin 已在 GitHub 全面开源，不仅包含高性能推理实现，还同步开放了百度内部验证过的生产级适配工具链与完整文档。开发者可实时跟踪功能演进与模型支持进度，并基于标准化流程独立完成私有模型的适配。

我们坚信，强大的硬件生态离不开活跃的开发者社区。vLLM-Kunlun Plugin 项目坚持透明规划，我们将通过 GitHub Issue 和官方 Slack 社区（ [vllm-kunlun.slack.com/](https://vllm-kunlun.slack.com/) ）提供技术答疑、经验分享与版本更新同步。

我们欢迎开发者深度参与上游贡献，让特定需求直接融入主干生态，共同推动国产 AI 基础设施的繁荣发展。

发布于 2025-12-11 11:11・北京[昆仑芯](https://www.zhihu.com/topic/25634365)[vLLM](https://www.zhihu.com/topic/29177728)[DeepSeek](https://www.zhihu.com/topic/28820212)[云和AI 就用阿里云](https://click.aliyun.com/m/1000411344/?spu=biz%3D0%26ci%3D3692046%26si%3Db6572ac6-55c6-4987-848c-f2faa3f99241%26ts%3D1775547744%26zid%3D1629)

[

阿里云JVS Claw 一键部署 Open Claw 39 元/月

](https://click.aliyun.com/m/1000411344/?spu=biz%3D0%26ci%3D3692046%26si%3Db6572ac6-55c6-4987-848c-f2faa3f99241%26ts%3D1775547744%26zid%3D1629)