# SagaSmith CoC Skills

[中文](README.md) · [English](README-en.md) · [CoC runtime](https://github.com/SagaSmithAI/Sagasmith-coc)

**面向兼容 SKILL.md Agent 的 Call of Cthulhu 7e 守秘工作流。** 本仓库描述调查、线索、检定、SAN、疯狂、战斗、追逐、场景可见性和调查团生命周期；规则与持久化由 `sagasmith-coc` / `sagasmith-core` 执行。

## 两种模式

| 模式 | 入口 | 适用场景 | 边界 |
|---|---|---|---|
| **Full runtime** | [`full/SKILL.md`](full/SKILL.md) | 持久化调查团、PDF/Markdown 模组、检索、场景进度、Snapshot | 当前通过 JSON CLI 编排 |
| **Standalone** | [`standalone/SKILL.md`](standalone/SKILL.md) | 无依赖演示、快速跑团和文件状态 | 能力子集，不等价于 Full |

CoC 正在向 D&D 已采用的独立 MCP + 会话 exposure 架构演进。在完成该边界前，Full Skill 必须把 CLI 输出当作唯一提交结果，不应宣称拥有 D&D MCP 的 principal、actor knowledge 或 combat exposure 保证。

## 覆盖范围

- Classic/Pulp 调查员创建与成长；
- d100 成功等级、奖励/惩罚骰、对抗与孤注一掷；
- 调查、核心线索、handout 和 Keeper-only 信息；
- SAN 损失、临时/不定期疯狂与症状；
- 近战、远程、反击/闪避和追逐；
- 普通 scenario、solo 节点图与 handout pack 解析；
- `party` / `group:<id>` / `player:<id>` 场景进度；
- 事件、长期记忆与分支 Snapshot。

## Keeper 回合闭环

1. 确定 acting investigator 与 scene scope；
2. 读取当前场景，过滤 Keeper-only 信息；
3. 澄清调查员实际方法，而不是只根据技能名猜行动；
4. 判断是否需要检定、难度、奖励/惩罚骰和失败代价；
5. 公开结算并叙述玩家可见后果；
6. 更新线索、handout、SAN、状态、事件和进度；
7. 重大揭示、危险选择或章节转换时创建 Snapshot。

## Full 安装

```bash
pip install "sagasmith-coc[documents]"
sagasmith-coc doctor --json
```

然后加载 [`full/SKILL.md`](full/SKILL.md)。商业规则书和模组不随 Skill 分发；只导入用户有权使用的文件。

## Standalone

```powershell
cd standalone
python portable.py doctor
python portable.py campaign start --name "Arkham"
python portable.py roll d100 --score 65
```

数据位于 `~/.sagasmith/`。无 PDF、FTS5、ChromaDB 或完整权限/分支保证。

## License

原创 Skill 内容使用 MIT License。Call of Cthulhu 及商业内容归各自权利人所有，不包含在本仓库中。
