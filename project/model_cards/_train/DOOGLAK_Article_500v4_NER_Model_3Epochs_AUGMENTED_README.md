---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v4_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v4_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v4_wikigold_split
      type: article500v4_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7284386021160628
    - name: Recall
      type: recall
      value: 0.7543160690571049
    - name: F1
      type: f1
      value: 0.7411515250366988
    - name: Accuracy
      type: accuracy
      value: 0.9409116656232299
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v4_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v4_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2097
- Precision: 0.7284
- Recall: 0.7543
- F1: 0.7412
- Accuracy: 0.9409

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
| No log        | 1.0   | 211  | 0.1880          | 0.7139    | 0.7480 | 0.7305 | 0.9400   |
| No log        | 2.0   | 422  | 0.2043          | 0.7266    | 0.7367 | 0.7316 | 0.9388   |
| 0.135         | 3.0   | 633  | 0.2097          | 0.7284    | 0.7543 | 0.7412 | 0.9409   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
