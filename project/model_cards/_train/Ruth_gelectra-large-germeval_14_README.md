---
language:
- de
license: mit
datasets:
- germeval_14
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: gelectra-large-germeval_14
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: germeval_14
      type: germeval_14
      args: default
    metrics:
    - name: precision
      type: precision
      value: 0.85778125349123
    - name: recall
      type: recall
      value: 0.8761839552664613
    - name: f1
      type: f1
      value: 0.8668849497572543
    - name: accuracy
      type: accuracy
      value: 0.976306430788049
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gelectra-large-germeval_14

This model is a fine-tuned version of [deepset/gelectra-large](https://huggingface.co/deepset/gelectra-large) on the germeval_14 dataset.
It achieves the following results on the evaluation set:
- precision: 0.8578
- recall: 0.8762
- f1: 0.8669
- accuracy: 0.9763

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- num_train_epochs: 5
- train_batch_size: 8
- eval_batch_size: 8
- learning_rate: 2e-05
- weight_decay_rate: 0.01
- num_warmup_steps: 0
- fp16: True

### Framework versions

- Transformers 4.18.0
- Datasets 1.18.0
- Tokenizers 0.12.1
