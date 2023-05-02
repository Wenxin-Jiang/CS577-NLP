---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v0_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v0_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v0_wikigold_split
      type: article250v0_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.316
    - name: Recall
      type: recall
      value: 0.2984349703184026
    - name: F1
      type: f1
      value: 0.3069664168748265
    - name: Accuracy
      type: accuracy
      value: 0.8677259136623094
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v0_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v0_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3397
- Precision: 0.316
- Recall: 0.2984
- F1: 0.3070
- Accuracy: 0.8677

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
| No log        | 1.0   | 28   | 0.5344          | 0.1336    | 0.0183 | 0.0323 | 0.7903   |
| No log        | 2.0   | 56   | 0.3736          | 0.2753    | 0.2221 | 0.2458 | 0.8528   |
| No log        | 3.0   | 84   | 0.3397          | 0.316     | 0.2984 | 0.3070 | 0.8677   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
