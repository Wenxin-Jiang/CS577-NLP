---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-base-timit-demo-google-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-timit-demo-google-colab

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5725
- Wer: 0.3413

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 3.508         | 1.0   | 500   | 1.9315          | 0.9962 |
| 0.8832        | 2.01  | 1000  | 0.5552          | 0.5191 |
| 0.4381        | 3.01  | 1500  | 0.4451          | 0.4574 |
| 0.2983        | 4.02  | 2000  | 0.4096          | 0.4265 |
| 0.2232        | 5.02  | 2500  | 0.4280          | 0.4083 |
| 0.1811        | 6.02  | 3000  | 0.4307          | 0.3942 |
| 0.1548        | 7.03  | 3500  | 0.4453          | 0.3889 |
| 0.1367        | 8.03  | 4000  | 0.5043          | 0.4138 |
| 0.1238        | 9.04  | 4500  | 0.4530          | 0.3807 |
| 0.1072        | 10.04 | 5000  | 0.4435          | 0.3660 |
| 0.0978        | 11.04 | 5500  | 0.4739          | 0.3676 |
| 0.0887        | 12.05 | 6000  | 0.5052          | 0.3761 |
| 0.0813        | 13.05 | 6500  | 0.5098          | 0.3619 |
| 0.0741        | 14.06 | 7000  | 0.4666          | 0.3602 |
| 0.0654        | 15.06 | 7500  | 0.5642          | 0.3657 |
| 0.0589        | 16.06 | 8000  | 0.5489          | 0.3638 |
| 0.0559        | 17.07 | 8500  | 0.5260          | 0.3598 |
| 0.0562        | 18.07 | 9000  | 0.5250          | 0.3640 |
| 0.0448        | 19.08 | 9500  | 0.5215          | 0.3569 |
| 0.0436        | 20.08 | 10000 | 0.5117          | 0.3560 |
| 0.0412        | 21.08 | 10500 | 0.4910          | 0.3570 |
| 0.0336        | 22.09 | 11000 | 0.5221          | 0.3524 |
| 0.031         | 23.09 | 11500 | 0.5278          | 0.3480 |
| 0.0339        | 24.1  | 12000 | 0.5353          | 0.3486 |
| 0.0278        | 25.1  | 12500 | 0.5342          | 0.3462 |
| 0.0251        | 26.1  | 13000 | 0.5399          | 0.3439 |
| 0.0242        | 27.11 | 13500 | 0.5626          | 0.3431 |
| 0.0214        | 28.11 | 14000 | 0.5749          | 0.3408 |
| 0.0216        | 29.12 | 14500 | 0.5725          | 0.3413 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
