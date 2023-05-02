---
license: mit
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: ko-en-m2m
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ko-en-m2m

This model is a fine-tuned version of [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4282
- Bleu: 25.8137
- Gen Len: 10.9556

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 0.5891        | 0.3   | 5000  | 0.7640          | 12.7212 | 10.465  |
| 0.5653        | 0.6   | 10000 | 0.7211          | 13.4957 | 11.5844 |
| 0.5464        | 0.91  | 15000 | 0.6875          | 13.5204 | 10.6604 |
| 0.5254        | 1.21  | 20000 | 0.6690          | 14.5273 | 10.5754 |
| 0.5308        | 1.51  | 25000 | 0.6757          | 14.1623 | 11.9493 |
| 0.5192        | 1.81  | 30000 | 0.6458          | 15.1048 | 10.8811 |
| 0.502         | 2.11  | 35000 | 0.6423          | 14.7989 | 11.047  |
| 0.4971        | 2.42  | 40000 | 0.6259          | 15.6324 | 11.0428 |
| 0.502         | 2.72  | 45000 | 0.6047          | 16.684  | 10.9814 |
| 0.4544        | 3.02  | 50000 | 0.5834          | 16.9704 | 10.9722 |
| 0.4541        | 3.32  | 55000 | 0.5722          | 17.6061 | 10.8485 |
| 0.4362        | 3.63  | 60000 | 0.5523          | 19.1337 | 10.7972 |
| 0.4285        | 3.93  | 65000 | 0.5325          | 19.4546 | 10.6665 |
| 0.3851        | 4.23  | 70000 | 0.5159          | 20.4035 | 10.6171 |
| 0.3891        | 4.53  | 75000 | 0.4926          | 21.8822 | 10.8857 |
| 0.3602        | 4.83  | 80000 | 0.4740          | 22.737  | 11.0248 |
| 0.336         | 5.14  | 85000 | 0.4570          | 23.7202 | 10.7115 |
| 0.3355        | 5.44  | 90000 | 0.4415          | 24.9891 | 10.9077 |
| 0.3244        | 5.74  | 95000 | 0.4282          | 25.8137 | 10.9556 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
