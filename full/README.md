# SagaSmith CoC Skills — Full Runtime

[中文](README.md) · [English](README-en.md) · [仓库说明](../README.md)

Full 模式通过 `sagasmith-coc --json` 编排 CoC 7e runtime 与 SagaSmith Core。Skill 负责 Keeper 工作流和信息边界；只有结构化 CLI 成功结果表示状态已提交。

## 启动

```bash
pip install "sagasmith-coc[documents]"
sagasmith-coc doctor --json
```

加载 [`SKILL.md`](SKILL.md)，并按需读取：

| 参考 | 内容 |
|---|---|
| `KEEPER_RULES.md` | d100 与常见裁决 |
| `INVESTIGATOR_CREATION.md` | Classic/Pulp 调查员 |
| `INVESTIGATION.md` | 线索、调查方法与信息释放 |
| `SANITY.md` | SAN 与疯狂 |
| `COMBAT_CHASE.md` | 战斗和追逐 |
| `SCENARIO_INDEX.md` | parser profile、visibility、scene scope 和质量门禁 |
| `KEEPER_TEMPLATES.md` | 可审计输出模板 |

## 运行约束

- 先读取当前 scene/scope，再叙事；不能把相邻场景的 Keeper 信息提前泄露。
- 规则不确定时检索来源；商业规则书必须由用户合法导入。
- 检定前明确目标、方法、难度与失败代价，避免无意义掷骰。
- 线索、SAN、伤害、状态和进度必须以结构化命令提交。
- Solo 跳转必须遵守 node edge；handout 只展示已解锁的玩家内容。
- 整本只有一个 scene、节点未拆、visibility 不可判断或页码大面积缺失时停止导入流程并报告质量问题。

当前 Full 模式仍是 CLI 架构；不要把它描述成已经具备 D&D MCP 的服务端 session exposure。
