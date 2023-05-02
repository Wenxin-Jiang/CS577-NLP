---
tags: autotrain
datasets:
- abhishek/autotrain-data-vision_79ca848474e24ad3a520c09e36452e85
- cifar10
co2_eq_emissions: 32.869648157119876
model-index:
- name: autotrain_cifar10_vit_base
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: cifar10
      type: cifar10
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9834
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: cifar10
      type: cifar10
      config: plain_text
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9811
      verified: true
    - name: Precision Macro
      type: precision
      value: 0.9812371727477451
      verified: true
    - name: Precision Micro
      type: precision
      value: 0.9811
      verified: true
    - name: Precision Weighted
      type: precision
      value: 0.9812371727477451
      verified: true
    - name: Recall Macro
      type: recall
      value: 0.9811
      verified: true
    - name: Recall Micro
      type: recall
      value: 0.9811
      verified: true
    - name: Recall Weighted
      type: recall
      value: 0.9811
      verified: true
    - name: F1 Macro
      type: f1
      value: 0.9811240087824231
      verified: true
    - name: F1 Micro
      type: f1
      value: 0.9811
      verified: true
    - name: F1 Weighted
      type: f1
      value: 0.981124008782423
      verified: true
    - name: loss
      type: loss
      value: 0.0649944543838501
      verified: true
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 300303
- CO2 Emissions (in grams): 32.869648157119876

## Validation Metrics

- Loss: 0.05070499703288078
- Accuracy: 0.9834
- Macro F1: 0.9834026834840477
- Micro F1: 0.9834
- Weighted F1: 0.9834026834840479
- Macro Precision: 0.9834502145172822
- Micro Precision: 0.9834
- Weighted Precision: 0.9834502145172822
- Macro Recall: 0.9833999999999999
- Micro Recall: 0.9834
- Weighted Recall: 0.9834