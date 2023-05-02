---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cstop_artificial
model-index:
- name: byt5-base-cstop_artificial
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# byt5-base-cstop_artificial

This model is a fine-tuned version of [google/byt5-base](https://huggingface.co/google/byt5-base) on the cstop_artificial dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0461
- Exact Match: 0.7996

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
| 0.2563        | 28.5   | 200  | 0.0461          | 0.0376      |
| 0.0065        | 57.13  | 400  | 0.0563          | 0.0376      |
| 0.0021        | 85.63  | 600  | 0.0592          | 0.0358      |
| 0.0013        | 114.25 | 800  | 0.0569          | 0.0376      |
| 0.0008        | 142.75 | 1000 | 0.0675          | 0.0358      |
| 0.0007        | 171.38 | 1200 | 0.0627          | 0.0394      |
| 0.0004        | 199.88 | 1400 | 0.0677          | 0.0358      |
| 0.0003        | 228.5  | 1600 | 0.0650          | 0.0376      |
| 0.0002        | 257.13 | 1800 | 0.0693          | 0.0394      |
| 0.0002        | 285.63 | 2000 | 0.0721          | 0.0394      |
| 0.0002        | 314.25 | 2200 | 0.0714          | 0.0376      |
| 0.0002        | 342.75 | 2400 | 0.0701          | 0.0394      |
| 0.0002        | 371.38 | 2600 | 0.0750          | 0.0394      |
| 0.0001        | 399.88 | 2800 | 0.0739          | 0.0394      |
| 0.0001        | 428.5  | 3000 | 0.0745          | 0.0394      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
