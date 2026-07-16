---
name: build-traffic-wiki
description: Build and maintain the project-local Traffic Wiki from supplied transportation texts. Use when Codex is given pasted text, Markdown, extracted book chapters, papers, reports, standards, or other traffic-engineering sources and should extract English-first entities, multilingual names, evidence-backed claims, source metadata, and a lightweight graph/wiki without writing historical narrative.
---

# Build Traffic Wiki

Create a lightweight, evidence-linked candidate knowledge graph from transport sources. Keep English as the canonical language while preserving translations, aliases, abbreviations, former names, and romanizations as structured name forms.

## Fixed boundaries

- Work only on knowledge extraction in this version.
- Write source, entity, claim, and run records; generate browseable pages and graph JSON from them.
- Do not write broad historical narratives or editorial syntheses.
- Treat every extracted claim as `proposed`.
- Never let the LLM directly overwrite existing JSONL records.
- Do not introduce SQLite, Neo4j, embeddings, a web UI, or multi-agent orchestration.

## Before ingesting

1. Use `traffic-wiki/` under the current project root.
2. If it does not exist, run:

   ```bash
   /Users/ran/WorkSpace/SoftWare/miniconda3/envs/research/bin/python3.10 \
     .agents/skills/build-traffic-wiki/scripts/traffic_wiki.py init \
     --root traffic-wiki
   ```

3. Read `traffic-wiki/purpose.md`, `traffic-wiki/schema.md`, [references/model.md](references/model.md), and [references/quality.md](references/quality.md) completely before producing records.
4. Search `traffic-wiki/data/entities.jsonl` before proposing a new entity.

## Ingest workflow

### 1. Register the source

Create one source record for the supplied material.

- Prefer `source:<author>-<year>-<short-title>` when author and year are known.
- Record the original path or user-provided label.
- Record SHA-256 when a local file is available.
- Use `paragraph:N` or `section:<name>/paragraph:N` locators for pasted text.
- Do not copy a private source into the repository unless the user asks.

### 2. Extract entities

Extract only entities needed by at least one claim or needed to identify the source.

- Set `canonical_name` to the best established English name.
- Add an English `preferred` entry to `names` matching `canonical_name`.
- Store every translation or synonym as a separate structured name form.
- Use BCP 47 language tags such as `en`, `zh-Hans`, `zh-Hant`, `ja`, or `de`.
- Use `locale` only when a country or regional convention matters.
- Distinguish `alias`, `translated`, `abbreviation`, `former`, and `romanized`.
- Do not merge entities solely because names translate similarly.
- Search every canonical name, alias, abbreviation, translation, and former name before creating an entity. Resolve same-type name collisions before merge.
- Keep `summary_en` short, neutral, and limited to the supplied source.

### 3. Extract claims

Create one atomic subject-predicate-object claim at a time.

- Use only predicates defined in `traffic-wiki/schema.md`.
- Attach at least one evidence item with `source_id`, `locator`, and a short exact `quote`.
- Make every quote one contiguous, character-exact source substring. Never insert ellipses, normalize wording, or stitch passages. Use multiple evidence items when support spans passages.
- Locate evidence under the deepest available numbered heading; use table rows, list items, and notes locators when applicable.
- Use `factual`, `attributed_view`, or `historiographical_interpretation` for `claim_kind`.
- Use `explicit` unless the source leaves a necessary implication; mark the latter `implicit`.
- Put time, place, role, and scope in `qualifiers`.
- Never infer causality from chronology.
- Do not emit `first_proposed`, `caused`, `founded_field`, `became_dominant`, `replaced`, or `marked_turning_point` unless the source explicitly makes that assessment. When it does, model it as an attributed or historiographical claim.
- Do not treat model confidence as truth.
- Calibrate extraction confidence with the bands in [references/quality.md](references/quality.md); do not assign near-certain confidence to implicit or cross-passage interpretations.

### 3a. Handle related material

- Represent a work merely cited by the supplied text as a `Work` entity supported by the supplied text.
- Register a separate `Source` only after that external material or authoritative metadata has actually been consulted.
- Attribute every externally enriched fact to its external source. Never cite the supplied book as evidence for details learned elsewhere.
- Add a DOI, URL, full title, or bibliographic detail only after verification. Do not invent or complete metadata from memory.

### 4. Create a staging payload

Write one JSON payload to:

`traffic-wiki/staging/<source-id>.<run-id>.json`

The payload must contain:

```json
{
  "source": {},
  "entities": [],
  "claims": [],
  "run": {}
}
```

Follow [references/model.md](references/model.md) exactly. Keep the payload source-specific; do not include unrelated cleanup.

### 5. Merge deterministically

Run:

```bash
/Users/ran/WorkSpace/SoftWare/miniconda3/envs/research/bin/python3.10 \
  .agents/skills/build-traffic-wiki/scripts/traffic_wiki.py upsert \
  --root traffic-wiki \
  --payload traffic-wiki/staging/<payload>.json
```

The script validates references, merges structured names, reuses exact English entity matches, deduplicates claims, and writes JSONL atomically. Fix the payload if validation fails; do not bypass the validator.

For corrections to records already merged, create a declarative repair payload and run `traffic_wiki.py repair`; never edit formal JSONL directly. See [references/quality.md](references/quality.md).

### 6. Validate and build

Run both commands:

```bash
/Users/ran/WorkSpace/SoftWare/miniconda3/envs/research/bin/python3.10 \
  .agents/skills/build-traffic-wiki/scripts/traffic_wiki.py validate \
  --root traffic-wiki

/Users/ran/WorkSpace/SoftWare/miniconda3/envs/research/bin/python3.10 \
  .agents/skills/build-traffic-wiki/scripts/traffic_wiki.py build \
  --root traffic-wiki
```

Generated files are disposable views. Never hand-edit `traffic-wiki/wiki/` or `traffic-wiki/graph/`.

## Finish criteria

Before reporting completion, verify:

- every entity has an English canonical name and English preferred name form;
- translations and aliases have language and name type;
- every claim resolves to known entities or a typed literal;
- every claim has a source, locator, and exact quote;
- every local-source quote passes character-exact verification and uses the deepest numbered section;
- no same-type entity name or abbreviation resolves to multiple entity IDs;
- related materials are clearly distinguished from sources actually consulted;
- no unsupported causal or “first” relation was added;
- validation succeeds;
- the entity index and graph were rebuilt;
- report inserted, merged, and skipped counts plus any unresolved ambiguity.

## Resources

- [references/model.md](references/model.md): complete record contracts, controlled values, and payload example.
- [references/quality.md](references/quality.md): mandatory evidence granularity, locator, related-material, confidence, and repair standards.
- `scripts/traffic_wiki.py`: initialize, validate, merge, and build the Traffic Wiki.
- `assets/purpose.md` and `assets/schema.md`: templates copied during initialization.
