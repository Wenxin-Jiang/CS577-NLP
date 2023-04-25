---
tags:
- spacy
- token-classification

language:
- es

license: gpl-3.0

model-index:
- name: es_cantemist_ner_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.8487622923
    - name: NER Recall
      type: recall
      value: 0.8416274378
    - name: NER F Score
      type: f_score
      value: 0.8451798075

widget:
- text: "JUICIO DIAGNÓSTICO Encefalitis límbica y polineuropatía sensitiva paraneoplásicas secundarias a carcinoma microcítico de pulmón cTxN2 M0 (enfermedad limitada) ."

---

Basic Spacy BioNER pipeline, with a RoBERTa-based model [bsc-bio-ehr-es] (https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) and a dataset, CANTEMIST, annotated with tumour morphology entities. For further information, check the  [official website](https://temu.bsc.es/cantemist/). Visit our [GitHub repository](https://github.com/PlanTL-GOB-ES/lm-biomedical-clinical-es). This work was funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL

| Feature | Description |
| --- | --- |
| **Name** | `es_cantemist_ner_trf` |
| **Version** | `3.4.0` |
| **spaCy** | `>=3.4.0,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | https://huggingface.co/datasets/PlanTL-GOB-ES/cantemist-ner |
| **License** | `[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)` |
| **Author** | [The Text Mining Unit from Barcelona Supercomputing Center.](https://huggingface.co/PlanTL-GOB-ES) |
| **Copyright** | Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022) |
| **Funding** | This work was funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL |



### Label Scheme

<details>

<summary>View label scheme (1 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `MORFOLOGIA_NEOPLASIA` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 84.52 |
| `ENTS_P` | 84.88 |
| `ENTS_R` | 84.16 |
| `TRANSFORMER_LOSS` | 25646.78 |
| `NER_LOSS` | 9622.84 |