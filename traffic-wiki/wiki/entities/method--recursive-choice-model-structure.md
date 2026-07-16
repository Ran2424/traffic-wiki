---
id: "method:recursive-choice-model-structure"
type: "Method"
canonical_name: "Recursive Choice Model Structure"
status: "proposed"
topics: ["model-structures", "discrete-choice", "multinomial-logit"]
---

# Recursive Choice Model Structure

Discrete-choice model structure expressing joint choices as marginal and conditional probability models ordered in a hierarchy.

## Names

| Name | Language | Type | Locale | Sources |
|---|---|---|---|---|
| Recursive Choice Model Structure | en | preferred |  | source:boyce-williams-2015-forecasting-urban-travel |
| recursive structures | en | alias |  | source:boyce-williams-2015-forecasting-urban-travel |
| sequential or recursive structures | en | alias |  | source:boyce-williams-2015-forecasting-urban-travel |

## Claims

- `in` **Simultaneous Choice Model Structure** — `contrasts_with` → **Recursive Choice Model Structure** [proposed; source:boyce-williams-2015-forecasting-urban-travel @ chapter:4/section:4.4.3/paragraph:3]
- `out` **Recursive Choice Model Structure** — `uses` → **Multinomial Logit Share Model** [proposed; source:boyce-williams-2015-forecasting-urban-travel @ chapter:4/section:4.4.3/paragraph:7]
- `in` **Composite Cost** — `part_of` → **Recursive Choice Model Structure** [proposed; source:boyce-williams-2015-forecasting-urban-travel @ chapter:4/section:4.4.3/list:composition-rules/item:3]
- `out` **Recursive Choice Model Structure** — `defined` → **Ben-Akiva used recursive to correspond to a sequential decision-making process; sequential is also used in the general literature.** [proposed; source:boyce-williams-2015-forecasting-urban-travel @ chapter:4/notes/note:21]

## Sources

- `source:boyce-williams-2015-forecasting-urban-travel` — Forecasting Urban Travel: Past, Present and Future
