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
- name: fr_ner4archives_camembert_base
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.872488408
    - name: NER Recall
      type: recall
      value: 0.8540090772
    - name: NER F Score
      type: f_score
      value: 0.8631498471
---

NER4Archives pipeline optimized for GPU and specialized on French National Archives findings aids (XML-EAD). Components: transformer, ner. Based on camembert-base model.   

| Feature | Description |
| --- | --- |
| **Name** | `fr_ner4archives_camembert_base` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.3.1,<3.4.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
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
| `ENTS_F` | 86.31 |
| `ENTS_P` | 87.25 |
| `ENTS_R` | 85.40 |
| `TRANSFORMER_LOSS` | 159157.68 |
| `NER_LOSS` | 27979.50 |