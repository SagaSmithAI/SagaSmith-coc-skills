# 🕯️ SagaSmith CoC Skills — 完整版

[中文](README.md) | [English](README-en.md)

<p align="center"><img src="images/Sagasmith.png" alt="SagaSmith" width="200"></p>

**跨平台 Call of Cthulhu 7e Keeper Skills** — 为 Claude Code、NanoBot、Codex、Cursor 等所有支持 SKILL.md 标准的 Agent 平台提供 CoC 守秘人能力。

> *"理智检定：0/1D6。"*

完整模式需要安装 `sagasmith-core` 和 `sagasmith-coc`。所有 Agent 平台通过同一 `sagasmith-coc --json` CLI 操作——本仓库不包含数据库、向量运行时、游戏引擎或平台专属工具。

商业规则书不随本仓库发布；用户可将自己合法持有的 PDF/Markdown 导入运行时。

---

## 生态

| 仓库 | 定位 |
|------|------|
| 📦 **SagaSmith-coc-skills**（本仓库） | CoC Agent Skill 定义 |
| 🕯️ [sagasmith-coc](https://github.com/dajiaohuang/sagasmith-coc) | CoC 7e 运行时 + CLI |
| 🏗️ [sagasmith-core](https://github.com/dajiaohuang/sagasmith-core) | 通用引擎 — DB、文档、RAG |
| 🎲 [SagaSmith-agent](https://github.com/dajiaohuang/SagaSmith-agent) | 完整 AI DM 运行时 |

---

## Skill 清单

| Skill | 文件 | 职责 |
|-------|------|------|
| 🎲 **coc7-keeper** | `skills/coc7-keeper/SKILL.md` | 核心 Keeper 人格（always-on）、规则裁决、SAN/疯狂、战斗与追逐、调查与线索、作用域式场景追踪 |
| 📋 **coc7-campaign-manager** | `skills/coc7-campaign-manager/SKILL.md` | 战役与调查团生命周期、Snapshot 存档/读档、模组导入 |

### 运行参考

Skill 按需从 `skills/coc7-keeper/references/` 加载详细流程：

| 参考文件 | 内容 |
|----------|------|
| `SCENARIO_INDEX.md` | 场景索引字段说明、质量门禁、scope 运行状态机 |
| `KEEPER_RULES.md` | 规则裁决速查 |
| `KEEPER_TEMPLATES.md` | 结构化场景/状态输出模板 |
| `INVESTIGATION.md` | 调查与线索管理 |
| `COMBAT_CHASE.md` | 战斗与追逐规则 |
| `SANITY.md` | SAN 与疯狂机制 |
| `SCENARIO_INDEX.md` | 场景导入、验证与导航参考 |

---

## 使用场景

### 需要 Runtime（持久化能力）

```powershell
sagasmith-coc module inspect --path ./scenario.pdf --json
sagasmith-coc module ingest --campaign <id> --path ./scenario.pdf --json
sagasmith-coc module index --campaign <id> --json
sagasmith-coc module current --campaign <id> --scope player:investigator --json
sagasmith-coc module set-progress --campaign <id> --scope party --scene <scene-id> --progress 50 --state '<json>' --json
sagasmith-coc save create --campaign <id> --label "进入废弃教堂前" --json
```

### 便携模式（无安装）

查看随附的参考文件，但不能持久化战役。

---

## 覆盖范围

Skill 覆盖 CoC 7e 完整 Keeper 工作流程：

- 调查员创建与成长（Classic / Pulp）
- 调查与线索管理（三线索法则、核心线索）
- d100 / 对抗检定、成功等级、孤注一掷
- SAN 检定、临时/ indefinite 疯狂、恐惧/狂躁
- 近战 / 远程回合制战斗
- 追逐轮次
- 场景推进与进度追踪
- 事件日志与修订式战役记忆
- Snapshot 存档/读档/校验

---

## 场景解析质量门禁

导入时 `SCENARIO_INDEX.md` 定义的质量门禁：

- ✅ 模组是否有合理数量的 scene？整本一个 scene → 停止并报告
- ✅ Solo 模组是否拆出编号节点？未拆 → 停止
- ✅ Handout 包是否拆成独立 handout？未分离 → 停止
- ✅ 规则章节是否被标为可推进场景？有 → 停止
- ✅ 场景/chunk 是否有页码？缺失 → 停止
- ✅ 是否可安全区分玩家文本与 Keeper 信息？不能 → 停止

---

## 快速安装

```bash
# Claude Code / Codex / Cursor
npx skills add dajiaohuang/SagaSmith-coc-skills
```

---

## 许可证

MIT
