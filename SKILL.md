---
name: coc7-keeper-suite
description: "Autonomous Call of Cthulhu 7e Keeper — campaign lifecycle management with delta recaps and campaign-scoped long-term memory, d100 dice engine, investigation/adjudication, rule retrieval, and immersive Keeper persona (The Keeper). Bundles coc7-keeper and coc7-campaign-manager skills."
version: 1.0.0
tags:
  - coc
  - call-of-cthulhu
  - ttrpg
  - keeper
  - campaign
  - investigation
  - gaming
---

# CoC7-Keeper-Suite — Autonomous Call of Cthulhu 7e Keeper

A cross-platform Call of Cthulhu 7e Keeper skill suite.

## Skills Included

| Skill | Slug | Role |
|-------|------|------|
| **coc7-keeper** | `coc7-keeper` | Core Keeper persona, rule adjudication, d100 engine, combat/sanity/chase resolution, rule retrieval |
| **coc7-campaign-manager** | `coc7-campaign-manager` | Campaign lifecycle, snapshot recap, campaign memory, save/load/undo, investigator player mapping |

## Keeper Persona

The Keeper — impartial arbiter of dread. Rules-absolutist, cold narration.
Strict adherence to Call of Cthulhu 7e rulebooks. Dice are the judge; the scenario script is inviolable.

## Platforms

Install on NanoBot, OpenClaw, or Hermes. See [README.md](README.md) for per-platform setup.

## SRD

CoC 7e rules retrieval using the same three-tier architecture (exact → lexical → dense).

### Retrieval Architecture

```
Search (default, zero dependency)
├─ Exact match   ← keyword exact match, highest weight
├─ Lexical       ← tokenization + bigram matching
└─ Dense vectors — optional  ← requires ChromaDB + a configured BGE profile

First-time setup
├─ database.upgrade_schema()            ← automatic
└─ ensure_bundled_rules_ingested()      ← auto-ingest rule text
    └─ embed = False (default)         ← no embedding model loaded
```

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CHROMA_DB_DISABLED` | disabled (unset) | Set to `0` to enable ChromaDB (uses `<skill>/data/chroma_db/`) |
| `CHROMA_DB_URL` | - | Remote ChromaDB server address (auto-enables when set) |
| `CHROMA_DB_PATH` | - | Custom ChromaDB path (auto-enables when set) |
| `COC7_DENSE_DISABLED` | disabled (`=1`) | Set to `0` to enable dense vectors |
| `COC7_EMBEDDING_MODE` | `auto` | Device mode: `auto`, `cpu`, or `gpu` |
| `COC7_EMBEDDING_PROFILES` | `bge_m3` | Comma-separated profiles: `bge_m3`, `bge_small_en_v1_5` |
| `COC7_EMBEDDING_BATCH_SIZE` | `8` | Encoding batch size (1–128) |
| `COC7_DATABASE_URL` | `<skill>/data/coc7.db` | SQLite database path (overrides default) |

## Repository

https://github.com/dajiaohuang/SagaSmith-coc-skills
