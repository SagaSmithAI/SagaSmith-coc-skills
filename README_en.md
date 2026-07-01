# 🦑 SagaSmith

[English](README_en.md) | [中文](README.md)

<p align="center"><img src="images/Sagasmith.png" alt="SagaSmith" width="200"></p>

**Autonomous CoC 7e AI Keeper** — campaign management · rule adjudication · autonomous GMing

> *"The rules are iron. The dice are the judge. The horror is the truth."*  
> — SagaSmith default Keeper

SagaSmith is a cross-platform AI game master skill pack. It bundles complete Call of Cthulhu 7th Edition Keeper capabilities — campaign lifecycle management, rule adjudication, investigator management, sanity/combat/chase engines — into an installable AI agent skill, compatible with NanoBot, OpenClaw, Hermes, Claude Code, and any platform supporting the SKILL.md standard.

---

## Ecosystem

| Repo | Role |
|------|------|
| 📦 **SagaSmith-coc-skills** (this repo) | CoC 7e skill pack |
| 🎲 [SagaSmith-agent](https://github.com/dajiaohuang/SagaSmith-agent) | Complete AI DM runtime |
| 🐉 [SagaSmith-dnd-skills](https://github.com/dajiaohuang/SagaSmith-dnd-skills) | D&D 5e skill pack |
| ✍️ [SagaSmith-module-gen-skills](https://github.com/dajiaohuang/SagaSmith-module-gen-skills) | Standalone module generator |

---

## Supported Platforms

SagaSmith follows the open SKILL.md standard and is theoretically compatible with all AI Agent platforms that support this standard. Below are tested/known compatible platforms:

| Platform | Status | Notes |
|----------|--------|-------|
| 🤖 **NanoBot** | ✅ Native | Primary development & testing platform |
| 🦞 **OpenClaw** | ✅ Compatible | Open-source Claude Code alternative |
| 🪽 **Hermes** | ✅ Compatible | Cross-platform AI Agent runtime |
| Claude Code | ✅ Compatible | Anthropic's official Agent |
| 🧩 **Codex** | ✅ Compatible | OpenAI's official IDE Agent |
| 🛠️ **TRAE** | ✅ Compatible | Volcano Engine AI IDE |
| 🌊 **Windsurf** | ✅ Compatible | CodeLlama-based AI IDE |
| 🤝 **WorkBuddy** | ✅ Compatible | Enterprise AI Coding Agent |
| 🔘 **Coze (扣子)** | 🔄 In progress | ByteDance Bot platform |
| Other SKILL.md platforms | ✅ Theoretically | Any platform supporting SKILL.md |

> PRs welcome to add more platforms!

---

## Why SagaSmith CoC

Most CoC AI tools do one thing: roll dice, look up a rule, or write a paragraph. SagaSmith is the **full Keeper**:

- 🏛️ **Campaign Management** — SQLite/PostgreSQL-backed campaign CRUD, Snapshot save/load/verify/undo, delta recaps, branch-aware long-term memory, event log, and module progress tracking
- 🎲 **Rule Adjudication** — Configurable BGE-M3 / BGE Small Dense Vector search over CoC 7e rules, exact-name + FTS5 full-text + Dense semantic hybrid retrieval with automatic tier fallback
- 🎭 **Investigator Management** — Full investigator/NPC/creature CRUD, 8 characteristic roll formulas, occupation/archetype system, skill allocation & development
- 🧠 **Sanity System** — SAN max calculation, temporary/indefinite insanity adjudication, bouts of madness table, Mythos Hardened rules, Pulp optional rules
- ⚔️ **Combat Engine** — Melee/ranged attacks, skill contest resolution, damage bonus (DB), range penalty dice, firearm malfunction, critical max damage
- 🏃 **Chase System** — Speed checks, action count calculation, distance tracking, assist adjudication
- 📈 **Character Development** — Skill growth checks (d100 > current → +1D10), skill mastery (≥90 → 2D6 SAN recovery), luck growth
- 🔍 **Module Retrieval** — Module/scenario import, chunked indexing, hybrid search (lexical + Dense), scene progress tracking
- 🌲 **Save DAG** — Immutable branching save tree, branch-isolated memories, SHA-256 integrity verification

---

## Usage Examples

Load SagaSmith into any compatible agent. The 8 phases below cover the full lifecycle.

### 1. Rulebook Import

```
User: Import CoC 7e rulebooks

Agent:
📚 Parsing CoC 7e rule corpus...
   Chunks: indexed · BGE embeddings: ready (1024/384-dim by profile)
   Books: Keeper Rulebook · Investigator Handbook
   ✅ Index ready
```

### 2. Module Import

```
User: [Upload Crimson_Letters.pdf]

Agent:
📄 Parsing — Markdown conversion · chapter detection
📦 Crimson Letters
   3 chapters · 18 scenes · 247 chunks · 247 vectors · ✅ ready
```

### 3. Campaign Start

```
User: Start a new campaign with Crimson Letters

Agent:
🎲 Campaign Setup
   ✅ Created: campaign_a1b2
   ✅ Rules bound: CoC 7e 2024
   ✅ Module bound: Crimson Letters unlocked
   ✅ Initial snapshot: slot 1 "Initial State"

   🎉 Campaign ready! Create investigators or say "random roll."
```

### 4. Investigator Creation

```
User: Build me a professor investigator

Agent:
📜 Investigator Creation — Professor
   1️⃣ Characteristics: STR 50 · CON 55 · SIZ 60 · DEX 65 · APP 45
                       INT 80 · POW 70 · EDU 85
   2️⃣ Derived: HP 11 · MP 14 · SAN 70 · LUK 55 · MOV 8 · DB 0 · BUILD 0
   3️⃣ Occupation: Professor — Skill Points: EDU×4 = 340
      Skills: Library Use · Occult · History · Persuade · Psychology · Archaeology · Language(Latin) · Own Language

User: Confirm

Agent:
✅ Dr. Henry Armitage — Professor · Miskatonic University
   HP 11 · SAN 70 · Library Use 75% · Occult 65% · Saved to database
```

### 5. Keeper Gameplay

```
Agent:
【Time: October 1925, dusk】【Location: Arkham · Miskatonic University Library】

What do you do?

User: Search for clues about the Crimson Letters

Agent:
🎲 Library Use (75%) → d100 = 42
   ✅ Regular Success!

   You find a dusty 1863 journal in the archives. It mentions a secret society called
   the "Crimson Order," whose three founding members were prominent scholars.
   The society disbanded abruptly in 1865 — no reason given.

   【Clue: Crimson Order 1863 journal】【NPC unlocked: Three founding members】

User: Visit the first scholar

Agent:
🎲 Emery Brown, 72, retired linguistics professor. Lives alone in a crumbling apartment
   in the old quarter. His eyes flicker with unease.
   "That matter... I haven't spoken of it in 50 years."
   
   ⚔️ 🅰️ Gentle questioning  🅱️ Apply pressure  🅲️ Search the apartment discreetly
```

### 6. Sanity Checks

```
User: 🅱️

Agent:
🎲 He pulls out a leather-bound notebook. The symbols on its pages make your eyes burn.

   SAN Check (1/1D6):
   Current SAN: 70 → d100 = 31  ✅ Pass
   Sanity Loss: 1 point → Current SAN: 69

   Notebook contents: "We summoned it in the catacombs. It answered.
   It demanded... our most precious possessions."

   【Clue: Catacombs location】【Mythos Tome: Nameless Book fragment】
```

### 7. Rules Q&A

```
User: Cthulhu Mythos skill effects?

Agent: 🔍 Cthulhu Mythos — Special skill, starts at 0%. SAN max = 99 - Cthulhu Mythos.
       As Mythos grows, max SAN permanently decreases. Non-Mythos creatures cannot have this skill.
       Source: Keeper Rulebook Ch.4


User: How do penalty dice work?

Agent: 🔍 Penalty Dice: Roll additional tens dice with d100, take the higher/highest.
       Each penalty die cancels one bonus die. Triggered by adverse conditions
       (darkness, range, prone, etc.).
       Source: Keeper Rulebook Ch.5


User: How long does temporary insanity last?

Agent: 🔍 Temporary Insanity:
       • Bout of Madness: 1D10 combat rounds (real-time) or hours (summary)
       • Underlying Insanity: 1D10 hours or until triggered by the scene
       Trigger: Single SAN loss ≥ 5
       Source: Keeper Rulebook Ch.7
```

### 8. Campaign Management

```
User: List campaigns

Agent:
📋 campaign_a1b2  Crimson Letters  Ch.1  Saves: 4
   campaign_c3d4  Edge of Darkness  Ch.2  Saves: 7

User: Switch to Edge of Darkness

Agent: ✅ Switched · 📍 Ch.2 Scene 3

User: Save

Agent: ✅ slot 8 "Before Abandoned Lighthouse" · 🔑 b7e1c...
   📝 Recap: Investigators found smuggling records pointing to the lighthouse
             and convinced Sheriff Harper to provide backup.
   🧠 Memory: 2 permanent · 3 candidates

User: Load slot 5

Agent: ⚠️ Auto-saving current → ⏪ Restored slot 5
   ✅ World / Party / Combat / Plot / Events — all restored
```

---

## Quick Install

### Claude Code / Codex / Cursor / Copilot (recommended)

```bash
npx skills add dajiaohuang/SagaSmith-coc-skills
```

### ClawHub

```bash
npx clawhub install coc7-keeper-suite
```

### Manual (NanoBot)

```bash
git clone https://github.com/dajiaohuang/SagaSmith-coc-skills.git
cp -r SagaSmith-coc-skills/skills/*    ~/.nanobot/skills/
cp -r SagaSmith-coc-skills/templates/* ~/.nanobot/templates/
cp -r SagaSmith-coc-skills/tools/*.py  ~/.nanobot/agent/tools/
cp -r SagaSmith-coc-skills/domain/*    ~/.nanobot/coc/
```

---

## Skill Breakdown

| Skill | SKILL.md | Role |
|-------|----------|------|
| 🦑 **coc7-keeper** | [SKILL.md](skills/coc7-keeper/SKILL.md) | Core Keeper persona (always-on), rule adjudication, d100 engine, sanity/combat/chase systems, investigator creation & development |
| 📋 **coc7-campaign-manager** | [SKILL.md](skills/coc7-campaign-manager/SKILL.md) | Campaign lifecycle, Snapshot save/recap, branch-aware long-term memory, save/load, module import & progress tracking |

---

## Engine Deep Dive

### d100 Core

| Capability | Detail |
|------------|--------|
| Bonus/Penalty Dice | 0-2 dice, environmental modifiers, net effect calculation |
| 5 Success Levels | Fumble (96-100) → Failure → Regular → Hard (½) → Extreme (⅕) → Critical (01) |
| Difficulty Tiers | Regular / Hard / Extreme / Critical / Impossible |

### Combat System

| Capability | Detail |
|------------|--------|
| Melee Attack | Skill contest (attack vs dodge/fighting), critical = max damage |
| Ranged Attack | Range penalty dice (normal/long/extreme), malfunction checks |
| Damage | Weapon formula + Damage Bonus (DB), critical = max weapon + max DB |
| DB Table | STR+SIZ → DB -2 to +4D6 |

### Sanity System

| Capability | Detail |
|------------|--------|
| SAN Max | 99 - Cthulhu Mythos |
| Temporary Insanity | Single SAN loss ≥ 5 → bout 1D10 rounds/hours |
| Indefinite Insanity | Daily cumulative ≥ SAN/5 → latent 1D10 months |
| Bouts of Madness | d10 table, real-time (combat) & summary (interlude) modes |
| Pulp Rules | Mythos Hardened halves SAN loss |

---

## Keeper Persona

A cold, rigorous arbiter of cosmic horror:

- **Rules Absolutism** — Strict CoC 7e rulebook adjudication. Dice are final.
- **Cold Narration** — Precise environmental detail, stark horror delivery. No melodrama.
- **Info Boundary** — Never reveals hidden info, true NPC motives, Mythos stat blocks, or undiscovered clues.
- **Player Agency** — Never decides for investigators, never fudges dice for drama. Hidden rolls declared without threshold.
- **Impartiality** — Horror is equal-opportunity. No pulling punches, no favoritism.

---

## Directory Structure

```
SagaSmith-coc-skills/
├── skills/                     # 2 Skills (pure Markdown, cross-platform)
│   ├── coc7-keeper/            #   Core Keeper + investigator creation/rules reference
│   │   └── references/         #     Creation guide · Keeper rules · Output templates
│   └── coc7-campaign-manager/  #   Campaign management + DB contract
├── templates/                  # Keeper persona templates
│   ├── SOUL.md                 #   Keeper soul persona
│   ├── IDENTITY.md             #   Identity constraints & rule hierarchy
│   └── AGENTS.md               #   Session startup protocol
├── tools/                      # Agent tools (Python)
│   ├── coc7_campaign.py        #   Campaign CRUD + one-shot start
│   ├── coc7_character.py       #   Investigator/NPC/creature + world state
│   ├── coc7_save.py            #   Snapshot, delta recap & branch memory
│   ├── coc7_rules.py           #   Hybrid rule search (exact + FTS5 + Dense)
│   ├── coc7_memory.py          #   Branch-aware long-term memory
│   └── coc7_module.py          #   Module import/search/scene progress
├── domain/                     # Business logic (pure Python, zero framework deps)
│   ├── db/                     #   ORM (22 tables) + snapshots + recap/memory + undo
│   │   └── models/             #     10 ORM model files
│   ├── engine/                 #   d100 engine, checks, combat, sanity, chase, development, templates
│   │   ├── dice/               #     General dice expressions + d100 (bonus/penalty)
│   │   └── checks/             #     Skill · Combat · Sanity · Chase
│   ├── rules/                  #   Markdown parsing, BGE embeddings, ingestion, 3-tier search
│   └── vector/                 #   ChromaDB client, vector search
├── images/                     #   Branding assets
└── SKILL.md                    #   Root manifest
```

---

## Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `CHROMA_DB_DISABLED` | disabled (unset) | Set to `0` to enable ChromaDB |
| `CHROMA_DB_URL` | — | Remote ChromaDB server |
| `CHROMA_DB_PATH` | — | Custom ChromaDB path |
| `COC7_DENSE_DISABLED` | `=1` (disabled) | Set to `0` to enable Dense vectors |
| `COC7_EMBEDDING_MODE` | `auto` | Device mode: auto/cpu/gpu |
| `COC7_EMBEDDING_PROFILES` | `bge_m3` | Comma-separated: bge_m3, bge_small_en_v1_5 |
| `COC7_EMBEDDING_BATCH_SIZE` | `8` | Encoding batch size |
| `COC7_DATABASE_URL` | `<skill>/data/coc7.db` | SQLite path |
| `COC7_AUDIT_UNDO_LIMIT` | `20` | Undo depth limit |

---

## Dependencies

| Dependency | Purpose |
|------------|---------|
| Python 3.11+ | Domain runtime |
| SQLAlchemy | Database ORM (SQLite / PostgreSQL) |
| FlagEmbedding | BGE-M3 / BGE Small Dense Vector retrieval |
| ChromaDB | Vector store (optional — purely lexical fallback available) |

---

## Design Highlights

- **Three-Tier Retrieval** — Exact name match → SQLite FTS5 full-text (BM25) → ChromaDB Dense semantic search, automatic fallback when backends unavailable
- **Save DAG** — Immutable branching tree, SHA-256 hash per node, natural memory isolation across branches
- **Append-Only Audit** — Dice rolls, tool calls, and state changes all append-recorded; UPDATE/DELETE blocked at DB level
- **Lazy Ingestion** — Rules auto-parsed and indexed on first use; no separate setup step needed
- **Zero-Dependency Engine** — d100/combat/sanity/chase/development engines are pure Python with no external library dependencies

---

## Registries

[![ClawHub](https://img.shields.io/badge/ClawHub-coc7--keeper--suite-blue)](https://clawhub.ai)
[![skills.sh](https://img.shields.io/badge/skills.sh-dajiaohuang%2FSagaSmith--coc--skills-green)](https://skills.sh)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

Published on **ClawHub** and **skills.sh** (72 agent compatible).  
LobeHub: submit at [agentskill.sh/submit](https://agentskill.sh/submit).

---

## License

- Code: MIT
