---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-base-STTTest
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-STTTest

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5198
- Wer: 0.3393

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
| 0.231         | 1.0   | 500   | 0.4337          | 0.4100 |
| 0.1845        | 2.01  | 1000  | 0.4296          | 0.3931 |
| 0.1551        | 3.01  | 1500  | 0.4397          | 0.3770 |
| 0.1479        | 4.02  | 2000  | 0.4524          | 0.3827 |
| 0.1186        | 5.02  | 2500  | 0.5182          | 0.3795 |
| 0.1079        | 6.02  | 3000  | 0.4799          | 0.3737 |
| 0.0974        | 7.03  | 3500  | 0.4966          | 0.3860 |
| 0.0878        | 8.03  | 4000  | 0.4993          | 0.3699 |
| 0.0788        | 9.04  | 4500  | 0.5183          | 0.3678 |
| 0.0732        | 10.04 | 5000  | 0.5064          | 0.3635 |
| 0.0664        | 11.04 | 5500  | 0.5330          | 0.3663 |
| 0.0596        | 12.05 | 6000  | 0.5147          | 0.3516 |
| 0.0538        | 13.05 | 6500  | 0.5254          | 0.3581 |
| 0.0535        | 14.06 | 7000  | 0.4902          | 0.3534 |
| 0.0492        | 15.06 | 7500  | 0.5115          | 0.3488 |
| 0.0455        | 16.06 | 8000  | 0.5250          | 0.3472 |
| 0.0434        | 17.07 | 8500  | 0.5338          | 0.3515 |
| 0.0351        | 18.07 | 9000  | 0.5365          | 0.3444 |
| 0.0341        | 19.08 | 9500  | 0.4886          | 0.3439 |
| 0.0332        | 20.08 | 10000 | 0.5234          | 0.3475 |
| 0.0289        | 21.08 | 10500 | 0.5375          | 0.3464 |
| 0.028         | 22.09 | 11000 | 0.5395          | 0.3478 |
| 0.0225        | 23.09 | 11500 | 0.5236          | 0.3428 |
| 0.0244        | 24.1  | 12000 | 0.5122          | 0.3402 |
| 0.0246        | 25.1  | 12500 | 0.5212          | 0.3390 |
| 0.0214        | 26.1  | 13000 | 0.5198          | 0.3393 |
| 0.0179        | 27.11 | 13500 | 0.5198          | 0.3393 |
| 0.0194        | 28.11 | 14000 | 0.5198          | 0.3393 |
| 0.0193        | 29.12 | 14500 | 0.5198          | 0.3393 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.1+cu111
- Datasets 1.18.3
- Tokenizers 0.12.1
