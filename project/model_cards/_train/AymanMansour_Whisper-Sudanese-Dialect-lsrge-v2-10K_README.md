---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: openai/whisper-large-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# openai/whisper-large-v2

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0925
- Wer: 41.4086

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
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 10000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.5216        | 1.04  | 1000  | 0.7054          | 58.7611 |
| 0.0872        | 3.02  | 2000  | 0.7803          | 60.1400 |
| 0.1073        | 4.06  | 3000  | 0.8312          | 61.0522 |
| 0.0617        | 6.04  | 4000  | 0.8583          | 48.2181 |
| 0.0053        | 8.02  | 5000  | 0.9135          | 41.8328 |
| 0.0049        | 9.06  | 6000  | 0.9697          | 43.3814 |
| 0.0044        | 11.04 | 7000  | 0.9863          | 41.9813 |
| 0.0006        | 13.02 | 8000  | 1.0359          | 42.7662 |
| 0.0019        | 14.06 | 9000  | 1.0714          | 41.3449 |
| 0.0007        | 16.04 | 10000 | 1.0925          | 41.4086 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
