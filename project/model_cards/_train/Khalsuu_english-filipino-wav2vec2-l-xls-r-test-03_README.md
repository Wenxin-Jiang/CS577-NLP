---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: english-filipino-wav2vec2-l-xls-r-test-03
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# english-filipino-wav2vec2-l-xls-r-test-03

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6932
- Wer: 0.3676

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 40
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.3398        | 2.09  | 400  | 0.5733          | 0.6166 |
| 0.5087        | 4.19  | 800  | 0.5210          | 0.4775 |
| 0.344         | 6.28  | 1200 | 0.5284          | 0.5008 |
| 0.2745        | 8.38  | 1600 | 0.5195          | 0.4457 |
| 0.2153        | 10.47 | 2000 | 0.5820          | 0.4668 |
| 0.1797        | 12.57 | 2400 | 0.4915          | 0.4432 |
| 0.1513        | 14.66 | 2800 | 0.6316          | 0.4513 |
| 0.1355        | 16.75 | 3200 | 0.5328          | 0.4070 |
| 0.1204        | 18.85 | 3600 | 0.5800          | 0.4405 |
| 0.1062        | 20.94 | 4000 | 0.6887          | 0.4532 |
| 0.0931        | 23.04 | 4400 | 0.6184          | 0.4152 |
| 0.0821        | 25.13 | 4800 | 0.7413          | 0.4461 |
| 0.0733        | 27.23 | 5200 | 0.7160          | 0.4549 |
| 0.071         | 29.32 | 5600 | 0.7001          | 0.4048 |
| 0.0577        | 31.41 | 6000 | 0.7839          | 0.4309 |
| 0.051         | 33.51 | 6400 | 0.7764          | 0.4128 |
| 0.046         | 35.6  | 6800 | 0.6753          | 0.3875 |
| 0.0384        | 37.7  | 7200 | 0.7106          | 0.3856 |
| 0.0359        | 39.79 | 7600 | 0.6932          | 0.3676 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
