---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: bert-base-uncased-mnli
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE MNLI
      type: glue
      args: mnli
    metrics:
    - type: accuracy
      value: 0.8500813669650122
      name: Accuracy
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: glue
      type: glue
      config: mnli_matched
      split: validation
    metrics:
    - type: accuracy
      value: 0.8467651553744269
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2MwZjZhM2RlMmU5Mjg5NzE0MTA3ODdjZGQwN2U5ZWNhYWUzMmRjMmVhMGEyMjQ3ZGMwOGRjNzkzM2VlNmUyOCIsInZlcnNpb24iOjF9.C6QBegyKVg-5xN06res-t3KxhUbC3kloOy_zf8Lxv981N2aNtmzpVPmiUimrESQj2j9h8PRhH3_shVd_iCpfCA
    - type: precision
      value: 0.8460148987014974
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWViM2QzYjgxZWFkMzlhMzA4ZjdiYzJjZTRhMDQwMjYwZmU3ZmQ5ZmU5YjgzY2FkOWNhMThhODczNjhiMWRiMyIsInZlcnNpb24iOjF9.yLUl2HVaLNjaQImJELdCZjGIqFoBjoCLMh4iijrlneVn87_fJxaieaES-lf6za141LSPSnHmp1H6SKo1L7GGCQ
    - type: precision
      value: 0.8467651553744269
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGIzMjJlMjIwNzA4YzAxYzQ5NGIxZjM0MWE2OWFlYTlmOTU5NzNjZTg0MTJiOTQ2N2U4NmE0NDFmNTc1MGQ5ZCIsInZlcnNpb24iOjF9.u-6lo01PvyYYLnVSc11mzEzga-p6b3gKxWLi_6ziAFZH_3HLZIqrdBoedqhkuRau5u6DcdUlGlWvs0k_7gxCBg
    - type: precision
      value: 0.8475656756385261
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2FlZmE0MTMwNjRlN2MwZjZiMWY1OWE2OTM5MTc3N2Q2ZTVkMzBiYWUyMjU5YThlYjE1MGJkN2ViZTM3ODBhOCIsInZlcnNpb24iOjF9.0u0DToJ9Y_xstI5UB2yXydcHWPasql0z60zLONiRVWEjR6dbs2JzAHmRUrN3IO1QDRz5ssH0w979VRa-lyk3AA
    - type: recall
      value: 0.8463172075485045
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzQ3MjA4MDI1YWZhYTg0NDliYjQ3NGQ5Y2I2NGI1NDNmNTQ3NjdkMmMxYWQ0NDExMzdhNzdmZWFmZTkyNGM5YiIsInZlcnNpb24iOjF9.veXK2iXkDSCDqM3_y3PyGwbZWsQRO_tvNRdmQB3vbvK1Bv4BYYL8WKUfIXm2Apr6IPRA0zeJNvfWIGnigX37Dg
    - type: recall
      value: 0.8467651553744269
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDdlMzcwMzEyNWYxZGFhY2JkNzZmZWQ5NzU4ODQ2MjU3ODMzZGRmZmNlYTM2YTBkNTI4MjAzM2FkOWUxNDBlZSIsInZlcnNpb24iOjF9.rRyz3xQyJ4plzLAc7bJhSbTWdJB7ioX4qhaX6k0e52JL5RdBfwmMJc9lVPUhE70__10Hk_MdzLor5sFF1yaFAA
    - type: recall
      value: 0.8467651553744269
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTc2YzUwMWZjNGYyMjczNzk1YWJkZjkxMDI5NGRjMzdlMTU3YzZlZDQxNmI2YWE3MTQ3ZDVkMDAwY2NlNTA2NSIsInZlcnNpb24iOjF9.j4Kdqqo9LQxsb0A1TEd5K2U7j0qXrv50pbIc9DVdhoIrfIyFiSHuhPHIPZLubr-w0gVjn6aYl-kcM9EiGOSgCg
    - type: f1
      value: 0.8459654597797398
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjcxOWM1YjBiNDVlODZlMjUyZTMwNDUzOTM2MmM4MGNiN2QwOGY1MTE2YjhkZDJjNTlhM2JhMzI4MTcwZjMyYyIsInZlcnNpb24iOjF9.T7zjSHGRWPNMYIiEWGRQTeqY9LHMm0j-3RE3wmYJ5je--eoMhBa7AvRefmSQwZgJtmxwITGGpvXz-0qdfel3Ag
    - type: f1
      value: 0.8467651553744269
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzIzMjFlYzZmMmEyMDRlNDY5ZmYxOGMxZWM2ZjFjYmZlMTRlOTFiMjg3MWJmNmFjMzdkYTM2ODJlOGEwZWY1MSIsInZlcnNpb24iOjF9.1ZvHppu3JfoorjOpQooRVUFlsR1lLLoW_NoswdSsIUwyArbIDg6KRZLwxf-G40efl7hbdXZbr7Ey1WsyTdc0Dw
    - type: f1
      value: 0.8469586362613581
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDM0MTlhYjZlNzBjNjIwNTQyMWIzN2VlNDU5ZmE5YWRlNGYyMGJmZTA4YzFjMGZmMmJlYTNiMzc0YjVhZjQ1NSIsInZlcnNpb24iOjF9.Na8fUEOkFTbctyzR7oSKJNTn2DCwHs-kEXUOBhz9_nxedczUDKiB1xOR372db9b3ot8ttlmceaNgBOnPIiBCBw
    - type: loss
      value: 0.42515239119529724
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDg5NWViMWNmYjczN2ZmMjIzODg2ZGYxZmU2ZjdjM2M2MDZjYTI0ZDc4OTUwZDk3YzBiZmFlMjI4ZmQ4Zjg0YSIsInZlcnNpb24iOjF9.4g708h4xeFXdR0vYBgU70gr-I-rLns2RrPWUg4hEQTO4RzQ1fCe-54gH5kH3DTRwLJU4qJYL4SQNZOE-62ahDg
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-mnli

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the GLUE MNLI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4056
- Accuracy: 0.8501

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.4526        | 1.0   | 12272 | 0.4244          | 0.8388   |
| 0.3344        | 2.0   | 24544 | 0.4252          | 0.8469   |
| 0.2307        | 3.0   | 36816 | 0.4974          | 0.8445   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
