---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article100v6_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_100v6_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article100v6_wikigold_split
      type: article100v6_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.5108527131782946
    - name: Recall
      type: recall
      value: 0.5017766497461928
    - name: F1
      type: f1
      value: 0.5062740076824584
    - name: Accuracy
      type: accuracy
      value: 0.9052396107190628
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_100v6_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article100v6_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2900
- Precision: 0.5109
- Recall: 0.5018
- F1: 0.5063
- Accuracy: 0.9052

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
| No log        | 1.0   | 53   | 0.3274          | 0.3068    | 0.2939 | 0.3002 | 0.8793   |
| No log        | 2.0   | 106  | 0.3055          | 0.5017    | 0.4797 | 0.4905 | 0.9007   |
| No log        | 3.0   | 159  | 0.2900          | 0.5109    | 0.5018 | 0.5063 | 0.9052   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
