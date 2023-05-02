---
language:
- de
license: mit
datasets:
- germaner
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: gbert-large-germaner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: germaner
      type: germaner
      args: default
    metrics:
    - name: precision
      type: precision
      value: 0.8693333333333333
    - name: recall
      type: recall
      value: 0.885640362225097
    - name: f1
      type: f1
      value: 0.8774110861903236
    - name: accuracy
      type: accuracy
      value: 0.9784210744831022
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gbert-large-germaner

This model is a fine-tuned version of [deepset/gbert-large](https://huggingface.co/deepset/gbert-large) on the germaner dataset.
It achieves the following results on the evaluation set:
- precision: 0.8693
- recall: 0.8856
- f1: 0.8774
- accuracy: 0.9784

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
