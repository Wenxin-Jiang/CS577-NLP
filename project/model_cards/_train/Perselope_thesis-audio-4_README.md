---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: thesis-audio-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# thesis-audio-4

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5585
- Wer: 0.3457

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
| 3.6041        | 1.0   | 500   | 2.7841          | 1.0    |
| 1.0447        | 2.01  | 1000  | 0.5261          | 0.5260 |
| 0.4404        | 3.01  | 1500  | 0.4699          | 0.4676 |
| 0.2945        | 4.02  | 2000  | 0.4232          | 0.4212 |
| 0.2223        | 5.02  | 2500  | 0.4348          | 0.4106 |
| 0.1849        | 6.02  | 3000  | 0.4559          | 0.4115 |
| 0.1566        | 7.03  | 3500  | 0.4942          | 0.3943 |
| 0.1389        | 8.03  | 4000  | 0.4142          | 0.3883 |
| 0.1244        | 9.04  | 4500  | 0.4382          | 0.3832 |
| 0.1028        | 10.04 | 5000  | 0.4644          | 0.3826 |
| 0.0972        | 11.04 | 5500  | 0.5119          | 0.3858 |
| 0.0868        | 12.05 | 6000  | 0.4886          | 0.3739 |
| 0.08          | 13.05 | 6500  | 0.5198          | 0.3736 |
| 0.0736        | 14.06 | 7000  | 0.4836          | 0.3672 |
| 0.0673        | 15.06 | 7500  | 0.5187          | 0.3769 |
| 0.0602        | 16.06 | 8000  | 0.6087          | 0.3800 |
| 0.0562        | 17.07 | 8500  | 0.5279          | 0.3630 |
| 0.0568        | 18.07 | 9000  | 0.5696          | 0.3700 |
| 0.047         | 19.08 | 9500  | 0.5964          | 0.3578 |
| 0.0426        | 20.08 | 10000 | 0.5801          | 0.3512 |
| 0.0411        | 21.08 | 10500 | 0.5889          | 0.3573 |
| 0.0349        | 22.09 | 11000 | 0.5654          | 0.3544 |
| 0.0342        | 23.09 | 11500 | 0.5610          | 0.3548 |
| 0.031         | 24.1  | 12000 | 0.5443          | 0.3468 |
| 0.0285        | 25.1  | 12500 | 0.5206          | 0.3469 |
| 0.0243        | 26.1  | 13000 | 0.5455          | 0.3484 |
| 0.0248        | 27.11 | 13500 | 0.5556          | 0.3474 |
| 0.0229        | 28.11 | 14000 | 0.5659          | 0.3457 |
| 0.0229        | 29.12 | 14500 | 0.5585          | 0.3457 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
