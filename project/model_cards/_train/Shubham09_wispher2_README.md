---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wispher2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wispher2

This model is a fine-tuned version of [openai/whisper-base.en](https://huggingface.co/openai/whisper-base.en) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8125
- Wer: 50.1754

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
| 0.7532        | 1.12  | 100  | 0.8125          | 50.1754 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1
- Datasets 2.7.1
- Tokenizers 0.13.2
