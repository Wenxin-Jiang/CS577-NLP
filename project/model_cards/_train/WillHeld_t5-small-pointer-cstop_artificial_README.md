---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cstop_artificial
model-index:
- name: t5-small-pointer-cstop_artificial
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-pointer-cstop_artificial

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the cstop_artificial dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0816
- Exact Match: 0.8050

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 32
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Exact Match |
|:-------------:|:------:|:----:|:---------------:|:-----------:|
| 2.08          | 28.5   | 200  | 0.3320          | 0.0376      |
| 0.272         | 57.13  | 400  | 0.1084          | 0.2630      |
| 0.0789        | 85.63  | 600  | 0.0830          | 0.3184      |
| 0.0355        | 114.25 | 800  | 0.0816          | 0.3363      |
| 0.0207        | 142.75 | 1000 | 0.0868          | 0.3292      |
| 0.014         | 171.38 | 1200 | 0.0952          | 0.3399      |
| 0.0099        | 199.88 | 1400 | 0.1089          | 0.3381      |
| 0.0076        | 228.5  | 1600 | 0.1104          | 0.3381      |
| 0.0057        | 257.13 | 1800 | 0.1153          | 0.3292      |
| 0.0048        | 285.63 | 2000 | 0.1153          | 0.3327      |
| 0.004         | 314.25 | 2200 | 0.1206          | 0.3363      |
| 0.0032        | 342.75 | 2400 | 0.1229          | 0.3363      |
| 0.0028        | 371.38 | 2600 | 0.1268          | 0.3381      |
| 0.0023        | 399.88 | 2800 | 0.1288          | 0.3399      |
| 0.002         | 428.5  | 3000 | 0.1292          | 0.3399      |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
