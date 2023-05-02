---
language: 
  - "de"
tags:
- "qa"

widget:
- text: ""
  context: ""
  example_title: "Extractive QA"
  
---
# GELECTRA-distilled-LegalQuAD

## Overview
**Language model:** GELECTRA-distilled  
**Language:** German
**Downstream-task:** Extractive QA  
**Training data:** German-legal-SQuAD   
**Eval data:** German-legal-SQuAD testset

## Hyperparameters

```
batch_size = 10
n_epochs = 2
max_seq_len=256,
learning_rate=1e-5,

## Eval results
Evaluated on German-legal-SQuAD testset
  "exact": 34.294
  "f1": 64.991
