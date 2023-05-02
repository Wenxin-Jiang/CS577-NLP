---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one100v2_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_100v2_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one100v2_wikigold_split
      type: tagged_one100v2_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.29022988505747127
    - name: Recall
      type: recall
      value: 0.12856415478615071
    - name: F1
      type: f1
      value: 0.17819336626676077
    - name: Accuracy
      type: accuracy
      value: 0.833149450650485
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_100v2_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one100v2_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4407
- Precision: 0.2902
- Recall: 0.1286
- F1: 0.1782
- Accuracy: 0.8331

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
| No log        | 1.0   | 40   | 0.5318          | 0.2817    | 0.0204 | 0.0380 | 0.7978   |
| No log        | 2.0   | 80   | 0.4431          | 0.2932    | 0.1146 | 0.1647 | 0.8291   |
| No log        | 3.0   | 120  | 0.4407          | 0.2902    | 0.1286 | 0.1782 | 0.8331   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
