# 🕯️ SagaSmith CoC Skills

[中文](README.md) | [English](README-en.md)

<p align="center"><img src="images/Sagasmith.png" alt="SagaSmith" width="200"></p>

**Cross-platform Call of Cthulhu 7e Keeper Skills** — provide Game Master capabilities for CoC 7e to Claude Code, NanoBot, Codex, Cursor, and any agent platform supporting the SKILL.md standard.

> *"Sanity check: 0/1D6."*

Runtime mode requires `sagasmith-core` and `sagasmith-coc`. Every supported agent platform operates the same compact `sagasmith-coc --json` CLI — this repository contains no database, vector runtime, game engine, or platform-specific tools.

Commercial rulebooks are not bundled; users may ingest documents they are permitted to use.

---

## Ecosystem

| Repo | Role |
|------|------|
| 📦 **SagaSmith-coc-skills** (this repo) | CoC agent skill definitions |
| 🕯️ [sagasmith-coc](https://github.com/dajiaohuang/sagasmith-coc) | CoC 7e runtime + CLI |
| 🏗️ [sagasmith-core](https://github.com/dajiaohuang/sagasmith-core) | General engine — DB, docs, RAG |
| 🎲 [SagaSmith-agent](https://github.com/dajiaohuang/SagaSmith-agent) | Complete AI DM runtime |

---

## Skill Inventory

| Skill | File | Role |
|-------|------|------|
| 🎲 **coc7-keeper** | `skills/coc7-keeper/SKILL.md` | Core Keeper persona (always-on), rule adjudication, SAN/insanity, combat & chases, investigation & clues, scoped scene tracking |
| 📋 **coc7-campaign-manager** | `skills/coc7-campaign-manager/SKILL.md` | Campaign lifecycle, Snapshot save/load, module import |

### Reference Documents

Detailed workflows are loaded on demand from `skills/coc7-keeper/references/`:

| File | Content |
|------|---------|
| `SCENARIO_INDEX.md` | Scene index fields, quality gates, scope runtime state machine |
| `KEEPER_RULES.md` | Quick rule adjudication reference |
| `KEEPER_TEMPLATES.md` | Structured scene/state output templates |
| `INVESTIGATION.md` | Investigation and clue management |
| `COMBAT_CHASE.md` | Combat and chase rules |
| `SANITY.md` | SAN and insanity mechanics |

---

## Runtime Usage

```powershell
sagasmith-coc module inspect --path ./scenario.pdf --json
sagasmith-coc module ingest --campaign <id> --path ./scenario.pdf --json
sagasmith-coc module index --campaign <id> --json
sagasmith-coc module current --campaign <id> --scope player:investigator --json
sagasmith-coc module set-progress --campaign <id> --scope party --scene <scene-id> --progress 50 --state '<json>' --json
sagasmith-coc save create --campaign <id> --label "Before entering the ruined church" --json
```

---

## Coverage

Skills cover the full CoC 7e Keeper workflow:

- Investigator creation and advancement (Classic / Pulp)
- Investigation and clue management (Three Clue Rule, core clues)
- d100 / opposed checks, success levels, pushed rolls
- SAN checks, temporary / indefinite madness, phobias / manias
- Melee / ranged turn-based combat
- Chase rounds
- Scene progression and progress tracking
- Event log and revisioned campaign memory
- Snapshot save / load / verify

---

## Scene Parsing Quality Gates

Quality gates defined in `SCENARIO_INDEX.md`:

- ✅ Reasonable number of scenes per module? One scene for whole document → stop
- ✅ Solo scenario nodes properly separated? Not split → stop
- ✅ Handout pack split into independent handouts? Not separated → stop
- ✅ Rules sections marked as playable scenes? Yes → stop
- ✅ Page ranges present on scenes/chunks? Missing → stop
- ✅ Can player text and Keeper text be safely distinguished? Cannot → stop

---

## Quick Install

```bash
# Claude Code / Codex / Cursor
npx skills add dajiaohuang/SagaSmith-coc-skills
```

---

## License

MIT
