---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-medium-finetuned-on-fleurs-ln_cd1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-medium-finetuned-on-fleurs-ln_cd1

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the "google/fleurs" "ln_cd" subset dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4483
- Wer: 14.7079

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0528        | 4.78  | 1000 | 0.3612          | 17.4812 |
| 0.0013        | 9.57  | 2000 | 0.4214          | 15.7308 |
| 0.0003        | 14.35 | 3000 | 0.4423          | 14.8670 |
| 0.0002        | 19.14 | 4000 | 0.4483          | 14.7079 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.8.0
- Tokenizers 0.13.2
