---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- f1
model-index:
- name: bart-large-mrpc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE MRPC
      type: glue
      args: mrpc
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8774509803921569
    - name: F1
      type: f1
      value: 0.9119718309859154
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-mrpc

This model is a fine-tuned version of [facebook/bart-large](https://huggingface.co/facebook/bart-large) on the GLUE MRPC dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5684
- Accuracy: 0.8775
- F1: 0.9120
- Combined Score: 0.8947

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results



### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu102
- Datasets 2.1.0
- Tokenizers 0.11.6
