---
license: bigscience-bloom-rail-1.0
tags:
- generated_from_trainer
datasets:
- pszemraj/riddlesense_plusplus
model-index:
- name: tst-modeling
  results: []
parameters:
  min_length: 16
  max_length: 96
  no_repeat_ngram_size: 1
  do_sample: True
pipeline_tag:
  text-generation
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tst-modeling

This model is a fine-tuned version of [bigscience/bloom-560m](https://huggingface.co/bigscience/bloom-560m) on the pszemraj/riddlesense_plusplus dataset.

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
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 5.0

### Training results



### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
