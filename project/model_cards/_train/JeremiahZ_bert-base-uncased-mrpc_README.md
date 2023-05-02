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
- f1
model-index:
- name: bert-base-uncased-mrpc
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE MRPC
      type: glue
      args: mrpc
    metrics:
    - type: accuracy
      value: 0.8578431372549019
      name: Accuracy
    - type: f1
      value: 0.9023569023569024
      name: F1
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: glue
      type: glue
      config: mrpc
      split: validation
    metrics:
    - type: accuracy
      value: 0.8578431372549019
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOWViZGIwMDMxMjA0ZTMwMWY3ZWU4YzA4ZjNjOWMyM2I0NGE2ZDZkMjg3MDdiZDUwYjEzNjMwYzZiODBhMzBiYyIsInZlcnNpb24iOjF9.8xsat2msiKS4S7KplRkr9xaLWCwMSbUNEXxZ3FgFXfIB6DhXWLoDdoc5X6GNux2ipDEdgHjqI8FMzAJURaD0DQ
    - type: precision
      value: 0.8507936507936508
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGE4ZTkyMzc1NTA4MjQxZGU4NjY5NmMyODI3ZWI0NGU4YWUzNmI3YzFhOTU0MDRkZWIzNzkxNTU0Y2ZhYTFmYiIsInZlcnNpb24iOjF9.f7odSB_ZEGkjTbewzM9SW7G5C324Hpuo6Z01uOr7OENrLPDC3z0OwgtoQmNj7pHVcU0fFp9FyRRiTowE6U4SAg
    - type: recall
      value: 0.9605734767025089
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOWVjYjhhNzJlYjdlMWI3Y2RmODkzZDQyYTBhMzdkY2NlNGE4OWM3YzY5MjBiZjMwNWY3ZmIwODk5ZDFkMjI4YSIsInZlcnNpb24iOjF9.yPZxpm9l7ctYxLEBuN0lOukQnT8ETLsBA4EzuqY5EJDuK6FZCqKeb1TKZ_qtthSQpI4n1366LzqSXeU8nZ3tBw
    - type: auc
      value: 0.8931260592926008
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjkwN2RmOTlmZDRlZTQ3ZTE1NjBjNTQxMDNkOTExMzQ5MjkyNjY1ZDFjZmQ4MDE0NmZlNDBhMjQzMTRhN2IxZCIsInZlcnNpb24iOjF9.e_gccDrQXc6s8fASle5wnZWc02ihuqBdicoDvehQO79nt-YHdm1oK11llTiUULReIOxTsOmFKCattvztyqOUCQ
    - type: f1
      value: 0.9023569023569024
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWNiOTUyMzEzMTRkNzBmOTdiMTNhOGQ0NzgyZjFiNjc2NmE1Y2FlOWM0NzdmNGM5ZGNmZTUyMzljZGRiZjNhOSIsInZlcnNpb24iOjF9.rxUf2PMqTz3N-tvfIo6L19RKTzmIjYRoxm1BEzrzNX1w-FATF69X2WZlqjAyB2xhMrSikvmsh7QryYmZn-P6AA
    - type: loss
      value: 0.5572634935379028
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYWIyMzZmMGYwMjEyMGFmOGRjNGE3YjQ5MmU5NGZjYmJjZGFiNTA4Mzk0MTAxNDQyYTk5YzE2OTA5YjlmODgzMCIsInZlcnNpb24iOjF9.bgoIjSqw70DaRXJ9LL3_dP33C0WPAZq5uMlencN-wOpjNes2v0VcCW1felmd_0JRwSbWI7v1eP2YYPiQg-a0AQ
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-mrpc

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the GLUE MRPC dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5572
- Accuracy: 0.8578
- F1: 0.9024
- Combined Score: 0.8801

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 5.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Combined Score |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:--------------:|
| No log        | 1.0   | 230  | 0.4111          | 0.8088   | 0.8704 | 0.8396         |
| No log        | 2.0   | 460  | 0.3762          | 0.8480   | 0.8942 | 0.8711         |
| 0.4287        | 3.0   | 690  | 0.5572          | 0.8578   | 0.9024 | 0.8801         |
| 0.4287        | 4.0   | 920  | 0.6087          | 0.8554   | 0.8977 | 0.8766         |
| 0.1172        | 5.0   | 1150 | 0.6524          | 0.8456   | 0.8901 | 0.8678         |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
