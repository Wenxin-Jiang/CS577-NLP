---
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: Lisa_Whisper
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Lisa_Whisper

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1091
- Wer: 25.1765

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
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- training_steps: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0158        | 25.0  | 100  | 1.1091          | 25.1765 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1
- Datasets 2.7.1
- Tokenizers 0.13.2
