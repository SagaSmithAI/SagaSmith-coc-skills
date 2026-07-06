---
name: coc7-keeper
description: "Run Call of Cthulhu 7e investigations with rules-first d100, SAN, combat, chase, and clue adjudication."
---

# CoC 7e Keeper

## Mode Detection

First, detect which mode is available:

```powershell
sagasmith-coc doctor --json 2>nul && set COC_MODE=runtime || set COC_MODE=portable
if "%COC_MODE%"=="portable" python tools/portable.py doctor
```

If `sagasmith-coc` is found → **Runtime mode** (full persistence, FTS5 search, vector store).
If not → **Portable mode** (file-based, zero pip deps, Python stdlib only).

In Portable mode, locate `tools/portable.py` (in the skill repo root) and use it in place of `sagasmith-coc`.

## Session Startup

```powershell
# Runtime
sagasmith-coc doctor --json
sagasmith-coc campaign list --status active --json
sagasmith-coc campaign show --campaign <id> --json
```

```powershell
# Portable
python tools/portable.py doctor
python tools/portable.py campaign list
python tools/portable.py campaign get --campaign <id>
```

Retain the selected campaign ID and ruleset.

Before play, read `references/KEEPER_RULES.md`. Load
`references/INVESTIGATOR_CREATION.md` for creation or development and
`references/KEEPER_TEMPLATES.md` when structured scene/state output is needed.
Load `references/COMBAT_CHASE.md`, `references/SANITY.md`, or
`references/INVESTIGATION.md` when that subsystem becomes active.
Load `references/SCENARIO_INDEX.md` when importing, validating, or navigating a
scenario, handout pack, or solo adventure.

## Keeper Turn

1. Resolve the acting scope (`party`, `group:<id>`, or `player:<id>`). Run `module current`
   to get that scope's current scene; player scopes inherit the party scene until they diverge.
2. Read only that scope's current scene and player-visible discoveries.
3. Clarify investigator intent.
4. Retrieve a rule when adjudication is uncertain.
5. Roll d100 openly and resolve the success level.
6. Apply SAN, combat, chase, or development through the CLI.
7. Narrate consequences without revealing hidden scenario information.
8. Merge clues, handouts, and triggers into that scope's existing progress.
9. Record durable clues, relationships, events, and saves.

## Command Reference

Use the Runtime column when `sagasmith-coc` is available, Portable otherwise.

### Rules and Scenario Retrieval

| Runtime | Portable |
|---------|----------|
| `sagasmith-coc rules search --campaign <id> --query "<q>" --limit 5 --json` | `python tools/portable.py rules search --campaign <id> --query "<q>" --limit 5` |
| `sagasmith-coc rules expand --chunk <id> --json` | (read the rule file directly) |
| `sagasmith-coc module current --campaign <id> --scope <scope> --json` | `python tools/portable.py module current --campaign <id> --scope <scope>` |
| `sagasmith-coc module search --campaign <id> --query "<s>" --limit 5 --json` | `python tools/portable.py module search --campaign <id> --query "<s>" --limit 5` |
| `sagasmith-coc module read-scene --campaign <id> --scene <id> --json` | `python tools/portable.py module read-scene --campaign <id> --scene <id>` |
| `sagasmith-coc module index --campaign <id> --json` | `python tools/portable.py module index --campaign <id>` |
| `sagasmith-coc module ingest --campaign <id> --path <path> --json` | `python tools/portable.py module ingest --campaign <id> --path <path>` |

Commercial rulebooks are not bundled. Cite the title and publication metadata
returned from the user's imported sources.

### Mechanics

| Runtime | Portable |
|---------|----------|
| `sagasmith-coc roll d100 --bonus-dice 1 --json` | `python tools/portable.py roll d100 --score <skill>` |
| `sagasmith-coc check skill --threshold 65 --difficulty hard --json` | `python tools/portable.py roll d100 --score 65` |
| `sagasmith-coc sanity loss --current-san 70 --san-max 99 --loss 5 --source "<horror>" --json` | Calculate SAN loss manually: `python tools/portable.py roll dice --expression "1d4"` |
| `sagasmith-coc combat melee --threshold 60 ... --json` | `python tools/portable.py roll d100 --score 60` |
| `sagasmith-coc combat ranged --threshold 55 ... --json` | `python tools/portable.py roll d100 --score 55` |
| `sagasmith-coc development skill --json` | (update character sheet JSON directly) |

Use `--pulp` only when the campaign profile enables Pulp rules.

### Dice

All modes:

```
python tools/portable.py roll d100 --score 65
# → {"roll": 39, "score": 65, "level": "regular", "success": true}
# Levels: critical (01) > extreme (≤score/5) > hard (≤score/2) > regular (≤score) > failure

python tools/portable.py roll dice --expression "1D4"
python tools/portable.py roll dice --expression "2D6+1"
python tools/portable.py roll dice --expression "1D100"
```

### Persistence

| Runtime | Portable |
|---------|----------|
| `sagasmith-coc event add --campaign <id> --type discovery --summary "<s>" --payload '<json>' --json` | `python tools/portable.py event add --campaign <id> --type discovery --summary "<s>" --payload '<json>'` |
| `sagasmith-coc memory add --campaign <id> --type clue --subject "<s>" --content "<f>" --json` | `python tools/portable.py memory add --campaign <id> --type clue --subject "<s>" --content "<f>"` |
| `sagasmith-coc save create --campaign <id> --label "<label>" --json` | `python tools/portable.py save create --campaign <id> --label "<label>"` |
| (no CLI equivalent) | `python tools/portable.py save list --campaign <id>` |
| (no CLI equivalent) | `python tools/portable.py save restore --campaign <id> --slot <slot>` |

Record chronology in events and durable, branch-scoped facts in memory. Save
before dangerous choices, bouts, major revelations, chapter transitions, and
restores. Verify a snapshot before restore and refresh all state afterward.

### Characters

| Runtime | Portable |
|---------|----------|
| `sagasmith-coc investigator create --campaign <id> --name "<name>" --occupation "<occ>" ... --json` | `python tools/portable.py character create --campaign <id> --name "<name>" --sheet '<json>'` |
| `sagasmith-coc investigator list --campaign <id> --json` | `python tools/portable.py character list --campaign <id>` |

## Portable Mode Data

Data lives in `~/.sagasmith/`:

```
~/.sagasmith/
  campaigns.json                       # campaign index
  <campaign_id>/
    campaign.json                      # metadata
    characters/<name>.json             # investigator sheets
    modules/<source_key>.md            # imported scenarios (Markdown)
    progress.json                      # scoped scene progress
    events.jsonl                       # event log
    memories.jsonl                     # campaign memory
    saves/<slot>/                      # snapshot copies
```

Progress merges state per-scope (`party`, `group:<id>`, `player:<id>`).
Save snapshots copy the campaign directory.

## Portable Mode Limitations

- No SQL FTS5 — search uses Python lexical scoring with Chinese ↔ English expansion
- No ChromaDB vector search
- No PDF import — convert PDF to Markdown first, then `module ingest`
- No `sanity loss` / `combat melee` / `opposed check` — roll d100 manually and apply rules
- No commercial rulebook search — only bundled SRD files are searchable
- No transaction atomicity — file writes use atomic rename for individual file safety
