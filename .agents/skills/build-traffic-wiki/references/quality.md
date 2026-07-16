# Traffic Wiki quality standard

Apply this standard before every merge and repair.

## 1. Claim and evidence granularity

- Store one independently reviewable proposition per claim. Split conjunctions when either part could be accepted or rejected separately.
- Keep time, place, role, population, model form, and study scope in `qualifiers`; do not use qualifiers to hide a second proposition.
- Support each claim with the smallest contiguous source passage that still proves the proposition.
- Copy `quote` character-for-character from the registered source. Do not paraphrase, correct OCR, change quotation marks, insert `...`, or join non-adjacent text.
- If support spans two or more passages, add one evidence item per passage. The evidence items jointly support the claim; each quote remains contiguous.
- Keep each quote at 600 characters or fewer. Split long passages at sentence boundaries.
- For a table, quote the exact Markdown or HTML row fragment containing the label and value. For a formula, quote the exact source formula block or the adjacent defining sentence.
- Delete a claim when no exact passage supports its subject, predicate, object, and material qualifiers. Do not preserve it by weakening the quote.

## 2. Locator standard

Use the deepest stable structure available.

```text
chapter:3/section:3.5.2/paragraph:4
chapter:3/section:3.7.1/table:3.1/row:gravity-model
chapter:3/section:3.9/list:policy-insensitivity/item:2
chapter:3/notes/note:23
page:325
```

- `section` must name the deepest numbered Markdown heading containing the quote, not merely its parent `###` section.
- Number `paragraph:N` by non-empty Markdown blocks, separated by blank lines, within that deepest heading. Exclude the heading itself.
- Prefer a stable semantic row or item key when one exists; otherwise use a one-based row or item number.
- Use `notes/note:N` for numbered endnotes. Do not locate a note-only statement in its parent prose section.
- When source pagination is reliable, a page locator may be added, but it does not replace the deepest section locator for structured Markdown.

## 3. Related materials and external enrichment

Distinguish these cases:

1. **Mentioned work**: the supplied source cites or discusses a publication. Create or reuse a `Work` entity only when a retained claim needs it. Evidence still points to the supplied source.
2. **Consulted source**: the full text, relevant pages, abstract, catalogue record, DOI registry, or official page was actually inspected. Register it as a separate `Source`, with its real path or URL and content hash when local.
3. **External enrichment**: a name, date, affiliation, title, DOI, URL, or substantive claim comes from a consulted external source. Cite that external `source_id`; do not attribute it to the original book.

Rules:

- Do not register an unconsulted bibliography entry as a `Source`.
- Do not infer a full title, author list, DOI, URL, edition, or publication year from a short author-year citation.
- Prefer publisher pages, DOI registries, institutional archives, standards bodies, and the publication itself over aggregators.
- A web search result is discovery only. Open and inspect the supporting page before recording it.
- Keep external material relevant to a retained entity or claim. Do not create link collections without graph relationships.
- If current predicates cannot express the source faithfully, skip the assertion and record the gap in the run warnings.
- Never let external material replace evidence from the section currently being extracted; use it only as separately sourced enrichment.

## 4. Entity identity and deduplication

- Compare normalized canonical names and every structured name form within the same entity type.
- A same-type alias or abbreviation may resolve to only one active entity ID. Merge duplicates or explicitly disambiguate names before validation.
- Do not merge different phases, editions, organizations, or similarly translated concepts without source evidence that they are the same identity.
- After a merge, rewrite claim references deterministically and rebuild generated views.
- Remove entities that neither identify a registered source nor participate in a retained claim.

## 5. Confidence calibration

`confidence` measures extraction certainty, not historical truth.

- `0.95–1.00`: direct, explicit, unambiguous wording or an exact table value.
- `0.85–0.94`: explicit support requiring limited context or multiple contiguous evidence items.
- `0.70–0.84`: necessary implication, collective attribution, OCR boundary, or residual identity ambiguity; use `implicit` where applicable.
- Below `0.70`: do not ingest by default. Record the unresolved issue in run warnings.

Do not raise confidence merely because the same model produced the claim twice. Independent source support may add evidence and run IDs, but source quality and semantic clarity still govern confidence.

## 6. Quality gate

Before merge or completion, require all of the following:

- every local-source quote is a character-exact substring;
- every numbered-section locator matches the deepest heading containing the quote;
- every claim is atomic and its evidence proves the full relation;
- no same-type name form belongs to multiple entity IDs;
- no unsupported causal, priority, replacement, or dominance predicate remains;
- no orphan entity remains except one needed to identify a registered source;
- `validate` and `build` both succeed.

## 7. Repair existing records

Never edit formal JSONL by hand. Create a staging repair payload with source note updates, entity merges, claim replacements or deletions, and one provenance run. Apply it with:

```bash
/Users/ran/WorkSpace/SoftWare/miniconda3/envs/research/bin/python3.10 \
  .agents/skills/build-traffic-wiki/scripts/traffic_wiki.py repair \
  --root traffic-wiki \
  --payload traffic-wiki/staging/<repair>.json
```

Back up uncommitted data before a broad repair. Run `validate` and `build` immediately afterwards.
