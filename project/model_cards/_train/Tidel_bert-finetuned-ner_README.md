---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- bionlp2004
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: bionlp2004
      type: bionlp2004
      config: bionlp2004
      split: train
      args: bionlp2004
    metrics:
    - name: Precision
      type: precision
      value: 0.7522050257946413
    - name: Recall
      type: recall
      value: 0.8139744282369891
    - name: F1
      type: f1
      value: 0.781871648503719
    - name: Accuracy
      type: accuracy
      value: 0.9379251370155868
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the bionlp2004 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2098
- Precision: 0.7522
- Recall: 0.8140
- F1: 0.7819
- Accuracy: 0.9379

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
| 0.2255        | 1.0   | 2078 | 0.2073          | 0.7080    | 0.7877 | 0.7457 | 0.9305   |
| 0.1709        | 2.0   | 4156 | 0.1995          | 0.7479    | 0.8106 | 0.7780 | 0.9364   |
| 0.1324        | 3.0   | 6234 | 0.2098          | 0.7522    | 0.8140 | 0.7819 | 0.9379   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
