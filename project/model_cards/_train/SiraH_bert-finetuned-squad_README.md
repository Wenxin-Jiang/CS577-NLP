---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: bert-finetuned-squad
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
      value: 40.2443
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTc3Y2YyY2Y5ZTMxMGQ3M2U3YThmMjFiM2JlOWQ4MjE0YzZmMmM3NzY4ZDcxYzY4ZTAwNTU4MGE3YmQxOTJhNiIsInZlcnNpb24iOjF9.tk2uBvygzQsexdkxKvFBgKGY8lPNzEG7Pqi-6fL688LTiCMACFFSrZUhyv5b31orF7_CbJkHFjKuMHmX0V_UCA
    - type: f1
      value: 44.135
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYmE1NWFlYzQ3YTZiMmY3ZDgyYWRlNzI5M2IwYzZkOWUwMDE2NGU4M2RjODBiNjEzY2YxNTVlZmE5OWNmNDU2NiIsInZlcnNpb24iOjF9.pgr2rkyQe-QdwVXuw-uBXheKFz0EhDiyO0doLMmcOi51t_slDPldk29YRXQKvpsfy3YpH_t-xaXQLs1n8VcjDQ
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: subjqa
      type: subjqa
      config: grocery
      split: train
    metrics:
    - type: exact_match
      value: 5.625
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDMyMDQ1OWFkY2IwYTcxNTljYTZjYTM0ZThjOGEwZWJjYjBlZWQxYWE1ZjMwNDg5NGY5MTFiYmM4YWM0Y2Y2NCIsInZlcnNpb24iOjF9.4nwNKC2teDPVd5YqvjS8sV3q-ylC9fWO5lOiZVk8o3UNdKyAtl3qAH6dU7lGcHZrxasN7zNrxv5kD5nNWr9YBQ
    - type: f1
      value: 15.8411
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMWMzMTAzNTljNjFlM2E4NGIzNjRjNzRiZTIxZjBlNjkzZWM4NjcxMjUzOGZjZTgxMGUxODk4ZjFkZmJiMjg4ZiIsInZlcnNpb24iOjF9.agcp8QkYeHBvs2Qp0YmEMlvEx1_4a_dv_0cm26UbF-YgYU_7cR86ar-h1V56mrfcKUjNRRiK79GD0P9WT6mADw
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-squad

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the squad dataset.

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
