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
- name: Whisper Small - Swedish
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small - Swedish

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 & NST dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3551
- Wer: 19.2143

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 8000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.2128        | 0.85  | 1000 | 0.2955          | 22.1613 |
| 0.0871        | 1.71  | 2000 | 0.2790          | 20.8034 |
| 0.0373        | 2.56  | 3000 | 0.2884          | 19.9269 |
| 0.0163        | 3.41  | 4000 | 0.3082          | 19.5477 |
| 0.0046        | 4.27  | 5000 | 0.3183          | 19.5881 |
| 0.0023        | 5.12  | 6000 | 0.3397          | 19.3757 |
| 0.0023        | 5.97  | 7000 | 0.3468          | 19.3219 |
| 0.0013        | 6.83  | 8000 | 0.3551          | 19.2143 |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1
- Datasets 2.7.1
- Tokenizers 0.13.2
