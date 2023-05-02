---
datasets:
- Poulpidot/FrenchHateSpeechSuperset
language:
- fr
metrics:
- accuracy
pipeline_tag: text-classification
model-index:
- name: distilcamenbert-french-hate-speech
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      type: french-hate-speech-superset
      name: french-hate-speech-superset
    metrics:
    - type: accuracy
      value: 0.830691
      name: Accuracy
---