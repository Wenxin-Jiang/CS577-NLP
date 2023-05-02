---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-base-vanilla-cstop_artificial
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-vanilla-cstop_artificial

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1598

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

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.2724        | 28.5   | 200  | 0.0776          |
| 0.0151        | 57.13  | 400  | 0.1004          |
| 0.1727        | 85.63  | 600  | 0.1202          |
| 0.0133        | 114.25 | 800  | 0.1005          |
| 0.0044        | 142.75 | 1000 | 0.1131          |
| 0.0022        | 171.38 | 1200 | 0.1285          |
| 0.0018        | 199.88 | 1400 | 0.1349          |
| 0.0014        | 228.5  | 1600 | 0.1451          |
| 0.003         | 257.13 | 1800 | 0.1215          |
| 0.003         | 285.63 | 2000 | 0.1345          |
| 0.0012        | 314.25 | 2200 | 0.1520          |
| 0.001         | 342.75 | 2400 | 0.1486          |
| 0.0008        | 371.38 | 2600 | 0.1559          |
| 0.0007        | 399.88 | 2800 | 0.1590          |
| 0.0006        | 428.5  | 3000 | 0.1598          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
