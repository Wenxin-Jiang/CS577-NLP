---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one50v0_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_50v0_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one50v0_wikigold_split
      type: tagged_one50v0_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.023255813953488372
    - name: Recall
      type: recall
      value: 0.000244081034903588
    - name: F1
      type: f1
      value: 0.00048309178743961357
    - name: Accuracy
      type: accuracy
      value: 0.780812356464178
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_50v0_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one50v0_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6550
- Precision: 0.0233
- Recall: 0.0002
- F1: 0.0005
- Accuracy: 0.7808

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
| No log        | 1.0   | 13   | 0.7660          | 0.0       | 0.0    | 0.0    | 0.7803   |
| No log        | 2.0   | 26   | 0.6781          | 0.0       | 0.0    | 0.0    | 0.7803   |
| No log        | 3.0   | 39   | 0.6550          | 0.0233    | 0.0002 | 0.0005 | 0.7808   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
