#!/usr/bin/env python3
"""Maintain the lightweight, extraction-only Traffic Wiki."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any, TypeVar

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator


SCHEMA_VERSION = "traffic-wiki-extraction-0.1.0"

ENTITY_TYPES = {
    "Person", "Organization", "Event", "Work", "Concept", "Theory", "Method",
    "Model", "Algorithm", "Metric", "Tool", "Technology", "Policy", "Standard",
    "Project", "Place", "NamedPeriod",
}
TYPE_PREFIX = {
    "Person": "person", "Organization": "organization", "Event": "event", "Work": "work",
    "Concept": "concept", "Theory": "theory", "Method": "method", "Model": "model",
    "Algorithm": "algorithm", "Metric": "metric", "Tool": "tool", "Technology": "technology",
    "Policy": "policy", "Standard": "standard", "Project": "project", "Place": "place",
    "NamedPeriod": "period",
}
SOURCE_TYPES = {
    "book", "chapter", "paper", "report", "standard", "policy", "web", "encyclopedia",
    "archival", "pasted_text", "other",
}
NAME_TYPES = {"preferred", "alias", "translated", "abbreviation", "former", "romanized"}
PREDICATES = {
    "authored", "edited", "translated", "affiliated_with", "founded", "participated_in",
    "defined", "coined_term", "formulated", "extends", "generalizes", "derived_from",
    "critiques", "contrasts_with", "operationalizes", "uses", "adopted_by", "implemented_in",
    "codified_in", "applied_to", "measured_by", "enabled_by", "has_participant", "occurred_at",
    "produced", "part_of", "preceded", "followed", "influenced", "caused", "first_proposed",
    "founded_field", "became_dominant", "replaced", "marked_turning_point",
}
HIGH_RISK_PREDICATES = {
    "enabled_by", "influenced", "caused", "first_proposed", "founded_field",
    "became_dominant", "replaced", "marked_turning_point",
}
CLAIM_KINDS = {"factual", "attributed_view", "historiographical_interpretation"}
ASSERTION_MODES = {"explicit", "implicit"}
POLARITIES = {"positive", "negative", "uncertain"}
ENTITY_STATUSES = {"proposed", "verified", "deprecated"}
CLAIM_STATUSES = {"proposed", "verified", "disputed", "rejected", "deprecated"}
RUN_STATUSES = {"completed", "partial", "failed"}
SCOPE_POSITIONS = {"core", "interface", "background"}
VISIBILITIES = {"private", "restricted", "public"}


class ModelError(ValueError):
    pass


class Record(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str = Field(min_length=1)


class Source(Record):
    title: str = Field(min_length=1)
    source_type: str
    language: str = Field(min_length=1)
    authors: list[str]
    year: int | None
    path: str = Field(min_length=1)
    content_hash: str | None
    visibility: str
    notes: str

    @model_validator(mode="after")
    def check_values(self) -> "Source":
        if not self.id.startswith("source:"):
            raise ValueError("source id must start with source:")
        if self.source_type not in SOURCE_TYPES:
            raise ValueError(f"unsupported source_type {self.source_type!r}")
        if self.visibility not in VISIBILITIES:
            raise ValueError(f"unsupported visibility {self.visibility!r}")
        if any(not value.strip() for value in self.authors):
            raise ValueError("authors cannot contain empty strings")
        if self.content_hash is not None and not self.content_hash.strip():
            raise ValueError("content_hash cannot be blank")
        return self


class NameForm(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str = Field(min_length=1)
    language: str = Field(min_length=1)
    name_type: str
    locale: str | None = None
    source_ids: list[str]

    @field_validator("name_type")
    @classmethod
    def check_name_type(cls, value: str) -> str:
        if value not in NAME_TYPES:
            raise ValueError(f"unsupported name_type {value!r}")
        return value


class Entity(Record):
    type: str
    canonical_name: str = Field(min_length=1)
    names: list[NameForm] = Field(min_length=1)
    summary_en: str
    topics: list[str]
    scope_position: str
    status: str
    first_seen_source_id: str

    @model_validator(mode="after")
    def check_values(self) -> "Entity":
        if self.type not in ENTITY_TYPES:
            raise ValueError(f"unsupported entity type {self.type!r}")
        prefix = f"{TYPE_PREFIX[self.type]}:"
        if not self.id.startswith(prefix):
            raise ValueError(f"{self.type} id must start with {prefix}")
        if self.scope_position not in SCOPE_POSITIONS:
            raise ValueError(f"unsupported scope_position {self.scope_position!r}")
        if self.status not in ENTITY_STATUSES:
            raise ValueError(f"unsupported entity status {self.status!r}")
        if any(not topic.strip() for topic in self.topics):
            raise ValueError("topics cannot contain empty strings")
        if not any(
            item.name_type == "preferred"
            and item.language.lower().startswith("en")
            and item.text == self.canonical_name
            for item in self.names
        ):
            raise ValueError("names needs an English preferred form matching canonical_name")
        return self


class LiteralValue(BaseModel):
    model_config = ConfigDict(extra="forbid")
    value: Any
    datatype: str = Field(min_length=1)
    unit: str | None


class Evidence(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source_id: str
    locator: str = Field(min_length=1)
    quote: str = Field(min_length=1, max_length=600)


class Claim(Record):
    subject_id: str
    predicate: str
    object_id: str | None
    literal: LiteralValue | None
    qualifiers: dict[str, Any]
    claim_kind: str
    assertion_mode: str
    polarity: str
    attributed_to_id: str | None
    evidence: list[Evidence] = Field(min_length=1)
    confidence: float = Field(ge=0, le=1)
    status: str
    run_ids: list[str] = Field(min_length=1)

    @model_validator(mode="after")
    def check_values(self) -> "Claim":
        if not self.id.startswith("claim:"):
            raise ValueError("claim id must start with claim:")
        if self.predicate not in PREDICATES:
            raise ValueError(f"unsupported predicate {self.predicate!r}")
        if (self.object_id is None) == (self.literal is None):
            raise ValueError("exactly one of object_id and literal must be non-null")
        if self.claim_kind not in CLAIM_KINDS:
            raise ValueError(f"unsupported claim_kind {self.claim_kind!r}")
        if self.claim_kind != "factual" and self.attributed_to_id is None:
            raise ValueError("attributed claims require attributed_to_id")
        if self.assertion_mode not in ASSERTION_MODES:
            raise ValueError(f"unsupported assertion_mode {self.assertion_mode!r}")
        if self.polarity not in POLARITIES:
            raise ValueError(f"unsupported polarity {self.polarity!r}")
        if self.status not in CLAIM_STATUSES:
            raise ValueError(f"unsupported claim status {self.status!r}")
        if self.predicate in HIGH_RISK_PREDICATES:
            if self.claim_kind == "factual" or self.attributed_to_id is None:
                raise ValueError("high-risk predicate requires an attributed claim")
            if self.assertion_mode != "explicit":
                raise ValueError("high-risk predicate must be explicit")
        return self


class Run(Record):
    source_id: str
    started_at: str = Field(min_length=1)
    completed_at: str = Field(min_length=1)
    model: str = Field(min_length=1)
    prompt_version: str = Field(min_length=1)
    schema_version: str
    input_hash: str = Field(min_length=1)
    status: str
    warnings: list[str]

    @model_validator(mode="after")
    def check_values(self) -> "Run":
        if not self.id.startswith("run:"):
            raise ValueError("run id must start with run:")
        if self.schema_version != SCHEMA_VERSION:
            raise ValueError(f"schema_version must be {SCHEMA_VERSION}")
        if self.status not in RUN_STATUSES:
            raise ValueError(f"unsupported run status {self.status!r}")
        return self


class Payload(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: Source
    entities: list[Entity]
    claims: list[Claim]
    run: Run


ModelT = TypeVar("ModelT", bound=Record)


def normalize_name(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def index_unique(records: list[ModelT], label: str) -> dict[str, ModelT]:
    result: dict[str, ModelT] = {}
    for record in records:
        if record.id in result:
            raise ModelError(f"{label}: duplicate id {record.id}")
        result[record.id] = record
    return result


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ModelError(f"{path}:{number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise ModelError(f"{path}:{number}: expected a JSON object")
        records.append(value)
    return records


def write_text_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.tmp")
    temp.write_text(content, encoding="utf-8")
    os.replace(temp, path)


def write_jsonl(path: Path, records: list[Record]) -> None:
    ordered = sorted(records, key=lambda item: item.id)
    content = "".join(
        json.dumps(item.model_dump(mode="json"), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
        for item in ordered
    )
    write_text_atomic(path, content)


def data_paths(root: Path) -> dict[str, Path]:
    return {name: root / "data" / f"{name}.jsonl" for name in ("sources", "entities", "claims", "runs")}


def load_store(root: Path) -> dict[str, list[dict[str, Any]]]:
    return {name: load_jsonl(path) for name, path in data_paths(root).items()}


def validate_store(raw: dict[str, list[dict[str, Any]]]) -> dict[str, list[Record]]:
    sources = [Source.model_validate(item) for item in raw["sources"]]
    entities = [Entity.model_validate(item) for item in raw["entities"]]
    claims = [Claim.model_validate(item) for item in raw["claims"]]
    runs = [Run.model_validate(item) for item in raw["runs"]]
    source_by_id = index_unique(sources, "sources")
    entity_by_id = index_unique(entities, "entities")
    index_unique(claims, "claims")
    run_by_id = index_unique(runs, "runs")

    canonical: dict[tuple[str, str], str] = {}
    for entity in entities:
        key = (entity.type, normalize_name(entity.canonical_name))
        if key in canonical and canonical[key] != entity.id:
            raise ModelError(f"duplicate English canonical identity: {entity.canonical_name!r}")
        canonical[key] = entity.id
        if entity.first_seen_source_id not in source_by_id:
            raise ModelError(f"{entity.id}: unknown first_seen_source_id")
        for name in entity.names:
            unknown = set(name.source_ids) - set(source_by_id)
            if unknown:
                raise ModelError(f"{entity.id}: name has unknown sources {sorted(unknown)}")

    for run in runs:
        if run.source_id not in source_by_id:
            raise ModelError(f"{run.id}: unknown source_id")
    for claim in claims:
        if claim.subject_id not in entity_by_id:
            raise ModelError(f"{claim.id}: unknown subject_id {claim.subject_id}")
        if claim.object_id is not None and claim.object_id not in entity_by_id:
            raise ModelError(f"{claim.id}: unknown object_id {claim.object_id}")
        if claim.attributed_to_id is not None and claim.attributed_to_id not in entity_by_id:
            raise ModelError(f"{claim.id}: unknown attributed_to_id {claim.attributed_to_id}")
        unknown_sources = {item.source_id for item in claim.evidence} - set(source_by_id)
        unknown_runs = set(claim.run_ids) - set(run_by_id)
        if unknown_sources:
            raise ModelError(f"{claim.id}: unknown evidence sources {sorted(unknown_sources)}")
        if unknown_runs:
            raise ModelError(f"{claim.id}: unknown run_ids {sorted(unknown_runs)}")
    return {"sources": sources, "entities": entities, "claims": claims, "runs": runs}


def raw_records(records: list[Record]) -> list[dict[str, Any]]:
    return [item.model_dump(mode="json") for item in records]


def merge_name_forms(existing: list[dict[str, Any]], incoming: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    for name in existing + incoming:
        key = (
            normalize_name(name["text"]), name["language"].casefold(), name["name_type"],
            str(name.get("locale") or "").casefold(),
        )
        if key not in merged:
            merged[key] = dict(name)
        merged[key]["source_ids"] = sorted(
            set(merged[key].get("source_ids", [])) | set(name.get("source_ids", []))
        )
    return sorted(merged.values(), key=lambda item: (item["language"], item["name_type"], item["text"]))


def merge_evidence(existing: list[dict[str, Any]], incoming: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged = {
        (item["source_id"], item["locator"], item["quote"]): dict(item)
        for item in existing + incoming
    }
    return [merged[key] for key in sorted(merged)]


def claim_key(claim: dict[str, Any]) -> str:
    fields = (
        "subject_id", "predicate", "object_id", "literal", "qualifiers", "claim_kind",
        "assertion_mode", "polarity", "attributed_to_id",
    )
    return json.dumps({key: claim[key] for key in fields}, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def merge_source(existing: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    if existing["title"] != incoming["title"]:
        raise ModelError(f"source {existing['id']}: title conflict")
    if existing.get("content_hash") and incoming.get("content_hash") and existing["content_hash"] != incoming["content_hash"]:
        raise ModelError(f"source {existing['id']}: hash conflict; create a new source id")
    merged = dict(existing)
    merged["authors"] = sorted(set(existing["authors"]) | set(incoming["authors"]))
    for field in ("content_hash", "path", "notes"):
        if not merged.get(field) and incoming.get(field):
            merged[field] = incoming[field]
    return merged


def merge_entity(existing: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    if existing["type"] != incoming["type"]:
        raise ModelError(f"entity {existing['id']}: type conflict")
    if normalize_name(existing["canonical_name"]) != normalize_name(incoming["canonical_name"]):
        raise ModelError(f"entity {existing['id']}: canonical_name conflict")
    merged = dict(existing)
    merged["names"] = merge_name_forms(existing["names"], incoming["names"])
    merged["topics"] = sorted(set(existing["topics"]) | set(incoming["topics"]))
    if not merged["summary_en"] and incoming["summary_en"]:
        merged["summary_en"] = incoming["summary_en"]
    return merged


def upsert_payload(root: Path, payload_path: Path) -> dict[str, Any]:
    payload = Payload.model_validate_json(payload_path.read_text(encoding="utf-8"))
    valid = validate_store(load_store(root))
    store = {name: raw_records(records) for name, records in valid.items()}
    incoming_source = payload.source.model_dump(mode="json")
    incoming_run = payload.run.model_dump(mode="json")

    source_by_id = {item["id"]: item for item in store["sources"]}
    source_inserted = int(incoming_source["id"] not in source_by_id)
    source_by_id[incoming_source["id"]] = (
        incoming_source if source_inserted else merge_source(source_by_id[incoming_source["id"]], incoming_source)
    )

    run_by_id = {item["id"]: item for item in store["runs"]}
    run_inserted = int(incoming_run["id"] not in run_by_id)
    if not run_inserted and run_by_id[incoming_run["id"]] != incoming_run:
        raise ModelError(f"run {incoming_run['id']}: conflicting payload")
    run_by_id[incoming_run["id"]] = incoming_run

    entity_by_id = {item["id"]: item for item in store["entities"]}
    canonical = {(item["type"], normalize_name(item["canonical_name"])): item["id"] for item in store["entities"]}
    id_map: dict[str, str] = {}
    entity_inserted = entity_merged = 0
    for entity_model in payload.entities:
        incoming = entity_model.model_dump(mode="json")
        source_id = incoming["id"]
        key = (incoming["type"], normalize_name(incoming["canonical_name"]))
        target_id = source_id if source_id in entity_by_id else canonical.get(key, source_id)
        id_map[source_id] = target_id
        incoming["id"] = target_id
        if target_id in entity_by_id:
            entity_by_id[target_id] = merge_entity(entity_by_id[target_id], incoming)
            entity_merged += 1
        else:
            entity_by_id[target_id] = incoming
            canonical[key] = target_id
            entity_inserted += 1

    claim_by_id = {item["id"]: item for item in store["claims"]}
    semantic = {claim_key(item): item["id"] for item in store["claims"]}
    claim_inserted = claim_merged = 0
    for claim_model in payload.claims:
        incoming = claim_model.model_dump(mode="json")
        for field in ("subject_id", "object_id", "attributed_to_id"):
            if incoming.get(field) is not None:
                incoming[field] = id_map.get(incoming[field], incoming[field])
        incoming["status"] = "proposed"
        key = claim_key(incoming)
        incoming_id = incoming["id"]
        if incoming_id in claim_by_id and claim_key(claim_by_id[incoming_id]) != key:
            raise ModelError(f"claim {incoming_id}: id already represents a different claim")
        target_id = semantic.get(key, incoming_id)
        if target_id in claim_by_id:
            existing = dict(claim_by_id[target_id])
            existing["evidence"] = merge_evidence(existing["evidence"], incoming["evidence"])
            existing["run_ids"] = sorted(set(existing["run_ids"]) | set(incoming["run_ids"]))
            existing["confidence"] = max(existing["confidence"], incoming["confidence"])
            claim_by_id[target_id] = existing
            claim_merged += 1
        else:
            claim_by_id[target_id] = incoming
            semantic[key] = target_id
            claim_inserted += 1

    combined = {
        "sources": list(source_by_id.values()), "entities": list(entity_by_id.values()),
        "claims": list(claim_by_id.values()), "runs": list(run_by_id.values()),
    }
    validated = validate_store(combined)
    for name, records in validated.items():
        write_jsonl(data_paths(root)[name], records)
    result = {
        "status": "merged", "source_inserted": source_inserted, "entities_inserted": entity_inserted,
        "entities_merged": entity_merged, "claims_inserted": claim_inserted,
        "claims_merged": claim_merged, "run_inserted": run_inserted,
        "totals": {name: len(records) for name, records in validated.items()},
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return result


def page_name(entity_id: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "--", entity_id).strip("-") + ".md"


def markdown_cell(value: Any) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def build_views(root: Path) -> dict[str, int]:
    valid = validate_store(load_store(root))
    sources = {item.id: item for item in valid["sources"]}
    entities = {item.id: item for item in valid["entities"]}
    claims = [item for item in valid["claims"] if item.status not in {"rejected", "deprecated"}]
    graph = {
        "schema_version": SCHEMA_VERSION,
        "nodes": [
            {
                "id": item.id, "label": item.canonical_name, "type": item.type,
                "names": [name.model_dump(mode="json") for name in item.names],
                "topics": item.topics, "status": item.status,
            }
            for item in sorted(entities.values(), key=lambda value: value.id)
        ],
        "edges": [
            {
                "id": item.id, "source": item.subject_id, "target": item.object_id,
                "predicate": item.predicate, "status": item.status, "evidence_count": len(item.evidence),
            }
            for item in sorted(claims, key=lambda value: value.id) if item.object_id is not None
        ],
    }
    write_text_atomic(root / "graph" / "graph.json", json.dumps(graph, ensure_ascii=False, indent=2, sort_keys=True) + "\n")

    related: dict[str, list[Claim]] = defaultdict(list)
    for claim in claims:
        related[claim.subject_id].append(claim)
        if claim.object_id is not None:
            related[claim.object_id].append(claim)
    entity_dir = root / "wiki" / "entities"
    entity_dir.mkdir(parents=True, exist_ok=True)
    for stale in entity_dir.glob("*.md"):
        stale.unlink()

    grouped: dict[str, list[Entity]] = defaultdict(list)
    for entity in entities.values():
        grouped[entity.type].append(entity)
        lines = [
            "---", f"id: {json.dumps(entity.id)}", f"type: {json.dumps(entity.type)}",
            f"canonical_name: {json.dumps(entity.canonical_name, ensure_ascii=False)}",
            f"status: {json.dumps(entity.status)}", f"topics: {json.dumps(entity.topics)}", "---", "",
            f"# {entity.canonical_name}", "", entity.summary_en or "No source-grounded summary has been extracted yet.",
            "", "## Names", "", "| Name | Language | Type | Locale | Sources |", "|---|---|---|---|---|",
        ]
        for name in entity.names:
            lines.append("| " + " | ".join([
                markdown_cell(name.text), markdown_cell(name.language), markdown_cell(name.name_type),
                markdown_cell(name.locale), markdown_cell(", ".join(name.source_ids)),
            ]) + " |")
        lines.extend(["", "## Claims", ""])
        claims_for_entity = sorted(related.get(entity.id, []), key=lambda value: value.id)
        if not claims_for_entity:
            lines.append("No claims extracted yet.")
        for claim in claims_for_entity:
            subject = entities[claim.subject_id].canonical_name
            obj = entities[claim.object_id].canonical_name if claim.object_id else str(claim.literal.value)
            evidence = "; ".join(f"{item.source_id} @ {item.locator}" for item in claim.evidence)
            direction = "out" if claim.subject_id == entity.id else "in"
            lines.append(f"- `{direction}` **{subject}** — `{claim.predicate}` → **{obj}** [{claim.status}; {evidence}]")
        source_ids = sorted({item.source_id for claim in claims_for_entity for item in claim.evidence})
        lines.extend(["", "## Sources", ""])
        lines.extend([f"- `{source_id}` — {sources[source_id].title}" for source_id in source_ids] or ["No sources linked yet."])
        lines.append("")
        write_text_atomic(entity_dir / page_name(entity.id), "\n".join(lines))

    index = ["# Traffic Wiki", ""]
    if not entities:
        index.append("No entities extracted yet.")
    for entity_type in sorted(grouped):
        index.extend([f"## {entity_type}", ""])
        for entity in sorted(grouped[entity_type], key=lambda value: value.canonical_name):
            index.append(f"- [{entity.canonical_name}](entities/{page_name(entity.id)}) — {entity.summary_en or 'No summary.'}")
        index.append("")
    write_text_atomic(root / "wiki" / "index.md", "\n".join(index))
    counts = {name: len(records) for name, records in valid.items()}
    print(json.dumps({"status": "built", **counts}, ensure_ascii=False, sort_keys=True))
    return counts


def init_wiki(root: Path) -> None:
    skill_root = Path(__file__).resolve().parents[1]
    for relative in ("raw", "data", "staging", "runs", "wiki/entities", "graph"):
        (root / relative).mkdir(parents=True, exist_ok=True)
    for name in ("purpose.md", "schema.md"):
        destination = root / name
        if not destination.exists():
            shutil.copyfile(skill_root / "assets" / name, destination)
    for path in data_paths(root).values():
        if not path.exists():
            write_text_atomic(path, "")
    build_views(root)
    print(json.dumps({"status": "initialized", "root": str(root)}, ensure_ascii=False))


def validate_root(root: Path) -> dict[str, int]:
    valid = validate_store(load_store(root))
    counts = {name: len(records) for name, records in valid.items()}
    print(json.dumps({"status": "valid", **counts}, ensure_ascii=False, sort_keys=True))
    return counts


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "validate", "build"):
        command = commands.add_parser(name)
        command.add_argument("--root", type=Path, required=True)
    upsert = commands.add_parser("upsert")
    upsert.add_argument("--root", type=Path, required=True)
    upsert.add_argument("--payload", type=Path, required=True)
    hash_command = commands.add_parser("hash")
    hash_command.add_argument("--file", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "init":
            init_wiki(args.root)
        elif args.command == "validate":
            validate_root(args.root)
        elif args.command == "build":
            build_views(args.root)
        elif args.command == "upsert":
            upsert_payload(args.root, args.payload)
        else:
            print(sha256_file(args.file))
        return 0
    except (ModelError, OSError, ValidationError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
