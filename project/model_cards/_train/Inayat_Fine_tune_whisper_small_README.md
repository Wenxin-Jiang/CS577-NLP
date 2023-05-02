---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: Fine_tune_whisper_small
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Fine_tune_whisper_small

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8238
- Wer: 42.9362

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- training_steps: 900
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.2994        | 3.92  | 200  | 0.6607          | 44.0797 |
| 0.0201        | 7.84  | 400  | 0.7371          | 42.6042 |
| 0.002         | 11.76 | 600  | 0.8027          | 42.5304 |
| 0.0011        | 15.69 | 800  | 0.8238          | 42.9362 |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
