# Traffic Wiki Extraction Schema

## Language policy

- Use English for `canonical_name`, `summary_en`, topics, and generated page titles.
- Preserve translations, aliases, abbreviations, former names, and romanizations in structured `names` entries.
- Use BCP 47 language tags and an optional locale code.

## Knowledge policy

- Store entities and atomic claims, not prose synthesis.
- Every extracted claim starts as `proposed`.
- Every claim includes a source, locator, and short exact quote.
- Every quote is one contiguous, character-exact source substring. Use multiple evidence items instead of ellipses or stitched passages.
- Use the deepest available numbered section in every structured Markdown locator.
- Store source views and later historical interpretations as attributed claims.
- Never infer causality, priority, dominance, replacement, or field-founding from chronology alone.

## Scope

- `core`: directly about traffic engineering or urban transport knowledge.
- `interface`: connects traffic engineering to rail, maritime, aviation, logistics, economics, or other adjacent fields.
- `background`: provides necessary historical or technical context.

## Local files

- `data/sources.jsonl`: registered source records.
- `data/entities.jsonl`: normalized candidate entities.
- `data/claims.jsonl`: evidence-backed candidate claims.
- `data/runs.jsonl`: extraction provenance.
- `staging/`: source-specific payloads before merge.
- `wiki/` and `graph/`: generated, disposable views.

## Related materials

- A publication cited by the current text is a `Work` entity, not automatically a consulted `Source`.
- Register external material as a `Source` only after inspecting it, and cite it for every externally enriched fact.
- Verify titles, DOI values, URLs, dates, and author lists; never complete them from memory or a short citation.

The full record contract and quality standard live in the project-local `build-traffic-wiki` skill references.
