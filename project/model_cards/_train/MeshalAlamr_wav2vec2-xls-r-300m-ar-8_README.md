---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-xls-r-300m-ar-8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-ar-8

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 76.6942
- Wer: 0.2108

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
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 60
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 6295.0487     | 4.71  | 400  | 615.8572        | 1.0    |
| 1464.0058     | 9.41  | 800  | 111.7187        | 0.5361 |
| 425.6333      | 14.12 | 1200 | 80.7770         | 0.3446 |
| 280.069       | 18.82 | 1600 | 74.0422         | 0.2980 |
| 213.0118      | 23.53 | 2000 | 78.4876         | 0.2783 |
| 175.6819      | 28.24 | 2400 | 70.4845         | 0.2491 |
| 148.5846      | 32.94 | 2800 | 70.5758         | 0.2443 |
| 131.1029      | 37.65 | 3200 | 75.3770         | 0.2371 |
| 116.7131      | 42.35 | 3600 | 78.7061         | 0.2268 |
| 105.369       | 47.06 | 4000 | 76.4783         | 0.2210 |
| 97.0829       | 51.76 | 4400 | 76.6051         | 0.2153 |
| 90.4009       | 56.47 | 4800 | 76.6942         | 0.2108 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0
- Datasets 1.18.4
- Tokenizers 0.11.6
