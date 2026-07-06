# 🕯️ SagaSmith CoC Skills

[中文](README.md) | [English](README-en.md)

<p align="center"><img src="full/images/Sagasmith.png" alt="SagaSmith" width="150"></p>

**Cross-platform Call of Cthulhu 7e Keeper Skills** — provide Game Master capabilities to Claude Code, NanoBot, Codex, Cursor, OpenClaw, Hermes, and any agent platform supporting the SKILL.md standard.

This repository is a **SKILL definition package** — it contains no database, game engine, or platform-specific tools. It ships two variants — **you choose** which to install:

| Variant | Directory | Dependency | When to use |
|---------|-----------|------------|-------------|
| 📦 Full | `full/` | `sagasmith-coc` Python package | Persistent campaigns, PDF import, FTS5 search, Snapshot DAG |
| 🪶 Standalone | `standalone/` | Python 3.11+ (stdlib only) | Instant setup, file-based storage, zero pip deps |

---

## 📦 full/ — Full Runtime (Recommended)

Requires the `sagasmith-coc` CLI on the local machine. All operations via `sagasmith-coc --json` commands.

```bash
pip install "sagasmith-coc[documents]"
sagasmith-coc doctor --json
```

Load `full/SKILL.md`.

### Features

- 🕯️ **Campaign Management** — Investigator group creation, character management, rule/module binding, event log
- 👤 **Investigators** — Classic/Pulp dual-edition validated sheets, skills, occupations, assets
- 🎲 **Rule Engine** — d100/opposed checks, success levels, pushed rolls, bonus/penalty dice
- 🧠 **SAN & Insanity** — Sanity checks, temporary/indefinite madness, phobias/manias
- ⚔️ **Combat & Chases** — Melee/ranged turn-based combat, chase rounds, actions/reactions
- 📖 **Modules** — PDF/Markdown import with three parsing modes: conventional investigation, solo scenario (numbered nodes + choice edges), handout pack
- 🔍 **Scene Metadata** — `scene_type`, `visibility`, clues, checks, SAN expressions
- 🧩 **Scene Progress** — scoped to `party`/`group:<id>`/`player:<id>` with transparent inheritance
- 💾 **Snapshot** — DAG save tree, branch-aware restore for investigator groups

### Ecosystem

| Repo | Role |
|------|------|
| 🕯️ [sagasmith-coc](https://github.com/SagaSmithAI/Sagasmith-coc) | CoC 7e runtime + CLI |
| 🏗️ [sagasmith-core](https://github.com/SagaSmithAI/Sagasmith-core) | General engine — DB, docs, RAG, FTS5 |
| 🎲 [SagaSmith-agent](https://github.com/SagaSmithAI/SagaSmith-agent) | Complete AI DM runtime (NanoBot-based) |

### Skill Inventory

| Skill | Path | Role |
|-------|------|------|
| 🎲 **coc7-keeper** | `full/skills/coc7-keeper/SKILL.md` | Core Keeper persona (always-on), rule adjudication, SAN/insanity, combat & chases, investigation |
| 📋 **coc7-campaign-manager** | `full/skills/coc7-campaign-manager/SKILL.md` | Campaign lifecycle, Snapshot save/load, module import |

### Reference Documents

Loaded on demand from `full/skills/coc7-keeper/references/`:

| File | Content |
|------|---------|
| `KEEPER_RULES.md` | Quick rule adjudication reference |
| `SCENARIO_INDEX.md` | Scene index fields, quality gates, scope runtime state machine |
| `KEEPER_TEMPLATES.md` | Structured scene/state output templates |
| `INVESTIGATION.md` | Investigation and clue management |
| `COMBAT_CHASE.md` | Combat and chase rules |
| `SANITY.md` | SAN and insanity mechanics |
| `INVESTIGATOR_CREATION.md` | Character creation workflow |

### Scenario Quality Gates

On PDF import, the full version detects and halts when:

- ✅ Only one scene for the whole module → stop
- ✅ Solo scenario nodes not separated → stop
- ✅ Handout pack not split → stop
- ✅ Rules sections marked as playable scenes → stop
- ✅ Scene/chunk page ranges missing → stop
- ✅ Cannot distinguish player text from Keeper text → stop

---

## 🪶 standalone/ — Lightweight

No pip dependencies. Python 3.11+ stdlib only.

Switch to the `standalone/` directory and run:

```powershell
python portable.py doctor
python portable.py campaign start --name "Arkham"
python portable.py roll d100 --score 65
```

Load `standalone/SKILL.md`.

Data is stored at `~/.sagasmith/`, all plain text (JSON / Markdown / JSONL).

### Supported Operations

| Command | Coverage |
|---------|----------|
| Campaign | `campaign start/list/get` |
| Investigators | `character create/list/get` |
| Scenarios | `module ingest/index/current/read-scene/search/set-progress` |
| Dice | `roll d100` — success levels (critical/extreme/hard/regular/failure), `roll dice` |
| Events | `event add/list` |
| Memory | `memory add/list/search` |
| Saves | `save create/list/restore` — full directory snapshots |

### Limitations

- ❌ No PDF import (convert to Markdown first)
- ❌ No commercial rulebook search (no bundled SRD)
- ❌ No FTS5 full-text index
- ❌ No ChromaDB semantic search
- ❌ No built-in SAN loss / combat melee — roll d100 and apply rules manually

---

## Keeper Workflow

Each investigator action:

1. **Scope resolution** — select `party` / `group:<id>` / `player:<id>`, call `module current`
2. **Scene reading** — read that scope's current scene, player-visible discoveries only
3. **Clarify intent** — ask what the investigator does
4. **Rule retrieval** — search before adjudicating uncertain mechanics
5. **Roll** — d100 openly, resolve success level
6. **Narrate** — consequences without revealing hidden information
7. **State merge** — clues, handouts, triggers into that scope's existing progress
8. **Record** — durable clues, events, memory
9. **Save** — snapshot at dangerous choices, major revelations, chapter transitions

---

## Agent Install Flow

```powershell
# 1. Check if sagasmith-coc is available
sagasmith-coc doctor --json 2>nul

# 2a. Available → Full mode
#     Load full/SKILL.md
#     All commands use sagasmith-coc xxx --json

# 2b. Not available → Standalone mode
#     Switch to standalone/ directory
#     Load SKILL.md
#     All commands use python portable.py xxx
```

---

## License

MIT
