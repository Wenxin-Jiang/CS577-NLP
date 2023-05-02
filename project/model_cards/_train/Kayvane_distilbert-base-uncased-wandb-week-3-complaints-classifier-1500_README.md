---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- consumer-finance-complaints
model-index:
- name: distilbert-base-uncased-wandb-week-3-complaints-classifier-1500
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-wandb-week-3-complaints-classifier-1500

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the consumer-finance-complaints dataset.

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1
