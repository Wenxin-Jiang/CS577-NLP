---
language:
- en
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: roberta-base-cola
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE COLA
      type: glue
      args: cola
    metrics:
    - type: matthews_correlation
      value: 0.6232164195970928
      name: Matthews Correlation
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: glue
      type: glue
      config: cola
      split: validation
    metrics:
    - type: accuracy
      value: 0.8456375838926175
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjhmNDQzMzM3ODExYjUzZDA0YjgxNGQxZTE5MGIwOGYzZDIxYjBmMzM3NWJhNTVjMTliYWM1MTNlZTQ3NDk0YyIsInZlcnNpb24iOjF9.pHFErdo8KYG7VgRCfmQnDo3ytNYuSlfBUujEGHD0_wIsHVsNffRPsdinIf-1BU3GzSnyoO3sXf_0M0h-Y3LVCg
    - type: precision
      value: 0.843528494100156
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzk3ZGViNTlhZmJkYTk3YTE5YjZiYjQ3NGMwM2QxNjA4ZTY4NjE0YzlmZDA4MjhhYmViY2U2MzI2NWZlNDUyZSIsInZlcnNpb24iOjF9.JREOHBP9mBJRjgF_Y_KpHQOcHcCoAzW3kUENn1pB5NLQHcFufn6vVastV06867fhIj5PGC8ZAfJYSvj-8oi3Ag
    - type: precision
      value: 0.8456375838926175
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGI4OTM5ZGRhYWI3MThlNTI1ZjlmYjliNDMxZDgyMGE2M2JlYzIxMzBmNmJjMjc4NGEwMGUyN2ExOGZjOGM3ZCIsInZlcnNpb24iOjF9.g3QKEc6pwxppQtwTVFspksNrFaFJvodaYGiOWDzfeYCL-33aEJiQN6zWq7_f1aDzExnKYmaY3TCAvDyfClrcCw
    - type: precision
      value: 0.8450074516171895
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjJkZTFhM2NlMWQ2N2U1ZDAwNWRhODc4NGU4NmIxYWJjNmI3MjJjMGY2MmVhZDMwOTY1N2EwZjJiMzAyNWNkNiIsInZlcnNpb24iOjF9.ThxBlZmBvglRrH_-9Lq4jmix1Q0RlFG9nf1zrw4wfuoOwByhCALYdBLE2q4QNTnS06umezgx1RBSt9cggMx-BQ
    - type: recall
      value: 0.7826539226919134
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTcxZDVmYmQ4NGNkMWZlY2RhZTM0ODA3NGI0ODJjZmYzNjFjZDJiZDgyMGE1ZGIzNjZlY2MyMGJjZDdkNzI2YyIsInZlcnNpb24iOjF9.9hMSyd6qi3H2v_FVCf3W1_hlSYW-uYrZlEhPxifBPhSWqPPxohTRte2UcmWApXGrkRBKI09Nt0wN6aJqLir5AA
    - type: recall
      value: 0.8456375838926175
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzhkNjA4Y2EzMjcyZGYyMmZhMTU2OTY3MTA3MTIxYTFmMzcxYjBmMzY0NDcxMGRiZDRkODdjNjMwMmY0YjUwNCIsInZlcnNpb24iOjF9.gw2I2qqsukk1tdUwER84wTDKy3ZgVAAo9pIIdp4SFgqb1cY9tpkcme5tfA5TGmWEQEKo_5Aot_IkH0XmNOvoDQ
    - type: recall
      value: 0.8456375838926175
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTk1NDMzOTQ0YjM2OWRkOTBmODEzMTIwMzVkMGMzNTM5MjkwMTVmNmI4YzVlMjkxNjU4MDQxYjY3MTYzNTZmYyIsInZlcnNpb24iOjF9.TH7SQ9c9A-MXRoprivGg3aHNeJ1e57S-n61-M4RU_DgoyoJPFQ4cQo4icQHnWt29WiY2TvSpqgFlNx8HNZUXDg
    - type: f1
      value: 0.8032750971481726
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjNiYWY5ZjMzMmEzN2M3MTE4YzMyYjE5Njc4ZTVjMjNjNWIwNTBkOGJmYzFkOGFhMTNkMmE3OTg2YjQ3YmZjNSIsInZlcnNpb24iOjF9.SOmEVhWy3JpdO0ZWbgL-FhdxbuCAZmRj44psK3ipMccssHU1ePKAFdrpArOMLomMfU7qLdYz0BhGusmA3JixBA
    - type: f1
      value: 0.8456375838926175
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjQ1MDVlNTczNWFjYzY3OWNkNTI5MmM2MGQ0NzBlMGNkOWRjZTY5YThkMmM3MjNlYjBmZTQ0YmQ1NjBlMTUyNiIsInZlcnNpb24iOjF9.oR6TJsIb5g44RhaWwq3ShS5jeK--o9Gn38dW7hccdsH03X2hj3OsE6tSjW5fftSFoeKqtK_wMojm_CWM-ZoCBg
    - type: f1
      value: 0.838197890972622
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGNjYjZkZjQyNDJiYWI5NzE2NDk3NzEyMTdmY2VjMjM3NTgxZmJkNzQ4NDIyZjliMzVjMDJjNmIzMWJhMmRkZCIsInZlcnNpb24iOjF9.COJKE4ndKtnNseK4yIxpqeQqQmQ9N6ijv9F6GLkN1cX2r-t4GjD9OHwNd8akl2bB09eU4u97NcZNEb7HlpfdBg
    - type: loss
      value: 1.0575031042099
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNjY4MTc2NjE4NzI0ZDUxOWUzZDFlZTgwNTA1NGY3ZDAzNjk2NWE5NmMzNGI1MTgyYWY0NDFhMDMxZmYxMDcyYiIsInZlcnNpb24iOjF9.UhKXZf7oLduFBfUJrOGTYdd_4gLoeRl9bSGmELkdxvZyJSG6sEkafgz2CoUW4huuEnMeY10ev-U5NOYNUBpuDQ
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-cola

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE COLA dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0571
- Matthews Correlation: 0.6232

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

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 0.5497        | 1.0   | 535  | 0.5504          | 0.4613               |
| 0.3786        | 2.0   | 1070 | 0.4850          | 0.5470               |
| 0.2733        | 3.0   | 1605 | 0.5036          | 0.5792               |
| 0.2204        | 4.0   | 2140 | 0.5532          | 0.6139               |
| 0.164         | 5.0   | 2675 | 0.9516          | 0.5934               |
| 0.1351        | 6.0   | 3210 | 0.9051          | 0.5754               |
| 0.1065        | 7.0   | 3745 | 0.9006          | 0.6161               |
| 0.0874        | 8.0   | 4280 | 0.9457          | 0.6157               |
| 0.0579        | 9.0   | 4815 | 1.0372          | 0.6007               |
| 0.0451        | 10.0  | 5350 | 1.0571          | 0.6232               |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
