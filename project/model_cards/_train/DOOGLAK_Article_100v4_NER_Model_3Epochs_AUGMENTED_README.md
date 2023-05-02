---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article100v4_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_100v4_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article100v4_wikigold_split
      type: article100v4_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.4062070859653941
    - name: Recall
      type: recall
      value: 0.3791335554985901
    - name: F1
      type: f1
      value: 0.39220365950676217
    - name: Accuracy
      type: accuracy
      value: 0.8895926764991446
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_100v4_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article100v4_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3216
- Precision: 0.4062
- Recall: 0.3791
- F1: 0.3922
- Accuracy: 0.8896

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
| No log        | 1.0   | 34   | 0.4586          | 0.1164    | 0.0559 | 0.0755 | 0.8209   |
| No log        | 2.0   | 68   | 0.3347          | 0.3528    | 0.3363 | 0.3444 | 0.8843   |
| No log        | 3.0   | 102  | 0.3216          | 0.4062    | 0.3791 | 0.3922 | 0.8896   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
