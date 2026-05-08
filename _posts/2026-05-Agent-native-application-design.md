基于 BidRisk 产品的 Agent 工程实践总结，覆盖理论选型、架构设计、工具体系、Prompt 规范、集成模式与反模式。适用于团队新成员上手与架构评审参考。

> 更新时间：2026-03-19 | 维护人：研发团队

---

## 一、产品定位与 Agent 原生哲学

BidRisk 是面向招标/投标/合规场景的 AI 风控平台。其核心特征是 Agent 原生（Agent-Native）——业务能力以工具（Tool）形式暴露给 LLM，由 LLM 自主决策调用路径，而非通过硬编码流程图驱动。

设计宣言（来自 AGENTS.md）：

- 奥卡姆剃刀：如无必要，勿增实体。每引入一个新工具/模块，必须证明其不可替代性。

- 开闭原则：新能力以插件（Tool 分类注册）形式接入，严禁侵入核心链路。

- YAGNI：只为当下需求写代码，拒绝"未来式"过度设计。

- 内容为王：设计服务于信息传递，不堆砌视觉与协议层噪声。

---

## 二、Workflow VS Agent

### 核心区分

### BidRisk 的选择

优先 Agent，仅在以下情形用 Workflow：

1. 步骤完全确定（如 PDF 处理 pipeline）

1. 需要严格幂等与重试（如异步评分任务）

1. 性能敏感，不允许 LLM 推理开销

当前落地：

- 对话问答 → ReAct Agent（create_react_agent）

- 合规审查 → ReAct Agent + 审查专属工具

- 评分规则提取 → ReAct Agent（自动翻阅 PDF）

- PDF 处理/文件入库 → Celery Workflow（确定性流水线）

### 何时升级为多 Agent 图

只有满足全部条件时，才考虑多 Agent 图（LangGraph 自定义 Graph）：

1. 业务天然是多阶段长链（如大型招标文件起草）

1. 需要章节级并行或局部重跑

1. 需要中断恢复与阶段化可观测

小场景（如公告通知起草）默认不图化，统一主 Agent + bounded loop 足够。

---

## 三、Agent && Celery（Django 集成模式）

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

- Conversation：会话实体，关联 project / flow / user

- Message：消息记录（role / content / evidences）

- FlowRun / FlowRunEvent：执行轨迹审计

### 异步任务（Celery）

评分链路走 Celery 异步任务，适合长时间运行的 Agent 循环：

```python
# 评分规则提取
@shared_task
def run_rules_agent(task_id: int):
    # 加载招标文件 PDF
    # 初始化 Scoring Agent（ReAct）
    # 循环迭代提取规则（get_toc → search_file_pages → vision_read）
    # 保存 JSON 结果到 ScoringTask.rules
```

Celery 适合做：

- 异步执行（不阻塞 HTTP 请求）

- 任务生命周期管理（pending → running → done）

- 进度轮询 API

Celery 不适合做：

- 替代 Agent 的决策逻辑

- 驱动多步推理路径（交给 LLM）

---

## 四、工具体系（Tool 注册 → 装配 → 过滤 → 守卫）

### 四层架构

```javascript
services/        ← 纯业务逻辑，不感知 Agent 框架
agent_tools/     ← 参数解析 + 上下文注入 + 服务编排
toolkit/policy/  ← 工具注册 + 分类装配 + allow/deny 过滤
运行时            ← llm.py / agent_logging.py / utils/
```

### 注册机制

各 Django App 在 agent_tools/__init__.py 中注册工具分类：

```python
from agents.registry import register_tool_category

register_tool_category(
    "file",
    [list_files, read_file_text, search_file_pages, ...],
    label="文件工具",
)
```

settings.py 声明需要加载的模块：

```python
AGENT_TOOL_MODULES = [
    'projects.agent_tools',
    'datahub.agent_tools',
    'regulations.agent_tools',
    'reviews.agent_tools',
    'scoring.agent_tools',
]
```

### Canonical Tool 集合

文件域（file）

- list_files — 列出项目文件

- search_file_pages — 统一页码检索入口

- get_file_profile — 文件画像（页数/标签/扫描状态）

- get_file_toc — 完整目录

- read_file_text — 按页区间读取文本

- read_file_with_vl — Vision-Language 读取（单页或区间）

- read_file_evidence_with_vl — VL 精读单页取证（bbox 定位）

项目域（project）

- get_project_overview / get_project_details / get_project_facts

- get_project_metrics / list_project_tasks / get_task_risks

审查域（review）

- get_review_project_context — 审查项目上下文

- get_project_slot_facts — 项目槽位候选值

- co_bid_signal — 投标人共同投标频次（纯统计，无结论）

- recommend_checks_for_project — 推荐检查项

数据域（data）

- resolve_company_name / get_company_profile / search_bulletins

- get_bidder_activity_stats / query_data_index

法规域（regulation）

- search_law_passages — 法规条款片段检索（支持辖区过滤）

Web 域（web） / 评分域（scoring）

- search_web（Tavily）

- get_scoring_context / list_bidder_files（复用 file 工具）

### 工具策略与守卫

ToolPolicy（AGENT_TOOL_POLICY）：allow/deny 过滤，支持 profile 切换（dry_run 模式仅记日志）

ToolOutputGuard（AGENT_TOOL_OUTPUT_GUARD）：文本/VL 输出长度约束，防止上下文溢出

```python
# 文本读取约束
"text_read": {"max_chars_per_page": 1500, "max_pages": 20, "max_total_chars": 30000}
# VL 读取约束
"vl_read": {"max_pages": 10, "max_items_per_page": 5}
```

### 上下文注入（ContextVar）

工具通过 Python ContextVar 获取异步安全的上下文，无需每次显式传参：

```python
# 工具执行前
token = set_tool_context({"project_id": 123, "task_id": 456})

# 工具内部
def my_tool(context=None):
    ctx = resolve_tool_context(context)  # 合并显式参数与全局上下文
    project_id = ctx.get("project_id")

# 执行后清理
reset_tool_context(token)
```

核心原则：单一能力单一入口，不维护别名工具，不在不同域重复定义同能力 Tool。

---

## 五、Prompt 设计原则

### 核心理念

> LLM 做判断，代码做边界。

> Prompt 承载业务约束，代码只管执行边界（最大轮次、Token 预算、持久化）。

### Prompt 分层

1. System Prompt：角色定义 + 工具使用规则 + 输出规范约束

1. Guard Prompt：输出格式守卫（禁止暴露内部 JSON/哈希/meta 字段）

1. 历史消息：最近 N 条（默认 5 条，由 Flow 配置覆盖）

1. 用户消息：本轮输入