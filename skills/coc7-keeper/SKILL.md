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
Load `references/COMBAT_CHASE.md`, `references/SANITY.md`, or
`references/INVESTIGATION.md` when that subsystem becomes active.
Load `references/SCENARIO_INDEX.md` when importing, validating, or navigating a
scenario, handout pack, or solo adventure.

## Keeper Turn

1. Resolve the acting scope (`party`, `group:<id>`, or `player:<id>`) and call
   `module current`; player scopes inherit the party scene until they diverge.
2. Read only that scope's current scene and player-visible discoveries.
3. Clarify investigator intent.
4. Retrieve a rule when adjudication is uncertain.
5. Roll d100 openly and resolve the success level.
6. Apply SAN, combat, chase, or development through the CLI.
7. Narrate consequences without revealing hidden scenario information.
8. Merge clues, handouts, and triggers into that scope's existing progress.
9. Record durable clues, relationships, events, and saves.

## Rules and Scenario Retrieval

```powershell
sagasmith-coc rules search --campaign <id> --query "<question>" --limit 5 --json
sagasmith-coc rules expand --chunk <chunk-id> --json
sagasmith-coc module current --campaign <id> --scope <scope> --json
sagasmith-coc module search --campaign <id> --query "<situation>" --limit 5 --json
sagasmith-coc module read-scene --campaign <id> --scene <scene-id> --json
```

Commercial rulebooks are not bundled. Cite the title and publication metadata
returned from the user's imported sources.

## Mechanics

```powershell
sagasmith-coc roll d100 --bonus-dice 1 --json
sagasmith-coc check skill --threshold 65 --difficulty hard --json
sagasmith-coc check opposed --payload '@<opposed-check.json>' --json
sagasmith-coc sanity loss --current-san 70 --san-max 99 --loss 5 --source "<horror>" --json
sagasmith-coc sanity bout --json
sagasmith-coc combat melee --threshold 60 --payload '@<melee.json>' --json
sagasmith-coc combat ranged --threshold 55 --expression "1D10" --payload '@<ranged.json>' --json
sagasmith-coc chase speed --mov 8 --json
sagasmith-coc development skill --current-value 55 --json
```

Use `--pulp` only when the campaign profile enables Pulp rules.
Never calculate an opposed melee defense from a placeholder: provide the
defender roll, threshold, and `defense` choice in the melee payload.

## Persistence

```powershell
sagasmith-coc event add --campaign <id> --type discovery --summary "<event>" --payload '<json>' --json
sagasmith-coc memory add --campaign <id> --type clue --subject "<subject>" --content "<fact>" --json
sagasmith-coc save create --campaign <id> --label "<decision point>" --json
```

Record chronology in events and durable, branch-scoped facts in memory. Save
before dangerous choices, bouts, major revelations, chapter transitions, and
restores. Verify a snapshot before restore and refresh all state afterward.
