---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v8_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v8_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v8_wikigold_split
      type: article500v8_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7349189934505344
    - name: Recall
      type: recall
      value: 0.7560283687943262
    - name: F1
      type: f1
      value: 0.7453242440132843
    - name: Accuracy
      type: accuracy
      value: 0.9421215763172877
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v8_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v8_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2113
- Precision: 0.7349
- Recall: 0.7560
- F1: 0.7453
- Accuracy: 0.9421

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
| No log        | 1.0   | 191  | 0.1914          | 0.7105    | 0.7181 | 0.7143 | 0.9382   |
| No log        | 2.0   | 382  | 0.2045          | 0.7283    | 0.7574 | 0.7426 | 0.9408   |
| 0.1441        | 3.0   | 573  | 0.2113          | 0.7349    | 0.7560 | 0.7453 | 0.9421   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
