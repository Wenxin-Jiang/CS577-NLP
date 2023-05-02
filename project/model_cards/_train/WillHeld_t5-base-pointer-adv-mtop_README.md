---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mtop
model-index:
- name: t5-base-pointer-adv-mtop
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-pointer-adv-mtop

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the mtop dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1281
- Exact Match: 0.7105

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
| 1.7704        | 1.09  | 200  | 0.3664          | 0.1315      |
| 1.9751        | 2.17  | 400  | 0.2091          | 0.3400      |
| 1.0019        | 3.26  | 600  | 0.1453          | 0.4586      |
| 1.313         | 4.35  | 800  | 0.1313          | 0.5065      |
| 0.6593        | 5.43  | 1000 | 0.1281          | 0.5266      |
| 0.3216        | 6.52  | 1200 | 0.1317          | 0.5253      |
| 0.4614        | 7.61  | 1400 | 0.1508          | 0.5262      |
| 0.3577        | 8.69  | 1600 | 0.1422          | 0.5360      |
| 0.3748        | 9.78  | 1800 | 0.1419          | 0.5459      |
| 0.2422        | 10.87 | 2000 | 0.1603          | 0.5356      |
| 0.4443        | 11.96 | 2200 | 0.1526          | 0.5472      |
| 0.2671        | 13.04 | 2400 | 0.1606          | 0.5481      |
| 0.227         | 14.13 | 2600 | 0.1774          | 0.5441      |
| 0.2053        | 15.22 | 2800 | 0.1752          | 0.5441      |
| 0.1517        | 16.3  | 3000 | 0.1770          | 0.5481      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
