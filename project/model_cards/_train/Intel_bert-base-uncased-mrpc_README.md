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
      value: 0.8602941176470589
      name: Accuracy
    - type: f1
      value: 0.9042016806722689
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
      value: 0.8602941176470589
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZWMzOWFiNmZjY2ZjMzYzYjk2YjA2ZTc0NjBmYmRlMWM4YWQwMzczYmU0NjcxNjU4YWNhMGMxMjQxNmEwNzM3NSIsInZlcnNpb24iOjF9.5c8Um2j-oDEviTR2S_mlrjQU2Z5zEIgoEldxU6NpIGkM22WhGRMmuCUlkPEpy1q2-HsA4Lz16SAF2bXOXZMqBw
    - type: precision
      value: 0.8512658227848101
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzA0MjM4OGYyYmNhYTU3OTBmNzE3YzViNzQyZTk2NmJiODE2NGJkZGVlMTYxZGQzOWE1YTRkZjZmNjI5ODljNyIsInZlcnNpb24iOjF9.mzDbq7IbSFWnlR6jV-KwuNhOrqnuZVVQX38UzQVClox6O1DRmxAFuo3wmSYBEEaydGipdDN1FAkLXDyZP4LFBg
    - type: recall
      value: 0.96415770609319
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDMxMzUyZDVhNGM0ZTk3NjUxYTVlYmRjYjMxZTY3NjEzZmU5YzA5NTRmZTM3YTU1MjE3MzBmYjA1NzhkNjJlYSIsInZlcnNpb24iOjF9.WxpDTp5ANy97jjbzn4BOeQc5A5JJsyK2NQDv651v7J8AHrt_Srvy5lVia_gyWgqt4bI-ZpPPmBCCCP9MdOhdBw
    - type: auc
      value: 0.8985718651885194
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMWE3ZDc1ZWMwY2RmZmM4ZjQyY2RiMGJjMzFmNmNjNzVmMzE4Y2FlMzJjNzk0MTI3YjdkMTY5ZDg3ZGZjMGFkNSIsInZlcnNpb24iOjF9.PiS1glSDlAM9r7Pvu0FdTCdx45Dr_IDe7TRuZD8QhJzKw__H-Lil5bkBW-FsoN6hKQe80-qtuhLhvLwlZPORCA
    - type: f1
      value: 0.9042016806722689
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2FiOTY2MDI1ZDcyYjE3OGVjOGJjOTc3NGRiODgwNzQxNTEzOGM4YTJhMDE0NjRlNjg1ODk0YzM5YTY0NTQxYSIsInZlcnNpb24iOjF9.gz3szT-MroNcsPhMznhg0kwgWsIa1gfJi8vrhcFMD0PK6djlvZIVKoAS2QE-1cgqPMph7AJXTLifQuPgPBQLDA
    - type: loss
      value: 0.6978028416633606
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDZjODM1NGYyZWMyNDQxOTg0ODkxODgyODcxMzRlZTVjMTc5YjU3MDJmMGMzYzczZDU1Y2NjNTYwYjM2MDEzZiIsInZlcnNpb24iOjF9.eNSy3R0flowu2c4OEAv9rayTQI4YluNN-AuXKzBJM6KPASzuVOD6vTElHMptXiJWc-2tfHJw6CdvyAQSEGTaBg
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-mrpc

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the GLUE MRPC dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6978
- Accuracy: 0.8603
- F1: 0.9042
- Combined Score: 0.8822

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu102
- Datasets 1.14.0
- Tokenizers 0.11.6
