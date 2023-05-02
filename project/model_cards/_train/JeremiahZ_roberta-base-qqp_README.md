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
- f1
model-index:
- name: roberta-base-qqp
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE QQP
      type: glue
      args: qqp
    metrics:
    - type: accuracy
      value: 0.9152609448429384
      name: Accuracy
    - type: f1
      value: 0.8867138416771377
      name: F1
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: glue
      type: glue
      config: qqp
      split: validation
    metrics:
    - type: accuracy
      value: 0.9153104130596093
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTBmYmQ4MjhlZDBkOWM4YzNiNTE3MDNhMDVlMDNhNmU4YjBiZjNmMDlhOGU2ZmZjMzAwODczNDA0NzkwMDJkMyIsInZlcnNpb24iOjF9.Xpv1jn9glM7lbsQNQvtCnQuueHeGLD0xzEaquc3HfB1p_zFvDRe38mv_B1aHt-YxR16AhfpIbENOM1sPTaAJDA
    - type: precision
      value: 0.8732009117551286
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTYyYWEwOWE0YjI1NWJiNWMwNTMxOTc4OTFmYWI4MTJmMDRkMmEwYWRhMDAzYzVmNDA3Y2YzMzJkMDIzYzNjYyIsInZlcnNpb24iOjF9.O0KMG-s8zO6-tAat0HZRL6MN1ZaZQ_Ng3a_-qC5FndZefHktoJDSD9hiuZFTmlY6Vn1UkDlvG1XnnAi1Gv6pBg
    - type: recall
      value: 0.9007725898555593
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjQ3MzQyM2FlZTc1Y2VjOGY4MGEwMzY2MGM0YjQwNzIwNmVjMmRlNmExYWFlZjU3ZTIyZmJkMGRiZmJkMGZhMCIsInZlcnNpb24iOjF9.eYT8-djtIVkGrr8rhjqE2arUYgXQY0so9o8F4dXkLQt1fNEVa9kxTicapp4h1yTfU2jPpH778J_nvMCzwqixDw
    - type: auc
      value: 0.9685235648551861
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOWRiZGYyYjE5MDFmNWQzN2ZkNGRkMTA4ZTEwNzYxMTg1NTNlY2VjODM0ZDY0NzA1NjQ3MGE2ZWNmY2MxYmNkMyIsInZlcnNpb24iOjF9.aQOO1uk3UON5hgbuMkKK93Yt1aRH4TpBad-KDwjj0_IM9Y11_-itRf6vZuWCkr0gZmyZ-4b0PA4v_dvf88y8Aw
    - type: f1
      value: 0.8867724867724867
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTgxODBkMjZmMjdlZjAyNjA3Njk5OTA4NWExOWQ4NzMwNDlhODNlYTQ1NWZhM2JmNjhjOTA4ZjQxY2QwYTk4ZiIsInZlcnNpb24iOjF9.AjkBwMnuDZVnIXs6EE_ooluFrJSavg58EmUt5Oux2feFP7SvUaWbnetkHIyzBIKb5MEyxuPkSxXU3A6Di-t6CA
    - type: loss
      value: 0.4435121417045593
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzU1ZDg0MGMyOGE0ZWM1Y2MwZjk0ZTAzNjc1MjBlZTUxNDIyNGZmN2EyZTUyZGM3N2E4NmQwOGUyNDBkOTVjNiIsInZlcnNpb24iOjF9.66LOnSclusAZY9uELpElvbcTuUVEJ95oXnspi9BHHw0tgwv38uUeq0cfojuQ_VsNN0UykiT0NooJdWaixpK4BA
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-qqp

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE QQP dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4435
- Accuracy: 0.9153
- F1: 0.8867
- Combined Score: 0.9010

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
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Accuracy | F1     | Combined Score |
|:-------------:|:-----:|:------:|:---------------:|:--------:|:------:|:--------------:|
| 0.2751        | 1.0   | 22741  | 0.3057          | 0.8905   | 0.8512 | 0.8709         |
| 0.2443        | 2.0   | 45482  | 0.2530          | 0.9005   | 0.8710 | 0.8857         |
| 0.2157        | 3.0   | 68223  | 0.2643          | 0.9070   | 0.8769 | 0.8919         |
| 0.1838        | 4.0   | 90964  | 0.2806          | 0.9109   | 0.8815 | 0.8962         |
| 0.146         | 5.0   | 113705 | 0.3277          | 0.9113   | 0.8809 | 0.8961         |
| 0.1262        | 6.0   | 136446 | 0.3939          | 0.9113   | 0.8812 | 0.8962         |
| 0.0867        | 7.0   | 159187 | 0.4435          | 0.9153   | 0.8867 | 0.9010         |
| 0.0757        | 8.0   | 181928 | 0.4812          | 0.9147   | 0.8844 | 0.8996         |
| 0.0479        | 9.0   | 204669 | 0.5081          | 0.9151   | 0.8871 | 0.9011         |
| 0.0379        | 10.0  | 227410 | 0.5647          | 0.9149   | 0.8858 | 0.9003         |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
