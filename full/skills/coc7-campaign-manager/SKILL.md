---
name: coc7-campaign-manager
description: "Manage CoC 7e campaigns, investigators, scenarios, saves, and memory through sagasmith-coc."
---

# CoC 7e Campaign Manager

All commands include `--json`.

Read `../coc7-keeper/references/KEEPER_RULES.md` before mutating an active
investigation. Keep player assignments in campaign state; platform profile files
are projections, not authority.

## Start

```powershell
sagasmith-coc campaign start --name "<name>" --ruleset classic --locale zh --json
sagasmith-coc campaign start --name "<name>" --ruleset pulp --locale zh --json
```

Import user-owned rules or scenarios:

```powershell
sagasmith-coc rules ingest --path "<rulebook.pdf>" --publication "<title>" --locale zh --json
sagasmith-coc module inspect --path "<scenario.pdf>" --json
sagasmith-coc module ingest --campaign <id> --path "<scenario.pdf>" --json
sagasmith-coc module index --campaign <id> --json
```

Inspect before ingest. Read
`../coc7-keeper/references/SCENARIO_INDEX.md` and stop automatic setup when its
quality gates fail. After ingest, verify scene types, page ranges, handouts, and
solo-node transitions through `module index`.

## Investigators

```powershell
sagasmith-coc investigator create --campaign <id> --name "<name>" --player "<player>" --sheet '@<sheet.json>' --json
sagasmith-coc investigator list --campaign <id> --json
sagasmith-coc investigator show --id <id> --json
sagasmith-coc investigator update --id <id> --sheet '@<sheet.json>' --json
```

Persist only after player confirmation.

Validate a complete draft before creation:

```powershell
sagasmith-coc investigator validate --sheet '@<sheet.json>' --json
```

The sheet retains characteristics, HP/MP/SAN/Luck, SAN limits and daily loss,
MOV, DB/Build, Dodge, skills, weapons, conditions, occupation/archetype,
development pools, biography, sanity encounters, inventory/books, money,
backstory, Mythos, and Pulp talents. Do not discard unknown campaign-approved
fields during updates.

## Saves and Continuity

```powershell
sagasmith-coc save create --campaign <id> --label "<label>" --json
sagasmith-coc save list --campaign <id> --json
sagasmith-coc save verify --campaign <id> --slot <n> --json
sagasmith-coc save lineage --campaign <id> --json
sagasmith-coc save restore --campaign <id> --slot <n> --json
sagasmith-coc memory search --campaign <id> --query "<question>" --limit 8 --json
```

Restore creates a new history branch and never overwrites old saves.

Use `save regenerate-recap`, `memory scope`, and `state undo`/`state redo` when
needed. Undo affects audited mutations and does not delete immutable snapshots.
