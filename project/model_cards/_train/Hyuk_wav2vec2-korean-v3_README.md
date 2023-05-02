---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-korean-v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-korean-v3

This model is a fine-tuned version of [Hyuk/wav2vec2-korean-v3](https://huggingface.co/Hyuk/wav2vec2-korean-v3) on the None dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.9860
- eval_wer: 0.3797
- eval_runtime: 56.5559
- eval_samples_per_second: 10.167
- eval_steps_per_second: 1.273
- epoch: 9.73
- step: 12300

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 400
- num_epochs: 10
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
