---
tags:
- autotrain
- vision
- image-classification
datasets:
- lewtun/dog_food
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/tiger.jpg
  example_title: Tiger
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/teapot.jpg
  example_title: Teapot
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/palace.jpg
  example_title: Palace
library_name: transformers
co2_eq_emissions:
  emissions: 6.799888815236616
eval_info:
  col_mapping: test
model-index:
- name: NimaBoscarino/dog_food
  results:
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: lewtun/dog_food
      type: lewtun/dog_food
      config: lewtun--dog_food
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 1.0
      verified: true
    - name: Precision Macro
      type: precision
      value: 1.0
      verified: true
    - name: Precision Micro
      type: precision
      value: 1.0
      verified: true
    - name: Precision Weighted
      type: precision
      value: 1.0
      verified: true
    - name: Recall Macro
      type: recall
      value: 1.0
      verified: true
    - name: Recall Micro
      type: recall
      value: 1.0
      verified: true
    - name: Recall Weighted
      type: recall
      value: 1.0
      verified: true
    - name: F1 Macro
      type: f1
      value: 1.0
      verified: true
    - name: F1 Micro
      type: f1
      value: 1.0
      verified: true
    - name: F1 Weighted
      type: f1
      value: 1.0
      verified: true
    - name: loss
      type: loss
      value: 1.848173087637406e-05
      verified: true
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1647758504
- CO2 Emissions (in grams): 6.7999

## Validation Metrics

- Loss: 0.001
- Accuracy: 1.000
- Macro F1: 1.000
- Micro F1: 1.000
- Weighted F1: 1.000
- Macro Precision: 1.000
- Micro Precision: 1.000
- Weighted Precision: 1.000
- Macro Recall: 1.000
- Micro Recall: 1.000
- Weighted Recall: 1.000