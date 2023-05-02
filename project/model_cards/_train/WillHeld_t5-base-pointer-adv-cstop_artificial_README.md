---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cstop_artificial
model-index:
- name: t5-base-pointer-adv-cstop_artificial
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-pointer-adv-cstop_artificial

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the cstop_artificial dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0728
- Exact Match: 0.7925

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 1.7423        | 12.5  | 200  | 0.1173          | 0.2397      |
| 0.3678        | 25.0  | 400  | 0.0728          | 0.3363      |
| 0.3202        | 37.5  | 600  | 0.0879          | 0.3381      |
| 0.3452        | 50.0  | 800  | 0.0908          | 0.3363      |
| 0.3099        | 62.5  | 1000 | 0.1056          | 0.3435      |
| 0.3057        | 75.0  | 1200 | 0.1109          | 0.3470      |
| 0.3045        | 87.5  | 1400 | 0.1273          | 0.3453      |
| 0.3052        | 100.0 | 1600 | 0.1065          | 0.3417      |
| 0.3037        | 112.5 | 1800 | 0.1387          | 0.3381      |
| 0.3036        | 125.0 | 2000 | 0.1421          | 0.3453      |
| 0.3023        | 137.5 | 2200 | 0.1649          | 0.3399      |
| 0.3028        | 150.0 | 2400 | 0.1574          | 0.3399      |
| 0.3025        | 162.5 | 2600 | 0.1563          | 0.3399      |
| 0.3017        | 175.0 | 2800 | 0.1589          | 0.3399      |
| 0.302         | 187.5 | 3000 | 0.1587          | 0.3417      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
