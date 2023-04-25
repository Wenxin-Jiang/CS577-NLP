---
tags:
- spacy
- token-classification
language:
- en
license: cc-by-nc-sa-3.0
model-index:
- name: en_Coff_Ev1
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9673151751
    - name: NER Recall
      type: recall
      value: 0.9872915012
    - name: NER F Score
      type: f_score
      value: 0.9772012579
---
Your Coffee Ordered at the Speed of Sound

For citations please use the included ```refs.bib``` this project was a collaboration between five students with a common goal of simplifying the ordering process. 

You *are permitted* to use this software for any projects, however this is *not permitted* for use in any commerical instances under our ```cc-by-nc-sa-3.0``` <br>
license without explicit permissions from the author(s).



| Feature | Description |
| --- | --- |
| **Name** | `en_Coff_Ev1` |
| **Version** | `1.4.0` |
| **spaCy** | `>=3.4.3,<3.5.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | `cc-by-nc-sa-3.0` |
| **Author** | [C.Bruinsma,I.Chi,J.Feliciano,J.Li,D.Paden]() |

*THIS SOFTWARE IS PROVIDED AS IS BY ITS AUTHORS UNDER NO WARRANTY OF ITS FUNCTION.*

### Label Scheme

<details>

<summary>View label scheme (20 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `Anti`, `Blended`, `Brew Style`, `Coffee Varietal`, `add-on`, `drink`, `extra`, `hot breakfast`, `milk`, `milk texture`, `pastry`, `pump quantity`, `roast`, `shot quality`, `shot quantity`, `size`, `syrup`, `temperature`, `toppings`, `upside-down` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 97.72 |
| `ENTS_P` | 96.73 |
| `ENTS_R` | 98.73 |
| `TOK2VEC_LOSS` | 54858.85 |
| `NER_LOSS` | 427986.33 |