---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article100v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_100v3_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article100v3_wikigold_split
      type: article100v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.3300321199143469
    - name: Recall
      type: recall
      value: 0.31191500126486216
    - name: F1
      type: f1
      value: 0.32071790870074135
    - name: Accuracy
      type: accuracy
      value: 0.8602180404138602
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_100v3_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article100v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3754
- Precision: 0.3300
- Recall: 0.3119
- F1: 0.3207
- Accuracy: 0.8602

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
| No log        | 1.0   | 23   | 0.5728          | 0.1855    | 0.0562 | 0.0862 | 0.7983   |
| No log        | 2.0   | 46   | 0.4070          | 0.2869    | 0.2315 | 0.2562 | 0.8445   |
| No log        | 3.0   | 69   | 0.3754          | 0.3300    | 0.3119 | 0.3207 | 0.8602   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
