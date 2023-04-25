---
tags:
- spacy
- token-classification
language:
- en
license: apache-2.0
widget:
- text: "But one other thing that we have to re;think is the way that we dy£ our #c!l.o|th?£+s."
  example_title: "Word camouflage detection"
model-index:
- name: en_roberta_base_leetspeak_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.7966001851
    - name: NER Recall
      type: recall
      value: 0.8619559279
    - name: NER F Score
      type: f_score
      value: 0.8279903783
---
| Feature | Description |
| --- | --- |
| **Name** | `en_roberta_base_leetspeak_ner` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | [roberta-base](https://huggingface.co/roberta-base) pre-trained model on English language using a masked language modeling (MLM) objective by Yinhan Liu et al. <br> [LeetSpeak-NER](https://huggingface.co/spaces/Huertas97/LeetSpeak-NER) app where this model is in production for countering information disorders|
| **License** | Apache 2.0 |
| **Author** | [Álvaro Huertas García](https://www.linkedin.com/in/alvaro-huertas-garcia/) at [AI+DA](http://aida.etsisi.upm.es/) |

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
| `ENTS_F` | 82.80 |
| `ENTS_P` | 79.66 |
| `ENTS_R` | 86.20 |
| `TRANSFORMER_LOSS` | 177808.42 |
| `NER_LOSS` | 608427.31 |