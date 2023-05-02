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
- name: roberta-base-qnli
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE QNLI
      type: glue
      args: qnli
    metrics:
    - type: accuracy
      value: 0.9245835621453414
      name: Accuracy
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: glue
      type: glue
      config: qnli
      split: validation
    metrics:
    - type: accuracy
      value: 0.924400512538898
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNmE1ZDY2YTAzNDFiNDdlMGFlNjk2OTkyNjVlMjgwNDJjMzBlMzkwMGZjOWNhZmY2OWFiZjVmOGZlZmU5OGUxNCIsInZlcnNpb24iOjF9._WT9aiP0YGqyVIBSqUt5E6MT6EjB8g2ol_xbl0d1RGLev-eYtACpvAex_qckbXcxqFSENjVqtGx24MqXvQZyAA
    - type: precision
      value: 0.9171997157071784
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDg3ZGEwNTNmZjc2ZDNmZGY5NzgzMDRlMzBiODc0ZDY2NDE5NDRiYzNmYzg4YzQ5ZGM0MmI0ODA5NjQ3OTcxMiIsInZlcnNpb24iOjF9.CCCWPcZ3Ut8yjdal-62KxakOqVF7Vfj_A6etOxRV4pUa1WSpdOtK4BobR59tJKtfUw_l-h32EMMGQK0ZQBNCAA
    - type: recall
      value: 0.9348062296269467
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDI0OTNkOWQ2NGYzYTQ5ZDcwNjk1NDJhYTMzNWQ2ZTkyZDcxZTA5OTFkZTNjZDBmMGZjMDQ4YmI2M2Y3ZWE2YSIsInZlcnNpb24iOjF9.gfgQq9FgLkOA4cBylEAVoJZLupqglQusjnpyd3MAk1zxLeFhYSQOiRmjjW2nPNV2cJM43bR4XPsqePWzWimzDA
    - type: auc
      value: 0.9744865501321541
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODkyODMyZTRmYTIxYmFjNWM3MWI3ZjBhOWExNDkzMjc5MGM2NmNlYmE5NjI0NDU1NjlmYTJkZWNjMDA5ZjhkMiIsInZlcnNpb24iOjF9._CNFbnkR7n2CDTj2lIc6zGSWCFCEJ0V4sj7JZ44xL_cxILp5-m7Y-Dmi43Hk19FaBLfRzdmK9UD-BScNn_vsBw
    - type: f1
      value: 0.9259192825112107
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOWVjN2E1YWNkMDgyMTk0Yjc2ZGFhYzJjNjFkY2VmNmU0NjNjZWQ3N2ZhYzgzNTg2N2FlNmY4YmMyYzJkNjFhOSIsInZlcnNpb24iOjF9.I1dkHU12MMeZerjCJ8JfBMyaR1fCEHvTZfpZN-hD2hTITjgkFcTFC_jFvydSwzKo7yX0ztA5ID3qqgW4qD7bAQ
    - type: loss
      value: 0.2990749478340149
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTM2ZjAwOWNjNWE3NjcwYTVmZTIyY2YzNGI3Mzk5ZjM0YjVmYjg3ODA4Mjc3NWViMDkxMDlmZWRiNTdiOGNjMCIsInZlcnNpb24iOjF9.ODKlAkIeFLR4XiugSVARPvDgVUf6bQas9gSm8r_Q8xzZISaVIOUKNs2Z7kq443LiBBulvBoPaapNPpwkBbMkAw
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-qnli

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE QNLI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2992
- Accuracy: 0.9246

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

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.2986        | 1.0   | 6547  | 0.2215          | 0.9171   |
| 0.243         | 2.0   | 13094 | 0.2321          | 0.9173   |
| 0.2048        | 3.0   | 19641 | 0.2992          | 0.9246   |
| 0.1629        | 4.0   | 26188 | 0.3538          | 0.9220   |
| 0.1308        | 5.0   | 32735 | 0.3533          | 0.9209   |
| 0.0846        | 6.0   | 39282 | 0.4277          | 0.9229   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
