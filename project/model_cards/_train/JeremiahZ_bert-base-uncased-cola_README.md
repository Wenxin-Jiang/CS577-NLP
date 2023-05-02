---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- matthews_correlation
model-index:
- name: bert-base-uncased-cola
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
      value: 0.5880094937717885
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
      value: 0.8322147651006712
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTlkZjIwODQ5NGZhMTk3OWJhNjQwOTE3MzIzOWZjMzZmMGRjYmZjYTdhNjhiYjYyNjY0YTk2Y2E5NmJhYzUzMSIsInZlcnNpb24iOjF9.RpXMfM7us7WT2XSMO8w0hxuqbxO1Oy-uFtzTS2Lvc7c27uutkByG1IAzAiT049c6LY7WmC3loigh2rD2kZP6CA
    - type: precision
      value: 0.830203748981255
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNmIzZGMxMjBhZmNiOTI1MDZmNTFjNDI2MDhlNWQ1ZGJlYjVjMjlhNTYxOGYyYWIxZTAwZjg5MWQyY2EzNDJmMyIsInZlcnNpb24iOjF9.oVmulbp5RHd7FbRrb255XJLemj2hPVGKBdfcq2PZADb-PgXLc0Q8_gQ90lvwE0xsx_e5dL8YKdCmbVVIkOxdDg
    - type: precision
      value: 0.8322147651006712
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYmNkYTA4MTU3YTM3ZGFlNWIwZjE4YWNkMTRhOGJlNTE2NDAyYmM4OGNlMDE3OGE4NjdkZjMxMjBiYTU0NTRiMSIsInZlcnNpb24iOjF9.yEbTY7dcAUedTiz2unWx5yAbC0lHe9yWzZ9S_b-sg3-YlM1hGGKjaQaIg8a-L1L_GUzbR7ULsJjkOPiJXNrBCA
    - type: precision
      value: 0.8315568610076411
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDFmNzY1ZTljZTM2ZjE1MzRkMGZmNGZkMDFiYzU0OTZlMzI0ZTg0NmU4MDdmMWJlZTkyYTM3MGRiZTY3MGMxZiIsInZlcnNpb24iOjF9.0epqwE7Qn_vdD9OlBo9pfvaJbKfO6KFp5h5sJ2OosuZHokWCqmF9_cHpYq86ujV8XyI2YLQQhFXxyKjUDJXqAA
    - type: recall
      value: 0.7617741060121812
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2NiMzQwMTQ5Yzk2YjQ3ZTQ5NTRkNGM0NzY2YTk0MGVhNGNkYmRmNzliYWY5OWIwNTczZWE1NjVmYWM2ZjQzNiIsInZlcnNpb24iOjF9.XmeO_f4tg0BAlkZLOZli0Bj34kfdrbOlN8DVRB5WHbbNd1XaB65Ix-RKMHdGWwfdpSHtI3GFcanDbzjdZUZ9Aw
    - type: recall
      value: 0.8322147651006712
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTA5ZGU3NmU3NjljYzU0MjMzMzM4ZjE1ZWFiYWQ3NWI0M2VkZWNkNDY1ODRlNDA2YzIyYmYyODRhYWIyZDFhNSIsInZlcnNpb24iOjF9.88dH3wwT9U0Lni5BVJGyBqkOydW2ndPzH_T1trnT0FdutztRr605dukzGPd2BBZ_yjdEDI4GIxvSvSKGwgZ6CQ
    - type: recall
      value: 0.8322147651006712
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMjc5NjE0NTg5OTljNmI3YTQyNDAzZDg3ODc0YjZmZDc2ZmVmNDZiODYwMTNhNzJkODM5ZThiYjk2YjdkMTVjMyIsInZlcnNpb24iOjF9.fjsGVW60Yv3ttfaICEvgb7s3jAbIyjg9EO1fwrMIxVKBhmg6jZzq0kThSAIOiyi2H-e6QKiibLTAsO0Zb10FAA
    - type: f1
      value: 0.7831814623565482
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGJkMWZmNTUxMzc0NTNlZDhkYTAzNDE5Njc5YzE3MGQ4ZDUyOWYzZTdiMTgzMzM5MDk2MDJlMzhiOWFkMGUwMSIsInZlcnNpb24iOjF9.oeyGkgzeBCSmEWU_NoUmbdBdENDQYIEAQkwoHa6pi-wzdFu7d6850j4-tUvoXFR3PJR8tuQNHDK-FcEOWUJzAw
    - type: f1
      value: 0.8322147651006712
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTc5ZDNkNWJhNzY5M2RmNDUxNDhiNTVjNzViNTdlN2FkODRiMDY0NjBkYmQ0ZGZjODNmODE5NTI3MTNhNWE3MSIsInZlcnNpb24iOjF9.vrmCa028J9GOUEx2G2mP5yx_OXTvEACuAYdK4eHwt70I5wAAMeJkNr-Nv8ZdlQ93KJpLJCxvsC7nl5lsRSMHDg
    - type: f1
      value: 0.8226255909753084
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGZhMzU4N2I0MjBmNTdhZmQwNzRjMjAxMjMyNTlmYTBmZTEyOTQ5NzJjNGI1YmU3ZWFhMTU0ZjM5ODNjN2Y5OCIsInZlcnNpb24iOjF9.bEr9kC61K9bqUoFiMWBjpH1W_LYxvYZSlCLrOAAf8D60ug4LmSQbib8JoydR0SecNocOYP2OMYmEFeujYcX2Aw
    - type: loss
      value: 0.5406177043914795
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYmM3MTBjMWFhOGZjZmI2ZDkyZjI5ODVlNDUxZjIwYjg3MGNjMzk3OTZmYmZmMjE4NjIzMWZhODRlMzE0ODAyZCIsInZlcnNpb24iOjF9.7IiSwd3Kw2on30IVSZB58QTfuJWsU-2-COZ75CkPxQ5QZr1t6Re4AfmKIgAQqeDqwUrxBJ-7tZcaCPDaSh8aBQ
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-cola

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the GLUE COLA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5406
- Matthews Correlation: 0.5880

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

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| No log        | 1.0   | 268  | 0.4598          | 0.5135               |
| 0.393         | 2.0   | 536  | 0.4875          | 0.5573               |
| 0.393         | 3.0   | 804  | 0.5406          | 0.5880               |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
