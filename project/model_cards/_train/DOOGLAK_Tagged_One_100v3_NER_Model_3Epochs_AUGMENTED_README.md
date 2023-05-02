---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one100v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_100v3_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one100v3_wikigold_split
      type: tagged_one100v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.20557491289198607
    - name: Recall
      type: recall
      value: 0.08955223880597014
    - name: F1
      type: f1
      value: 0.12475770925110131
    - name: Accuracy
      type: accuracy
      value: 0.8123509941439252
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_100v3_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one100v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4863
- Precision: 0.2056
- Recall: 0.0896
- F1: 0.1248
- Accuracy: 0.8124

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
| No log        | 1.0   | 26   | 0.6246          | 0.1111    | 0.0003 | 0.0005 | 0.7773   |
| No log        | 2.0   | 52   | 0.5272          | 0.1238    | 0.0296 | 0.0478 | 0.7948   |
| No log        | 3.0   | 78   | 0.4863          | 0.2056    | 0.0896 | 0.1248 | 0.8124   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
