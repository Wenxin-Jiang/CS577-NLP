---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: librispeech-100h-supervised-meta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# librispeech-100h-supervised-meta

This model is a fine-tuned version of [Kuray107/librispeech-5h-supervised](https://huggingface.co/Kuray107/librispeech-5h-supervised) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0965
- Wer: 0.0330

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
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.1131        | 1.12  | 1000  | 0.0755          | 0.0487 |
| 0.0725        | 2.24  | 2000  | 0.0637          | 0.0404 |
| 0.0539        | 3.36  | 3000  | 0.0661          | 0.0389 |
| 0.0441        | 4.48  | 4000  | 0.0637          | 0.0371 |
| 0.0379        | 5.61  | 5000  | 0.0675          | 0.0356 |
| 0.0341        | 6.73  | 6000  | 0.0735          | 0.0360 |
| 0.0295        | 7.85  | 7000  | 0.0737          | 0.0362 |
| 0.0265        | 8.97  | 8000  | 0.0741          | 0.0350 |
| 0.0244        | 10.09 | 9000  | 0.0779          | 0.0337 |
| 0.0217        | 11.21 | 10000 | 0.0835          | 0.0343 |
| 0.0203        | 12.33 | 11000 | 0.0785          | 0.0339 |
| 0.0188        | 13.45 | 12000 | 0.0827          | 0.0344 |
| 0.0179        | 14.57 | 13000 | 0.0875          | 0.0332 |
| 0.0169        | 15.7  | 14000 | 0.0860          | 0.0330 |
| 0.0158        | 16.82 | 15000 | 0.0954          | 0.0330 |
| 0.0147        | 17.94 | 16000 | 0.0934          | 0.0329 |
| 0.0148        | 19.06 | 17000 | 0.0965          | 0.0330 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3
