---
tags: autotrain
datasets:
- abhishek/autotrain-data-vision_877913e77fb94b7abd4dafc5ebf830b0
- fashion_mnist
co2_eq_emissions: 0.2438639401641305
model-index:
- name: autotrain_fashion_mnist_vit_base
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: fashion_mnist
      type: fashion_mnist
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9473
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: fashion_mnist
      type: fashion_mnist
      config: fashion_mnist
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9431
      verified: true
    - name: Precision Macro
      type: precision
      value: 0.9435374485262068
      verified: true
    - name: Precision Micro
      type: precision
      value: 0.9431
      verified: true
    - name: Precision Weighted
      type: precision
      value: 0.9435374485262069
      verified: true
    - name: Recall Macro
      type: recall
      value: 0.9430999999999999
      verified: true
    - name: Recall Micro
      type: recall
      value: 0.9431
      verified: true
    - name: Recall Weighted
      type: recall
      value: 0.9431
      verified: true
    - name: F1 Macro
      type: f1
      value: 0.9431357840300738
      verified: true
    - name: F1 Micro
      type: f1
      value: 0.9431
      verified: true
    - name: F1 Weighted
      type: f1
      value: 0.9431357840300738
      verified: true
    - name: loss
      type: loss
      value: 0.17352284491062164
      verified: true
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 7024732
- CO2 Emissions (in grams): 0.2438639401641305

## Validation Metrics

- Loss: 0.16775867342948914
- Accuracy: 0.9473333333333334
- Macro F1: 0.9473921270228505
- Micro F1: 0.9473333333333334
- Weighted F1: 0.9473921270228505
- Macro Precision: 0.9478705813419325
- Micro Precision: 0.9473333333333334
- Weighted Precision: 0.9478705813419323
- Macro Recall: 0.9473333333333332
- Micro Recall: 0.9473333333333334
- Weighted Recall: 0.9473333333333334