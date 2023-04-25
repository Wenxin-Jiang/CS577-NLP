---
inference: false
language:
- en
license: cc # license from https://hf.co/docs/hub/repositories-licenses
library_name: spacy # library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
tags:
- spacy
- token-classification

model-index:
- name: dataset-references
  results:
  - task:
      name: NER
      type: token-classification
    metrics:
    - name: NER Precision
      type: precision
      value: 0.85
    - name: NER Recall
      type: recall
      value: 0.88
    - name: NER F Score
      type: f_score
      value: 0.87
---

| Feature | Description |
| --- | --- |
| **Name** | `dataset-references` |
| **Version** | n/a |
| **spaCy** | `3.1.1` |
| **Components** | `transformer`, `ner` |
| **License** | `CC` |
| **Author** | [Sara Lafia](saralafia.com) |