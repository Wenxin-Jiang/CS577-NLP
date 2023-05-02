---
language: 
  - en
tags:
- question-answering
license: mit
datasets:
- SQuAD
metrics:
- EM
- F1
---

# Test model for DL4NLP 2022 HW06  
xtremedistil-l6-h256-uncased trained on SQuAD

## Hyper parameters
- learning rate: 1e-5 
- weight decay: 0.01
- warm up steps: 0
- learning rate scheduler: linear 
- epochs: 1

## Metric results on the dev set
- F1: 65.48
- EM: 51.67