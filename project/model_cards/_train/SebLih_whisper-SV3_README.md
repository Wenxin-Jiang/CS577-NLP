---
language:
- sv
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
metrics:
- wer
model-index:
- name: Whisper Small SV
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small SV

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3516
- Wer: 23.0598

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
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.3274        | 0.86  | 200  | 0.3552          | 24.7469 |
| 0.1395        | 1.72  | 400  | 0.3303          | 23.5038 |
| 0.074         | 2.59  | 600  | 0.3349          | 22.6603 |
| 0.0199        | 3.45  | 800  | 0.3451          | 22.7935 |
| 0.0089        | 4.31  | 1000 | 0.3516          | 23.0598 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
