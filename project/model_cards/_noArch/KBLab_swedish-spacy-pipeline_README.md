---
tags:
- spacy
- token-classification
language:
- sv
license: mit
model-index:
- name: sv_pipeline
  results:
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS Accuracy
      type: accuracy
      value: 0.9818079056
  - task:
      name: SENTER
      type: token-classification
    metrics:
    - name: SENTER Precision
      type: precision
      value: 0.9212548015
    - name: SENTER Recall
      type: recall
      value: 0.9368489583
    - name: SENTER F Score
      type: f_score
      value: 0.9289864429
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Dependencies Accuracy
      type: accuracy
      value: 0.9198832946
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Dependencies Accuracy
      type: accuracy
      value: 0.9198832946
---
