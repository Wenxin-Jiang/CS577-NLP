---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-vi-colab-all
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-vi-colab-all

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: inf
- Wer: 0.4537

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 7.448         | 2.4   | 400  | inf             | 1.0    |
| 2.8589        | 4.79  | 800  | inf             | 0.7777 |
| 1.4919        | 7.19  | 1200 | inf             | 0.5968 |
| 1.1255        | 9.58  | 1600 | inf             | 0.5540 |
| 0.9354        | 11.98 | 2000 | inf             | 0.4970 |
| 0.7816        | 14.37 | 2400 | inf             | 0.4799 |
| 0.6822        | 16.77 | 2800 | inf             | 0.4785 |
| 0.5768        | 19.16 | 3200 | inf             | 0.4704 |
| 0.5031        | 21.56 | 3600 | inf             | 0.4609 |
| 0.4589        | 23.95 | 4000 | inf             | 0.4585 |
| 0.4136        | 26.35 | 4400 | inf             | 0.4592 |
| 0.3829        | 28.74 | 4800 | inf             | 0.4537 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
