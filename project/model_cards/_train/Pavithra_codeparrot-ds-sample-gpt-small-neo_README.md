---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: codeparrot-ds-sample-gpt-small-neo
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# codeparrot-ds-sample-gpt-small-neo

This model is a fine-tuned version of [EleutherAI/gpt-neo-125M](https://huggingface.co/EleutherAI/gpt-neo-125M) on an unknown dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1000
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.11.6
