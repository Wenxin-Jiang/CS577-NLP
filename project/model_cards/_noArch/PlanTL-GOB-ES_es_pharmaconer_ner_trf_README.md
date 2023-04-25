---
tags:
- spacy
- token-classification
language:
- es
license: mit
model-index:
- name: es_pharmaconer_ner_trf
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9066736184
    - name: NER Recall
      type: recall
      value: 0.9152631579
    - name: NER F Score
      type: f_score
      value: 0.9109481404

widget:
- text: "Se realizó estudio analítico destacando incremento de niveles de PTH y vitamina D (103,7 pg/ml y 272 ng/ml, respectivamente), atribuidos al exceso de suplementación de vitamina D."
- text: "Por el hallazgo de múltiples fracturas por estrés, se procedió a estudio en nuestras consultas, realizándose análisis con función renal, calcio sérico y urinario, calcio iónico, magnesio y PTH, que fueron normales."
- text: "Se solicitó una analítica que incluía hemograma, bioquímica, anticuerpos antinucleares (ANA) y serologías, examen de orina, así como biopsia de la lesión. Los resultados fueron normales, con ANA, anti-Sm, anti-RNP, anti-SSA, anti-SSB, anti-Jo1 y anti-Scl70 negativos."
---
Basic Spacy BioNER pipeline, with a RoBERTa-based model [bsc-bio-ehr-es] (https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) and a dataset, Pharmaconer, a NER dataset annotated with substances, compounds and proteins entities. For further information, check the  [official website](https://temu.bsc.es/pharmaconer/). Visit our [GitHub repository](https://github.com/PlanTL-GOB-ES/lm-biomedical-clinical-es). This work was funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL

| Feature | Description |
| --- | --- |
| **Name** | `es_pharmaconer_ner_trf` |
| **Version** | `3.4.1` |
| **spaCy** | `>=3.4.1,<3.5.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | `mit` |
| **Author** | [The Text Mining Unit from Barcelona Supercomputing Center.](https://huggingface.co/PlanTL-GOB-ES/) |
| **Copyright** | Copyright by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) (2022) |
| **Funding** | This work was funded by the Spanish State Secretariat for Digitalization and Artificial Intelligence (SEDIA) within the framework of the Plan-TL |

### Label Scheme

<details>

<summary>View label scheme (4 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `NORMALIZABLES`, `NO_NORMALIZABLES`, `PROTEINAS`, `UNCLEAR` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 91.09 |
| `ENTS_P` | 90.67 |
| `ENTS_R` | 91.53 |
| `TRANSFORMER_LOSS` | 15719.51 |
| `NER_LOSS` | 22469.88 |