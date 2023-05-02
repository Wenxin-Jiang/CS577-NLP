---
language:
- en
tags:
- generated_from_trainer
datasets:
- glue
model_index:
- name: filter
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE STSB
      type: glue
      args: stsb
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# filter

This model is a fine-tuned version of [bert-base-chinese](https://huggingface.co/bert-base-chinese) on the GLUE STSB dataset.

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
- train_batch_size: 6
- eval_batch_size: 6
- seed: 13
- gradient_accumulation_steps: 2
- total_train_batch_size: 12
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.8.2
- Pytorch 1.8.1+cu111
- Datasets 1.9.0
- Tokenizers 0.10.3
