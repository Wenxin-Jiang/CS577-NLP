---
license: bigscience-bloom-rail-1.0
tags:
- generated_from_trainer
datasets:
- pszemraj/riddlesense_plusplus
metrics:
- accuracy
model-index:
- name: bloom-better-riddles
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: pszemraj/riddlesense_plusplus
      type: pszemraj/riddlesense_plusplus
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.6594206731193033
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

# bloom-better-riddles

This model is a fine-tuned version of [bigscience/bloom-560m](https://huggingface.co/bigscience/bloom-560m) on the pszemraj/riddlesense_plusplus dataset.
It achieves the following results on the evaluation set:
- Loss: 4.8107
- Accuracy: 0.6594

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
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 10.0

### Training results



### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
