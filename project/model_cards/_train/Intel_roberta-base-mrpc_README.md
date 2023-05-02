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
- name: roberta-base-mrpc
  results:
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
      value: 0.8774509803921569
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzdmODEyMjE4YmRmOTU3M2I1ODE0OWFiNDAzMTdiMDAwNWY5MzA4ZTZkM2IwNTRiZGQ5ZDRiMmEyMGM4ZDFmYyIsInZlcnNpb24iOjF9.w9yMqALfZG7spR6S9DA4JjWcx58TmDcz-58cSWtt7IuPc7XTxD5Ul41oHDsd17MW2hXtysOIMF23VIFmG6s3Bg
    - type: precision
      value: 0.8803986710963455
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTZlNzNhY2NjYjQyYmM5ODgxOGQ2ZGEzOTExNGI1MjU3ZDU5M2E0YzE5ZjRmNDQ0YzMzNWQzMzUzMzkwYjIwNiIsInZlcnNpb24iOjF9.2D7xCmAnHtu3JxhgxmAVS4IUB6QjcN-5VBTga68if0ZQfww_fQ4RrhA6u2QmG06b2e0HLpSb81Ms_BkvQ1GYAA
    - type: recall
      value: 0.9498207885304659
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTcyZmEzYzA1NDI2OTU2YzM2ZDQwOWYzODc4NDkzOGZhMmM3MjljMzM5NjE0NTQxZDFjNDk2MTBmNzE3ODE2YSIsInZlcnNpb24iOjF9.W5VriUXKqNxLkuG5nZEZ3cIri0-7Jb1omdivO8gZVz8ejKsUUZgh7_Lxlp5dpPiMYcAb_ZFn5VhkvUi3a3v-BA
    - type: auc
      value: 0.9474174099080325
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYWYyNGNlNTYxYTBjODU4Mzc4OGQ1ODEyOTEzMTZmMTJjNDJiOTg3NTM3MjgxNDlkMTU1NDU4ZmEyNmJlNmIxMyIsInZlcnNpb24iOjF9.Ps6oFgV_GVAn6-qVR6ips2V3QPris_tw9P3KjaeAs4R6ZQKpq_gAo60lCOG8l2UFLlDz1rHtiTNI8ErLFRtHAQ
    - type: f1
      value: 0.9137931034482758
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNDVmMWUzZmU0OTFlODIzZGQwZTcwMjEyNjc3MzA2MjMzMmZjYWJhYzc3MDBiNjg5ZjE0YTQ3ZjkyZmFmYjBjYiIsInZlcnNpb24iOjF9.IlmOiHR12pik2JktSHBpwpPZOq5CjlFmZD1KlYGnFSZExhCQt_XSFk6pzYaG_ckvO9-H0ktpvpSY0LbD6iSHBQ
    - type: loss
      value: 0.5562044978141785
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYzk0ODEyMTEwNDhkYTZmY2JhNTUzMjRmZGJjYmUwZGNkZTNiZDBlMzdmZGM3NTQwNmRjNmE2MTk1NWIwMzFmYSIsInZlcnNpb24iOjF9.W3XQdn-RsmqKYIZJ47y18iYU6FjQp11fpEY8DWkh0RaWyDAK5Jwkwjqir7-LvgRJgMT7ZbaVRY4I2ozEBo_3Bg
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-mrpc

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE MRPC dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5565
- Accuracy: 0.8775
- F1: 0.9138
- Combined Score: 0.8956

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
- num_epochs: 5.0

### Training results



### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu102
- Datasets 2.1.0
- Tokenizers 0.11.6
