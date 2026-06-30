# CoC7-Keeper-Suite — Autonomous Call of Cthulhu 7e Keeper

一个跨平台的 CoC 7e 守秘人技能套件。

## 结构

```
SagaSmith-coc-skills/
├── SKILL.md                         # 根 Manifest
├── skills/
│   ├── coc7-keeper/SKILL.md         # 核心守秘人技能 (always-on)
│   └── coc7-campaign-manager/SKILL.md # 战役管理技能
├── tools/                           # NanoBot Tool 实现
│   ├── coc7_campaign.py
│   ├── coc7_save.py
│   ├── coc7_character.py
│   ├── coc7_rules.py
│   ├── coc7_memory.py
│   └── coc7_module.py
├── domain/
│   ├── engine/                      # 纯 Python 引擎
│   │   ├── dice/rolls.py            # d100 骰子引擎
│   │   ├── checks/skill.py          # 技能检定
│   │   ├── checks/combat.py         # 战斗解析
│   │   ├── checks/sanity.py         # 理智系统
│   │   ├── checks/chase.py          # 追逐系统
│   │   ├── development.py           # 技能成长
│   │   └── templates.py             # 数据模板工厂
│   ├── db/                          # 数据库层
│   │   ├── models/                  # SQLAlchemy ORM 模型
│   │   ├── campaigns.py
│   │   ├── snapshots.py
│   │   ├── characters.py
│   │   ├── memory.py
│   │   ├── world.py
│   │   ├── events.py
│   │   └── undo.py
│   ├── rules/                       # 规则库层
│   │   ├── parser.py
│   │   ├── embedding.py
│   │   ├── ingest.py
│   │   └── search.py
│   └── vector/                      # 向量检索层
│       ├── client.py
│       └── search.py
└── templates/                       # 人格模板
    ├── SOUL.md
    ├── IDENTITY.md
    └── AGENTS.md
```

## 引擎能力

| 模块 | 能力 |
|------|------|
| `dice/rolls.py` | d100 掷骰、奖励/惩罚骰、通用骰子表达式 |
| `checks/skill.py` | 技能检定 (常规/困难/极难/大成功/大失败) |
| `checks/combat.py` | 近战/远程攻击、伤害结算 (含 DB) |
| `checks/sanity.py` | 理智损失、临时/不定期疯狂、狂乱发作 |
| `checks/chase.py` | 追逐速度检定、行动次数 |
| `development.py` | 技能成长、幸运成长、技能掌握 |
| `templates.py` | 调查员/战斗/事件数据模板 |

## 安装

```
npx skills add dajiaohuang/SagaSmith-coc-skills
```

或

```
npx clawhub install coc7-keeper-suite
```
