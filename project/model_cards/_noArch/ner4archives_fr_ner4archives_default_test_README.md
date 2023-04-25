---
widget:
- text: "415 Lyon Lettres de rémission accordées à Denis Fromant, marinier, pour meurtre commis à Saint-Haon 1, au pays de Roannais, sur la personne de Driet Cantin qui l'accusait d'avoir maltraité un de ses pages et de l'avoir dépouillé d'une jument (Fol 145 v°, n° 415) Septembre 1501."
  example_title: "FRAN_IR_000061"
- text: "BB/29/988  page 143  Penne (Lot-et-Garronne) 14 décembre 1822. BB/29/988  page 145  Billom (Puy-de-Dôme) 11 janvier 1823."
  example_title: "FRAN_IR_050370"
  
tags:
- spacy
- token-classification
language:
- fr
model-index:
- name: fr_ner4archives_default_test
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8
    - name: NER Recall
      type: recall
      value: 0.741301059
    - name: NER F Score
      type: f_score
      value: 0.7695327837
---


NER4Archives pipeline optimized for CPU and specialized on French National Archives findings aids (XML-EAD) - Corpus V2. Components: tok2vec, ner. Base default CNN architecture.

| Feature | Description |
| --- | --- |
| **Name** | `fr_ner4archives_default_test` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.3.1,<3.4.0` |
| **Default Pipeline** | `tok2vec`, `ner` |
| **Components** | `tok2vec`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | French corpus for the NER task composed of finding aids in XML-EAD ​​from the National Archives of France (v. 2.0) - [Check corpus version on GitHub](https://github.com/NER4Archives-project/Corpus_TrainingData) |
| **License** | CC-BY-4.0 license  |
| **Author** | [Archives nationales]() / [Inria-Almanach]() |

### Label Scheme

<details>

<summary>View label scheme (5 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `EVENT`, `LOCATION`, `ORGANISATION`, `PERSON`, `TITLE` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 76.95 |
| `ENTS_P` | 80.00 |
| `ENTS_R` | 74.13 |
| `TOK2VEC_LOSS` | 76044.50 |
| `NER_LOSS` | 75529.77 |