---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mtop
model-index:
- name: t5-small-pointer-mtop
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-pointer-mtop

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the mtop dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1202
- Exact Match: 0.7445

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

| Training Loss | Epoch | Step | Validation Loss | Exact Match |
|:-------------:|:-----:|:----:|:---------------:|:-----------:|
| 2.1451        | 6.65  | 200  | 0.5966          | 0.0134      |
| 0.4695        | 13.33 | 400  | 0.2264          | 0.2998      |
| 0.2229        | 19.98 | 600  | 0.1446          | 0.4649      |
| 0.1389        | 26.65 | 800  | 0.1227          | 0.5154      |
| 0.097         | 33.33 | 1000 | 0.1213          | 0.5221      |
| 0.0724        | 39.98 | 1200 | 0.1202          | 0.5365      |
| 0.0562        | 46.65 | 1400 | 0.1207          | 0.5436      |
| 0.0457        | 53.33 | 1600 | 0.1240          | 0.5441      |
| 0.0399        | 59.98 | 1800 | 0.1349          | 0.5441      |
| 0.0317        | 66.65 | 2000 | 0.1369          | 0.5477      |
| 0.0271        | 73.33 | 2200 | 0.1409          | 0.5490      |
| 0.0237        | 79.98 | 2400 | 0.1462          | 0.5539      |
| 0.0207        | 86.65 | 2600 | 0.1470          | 0.5517      |
| 0.0188        | 93.33 | 2800 | 0.1505          | 0.5508      |
| 0.0174        | 99.98 | 3000 | 0.1505          | 0.5512      |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
