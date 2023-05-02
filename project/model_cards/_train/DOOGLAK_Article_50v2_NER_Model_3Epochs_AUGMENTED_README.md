---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article50v2_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_50v2_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article50v2_wikigold_split
      type: article50v2_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.40702479338842973
    - name: Recall
      type: recall
      value: 0.09621489621489622
    - name: F1
      type: f1
      value: 0.15563894923958127
    - name: Accuracy
      type: accuracy
      value: 0.8049464101529217
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_50v2_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article50v2_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5035
- Precision: 0.4070
- Recall: 0.0962
- F1: 0.1556
- Accuracy: 0.8049

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
| No log        | 1.0   | 20   | 0.6642          | 0.52      | 0.0063 | 0.0125 | 0.7816   |
| No log        | 2.0   | 40   | 0.5316          | 0.3772    | 0.0630 | 0.1080 | 0.7974   |
| No log        | 3.0   | 60   | 0.5035          | 0.4070    | 0.0962 | 0.1556 | 0.8049   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
