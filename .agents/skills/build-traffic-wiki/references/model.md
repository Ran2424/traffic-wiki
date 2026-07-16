# Traffic Wiki extraction model

## Contents

1. Storage files
2. Identifier rules
3. Source record
4. Entity record
5. Multilingual names
6. Claim record
7. Evidence and qualifiers
8. Run record
9. Controlled values
10. Complete payload example
11. Repair payload

## 1. Storage files

The lightweight extraction layer uses four append-and-merge JSONL files:

| File | Contents |
|---|---|
| `data/sources.jsonl` | one registered source per line |
| `data/entities.jsonl` | normalized candidate entities |
| `data/claims.jsonl` | atomic, evidence-backed candidate claims |
| `data/runs.jsonl` | extraction run provenance |

`staging/*.json` contains source-specific payloads before deterministic merge. `wiki/` and `graph/` are generated views.

## 2. Identifier rules

Use lowercase, readable, stable IDs:

```text
source:<author>-<year>-<short-title>
person:<english-name>
organization:<english-name>
concept:<english-name>
method:<english-name>
model:<english-name>
claim:<source-short-id>:<sequence>
run:<date-time-or-unique-suffix>
```

Normalize spaces to hyphens and remove punctuation that has no identifying value. Once stored, do not rename an ID merely because `canonical_name` is corrected.

## 3. Source record

Required fields:

```json
{
  "id": "source:wardrop-1952-road-traffic",
  "title": "Some Theoretical Aspects of Road Traffic Research",
  "source_type": "paper",
  "language": "en",
  "authors": ["John Glen Wardrop"],
  "year": 1952,
  "path": "external-or-project-relative-path",
  "content_hash": "sha256-or-null",
  "visibility": "private",
  "notes": ""
}
```

Rules:

- `language` uses a BCP 47 tag.
- `path` can be a user-provided source label when no file exists.
- `content_hash` is required when a readable local file exists.
- `authors` contains display names, not entity IDs; authorship claims connect source Works to Person entities.
- Do not overwrite an existing source ID with a different non-null content hash.

## 4. Entity record

Required fields:

```json
{
  "id": "person:john-glen-wardrop",
  "type": "Person",
  "canonical_name": "John Glen Wardrop",
  "names": [],
  "summary_en": "British traffic engineer associated with early traffic assignment theory.",
  "topics": ["traffic-assignment"],
  "scope_position": "core",
  "status": "proposed",
  "first_seen_source_id": "source:wardrop-1952-road-traffic"
}
```

Rules:

- `canonical_name` is English.
- `names` contains an English `preferred` name exactly matching `canonical_name`.
- `summary_en` is short, neutral, and grounded only in ingested sources.
- `topics` uses lowercase hyphen-case terms.
- `scope_position` is `core`, `interface`, or `background`.
- New extracted entities use `proposed`.
- Reuse an existing entity when type and normalized English canonical name match exactly.

Allowed entity types:

```text
Person
Organization
Event
Work
Concept
Theory
Method
Model
Algorithm
Metric
Tool
Technology
Policy
Standard
Project
Place
NamedPeriod
```

## 5. Multilingual names

Use structured name forms instead of a flat `other_names` list:

```json
{
  "text": "约翰·格伦·沃德罗普",
  "language": "zh-Hans",
  "name_type": "translated",
  "locale": "CN",
  "source_ids": ["source:example-chinese-book"]
}
```

Required fields:

- `text`
- `language`
- `name_type`
- `source_ids`

Optional field:

- `locale`: ISO country or regional code when the form is locale-specific.

Allowed `name_type` values:

```text
preferred
alias
translated
abbreviation
former
romanized
```

Name rules:

- Use `translated` for a conventional translated name.
- Use `romanized` for transliteration into another script.
- Use `alias` only for a genuine alternative name, not a loose description.
- Use `former` for historical organization or policy names.
- Use `abbreviation` for acronyms and initialisms.
- Multiple countries may use different translations in the same language; distinguish them with `locale` and evidence.
- Every non-preferred name should cite at least one source when known.

## 6. Claim record

Entity-object claim:

```json
{
  "id": "claim:wardrop-1952:001",
  "subject_id": "work:some-theoretical-aspects-of-road-traffic-research",
  "predicate": "formulated",
  "object_id": "concept:user-equilibrium",
  "literal": null,
  "qualifiers": {"time": {"year": 1952}},
  "claim_kind": "factual",
  "assertion_mode": "explicit",
  "polarity": "positive",
  "attributed_to_id": null,
  "evidence": [],
  "confidence": 0.96,
  "status": "proposed",
  "run_ids": ["run:2026-07-15-001"]
}
```

Literal-object claim:

```json
{
  "object_id": null,
  "literal": {
    "value": 1952,
    "datatype": "year",
    "unit": null
  }
}
```

Rules:

- Exactly one of `object_id` and `literal` is non-null.
- `subject_id` and entity `object_id` must resolve to known entities after merge.
- `claim_kind` is `factual`, `attributed_view`, or `historiographical_interpretation`.
- `attributed_view` and `historiographical_interpretation` require `attributed_to_id`.
- `assertion_mode` is `explicit` or `implicit`.
- `polarity` is `positive`, `negative`, or `uncertain`.
- Extracted claims always start as `proposed`.
- `confidence` records extraction confidence only and must be between 0 and 1.
- `run_ids` contains every extraction run that produced or independently reproduced the claim.

## 7. Evidence and qualifiers

Every claim needs at least one evidence item:

```json
{
  "source_id": "source:wardrop-1952-road-traffic",
  "locator": "page:325",
  "quote": "short exact wording from the supplied source"
}
```

Use the most precise stable locator available:

```text
page:325
chapter:4/page:87
section:Introduction/paragraph:3
paragraph:12
```

Keep quotes short and exact. Do not store a model paraphrase in `quote`.

Apply the mandatory quote granularity, deepest-section locator, table, note, and multi-passage rules in [quality.md](quality.md).

Use `qualifiers` for structured context:

```json
{
  "time": {"year": 1952},
  "place_id": "place:united-kingdom",
  "role": "author",
  "scope": "static-traffic-assignment"
}
```

Do not put source metadata, confidence, or review comments in `qualifiers`.

## 8. Run record

```json
{
  "id": "run:2026-07-15-001",
  "source_id": "source:wardrop-1952-road-traffic",
  "started_at": "2026-07-15T10:00:00+08:00",
  "completed_at": "2026-07-15T10:04:00+08:00",
  "model": "provider/model-version",
  "prompt_version": "build-traffic-wiki-0.1.0",
  "schema_version": "traffic-wiki-extraction-0.1.0",
  "input_hash": "sha256",
  "status": "completed",
  "warnings": []
}
```

Run status is `completed`, `partial`, or `failed`.

## 9. Controlled values

Allowed predicates:

```text
authored
edited
translated
affiliated_with
founded
participated_in
defined
coined_term
formulated
extends
generalizes
derived_from
critiques
contrasts_with
operationalizes
uses
adopted_by
implemented_in
codified_in
applied_to
measured_by
enabled_by
has_participant
occurred_at
produced
part_of
preceded
followed
influenced
caused
first_proposed
founded_field
became_dominant
replaced
marked_turning_point
```

`enabled_by` and the last seven predicates are interpretive or causal. Emit them only when the source explicitly makes the assessment, and use an attributed claim kind.

## 10. Complete payload example

```json
{
  "source": {
    "id": "source:example-1952-paper",
    "title": "Example Traffic Paper",
    "source_type": "paper",
    "language": "en",
    "authors": ["Example Author"],
    "year": 1952,
    "path": "user-pasted-text",
    "content_hash": null,
    "visibility": "private",
    "notes": "Pasted excerpt"
  },
  "entities": [
    {
      "id": "person:example-author",
      "type": "Person",
      "canonical_name": "Example Author",
      "names": [
        {
          "text": "Example Author",
          "language": "en",
          "name_type": "preferred",
          "locale": null,
          "source_ids": ["source:example-1952-paper"]
        },
        {
          "text": "示例作者",
          "language": "zh-Hans",
          "name_type": "translated",
          "locale": "CN",
          "source_ids": ["source:example-1952-paper"]
        }
      ],
      "summary_en": "Author of the supplied traffic paper.",
      "topics": ["traffic-flow"],
      "scope_position": "core",
      "status": "proposed",
      "first_seen_source_id": "source:example-1952-paper"
    },
    {
      "id": "work:example-traffic-paper",
      "type": "Work",
      "canonical_name": "Example Traffic Paper",
      "names": [
        {
          "text": "Example Traffic Paper",
          "language": "en",
          "name_type": "preferred",
          "locale": null,
          "source_ids": ["source:example-1952-paper"]
        }
      ],
      "summary_en": "The source work represented by the supplied excerpt.",
      "topics": ["traffic-flow"],
      "scope_position": "core",
      "status": "proposed",
      "first_seen_source_id": "source:example-1952-paper"
    }
  ],
  "claims": [
    {
      "id": "claim:example-1952:001",
      "subject_id": "person:example-author",
      "predicate": "authored",
      "object_id": "work:example-traffic-paper",
      "literal": null,
      "qualifiers": {"time": {"year": 1952}},
      "claim_kind": "factual",
      "assertion_mode": "explicit",
      "polarity": "positive",
      "attributed_to_id": null,
      "evidence": [
        {
          "source_id": "source:example-1952-paper",
          "locator": "paragraph:1",
          "quote": "Example Author"
        }
      ],
      "confidence": 0.99,
      "status": "proposed",
      "run_ids": ["run:2026-07-15-example"]
    }
  ],
  "run": {
    "id": "run:2026-07-15-example",
    "source_id": "source:example-1952-paper",
    "started_at": "2026-07-15T10:00:00+08:00",
    "completed_at": "2026-07-15T10:01:00+08:00",
    "model": "provider/model-version",
    "prompt_version": "build-traffic-wiki-0.1.0",
    "schema_version": "traffic-wiki-extraction-0.1.0",
    "input_hash": "example-input-hash",
    "status": "completed",
    "warnings": []
  }
}
```

## 11. Repair payload

Use repairs only for records already merged. A repair payload may update source notes, merge duplicate entities, replace claim evidence or confidence, and delete unsupported claims:

```json
{
  "source_updates": [{"id": "source:example", "notes": "Updated coverage note"}],
  "entity_merges": [{"from_id": "tool:old-id", "into_id": "tool:canonical-id"}],
  "claim_updates": [{
    "id": "claim:example:001",
    "evidence": [{"source_id": "source:example", "locator": "section:1.2/paragraph:3", "quote": "Exact text"}],
    "confidence": 0.92
  }],
  "delete_claim_ids": ["claim:example:unsupported"],
  "run": {}
}
```

The repair command rewrites entity references, validates the complete store, and writes JSONL atomically. It does not permit arbitrary field replacement.
