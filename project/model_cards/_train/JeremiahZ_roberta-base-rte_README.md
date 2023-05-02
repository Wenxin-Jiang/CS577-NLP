---
language:
- en
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: roberta-base-rte
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE RTE
      type: glue
      args: rte
    metrics:
    - type: accuracy
      value: 0.7978339350180506
      name: Accuracy
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: glue
      type: glue
      config: rte
      split: validation
    metrics:
    - type: accuracy
      value: 0.7906137184115524
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMWVhOWZkNGYyMWRmNzdmZTM5MTVmNzFhNjVlMzA1NWU4YjJjODk5ZjM4MTY1Yjg0MTc0MmRmZTNkMzIwZDAzNyIsInZlcnNpb24iOjF9.nFZpFXDSLEIcO-_Z43_5b08GIVQiU9hFUEZpTftW3h6_zqIYZSuM7jOIuDYS3YYWMz42NoH_kosEpJg7TK15Bg
    - type: precision
      value: 0.7552447552447552
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDYxZTkzZjk1NDU0MjhmNzYxM2IzNzJjNjE1Y2UxYTQ0MTJmNjJlMmUzNGY3MDdiMDAyZjQ2MmE4ODExYjYxNiIsInZlcnNpb24iOjF9.98rxE2rgU5ECIv4MGzMnaPRRYg3kGLsG4pZbMuYeAFEfXqBU1K0i_G-_cU7oxIqGypNmMhYVhVxZfC7wS_saAw
    - type: recall
      value: 0.8244274809160306
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTNhNDZiZjMzOWM0ZGJkODMzM2VmOGYxMTYyZDNjYTgwN2NiMDFlOGI4NzM5NjQ5ODc4MWM2YmM5MTZjMWFiOCIsInZlcnNpb24iOjF9.C9aEgIz392h-zFSd98CSmzQ7Y6N0Xq3VmGIMEq9aP3dQPPrtUfl9Ms_QMSgSyWMPDYHup3SAGAP0JmkiVeOoBg
    - type: auc
      value: 0.8564258078008994
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWVlNGVhOTRkNjUxMGMwZmE0YzBjZDQ0YzQ0ODRmYTc0YjI0MDQ2NTNkOWQ2YjU3MmI5NzI4ZWIwMzBlNTQ1NyIsInZlcnNpb24iOjF9.hSyJjOktSt3AItNnVtgWO9jgHwtNbhv4_KrWEV1r_ywopvbpNmSG4yzaI9PZ_bQQ-4ZSmFM8zUYxCl656TWoDQ
    - type: f1
      value: 0.7883211678832117
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGI4Mzk1MTkyZGJkZjQ1MWZkZDIyZTA3OTU0YmZhNjI4NGUxMjk4ZGZhNjZkN2JmZWRmZGU3OWM5Zjc0ODg4NyIsInZlcnNpb24iOjF9.gkQh5Y4dm8NimTtI0i-gHAYTxFRNlOtdgz-NJW8EvNKeFNWYXqa495Q-KEnSBRv88RKiNQXBp-3fyttjhX2HCw
    - type: loss
      value: 0.5560466051101685
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjczNTgxODRlN2Q4NmUyOTdjNzE0ZTZkOWVjZDgzNTdhODAyNGVkM2M1M2I4MGM2ZWMyMDE0ODdhMzQ0N2E1NCIsInZlcnNpb24iOjF9.TfXjqAGtiIQ62HzMkEQmKMMcL9a9bvfBTJARVmTPlIdOOxxF-xuVLXSyFqq2ajhDJXmUEETXBcFzSon_zbHTCQ
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-rte

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE RTE dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5446
- Accuracy: 0.7978

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 156  | 0.7023          | 0.4729   |
| No log        | 2.0   | 312  | 0.6356          | 0.6895   |
| No log        | 3.0   | 468  | 0.5177          | 0.7617   |
| 0.6131        | 4.0   | 624  | 0.6238          | 0.7473   |
| 0.6131        | 5.0   | 780  | 0.5446          | 0.7978   |
| 0.6131        | 6.0   | 936  | 0.9697          | 0.7545   |
| 0.2528        | 7.0   | 1092 | 1.1004          | 0.7690   |
| 0.2528        | 8.0   | 1248 | 1.1937          | 0.7726   |
| 0.2528        | 9.0   | 1404 | 1.3313          | 0.7726   |
| 0.1073        | 10.0  | 1560 | 1.3534          | 0.7726   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
