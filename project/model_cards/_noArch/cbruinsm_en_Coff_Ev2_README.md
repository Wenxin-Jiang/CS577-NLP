---
tags:
- spacy
- token-classification
language:
- en
license: mit
model-index:
- name: en_Coff_Ev2
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9922248804
    - name: NER Recall
      type: recall
      value: 0.9916317992
    - name: NER F Score
      type: f_score
      value: 0.9919282511
---
Your Coffee at the Speed of Sound

| Feature | Description |
| --- | --- |
| **Name** | `en_Coff_Ev2` |
| **Version** | `1.1.6` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | `MIT` |
| **Author** | [Chris Bruinsma,Iris Chi,Jack Felciano,Jeffrey Li,Dustin Paden]() |

### Label Scheme

<details>

<summary>View label scheme (18 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Anti`, `Brew Style`, `add-on`, `drink`, `extra`, `hot breakfast`, `milk`, `milk texture`, `pastry`, `pump quantity`, `roast`, `shot quality`, `shot quantity`, `size`, `syrup`, `temperature`, `toppings`, `upside-down` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 99.19 |
| `ENTS_P` | 99.22 |
| `ENTS_R` | 99.16 |
| `TOK2VEC_LOSS` | 58625.70 |
| `NER_LOSS` | 168185.77 |