---
tags:
- generated_from_trainer
datasets:
- imdb
model-index:
- name: distilbert-base-uncased-finetuned-imdb-finetuned-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-imdb-finetuned-imdb

This model was trained from scratch on the imdb dataset.
It achieves the following results on the evaluation set:
- eval_loss: 2.1896
- eval_runtime: 3.5892
- eval_samples_per_second: 1707.604
- eval_steps_per_second: 26.747
- epoch: 1.74
- step: 1500

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.24.0
- Pytorch 1.10.0
- Datasets 2.7.1
- Tokenizers 0.13.2
