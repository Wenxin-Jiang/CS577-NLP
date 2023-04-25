---
tags:
- spacy
- token-classification
language:
- es
license: apache-2.0
widget:
- text: "La C0v!d es un 3ng@ño de los G0b!3rno$"
  example_title: "Word camouflage detection"
model-index:
- name: es_roberta_base_bne_leetspeak_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8979055626
    - name: NER Recall
      type: recall
      value: 0.9393701406
    - name: NER F Score
      type: f_score
      value: 0.9181699547
---
| Feature | Description |
| --- | --- |
| **Name** | `es_roberta_base_bne_leetspeak_ner` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [PlanTL-GOB-ES/roberta-base-bne](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne) model a transformer-based masked language model for the Spanish language pre-trained with a total of 570GB of clean and deduplicated text compiled from the web crawlings performed by the National Library of Spain (Biblioteca Nacional de España) <br> [LeetSpeak-NER](https://huggingface.co/spaces/Huertas97/LeetSpeak-NER) app where this model is in production for countering information disorders|
| **License** | Apache 2.0 |
| **Author** | [Álvaro Huertas García](https://www.linkedin.com/in/alvaro-huertas-garcia/) at [AI+DA](http://aida.etsisi.upm.es/)  |

### Label Scheme

<details>

<summary>View label scheme (4 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `INV_CAMO`, `LEETSPEAK`, `MIX`, `PUNCT_CAMO` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 91.82 |
| `ENTS_P` | 89.79 |
| `ENTS_R` | 93.94 |
| `TRANSFORMER_LOSS` | 166484.92 |
| `NER_LOSS` | 318457.35 |