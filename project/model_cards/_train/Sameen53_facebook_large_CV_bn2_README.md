---
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: facebook_large_CV_bn2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# facebook_large_CV_bn2

This model is a fine-tuned version of [Sameen53/facebook_large_CV_bn3](https://huggingface.co/Sameen53/facebook_large_CV_bn3) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3172
- Wer: 0.2524

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 16
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 0.92  | 500  | 0.4366          | 0.2610 |
| 0.0648        | 1.85  | 1000 | 0.3689          | 0.2563 |
| 0.097         | 2.77  | 1500 | 0.3613          | 0.2677 |
| 0.0998        | 3.7   | 2000 | 0.3669          | 0.2573 |
| 0.1003        | 4.62  | 2500 | 0.3472          | 0.2520 |
| 0.1017        | 5.54  | 3000 | 0.3635          | 0.2559 |
| 0.1052        | 6.47  | 3500 | 0.3546          | 0.2559 |
| 0.1128        | 7.39  | 4000 | 0.3439          | 0.2554 |
| 0.1136        | 8.32  | 4500 | 0.3483          | 0.2515 |
| 0.1178        | 9.24  | 5000 | 0.3469          | 0.2526 |
| 0.1217        | 10.17 | 5500 | 0.3408          | 0.2523 |
| 0.1269        | 11.09 | 6000 | 0.3420          | 0.2556 |
| 0.1273        | 12.01 | 6500 | 0.3331          | 0.2533 |
| 0.1273        | 12.94 | 7000 | 0.3344          | 0.2531 |
| 0.136         | 13.86 | 7500 | 0.3302          | 0.2551 |
| 0.1397        | 14.79 | 8000 | 0.3252          | 0.2522 |
| 0.1447        | 15.71 | 8500 | 0.3172          | 0.2524 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
