---
license: gpl-3.0
language:
- es
library_name: spacy
pipeline_tag: token-classification
tags:
- spacy
- token-classification
widget:
- text: "Fue antes de llegar a Sigüeiro, en el Camino de Santiago."
- text: "El proyecto lo financia el Ministerio de Industria y Competitividad."
model-index:
- name: es_spacy_ner_cds
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9690286251
    - name: NER Recall
      type: recall
      value: 0.9683470106
    - name: NER F Score
      type: f_score
      value: 0.9686876979
---

# Introduction

spaCy NER model for Spanish trained with interviews in the domain of tourism related to the Way of Saint Jacques. It recognizes four types of entities: location (LOC), organizations (ORG), person (PER) and miscellaneous (MISC).

| Feature | Description |
| --- | --- |
| **Name** | `es_spacy_ner_cds_trf` |
| **Version** | `0.0.1a` |
| **spaCy** | `>=3.4.4,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |

### Label Scheme

<details>

<summary>View label scheme (4 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `LOC`, `MISC`, `ORG`, `PER` |

</details>

## Usage

You can use this model with the spaCy *pipeline* for NER.

```python
import spacy
from spacy.pipeline import merge_entities


nlp = spacy.load("es_spacy_ner_cds_trf")
nlp.add_pipe('sentencizer')

example = "Fue antes de llegar a Sigüeiro, en el Camino de Santiago. El proyecto lo financia el Ministerio de Industria y Competitividad."
ner_pipe = nlp(example)

print(ner_pipe.ents)
for token in merge_entities(ner_pipe):
    print(token.text, token.ent_type_)
```

## Dataset

ToDo

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 96.87 |
| `ENTS_P` | 96.90 |
| `ENTS_R` | 96.83 |
| `TRANSFORMER_LOSS` | 7662.71 |
| `NER_LOSS` | 7673.80 |
