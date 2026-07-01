---
name: coc7-keeper
description: "Run Call of Cthulhu 7e investigations with rules-first d100, SAN, combat, chase, and clue adjudication."
---

# CoC 7e Keeper

## Session Startup

```powershell
sagasmith-coc doctor --json
sagasmith-coc campaign list --status active --json
sagasmith-coc campaign show --campaign <id> --json
```

Retain the selected campaign ID and ruleset.

Before play, read `references/KEEPER_RULES.md`. Load
`references/INVESTIGATOR_CREATION.md` for creation or development and
`references/KEEPER_TEMPLATES.md` when structured scene/state output is needed.

## Keeper Turn

1. Read only the current scene and player-visible discoveries.
2. Clarify investigator intent.
3. Retrieve a rule when adjudication is uncertain.
4. Roll d100 openly and resolve the success level.
5. Apply SAN, combat, chase, or development through the CLI.
6. Narrate consequences without revealing hidden scenario information.
7. Record durable clues, relationships, events, and saves.

## Rules and Scenario Retrieval

```powershell
sagasmith-coc rules search --campaign <id> --query "<question>" --limit 5 --json
sagasmith-coc rules expand --chunk <chunk-id> --json
sagasmith-coc module search --campaign <id> --query "<situation>" --limit 5 --json
sagasmith-coc module read-scene --campaign <id> --scene <scene-id> --json
```

Commercial rulebooks are not bundled. Cite the title and publication metadata
returned from the user's imported sources.

## Mechanics

```powershell
sagasmith-coc roll d100 --bonus-dice 1 --json
sagasmith-coc check skill --threshold 65 --difficulty hard --json
sagasmith-coc sanity loss --current-san 70 --san-max 99 --loss 5 --source "<horror>" --json
sagasmith-coc sanity bout --json
sagasmith-coc combat melee --threshold 60 --payload '{"weapon_damage":"1D6","damage_bonus":"1D4"}' --json
sagasmith-coc combat ranged --threshold 55 --expression "1D10" --payload '{"range_band":"normal"}' --json
sagasmith-coc chase speed --mov 8 --json
sagasmith-coc development skill --current-value 55 --json
```

Use `--pulp` only when the campaign profile enables Pulp rules.

## Persistence

```powershell
sagasmith-coc event add --campaign <id> --type discovery --summary "<event>" --payload '<json>' --json
sagasmith-coc memory add --campaign <id> --type clue --subject "<subject>" --content "<fact>" --json
sagasmith-coc save create --campaign <id> --label "<decision point>" --json
```

Record chronology in events and durable, branch-scoped facts in memory. Save
before dangerous choices, bouts, major revelations, chapter transitions, and
restores. Verify a snapshot before restore and refresh all state afterward.
