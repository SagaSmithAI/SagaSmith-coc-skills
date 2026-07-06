---
name: coc7-keeper-suite
description: "Cross-platform Call of Cthulhu 7e Keeper and campaign workflow using the SagaSmith JSON CLI."
version: 2.0.0
---

# SagaSmith CoC 7e Suite

This is a pure Agent Skill package. Runtime mode operates `sagasmith-coc`
through shell commands ending in `--json`.

## Startup

1. Run `sagasmith-coc doctor --json`.
2. If available, use Runtime mode.
3. Otherwise use Portable mode for Keeper guidance and authored rule summaries.
4. Portable mode must never claim to persist campaigns, investigators, saves, or memory.

## Included Skills

- `skills/coc7-keeper`: investigation, adjudication, SAN, combat, chase, and horror.
- `skills/coc7-campaign-manager`: campaign, investigator, scenario, save, and memory.

## Invariants

- Keep `campaign_id`, ruleset (`classic`/`pulp`), and locale explicit.
- Rules are retrieved from user-provided sources; do not claim commercial books are bundled.
- Search first, then expand only the selected rule or scenario chunk.
- Treat stdout as one JSON envelope and branch on `error.code`.
- Separate player-visible clues from Keeper-only secrets.

See `references/cli-contract.md` and `references/workflows.md`.
