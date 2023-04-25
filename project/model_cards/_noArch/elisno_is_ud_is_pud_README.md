---
tags:
- spacy
- token-classification
language:
- is
model-index:
- name: is_ud_is_pud
  results:
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS Accuracy
      type: accuracy
      value: 0.7356746765
  - task:
      name: SENTER
      type: token-classification
    metrics:
    - name: SENTER Precision
      type: precision
      value: 0.8611111111
    - name: SENTER Recall
      type: recall
      value: 0.93
    - name: SENTER F Score
      type: f_score
      value: 0.8942307692
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Dependencies Accuracy
      type: accuracy
      value: 0.7336065574
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Dependencies Accuracy
      type: accuracy
      value: 0.7336065574
---
