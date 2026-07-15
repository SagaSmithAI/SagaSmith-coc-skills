# SagaSmith CoC Skills — Full Runtime

[中文](README.md) · [English](README-en.md) · [Repository overview](../README.md)

Full mode orchestrates the CoC 7e runtime and SagaSmith Core through `sagasmith-coc --json`. The Skill owns Keeper procedure and information boundaries; only a successful structured CLI response means state was committed.

## Start

```bash
pip install "sagasmith-coc[documents]"
sagasmith-coc doctor --json
```

Load [`SKILL.md`](SKILL.md) and use the focused references for rules, investigator creation, investigation, sanity, combat/chases, scenario indexing, and output templates.

## Runtime constraints

- Read the current scene/scope before narration and never leak adjacent Keeper-only material.
- Retrieve sources for uncertain rules; users must legally supply commercial books.
- Set goal, method, difficulty, and failure consequences before a roll.
- Commit clues, SAN, damage, conditions, and progress through structured commands.
- Follow solo node edges and reveal only unlocked player handouts.
- Stop and report quality failures when a book becomes one scene, nodes are not separated, visibility is unsafe, or page provenance is broadly missing.

This is currently a CLI architecture. Do not describe it as already having the server-side session exposure of the D&D MCP.
