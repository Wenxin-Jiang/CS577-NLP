---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article100v1_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_100v1_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article100v1_wikigold_split
      type: article100v1_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.4708254907233127
    - name: Recall
      type: recall
      value: 0.45504158004158
    - name: F1
      type: f1
      value: 0.4627989956389586
    - name: Accuracy
      type: accuracy
      value: 0.8931865655878142
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_100v1_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article100v1_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3140
- Precision: 0.4708
- Recall: 0.4550
- F1: 0.4628
- Accuracy: 0.8932

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
| No log        | 1.0   | 40   | 0.4092          | 0.1933    | 0.1445 | 0.1654 | 0.8398   |
| No log        | 2.0   | 80   | 0.3279          | 0.4254    | 0.3924 | 0.4082 | 0.8851   |
| No log        | 3.0   | 120  | 0.3140          | 0.4708    | 0.4550 | 0.4628 | 0.8932   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
