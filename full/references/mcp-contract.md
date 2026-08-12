# SagaSmith CoC MCP contract

This reference describes the current public surface. Native schemas returned by
the running server are authoritative; inspect them before constructing a write.
There is no CLI or fixed-superset compatibility path.

## Always-visible tools

The six bootstrap tools are visible in every phase:

| Tool | Purpose |
|---|---|
| exposure | open/get/search/set the session's native tool exposure |
| server_capabilities | system, Pack schema, phases, and tool policy |
| storage_status | local database/artifact readiness |
| campaign_query | list/get accessible coc7e campaigns |
| game_phase | read authoritative Lobby/Play/Combat phase |
| skill_query | list/read installed CoC and ModuleGen Skills |

Start an MCP session with exposure(action="open"). Before a campaign exists,
search/set only campaign_change. After creation, open a new exposure bound to the
campaign. On a phase change, restore, branch checkout, undo, or redo, consume
tools/list_changed, refresh schemas, and use search/set for the next phase.

## Complete 43-tool inventory

The server exposes exactly these public tool identities:

~~~text
actor_knowledge_change  actor_knowledge_query
branch_change           branch_query
campaign_change         campaign_query         campaign_event
character_change        character_query
chase_action            chase_end              chase_query            chase_start
coc_dice_roll           coc_hp_change          coc_resolve            coc_sanity_check
combat_action           combat_attack          combat_end             combat_query
combat_start            content_pack           continuity_context
development_query       development_settle
exposure                game_phase
group_luck_check        group_luck_query
investigation_check     investigation_query
memory_change           memory_query
module_change           module_draft           module_query
server_capabilities     skill_query
snapshot_change         snapshot_query         state_revision
storage_status
~~~

CORE tools are the six bootstrap tools above. Every other tool must be
phase-legal, exposed for the current session, and authorized again at call time.

## Phase catalog

### Lobby

Loadable Lobby tools:

~~~text
actor_knowledge_change actor_knowledge_query branch_change branch_query
campaign_change campaign_event character_change character_query coc_dice_roll
coc_resolve content_pack continuity_context development_query
development_settle memory_change memory_query module_change module_draft
module_query snapshot_change snapshot_query state_revision
~~~

DM/owner authorization is required for actor_knowledge_change, branch_change,
campaign_event, character_change, content_pack, memory_change, memory_query,
module_change, module_draft, snapshot_change, snapshot_query, and state_revision.

### Play

Loadable Play tools:

~~~text
actor_knowledge_change actor_knowledge_query branch_change branch_query
campaign_change campaign_event character_change character_query chase_action
chase_end chase_query chase_start coc_dice_roll coc_hp_change coc_resolve
coc_sanity_check combat_start continuity_context group_luck_check
group_luck_query investigation_check investigation_query memory_change
memory_query module_change module_query snapshot_change snapshot_query
state_revision
~~~

DM/owner authorization is required for actor_knowledge_change, branch_change,
campaign_change, campaign_event, chase_end, chase_start, combat_start,
group_luck_check, group_luck_query, memory_change, memory_query, module_change,
snapshot_change, snapshot_query, and state_revision. Player calls remain limited
by campaign membership and actor control.

### Combat

Loadable Combat tools:

~~~text
actor_knowledge_query branch_change branch_query character_change
character_query coc_dice_roll coc_hp_change coc_resolve coc_sanity_check
combat_action combat_attack combat_end combat_query continuity_context
module_query snapshot_change snapshot_query state_revision
~~~

branch_change, combat_end, snapshot_change, snapshot_query, and state_revision
require DM/owner authorization. Call-specific actor control and encounter-turn
checks still apply to other tools.

## Facade actions

| Tool | Current actions or kinds |
|---|---|
| campaign_change | create, set_phase, grant_campaign, grant_actor |
| campaign_query | list, get |
| character_query / character_change | list/get; create/instantiate/update |
| module_draft | start, get, evidence, edit, finalize |
| content_pack | list, get, import, export, activate, deactivate, remove |
| module_query / module_change | list/index/current/progress/search; set_progress |
| memory_query / memory_change | list/search; add/upsert/revise/commit |
| campaign_event | add, list |
| actor_knowledge_query / change | list/search; add/revise |
| branch_query / change | current/list/get/compare; create/checkout |
| snapshot_query / change | list/get/verify/lineage; create/restore |
| state_revision | history, receipt, undo, redo |
| coc_dice_roll | d100, expression |
| coc_resolve | skill, opposed, sanity, melee, ranged, chase_speed, chase_action |
| development_query / settle | read checked skills; settle all checked skills |
| group_luck_query / check | read lowest candidates; authoritative group roll |
| investigation_query | pending, history |
| investigation_check | open, spend_luck, push, settle, abort |
| coc_hp_change | damage, heal |
| chase_action | move, check, speed_check, end_turn |
| combat_action | join, move, end_turn |
| combat_attack | open, resolve, abort |
| exposure | open, get, search, set |
| skill_query | list, read |

Use module_draft edit operations source_text, content, statblock, asset, actor,
package, and advance. Use data as the action wrapper for current CoC module and
Pack calls. Finalize a CoC draft with data.package_id.

character_change(action="instantiate") is a Keeper-only Lobby operation for a
Pack actor bound as preset_pc. Pass the library character id returned in
content_pack import actor_map as data.template_id; data.name and
data.player_name are optional overrides. The server validates the stored CoC
investigator sheet, creates a campaign-local copy, and grants the Keeper actor
control. Grant the resulting actor to its player explicitly with
campaign_change(action="grant_actor").

## Revision and idempotency rules

- Read current campaign, character, and branch revisions immediately before a
  guarded write.
- Use a stable idempotency key unique to one exact request. Reuse it only after a
  transport interruption or other exact retry.
- If any request field changes, use a new key.
- On a revision conflict, reread state and reconsider the action. Never overwrite
  by guessing the next revision.
- branch_change and snapshot_change require both expected_revision and
  expected_branch_id.
- Random-settlement tools commit the random-stream position and receipt with the
  authoritative state they own.

## Resolution ownership

Use the highest-level tool that owns the entire deterministic mechanic:

1. investigation_check for live ordinary/combined checks, Luck/Push decisions,
   and development marking;
2. group_luck_check for present-group Luck;
3. coc_sanity_check for SAN encounter settlement;
4. coc_hp_change for non-combat injury/healing;
5. chase tools for an active Chase;
6. combat tools for an active Combat;
7. coc_resolve for source-explicit one-shot mechanics without a task facade;
8. coc_dice_roll only when no higher-level tool owns the roll.

Never pre-roll or locally select a favorable result. A random receipt proves the
mechanical transaction, not the Agent's later interpretation.

## Investigation and continuity

investigation_check is resumable per actor:

1. open reads the current actor sheet and performs one campaign-stream roll;
2. spend_luck or push records the authorized decision;
3. settle moves the check to history and marks eligible skills;
4. abort is Keeper-only and records a reason.

After settle, the response requests continuity. The Agent decides actual clue,
audience, knowledge, and consequences, then memory_change(action="commit") may
atomically write:

- one branch event;
- zero or more objective facts;
- zero or more actor-specific knowledge entries;
- an optional snapshot.

Mechanical settlement and continuity commit are deliberately separate
transactions. On interruption, query check history and continuity before
deciding whether the semantic commit is still missing.

## Phase transitions and exclusivity

- campaign_change(set_phase) can set only Lobby or Play.
- Returning to Lobby is rejected while an investigation check is pending.
- combat_start derives Combat phase from authoritative combat.active.
- combat_end closes the encounter and returns to Play.
- Chase starts only in Play and cannot coexist with Combat.
- Combat starts only in Play and cannot coexist with Chase.
- Resolve or abort pending response choices before ending or changing context.

## Authorization and audiences

- The host binds principal_id; the model never selects it.
- DM/owner tools enforce role again at call time.
- Player writes require actor control where applicable.
- continuity_context forces player-safe audience projection for non-DM callers.
- module_query filters Keeper-only scenes/results for players.
- actor knowledge is branch-scoped and actor-authorized.
- campaign events carry explicit dm/party/public/actor audiences and
  participants.

## Known current boundaries

Do not claim tools that do not exist. The current CoC MCP does not yet expose:

- rulebook_draft or rule-search/expand Pack facades;
- isolated npc_conversation or bounded_evaluation;
- D&D-style granular inventory/wallet/equipment transfer tools;
- a separate module_expand tool;
- granular long-term therapy, aging, Luck recovery, tome, spell-learning, or
  vehicle-chase settlement.

Use source-backed Agent rulings and the existing standard writes only where that
does not fabricate a missing deterministic mechanic.
