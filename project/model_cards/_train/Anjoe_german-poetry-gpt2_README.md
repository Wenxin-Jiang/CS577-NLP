---
license: mit
tags:
- generated_from_trainer
model-index:
- name: german-poetry-gpt2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# german-poetry-gpt2

This model is a fine-tuned version of [dbmdz/german-gpt2](https://huggingface.co/dbmdz/german-gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 3.8196
- eval_runtime: 43.8543
- eval_samples_per_second: 86.993
- eval_steps_per_second: 5.45
- epoch: 9.0
- step: 11520

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 22

### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Tokenizers 0.12.1
