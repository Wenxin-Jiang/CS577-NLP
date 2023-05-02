---
language: en
license: mit
tags:
- exbert
datasets:
- squad_v2
thumbnail: https://thumb.tildacdn.com/tild3433-3637-4830-a533-353833613061/-/resize/720x/-/format/webp/germanquad.jpg
model-index:
- name: Shobhank-iiitdwd/DistBERT-squad2-QA-768d
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad_v2
      type: squad_v2
      config: squad_v2
      split: validation
    metrics:
    - type: exact_match
      value: 73.8248
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMGFmZmFiN2E5ODZkOTkyMjQ1NTUzMmQwMjc0M2RlYzVlNmM4YTFlNzA4YzIwY2JkY2EyNDg2ZTY3OTdjZTVlZiIsInZlcnNpb24iOjF9.ZZ6c2OI3lzeNhuSWTh28j00zk-sPrqkTvdVBZv2wJc1D4YnR-xOj72haybT6MV_xeYqTg3-x9L8PsWSS20NaDw
    - type: f1
      value: 77.1684
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzAxMDk1YzI5ZjA2N2ZmMzAxNjgxYzJiNzAzYmI1ZWU5ZDRmYWY3OWJmMjlmNDcyMGE0YWY5NjNhZTk4YWY5ZSIsInZlcnNpb24iOjF9.rF3raNGUSYv5D2xzWLZztD99vwDKvWb22LG32RomrDGP6XKTbCVqZzAw5UFw93jKb0VoLApbQQ-AOGxLj3U_Cg
---

## Overview
**Language model:** Shobhank-iiitdwd/DistBERT-squad2-QA   
**Language:** English  
**Training data:** SQuAD 2.0 training set x 20 augmented + SQuAD 2.0 training set without augmentation  
**Eval data:** SQuAD 2.0 dev set  
**Infrastructure**: 1x V100 GPU  
**Published**: Dec 8th, 2021

## Details
- haystack's intermediate layer and prediction layer distillation features were used for training. bert-base-uncased-squad2 was used as the teacher model and DBERT_General_6L_768D was used as the student model.

## Hyperparameters
### Intermediate layer distillation
```
batch_size = 26
n_epochs = 5
max_seq_len = 384
learning_rate = 5e-5
lr_schedule = LinearWarmup
embeds_dropout_prob = 0.1
temperature = 1
```
### Prediction layer distillation 
```
batch_size = 26
n_epochs = 5
max_seq_len = 384
learning_rate = 3e-5
lr_schedule = LinearWarmup
embeds_dropout_prob = 0.1
temperature = 1
distillation_loss_weight = 1.0
```
## Performance
```
"exact": 71.87736882001179
"f1": 76.36111895973675
```
