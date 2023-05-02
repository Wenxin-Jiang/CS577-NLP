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
- Loss: 0.5182
- Wer: 0.3329

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
| 3.5177        | 1.0   | 500   | 1.8932          | 0.9837 |
| 0.854         | 2.01  | 1000  | 0.5295          | 0.5266 |
| 0.4205        | 3.01  | 1500  | 0.4299          | 0.4453 |
| 0.2934        | 4.02  | 2000  | 0.3940          | 0.4180 |
| 0.2272        | 5.02  | 2500  | 0.4269          | 0.4149 |
| 0.1856        | 6.02  | 3000  | 0.4277          | 0.4335 |
| 0.1668        | 7.03  | 3500  | 0.4214          | 0.3852 |
| 0.1388        | 8.03  | 4000  | 0.4410          | 0.3805 |
| 0.1254        | 9.04  | 4500  | 0.4152          | 0.3716 |
| 0.1073        | 10.04 | 5000  | 0.4257          | 0.3726 |
| 0.1           | 11.04 | 5500  | 0.4405          | 0.3642 |
| 0.0928        | 12.05 | 6000  | 0.4823          | 0.3708 |
| 0.0829        | 13.05 | 6500  | 0.4636          | 0.3548 |
| 0.0682        | 14.06 | 7000  | 0.4718          | 0.3599 |
| 0.0643        | 15.06 | 7500  | 0.4965          | 0.3583 |
| 0.0609        | 16.06 | 8000  | 0.5279          | 0.3576 |
| 0.0586        | 17.07 | 8500  | 0.4869          | 0.3528 |
| 0.055         | 18.07 | 9000  | 0.4671          | 0.3567 |
| 0.0465        | 19.08 | 9500  | 0.5090          | 0.3508 |
| 0.0432        | 20.08 | 10000 | 0.5024          | 0.3543 |
| 0.0427        | 21.08 | 10500 | 0.4658          | 0.3417 |
| 0.033         | 22.09 | 11000 | 0.5276          | 0.3418 |
| 0.0297        | 23.09 | 11500 | 0.5095          | 0.3415 |
| 0.0317        | 24.1  | 12000 | 0.5061          | 0.3364 |
| 0.0262        | 25.1  | 12500 | 0.4910          | 0.3367 |
| 0.0257        | 26.1  | 13000 | 0.4869          | 0.3331 |
| 0.0237        | 27.11 | 13500 | 0.5023          | 0.3333 |
| 0.0228        | 28.11 | 14000 | 0.5131          | 0.3333 |
| 0.021         | 29.12 | 14500 | 0.5182          | 0.3329 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
