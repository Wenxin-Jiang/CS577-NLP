---
tags:
- spacy
- token-classification
language:
- hi
model-index:
- name: hi_ud_hi_ewt
  results:
  - task:
      name: POS
      type: token-classification
    metrics:
    - name: POS Accuracy
      type: accuracy
      value: 0.9539693129
  - task:
      name: SENTER
      type: token-classification
    metrics:
    - name: SENTER Precision
      type: precision
      value: 0.9902617164
    - name: SENTER Recall
      type: recall
      value: 0.9807112719
    - name: SENTER F Score
      type: f_score
      value: 0.9854633555
  - task:
      name: UNLABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Unlabeled Dependencies Accuracy
      type: accuracy
      value: 0.9198922358
  - task:
      name: LABELED_DEPENDENCIES
      type: token-classification
    metrics:
    - name: Labeled Dependencies Accuracy
      type: accuracy
      value: 0.9198922358
---
