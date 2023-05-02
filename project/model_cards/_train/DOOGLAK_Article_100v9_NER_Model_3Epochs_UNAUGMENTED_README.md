---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article100v9_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_100v9_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article100v9_wikigold_split
      type: article100v9_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.14901960784313725
    - name: Recall
      type: recall
      value: 0.03918535705078628
    - name: F1
      type: f1
      value: 0.06205348030210247
    - name: Accuracy
      type: accuracy
      value: 0.8030657373746729
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_100v9_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article100v9_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5642
- Precision: 0.1490
- Recall: 0.0392
- F1: 0.0621
- Accuracy: 0.8031

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
| No log        | 1.0   | 13   | 0.7073          | 0.0       | 0.0    | 0.0    | 0.7816   |
| No log        | 2.0   | 26   | 0.6007          | 0.0734    | 0.0062 | 0.0114 | 0.7875   |
| No log        | 3.0   | 39   | 0.5642          | 0.1490    | 0.0392 | 0.0621 | 0.8031   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
