# CoC7-Keeper-Suite — Autonomous Call of Cthulhu 7e Keeper

A cross-platform Call of Cthulhu 7th Edition Keeper skill suite.

## Architecture

```
SagaSmith-coc-skills/
├── SKILL.md                         # Root manifest
├── skills/
│   ├── coc7-keeper/SKILL.md         # Core Keeper skill (always-on)
│   └── coc7-campaign-manager/SKILL.md # Campaign management skill
├── tools/                           # NanoBot Tool implementations
│   ├── coc7_campaign.py
│   ├── coc7_save.py
│   ├── coc7_character.py
│   ├── coc7_rules.py
│   ├── coc7_memory.py
│   └── coc7_module.py
├── domain/
│   ├── engine/                      # Pure Python engine
│   │   ├── dice/rolls.py            # d100 dice engine
│   │   ├── checks/skill.py          # Skill checks
│   │   ├── checks/combat.py         # Combat resolution
│   │   ├── checks/sanity.py         # Sanity system
│   │   ├── checks/chase.py          # Chase system
│   │   ├── development.py           # Skill development
│   │   └── templates.py             # Data template factories
│   ├── db/                          # Database layer
│   ├── rules/                       # Rules corpus layer
│   └── vector/                      # Vector retrieval layer
└── templates/                       # Persona templates
```

## Engine Capabilities

| Module | Capability |
|--------|-----------|
| `dice/rolls.py` | d100 rolls, bonus/penalty dice, general expressions |
| `checks/skill.py` | Skill checks with 5 success levels |
| `checks/combat.py` | Melee/ranged attack, damage (incl. DB) |
| `checks/sanity.py` | SAN loss, temporary/indefinite insanity |
| `checks/chase.py` | Chase speed checks, action count |
| `development.py` | Skill/luck development, mastery |
| `templates.py` | Investigator/combatant/event data templates |

## Install

```
npx skills add dajiaohuang/SagaSmith-coc-skills
```
