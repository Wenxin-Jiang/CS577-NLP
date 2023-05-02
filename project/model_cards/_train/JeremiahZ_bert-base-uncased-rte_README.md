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
- name: bert-base-uncased-rte
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
      value: 0.6895306859205776
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
      value: 0.6823104693140795
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTc4OTUzYmQ0NWRkMjdmYjI3ZDhmNWU5MTQ1YTM4ZTQzOWM5MTJjYzlmMjM3ZTE2Y2ZhMGJlNTI0OTJhYjNmMCIsInZlcnNpb24iOjF9.siPkmQhZKOZ1k_SyS1xIMavpK_CQ8tHTm39McCIEjiF7G1x62lbuKfrZsLoKoPf9XpNJqXoaXIRPCpHBKlfwCA
    - type: precision
      value: 0.7047619047619048
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzdmMjk0ZjRkNzM4ZWE1ZGUyOWUxZTFjNmEyNTRmNjZmMDUxOTJlZmUxNjUzMWFhZTYzZTM1ZGNkMDg1YTMzYyIsInZlcnNpb24iOjF9.Cm2kMSTsWVPU9mBv8xAyvo7msTHdG3SECIYZ4kQ5RpN4NV3WE1k0EqmcGzAedwYNfSEg1qXL-qWDKOeoXDAnCw
    - type: recall
      value: 0.5648854961832062
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjc1NTMzYWI5OGRjODdhYmJjZDQ3ODdiMWE3ODYzZjNhZDg1MGIyNjA1YzQwNzcwYTQzNjJkNGVjNmNjMWJmNSIsInZlcnNpb24iOjF9.MwRAu1AKhCt__2vBjhvEqU0gvXaJ5EMOOotKmwGXsuF3eGJEEDDuiWBgu9y291aqndTTwWvuH9CNQjGKLCoNCw
    - type: auc
      value: 0.7394646031580048
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGQwMWVhZjlhNjhhZDRhNGYwNWUyOTZjMTgwMDQ5ZWM3MDcxNDc5OGJiNDE5NTNhOTU0MDMwYTdkYjcxNzFiZiIsInZlcnNpb24iOjF9.ZLyE_ZDWyVAr_GL_3lSqBmuIip7C13oj5kT1lI9JQOidt-IXsRHYUmJt_f7HWUNU1-FBD5lzHYcstF6WQ0VrAw
    - type: f1
      value: 0.6271186440677967
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYmU0YjI4Y2MyMzU5ZTYzMmE0YzhjOTgwM2UwYTNhZDFmZWE3NTdhODMzYmU1ZWUxYTc2Yjk3Nzg3MjAyOThiOSIsInZlcnNpb24iOjF9.GJhnKNSHN5Sv9W3gl8fgPAAbM5EtMlhOHoOFcj_O65FLtcTi_ANpyv7gi41fPbMjS2TG4fgdVHQ_UZg7M6W2Cw
    - type: loss
      value: 0.7001310586929321
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjMwMTY5OGVkMzVhMzdjMmY1YmIzYTViOTRlNzcxMTI4NWNiOTQ5ZjMwMjRlODE4ZWUwMGVhZjhiMmIzM2ViOSIsInZlcnNpb24iOjF9.IsJhfeeqnVZFn10sOkCW7vAzfw1WQMwR8b99B3-hct_lrI1xodt5ySGltDvx2Q8ufD6hzfQ7YaDeHytDmeeFBw
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-rte

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the GLUE RTE dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6972
- Accuracy: 0.6895

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
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 156  | 0.6537          | 0.6318   |
| No log        | 2.0   | 312  | 0.6383          | 0.6534   |
| No log        | 3.0   | 468  | 0.6972          | 0.6895   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
