---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one100v5_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_100v5_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one100v5_wikigold_split
      type: tagged_one100v5_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.27906976744186046
    - name: Recall
      type: recall
      value: 0.21439509954058192
    - name: F1
      type: f1
      value: 0.24249422632794454
    - name: Accuracy
      type: accuracy
      value: 0.8484087686263571
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_100v5_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one100v5_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4636
- Precision: 0.2791
- Recall: 0.2144
- F1: 0.2425
- Accuracy: 0.8484

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 41   | 0.5040          | 0.2172    | 0.1266 | 0.1599 | 0.8226   |
| No log        | 2.0   | 82   | 0.4381          | 0.2656    | 0.2154 | 0.2379 | 0.8475   |
| No log        | 3.0   | 123  | 0.4636          | 0.2791    | 0.2144 | 0.2425 | 0.8484   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
