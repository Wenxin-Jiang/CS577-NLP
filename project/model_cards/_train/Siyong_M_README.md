---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: Millad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Millad

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2265
- Wer: 0.5465
- Cer: 0.3162

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
- lr_scheduler_warmup_steps: 4000
- num_epochs: 750
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:------:|:-----:|:---------------:|:------:|:------:|
| 3.2911        | 33.9   | 2000  | 2.2097          | 0.9963 | 0.6047 |
| 1.3419        | 67.8   | 4000  | 1.9042          | 0.7007 | 0.3565 |
| 0.6542        | 101.69 | 6000  | 1.7195          | 0.5985 | 0.3194 |
| 0.373         | 135.59 | 8000  | 2.2219          | 0.6078 | 0.3241 |
| 0.2805        | 169.49 | 10000 | 2.3114          | 0.6320 | 0.3304 |
| 0.2014        | 203.39 | 12000 | 2.6898          | 0.6338 | 0.3597 |
| 0.1611        | 237.29 | 14000 | 2.7808          | 0.6041 | 0.3379 |
| 0.1265        | 271.19 | 16000 | 2.8304          | 0.5632 | 0.3289 |
| 0.1082        | 305.08 | 18000 | 2.8373          | 0.5874 | 0.3344 |
| 0.103         | 338.98 | 20000 | 2.8580          | 0.5743 | 0.3292 |
| 0.0854        | 372.88 | 22000 | 2.5413          | 0.5539 | 0.3186 |
| 0.0675        | 406.78 | 24000 | 2.5523          | 0.5502 | 0.3229 |
| 0.0531        | 440.68 | 26000 | 2.9369          | 0.5483 | 0.3142 |
| 0.0504        | 474.58 | 28000 | 3.1416          | 0.5595 | 0.3225 |
| 0.0388        | 508.47 | 30000 | 2.5655          | 0.5390 | 0.3111 |
| 0.0396        | 542.37 | 32000 | 3.1923          | 0.5558 | 0.3178 |
| 0.0274        | 576.27 | 34000 | 2.9235          | 0.5520 | 0.3257 |
| 0.0361        | 610.17 | 36000 | 3.3828          | 0.5762 | 0.3312 |
| 0.02          | 644.07 | 38000 | 3.3822          | 0.5874 | 0.3466 |
| 0.0176        | 677.97 | 40000 | 3.1191          | 0.5539 | 0.3209 |
| 0.0181        | 711.86 | 42000 | 3.2022          | 0.5576 | 0.3237 |
| 0.0124        | 745.76 | 44000 | 3.2265          | 0.5465 | 0.3162 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
