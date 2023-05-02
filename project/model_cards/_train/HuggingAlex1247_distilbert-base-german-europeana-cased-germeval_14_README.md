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
- name: distilbert-base-german-europeana-cased-germeval_14
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
      value: 0.7437097717963721
    - name: recall
      type: recall
      value: 0.7571485305798252
    - name: f1
      type: f1
      value: 0.7503689855357669
    - name: accuracy
      type: accuracy
      value: 0.9541357066185896
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-german-europeana-cased-germeval_14

This model is a fine-tuned version of [dbmdz/distilbert-base-german-europeana-cased](https://huggingface.co/dbmdz/distilbert-base-german-europeana-cased) on the germeval_14 dataset.
It achieves the following results on the evaluation set:
- precision: 0.7437
- recall: 0.7571
- f1: 0.7504
- accuracy: 0.9541

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- num_train_epochs: 10
- train_batch_size: 8
- eval_batch_size: 8
- learning_rate: 1e-05
- weight_decay_rate: 0.01
- num_warmup_steps: 0
- fp16: True

### Framework versions

- Transformers 4.17.0
- Datasets 1.18.0
- Tokenizers 0.11.6
