---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one500v7_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_500v7_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one500v7_wikigold_split
      type: tagged_one500v7_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6700655498907502
    - name: Recall
      type: recall
      value: 0.6767193821257815
    - name: F1
      type: f1
      value: 0.6733760292772187
    - name: Accuracy
      type: accuracy
      value: 0.9237216043353603
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_500v7_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one500v7_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2679
- Precision: 0.6701
- Recall: 0.6767
- F1: 0.6734
- Accuracy: 0.9237

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
| No log        | 1.0   | 156  | 0.3336          | 0.5893    | 0.4855 | 0.5324 | 0.8955   |
| No log        | 2.0   | 312  | 0.2580          | 0.6617    | 0.6561 | 0.6589 | 0.9215   |
| No log        | 3.0   | 468  | 0.2679          | 0.6701    | 0.6767 | 0.6734 | 0.9237   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
