---
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: rubert-base-srl
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# rubert-base-srl

This model is a fine-tuned version of [./ruBert-base/](https://huggingface.co/./ruBert-base/) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2429
- F1: 0.9563

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.98) and epsilon=1e-06
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.5816        | 1.0   | 57   | 0.3865          | 0.8371 |
| 0.3685        | 2.0   | 114  | 0.1707          | 0.9325 |
| 0.1057        | 3.0   | 171  | 0.0972          | 0.9563 |
| 0.0964        | 4.0   | 228  | 0.1429          | 0.9775 |
| 0.1789        | 5.0   | 285  | 0.2493          | 0.9457 |
| 0.0016        | 6.0   | 342  | 0.1900          | 0.6349 |
| 0.0013        | 7.0   | 399  | 0.2060          | 0.9563 |
| 0.0008        | 8.0   | 456  | 0.2321          | 0.9563 |
| 0.0006        | 9.0   | 513  | 0.2412          | 0.9563 |
| 0.0006        | 10.0  | 570  | 0.2429          | 0.9563 |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.15.1
- Tokenizers 0.10.3
