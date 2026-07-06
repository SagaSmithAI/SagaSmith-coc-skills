# 🕯️ SagaSmith CoC Skills

[中文](README.md) | [English](README-en.md)

<p align="center"><img src="full/images/Sagasmith.png" alt="SagaSmith" width="150"></p>

**跨平台 Call of Cthulhu 7e Keeper Skills** — 为 Claude Code、NanoBot、Codex、Cursor、OpenClaw、Hermes 等所有支持 SKILL.md 标准的 AI Agent 平台提供守秘人能力。

本仓库是一个 **SKILL 定义包**，不包含数据库、游戏引擎或平台专属工具。它提供两种使用方式，**由你选择**：

| 方式 | 目录 | 依赖 | 适用场景 |
|------|------|------|---------|
| 📦 完整版 | `full/` | `sagasmith-coc` Python 包 | 持久化战役、PDF 导入、FTS5 搜索、Snapshot DAG |
| 🪶 轻量版 | `standalone/` | Python 3.11+（标准库） | 即装即用，纯文件系统，零依赖 |

---

## 📦 full/ — 完整版（推荐）

要求本机安装 `sagasmith-coc` CLI。所有操作通过 `sagasmith-coc --json` 命令完成。

```bash
pip install "sagasmith-coc[documents]"
sagasmith-coc doctor --json
```

加载 `full/SKILL.md`。

### 特性

- 🕯️ **战役管理** — 调查团创建、调查员管理、规则/模组绑定、事件日志
- 👤 **调查员** — Classic/Pulp 双版属性面板验证，技能、职业、资产
- 🎲 **规则引擎** — d100/对抗检定、成功等级、孤注一掷、奖励/惩罚骰
- 🧠 **SAN 与疯狂** — 理智检定、临时/indefinite 疯狂、恐惧/狂躁
- ⚔️ **战斗与追逐** — 近战/远程回合制、追逐轮次、动作/反应
- 📖 **模组** — PDF/Markdown 导入、三种解析模式（常规调查、solo 节点、handout 包）
- 🔍 **场景元数据** — `scene_type`、`visibility`、clues、checks、sanity 表达式
- 🧩 **场景进度** — `party`/`group:<id>`/`player:<id>` 作用域追踪，透明继承
- 💾 **Snapshot** — DAG 存档树，支持调查团分支读档

### 生态

| 仓库 | 定位 |
|------|------|
| 🕯️ [sagasmith-coc](https://github.com/SagaSmithAI/Sagasmith-coc) | CoC 7e 运行时 + CLI |
| 🏗️ [sagasmith-core](https://github.com/SagaSmithAI/Sagasmith-core) | 通用引擎 — DB、文档、RAG、FTS5 |
| 🎲 [SagaSmith-agent](https://github.com/SagaSmithAI/SagaSmith-agent) | 完整 AI DM 运行时（基于 NanoBot） |

### Skill 清单

| Skill | 路径 | 职责 |
|-------|------|------|
| 🎲 **coc7-keeper** | `full/skills/coc7-keeper/SKILL.md` | 核心 Keeper 人格（always-on）、规则裁决、SAN/疯狂、战斗与追逐、调查与线索 |
| 📋 **coc7-campaign-manager** | `full/skills/coc7-campaign-manager/SKILL.md` | 战役与调查团生命周期、Snapshot 存档/读档、模组导入 |

### 运行参考

Skill 按需从 `full/skills/coc7-keeper/references/` 加载详细流程：

| 参考文件 | 内容 |
|----------|------|
| `KEEPER_RULES.md` | 规则裁决速查 |
| `SCENARIO_INDEX.md` | 场景索引字段说明、质量门禁、scope 运行状态机 |
| `KEEPER_TEMPLATES.md` | 结构化场景/状态输出模板 |
| `INVESTIGATION.md` | 调查与线索管理 |
| `COMBAT_CHASE.md` | 战斗与追逐规则 |
| `SANITY.md` | SAN 与疯狂机制 |
| `INVESTIGATOR_CREATION.md` | 调查员创建模板 |

### 场景解析质量门禁

full 版 PDF 导入时自动检测以下问题并停止引导：

- ✅ 整本模组只有一个 scene？→ 停止
- ✅ Solo 模组未拆出编号节点？→ 停止
- ✅ Handout 包未分离？→ 停止
- ✅ 规则章节标为可推进场景？→ 停止
- ✅ 场景/chunk 缺失页码？→ 停止
- ✅ 无法区分玩家文本与 Keeper 信息？→ 停止

---

## 🪶 standalone/ — 轻量版

不需要安装任何 Python 包。Python 3.11+ 标准库即可运行。

切换到 `standalone/` 目录后操作：

```powershell
python portable.py doctor
python portable.py campaign start --name "Arkham"
python portable.py roll d100 --score 65
```

加载 `standalone/SKILL.md`。

数据存储在 `~/.sagasmith/`，全部为纯文本文件（JSON / Markdown / JSONL）。

### 支持的操作

| 命令组 | 覆盖能力 |
|--------|---------|
| 战役 | `campaign start/list/get` |
| 调查员 | `character create/list/get` |
| 模组 | `module ingest/index/current/read-scene/search/set-progress` |
| 掷骰 | `roll d100` — 成功等级（critical/extreme/hard/regular/failure），`roll dice` |
| 事件 | `event add/list` |
| 记忆 | `memory add/list/search` |
| 存档 | `save create/list/restore` — 全目录快照 |

### 限制

- ❌ 不支持 PDF 导入（需用户先转为 Markdown）
- ❌ 不支持商业规则书搜索（无捆绑 SRD）
- ❌ 不支持 FTS5 全文索引
- ❌ 不支持 ChromaDB 语义搜索

---

## Keeper 工作流程

每次处理调查员行动：

1. **Scope 决议** — 根据行动者选择 `party` / `group:<id>` / `player:<id>`，调用 `module current`
2. **场景读取** — 读取该 scope 的当前场景，只展示玩家可见信息
3. **澄清意图** — 询问玩家的具体行动
4. **检索规则** — 裁决不确定的规则时先搜索
5. **掷骰** — d100 公开掷骰，解析成功等级
6. **叙事** — 在不泄露隐藏信息的前提下描述后果
7. **状态合并** — 线索、handout、触发器合并到该 scope 的现有进度
8. **记录** — 持久化线索、事件、记忆
9. **存档** — 危险选择、重大揭示、章节切换前创建 Snapshot

---

## Agent 安装流程

```powershell
# 1. 检测 sagasmith-coc 是否可用
sagasmith-coc doctor --json 2>nul

# 2a. 可用 → 完整版
#     加载 full/SKILL.md
#     所有命令使用 sagasmith-coc xxx --json

# 2b. 不可用 → 轻量版
#     切换到 standalone/ 目录
#     加载 SKILL.md
#     所有命令使用 python portable.py xxx
```

---

## 许可

MIT
