---
license: mit
tags:
- generated_from_trainer
model-index:
- name: german-poetry-gpt2-large
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# german-poetry-gpt2-large

This model is a fine-tuned version of [benjamin/gerpt2-large](https://huggingface.co/benjamin/gerpt2-large) on German poems.
It achieves the following results on the evaluation set:
- eval_loss: 3.5753
- eval_runtime: 100.7173
- eval_samples_per_second: 51.6
- eval_steps_per_second: 25.805
- epoch: 4.0
- step: 95544

## Model description

large version of gpt-2

## Intended uses & limitations

It could be used for poetry generation

## Training and evaluation data

The model was trained on german poems from projekt Gutenberg

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 6

### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.3.0
- Tokenizers 0.12.1
