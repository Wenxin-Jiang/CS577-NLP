---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cstop_artificial
model-index:
- name: t5-base-adv-cstop_artificial
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-adv-cstop_artificial

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the cstop_artificial dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0997
- Exact Match: 0.8479

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
| 1.8954        | 12.5  | 200  | 0.1003          | 0.4902      |
| 0.3392        | 25.0  | 400  | 0.0997          | 0.5671      |
| 0.3092        | 37.5  | 600  | 0.1067          | 0.5653      |
| 0.3062        | 50.0  | 800  | 0.1245          | 0.5689      |
| 0.5401        | 62.5  | 1000 | 0.1096          | 0.5581      |
| 0.3075        | 75.0  | 1200 | 0.1197          | 0.5581      |
| 0.3039        | 87.5  | 1400 | 0.1339          | 0.5689      |
| 0.3041        | 100.0 | 1600 | 0.1485          | 0.5635      |
| 0.3036        | 112.5 | 1800 | 0.1498          | 0.5581      |
| 0.304         | 125.0 | 2000 | 0.1454          | 0.5617      |
| 0.3022        | 137.5 | 2200 | 0.1516          | 0.5689      |
| 0.3032        | 150.0 | 2400 | 0.1361          | 0.5635      |
| 0.3035        | 162.5 | 2600 | 0.1427          | 0.5635      |
| 0.3001        | 175.0 | 2800 | 0.1466          | 0.5635      |
| 0.3048        | 187.5 | 3000 | 0.1471          | 0.5635      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
