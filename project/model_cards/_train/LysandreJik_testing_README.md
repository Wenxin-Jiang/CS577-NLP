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
- name: testing
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
      value: 0.6813725490196079
    - name: F1
      type: f1
      value: 0.8104956268221574
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# testing

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the GLUE MRPC dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6644
- Accuracy: 0.6814
- F1: 0.8105
- Combined Score: 0.7459

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
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 10

### Training results



### Framework versions

- Transformers 4.11.0.dev0
- Pytorch 1.9.0+cu111
- Datasets 1.11.0
- Tokenizers 0.10.3
