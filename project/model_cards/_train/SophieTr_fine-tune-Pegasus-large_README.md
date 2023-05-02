---
tags:
- generated_from_trainer
model-index:
- name: fine-tune-Pegasus-large
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fine-tune-Pegasus-large

This model is a fine-tuned version of [google/pegasus-large](https://huggingface.co/google/pegasus-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 11.0526

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6.35e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 500
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1
- Datasets 1.17.0
- Tokenizers 0.10.3
