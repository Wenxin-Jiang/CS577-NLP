---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-base-checkpoint-12
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-checkpoint-12

This model is a fine-tuned version of [jiobiala24/wav2vec2-base-checkpoint-11.1](https://huggingface.co/jiobiala24/wav2vec2-base-checkpoint-11.1) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0795
- Wer: 0.3452

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
- train_batch_size: 32
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
| 0.2793        | 1.64  | 1000  | 0.5692          | 0.3518 |
| 0.2206        | 3.28  | 2000  | 0.6127          | 0.3460 |
| 0.1733        | 4.93  | 3000  | 0.6622          | 0.3580 |
| 0.1391        | 6.57  | 4000  | 0.6768          | 0.3519 |
| 0.1193        | 8.21  | 5000  | 0.7559          | 0.3540 |
| 0.1053        | 9.85  | 6000  | 0.7873          | 0.3562 |
| 0.093         | 11.49 | 7000  | 0.8170          | 0.3612 |
| 0.0833        | 13.14 | 8000  | 0.8682          | 0.3579 |
| 0.0753        | 14.78 | 9000  | 0.8317          | 0.3573 |
| 0.0698        | 16.42 | 10000 | 0.9213          | 0.3525 |
| 0.0623        | 18.06 | 11000 | 0.9746          | 0.3531 |
| 0.0594        | 19.7  | 12000 | 1.0027          | 0.3502 |
| 0.0538        | 21.35 | 13000 | 1.0045          | 0.3545 |
| 0.0504        | 22.99 | 14000 | 0.9821          | 0.3523 |
| 0.0461        | 24.63 | 15000 | 1.0818          | 0.3462 |
| 0.0439        | 26.27 | 16000 | 1.0995          | 0.3495 |
| 0.0421        | 27.91 | 17000 | 1.0533          | 0.3430 |
| 0.0415        | 29.56 | 18000 | 1.0795          | 0.3452 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3
