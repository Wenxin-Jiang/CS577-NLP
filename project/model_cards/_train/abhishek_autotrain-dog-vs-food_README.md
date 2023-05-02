---
tags: autotrain
datasets:
- abhishek/autotrain-data-vision_652fee16113a4f07a2452e021a22a934
- sasha/dog-food
co2_eq_emissions: 2.050948967287266
model-index:
- name: autotrain-dog-vs-food
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: sasha/dog-food
      type: sasha/dog-food
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9976190476190476
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: sasha/dog-food
      type: sasha/dog-food
      config: sasha--dog-food
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 1.0
      verified: true
    - name: Precision
      type: precision
      value: 1.0
      verified: true
    - name: Recall
      type: recall
      value: 1.0
      verified: true
    - name: AUC
      type: auc
      value: 1.0
      verified: true
    - name: F1
      type: f1
      value: 1.0
      verified: true
    - name: loss
      type: loss
      value: 0.001115015591494739
      verified: true
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 264300
- CO2 Emissions (in grams): 2.050948967287266

## Validation Metrics

- Loss: 0.009216072037816048
- Accuracy: 0.9976190476190476
- Macro F1: 0.9973261861865685
- Micro F1: 0.9976190476190476
- Weighted F1: 0.997621154535828
- Macro Precision: 0.9964539007092199
- Micro Precision: 0.9976190476190476
- Weighted Precision: 0.9976359338061465
- Macro Recall: 0.9982142857142857
- Micro Recall: 0.9976190476190476
- Weighted Recall: 0.9976190476190476