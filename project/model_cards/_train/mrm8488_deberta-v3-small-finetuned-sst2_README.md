---
language:
- en
license: mit
tags:
- generated_from_trainer
- deberta-v3
datasets:
- glue
metrics:
- accuracy
model-index:
- name: deberta-v3-small
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE SST2
      type: glue
      args: sst2
    metrics:
    - type: accuracy
      value: 0.9403669724770642
      name: Accuracy
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: glue
      type: glue
      config: sst2
      split: validation
    metrics:
    - type: accuracy
      value: 0.9403669724770642
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiM2MyOTE4ZTk0YzUyNGFkMGVjNTk4MDBlZGRlZjgzOGIzYWY0YjExMmZmMDZkYjFmOTlkYmM2ZDEwYjMxM2JkOCIsInZlcnNpb24iOjF9.Ks2vdjAFUe0isZp4F-OFK9HzvPqeU3mJEG_XJfOvkTdm9DyaefT9x78sof8i_EbIync5Ao7NOC4STCTQIUvgBw
    - type: precision
      value: 0.9375
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzNiZTEwNGNlZWUwZjMxYmRjNWU0ZGQ1Njg1M2MwNTQ3YWEwN2JlNDk4OWQ4MzNkMmNhOGUwMzA0YWU3ZWZjMiIsInZlcnNpb24iOjF9.p5Gbs680U45zHoWH9YgRLmOxINR4emvc2yNe9Kt3-y_WyyCd6CAAK9ht-IyGJ7GSO5WQny-ISngJFtyFt5NqDQ
    - type: recall
      value: 0.9459459459459459
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjk2MmJjMDZlZDUzM2QzMWZhMzMxNWRkYjJlYzA3MjUwMThiYWMwNmQzODE1MTMxNTdkNWVmMDhhNzJjMjg3MyIsInZlcnNpb24iOjF9.Jeu6tyhXQxMykqqFH0V-IXvyTrxAsgnYByYCOJgfj86957G5LiGdfQzDtTuGkt0XcoenXhPuueT8m5tsuJyLBA
    - type: auc
      value: 0.9804217184474193
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiM2Q5MWU1MGMzMjEwNzY4MDkzN2Q5ZjM5MTQ2MDc5YTRkZTNmNTk2YTdhODI1ZGJlOTlkNTQ2M2Q4YTUxN2Y3OSIsInZlcnNpb24iOjF9.INkDvQhg2jfD7WEE4qHJazPYo10O4Ffc5AZz5vI8fmN01rK3sXzzydvmrmTMzYSSmLhn9sc1-ZkoWbcv81oqBA
    - type: f1
      value: 0.9417040358744394
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYWRhNjljZjk0NjY1ZjU1ZjU2ZmM5ODk1YTVkMTI0ZGY4MjI1OTFlZWJkZWMyMGYxY2I1MzRjODBkNGVlMzJkZSIsInZlcnNpb24iOjF9.kQ547NVFUxeE4vNiGzGsCvMxR1MCJTChX44ds27qQ4Rj2m1UuD2C9TLTuiu8KMvq1mH1io978dJEpOCHYq6KCQ
    - type: loss
      value: 0.21338027715682983
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2YyYmVhNzgxMzMyNjJiNzZkYjE1YWM5Y2ZmMTlkNjQ5MThhYjIxNTE5MmE3Y2E0ODllODMyYjAzYWI3ZWRlMSIsInZlcnNpb24iOjF9.ad9rLnOeJZbRi_QQKEBpNNBp_Bt5SHf39ZeWQOZxp7tAK9dc0OK8XOqtihoXcAWDahwuoGiiYtcFNtvueaX6DA
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DeBERTa v3 (small) fine-tuned on SST2

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the GLUE SST2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2134
- Accuracy: 0.9404

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.176         | 1.0   | 4210  | 0.2134          | 0.9404   |
| 0.1254        | 2.0   | 8420  | 0.2362          | 0.9415   |
| 0.0957        | 3.0   | 12630 | 0.3187          | 0.9335   |
| 0.0673        | 4.0   | 16840 | 0.3039          | 0.9266   |
| 0.0457        | 5.0   | 21050 | 0.3521          | 0.9312   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3
