---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: filipino-wav2vec2-l-xls-r-300m-official
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# filipino-wav2vec2-l-xls-r-300m-official

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4672
- Wer: 0.2922

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.3671        | 2.09  | 400  | 0.5584          | 0.5987 |
| 0.48          | 4.19  | 800  | 0.4244          | 0.4195 |
| 0.2796        | 6.28  | 1200 | 0.3742          | 0.3765 |
| 0.1916        | 8.38  | 1600 | 0.4291          | 0.3667 |
| 0.1463        | 10.47 | 2000 | 0.3745          | 0.3415 |
| 0.1165        | 12.57 | 2400 | 0.4472          | 0.3407 |
| 0.0955        | 14.66 | 2800 | 0.4269          | 0.3290 |
| 0.0823        | 16.75 | 3200 | 0.4608          | 0.3475 |
| 0.0709        | 18.85 | 3600 | 0.4706          | 0.3281 |
| 0.0603        | 20.94 | 4000 | 0.4380          | 0.3183 |
| 0.0527        | 23.04 | 4400 | 0.4473          | 0.3067 |
| 0.0449        | 25.13 | 4800 | 0.4550          | 0.3029 |
| 0.041         | 27.23 | 5200 | 0.4671          | 0.3020 |
| 0.0358        | 29.32 | 5600 | 0.4672          | 0.2922 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
