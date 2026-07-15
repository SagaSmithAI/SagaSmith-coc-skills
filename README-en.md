# SagaSmith CoC Skills

[中文](README.md) · [English](README-en.md) · [CoC runtime](https://github.com/SagaSmithAI/Sagasmith-coc)

**Call of Cthulhu 7e Keeper workflows for SKILL.md-compatible agents.** This repository describes investigation, clues, checks, sanity, insanity, combat, chases, scene visibility, and campaign operation. `sagasmith-coc` and `sagasmith-core` execute rules and persistence.

## Two modes

| Mode | Entry | Best for | Boundary |
|---|---|---|---|
| **Full runtime** | [`full/SKILL.md`](full/SKILL.md) | persistent campaigns, PDF/Markdown scenarios, retrieval, progress, snapshots | currently orchestrates the JSON CLI |
| **Standalone** | [`standalone/SKILL.md`](standalone/SKILL.md) | zero-dependency demos and file-based play | a subset, not Full parity |

CoC is converging on the independent MCP and session-exposure architecture already used by D&D. Until that boundary exists, Full Skills treat structured CLI output as the only committed result and do not claim D&D MCP-level principal, actor-knowledge, or combat-exposure guarantees.

## Coverage

- Classic/Pulp investigator creation and development;
- d100 success levels, bonus/penalty dice, opposed and pushed rolls;
- investigation, core clues, handouts, and Keeper-only information;
- sanity loss, temporary/indefinite insanity, and symptoms;
- melee, firearms, fight back/dodge, and chases;
- ordinary scenarios, solo node graphs, and handout packs;
- `party`, `group:<id>`, and `player:<id>` scene progress;
- events, long-term memory, and branch snapshots.

## Keeper turn loop

1. Resolve the acting investigator and scene scope.
2. Read the current scene and filter Keeper-only information.
3. Clarify method and intent instead of inferring an action from a skill name.
4. Decide whether a check is required, its difficulty, bonus/penalty dice, and consequences.
5. Settle openly and narrate player-visible results.
6. Update clues, handouts, SAN, state, events, and progress.
7. Snapshot major reveals, dangerous choices, and chapter transitions.

## Full install

```bash
pip install "sagasmith-coc[documents]"
sagasmith-coc doctor --json
```

Load [`full/SKILL.md`](full/SKILL.md). Commercial books and scenarios are not distributed; import only material the user is authorized to use.

## Standalone

```powershell
cd standalone
python portable.py doctor
python portable.py campaign start --name "Arkham"
python portable.py roll d100 --score 65
```

Data lives at `~/.sagasmith/`. There is no PDF ingestion, FTS5, ChromaDB, or Full-grade permission/branch guarantee.

## License

Original Skill content is MIT licensed. Call of Cthulhu and commercial material belong to their respective rights holders and are not included.
