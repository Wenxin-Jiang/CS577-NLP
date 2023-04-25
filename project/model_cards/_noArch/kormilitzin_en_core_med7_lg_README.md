---
tags:
- spacy
- token-classification
language:
- en
license: mit
model-index:
- name: en_core_med7_lg
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8649613325
    - name: NER Recall
      type: recall
      value: 0.8892966361
    - name: NER F Score
      type: f_score
      value: 0.876960193
---
| Feature | Description |
| --- | --- |
| **Name** | `en_core_med7_lg` |
| **Version** | `3.4.2.1` |
| **spaCy** | `>=3.4.2,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 514157 keys, 514157 unique vectors (300 dimensions) |
| **Sources** | n/a |
| **License** | `MIT` |
| **Author** | [Andrey Kormilitzin](https://www.kormilitzin.com/) |

### Label Scheme

<details>

<summary>View label scheme (7 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `DOSAGE`, `DRUG`, `DURATION`, `FORM`, `FREQUENCY`, `ROUTE`, `STRENGTH` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 87.70 |
| `ENTS_P` | 86.50 |
| `ENTS_R` | 88.93 |
| `TOK2VEC_LOSS` | 226109.53 |
| `NER_LOSS` | 302222.55 |

### BibTeX entry and citation info

```bibtex
@article{kormilitzin2021med7,
  title={Med7: A transferable clinical natural language processing model for electronic health records},
  author={Kormilitzin, Andrey and Vaci, Nemanja and Liu, Qiang and Nevado-Holgado, Alejo},
  journal={Artificial Intelligence in Medicine},
  volume={118},
  pages={102086},
  year={2021},
  publisher={Elsevier}
}
```