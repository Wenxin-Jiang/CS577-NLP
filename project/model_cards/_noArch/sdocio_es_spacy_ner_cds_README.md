---
language: es
license: gpl-3.0
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
      value: 0.9648998822
    - name: NER Recall
      type: recall
      value: 0.9603751465
    - name: NER F Score
      type: f_score
      value: 0.9626321974
---

# Introduction

spaCy NER model for Spanish trained with interviews in the domain of tourism related to the Way of Saint Jacques. It recognizes four types of entities: location (LOC), organizations (ORG), person (PER) and miscellaneous (MISC).

| Feature | Description |
| --- | --- |
| **Name** | `es_spacy_ner_cds` |
| **Version** | `0.0.1a` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |

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


nlp = spacy.load("es_spacy_ner_cds")
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
| `ENTS_F` | 96.26 |
| `ENTS_P` | 96.49 |
| `ENTS_R` | 96.04 |
| `TOK2VEC_LOSS` | 62780.17 |
| `NER_LOSS` | 34006.41 |
