---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- spearmanr
model_index:
- name: stsb
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE STSB
      type: glue
      args: stsb
    metric:
      name: Spearmanr
      type: spearmanr
      value: 0.9050744778895732
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# stsb

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on the GLUE STSB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3978
- Pearson: 0.9090
- Spearmanr: 0.9051
- Combined Score: 0.9071

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4.0

### Training results



### Framework versions

- Transformers 4.9.0
- Pytorch 1.9.0+cu102
- Datasets 1.10.2
- Tokenizers 0.10.3
