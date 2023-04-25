
---
tags:
- spacy
- token-classification
language:
- en
widget:
- text: "Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), the cause of the coronavirus disease-19 (COVID-19) pandemic, was identified in late 2019 and caused >5 million deaths by February 2022. To date, targeted antiviral interventions against COVID-19 are limited. The spectrum of SARS-CoV-2 infection ranges from asymptomatic to fatal disease. However, the reasons for varying outcomes to SARS-CoV-2 infection are yet to be elucidated. Here we show that an endogenously activated interferon lambda (IFNλ1) pathway leads to resistance against SARS-CoV-2 infection."
- text: "The NHS is offering antibody and antiviral treatments to people with coronavirus (COVID-19) who are at highest risk of becoming seriously ill."
model-index:
- name: en_covid19_ner
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.9139786332
    - name: NER Recall
      type: recall
      value: 0.9362022309
    - name: NER F Score
      type: f_score
      value: 0.9249569618
---
COVID 19 Bio Annotations

The dataset was taken from https://github.com/davidcampos/covid19-corpus

Dataset
The dataset was then split into several datasets each one representing one entity. Namely, Disorder, Species, Chemical or Drug, Gene and Protein, Enzyme, Anatomy, Biological Process, Molecular Function, Cellular Component, Pathway and microRNA. Moreover, another dataset is also created with all those aforementioned that are non-overlapping in nature.

Other Dataset Formats
The datasets are available in two formats IOB and Spacy's JSONL format.

IOB: https://github.com/tsantosh7/COVID-19-Named-Entity-Recognition/tree/master/Datasets/BIO

SpaCy JSONL: https://github.com/tsantosh7/COVID-19-Named-Entity-Recognition/tree/master/Datasets/SpaCy


| Feature | Description |
| --- | --- |
| **Name** | `en_covid19_ner` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.2.4,<3.3.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [Santosh Tirunagai]() |

### Label Scheme

<details>

<summary>View label scheme (10 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `ANAT`, `CHED`, `COMP`, `DISO`, `ENZY`, `FUNC`, `PATH`, `PRGE`, `PROC`, `SPEC` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 92.50 |
| `ENTS_P` | 91.40 |
| `ENTS_R` | 93.62 |
| `TRANSFORMER_LOSS` | 311768.03 |
| `NER_LOSS` | 371171.50 |