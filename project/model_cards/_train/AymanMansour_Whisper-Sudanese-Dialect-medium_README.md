---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: openai/whisper-medium
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# openai/whisper-medium

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2201
- Wer: 44.6966

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0566        | 6.02  | 1000 | 0.9354          | 47.1998 |
| 0.0025        | 13.01 | 2000 | 1.0806          | 47.5605 |
| 0.0012        | 19.03 | 3000 | 1.1642          | 47.6665 |
| 0.0002        | 26.01 | 4000 | 1.1866          | 44.9724 |
| 0.0001        | 33.0  | 5000 | 1.2201          | 44.6966 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
