---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cstop_artificial
model-index:
- name: t5-base-pointer-cstop_artificial
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-pointer-cstop_artificial

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the cstop_artificial dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0776
- Exact Match: 0.7746

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

| Training Loss | Epoch  | Step | Validation Loss | Exact Match |
|:-------------:|:------:|:----:|:---------------:|:-----------:|
| 1.7482        | 28.5   | 200  | 0.2505          | 0.1020      |
| 0.1366        | 57.13  | 400  | 0.0776          | 0.3238      |
| 0.0275        | 85.63  | 600  | 0.0881          | 0.3381      |
| 0.0114        | 114.25 | 800  | 0.0990          | 0.3399      |
| 0.0064        | 142.75 | 1000 | 0.1120          | 0.3417      |
| 0.0045        | 171.38 | 1200 | 0.1081          | 0.3435      |
| 0.0036        | 199.88 | 1400 | 0.1230          | 0.3435      |
| 0.0025        | 228.5  | 1600 | 0.1211          | 0.3399      |
| 0.002         | 257.13 | 1800 | 0.1367          | 0.3399      |
| 0.0016        | 285.63 | 2000 | 0.1324          | 0.3435      |
| 0.0013        | 314.25 | 2200 | 0.1340          | 0.3470      |
| 0.001         | 342.75 | 2400 | 0.1374          | 0.3435      |
| 0.0009        | 371.38 | 2600 | 0.1384          | 0.3417      |
| 0.0007        | 399.88 | 2800 | 0.1422          | 0.3435      |
| 0.0006        | 428.5  | 3000 | 0.1452          | 0.3417      |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
