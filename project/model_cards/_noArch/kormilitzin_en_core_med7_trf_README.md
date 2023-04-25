---
tags:
- spacy
- token-classification
language:
- en
license: mit
model-index:
- name: en_core_med7_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8822157434
    - name: NER Recall
      type: recall
      value: 0.925382263
    - name: NER F Score
      type: f_score
      value: 0.9032835821
---
| Feature | Description |
| --- | --- |
| **Name** | `en_core_med7_trf` |
| **Version** | `3.4.2.1` |
| **spaCy** | `>=3.4.2,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
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
| `ENTS_F` | 90.33 |
| `ENTS_P` | 88.22 |
| `ENTS_R` | 92.54 |
| `TRANSFORMER_LOSS` | 2502627.06 |
| `NER_LOSS` | 114576.77 |

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