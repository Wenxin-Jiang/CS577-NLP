---
license: mit
tags:
- generated_from_trainer
model-index:
- name: ko-en-following
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ko-en-following

This model is a fine-tuned version of [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) on the None dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.2770
- eval_bleu: 39.2282
- eval_gen_len: 11.2812
- eval_runtime: 2002.6187
- eval_samples_per_second: 16.527
- eval_steps_per_second: 1.033
- epoch: 2.0
- step: 33098

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
