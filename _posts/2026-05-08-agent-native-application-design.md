---
layout: post
title: 我们为什么选择 Agent-Native 架构？BidRisk 产品实践总结
excerpt: 从 Workflow vs Agent 的决策、工具四层体系、Prompt 设计原则，到 Django + Celery 的完整集成方案，分享我们在 BidRisk 项目中落地的 Agent 原生工程实践。
date: 2026-05-08
tags: [Agent, AI架构, 工程实践, Tool, Django]
---

在构建 BidRisk（AI 风控平台）时，我们选择了 **Agent-Native** 架构而非传统 Workflow。这篇文章记录了我们做这个决定的原因、落地中的关键设计，以及与 Django + Celery 的集成实践。

## 一、产品定位与 Agent 原生哲学

BidRisk 是面向招标/投标/合规场景的 AI 风控平台。其核心特征是 **Agent 原生（Agent-Native）** —— 业务能力以工具（Tool）形式暴露给 LLM，由 LLM 自主决策调用路径，而非通过硬编码流程图驱动。

我们的设计宣言：

- **奥卡姆剃刀**：如无必要，勿增实体。每引入一个新工具/模块，必须证明其不可替代性。
- **开闭原则**：新能力以插件（Tool 分类注册）形式接入，严禁侵入核心链路。
- **YAGNI**：只为当下需求写代码，拒绝“未来式”过度设计。
- **内容为王**：设计服务于信息传递，不堆砌视觉与协议层噪声。

---

## 二、Workflow VS Agent

### BidRisk 的选择

优先 Agent，仅在以下情形使用 Workflow：

1. 步骤完全确定（如 PDF 处理 pipeline）
2. 需要严格幂等与重试（如异步评分任务）
3. 性能敏感，不允许 LLM 推理开销

**当前落地**：

- 对话问答 → ReAct Agent
- 合规审查 → ReAct Agent + 审查专属工具
- 评分规则提取 → ReAct Agent（自动翻阅 PDF）
- PDF 处理/文件入库 → Celery Workflow（确定性流水线）

### 何时升级为多 Agent 图

只有满足**全部**条件时，才考虑使用 LangGraph 自定义 Graph：

1. 业务天然是多阶段长链（如大型招标文件起草）
2. 需要章节级并行或局部重跑
3. 需要中断恢复与阶段化可观测

小场景（如公告通知起草）默认不图化，统一主 Agent + bounded loop 足够。

---

## 三、Agent 与 Celery 的集成模式

### 架构全景

```javascript
HTTP 请求
    │
    ▼
Django View（chat_stream_view）
    │  保存用户消息 → Message 表
    │
    ▼
异步生成器 stream_generator()
    │  初始化 FlowRun 追踪
    │
    ▼
stream_conversation_message()
    │  构建 Prompt
    │  装配 Tool 集
    │  设置 ContextVar（project_id 等）
    │  创建 ReAct Agent
    │
    ▼
LangGraph astream_events()
    ├── on_tool_start  → SSE: thinking
    ├── on_tool_end    → SSE: evidence（白名单工具）
    ├── on_chat_model_stream → SSE: answer（主通道）
    └── on_chat_model_end   → 兜底补全
    │
    ▼
保存 AI 回复 → Message 表（含 evidences）
完成 FlowRun 记录
    │
    ▼
SSE 流关闭
```

### 对话持久化模型

- **Conversation**：会话实体，关联 project / flow / user
- **Message**：消息实体，包含 role、content、evidences 等
- **ToolCall / FlowRun**：工具调用与流程运行记录，用于可观测

---

## 四、工具体系（Tool 注册 → 装配 → 过滤 → 守卫）

我们设计了一套四层工具体系，确保安全、可控、可扩展。

（详细内容包括：注册机制、Canonical Tool 集合、工具策略与守卫、上下文注入等）

---

## 五、Prompt 设计原则

核心理念与分层设计...

---

**本系列上一篇**：  
《2026 年 AI 产品应该怎么架构？从背景到治理的完整蓝图》
