---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v9_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v9_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v9_wikigold_split
      type: article500v9_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.74375
    - name: Recall
      type: recall
      value: 0.7617924528301887
    - name: F1
      type: f1
      value: 0.7526631158455394
    - name: Accuracy
      type: accuracy
      value: 0.9441837337228455
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v9_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v9_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1931
- Precision: 0.7438
- Recall: 0.7618
- F1: 0.7527
- Accuracy: 0.9442

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
| No log        | 1.0   | 194  | 0.1870          | 0.7335    | 0.7335 | 0.7335 | 0.9401   |
| No log        | 2.0   | 388  | 0.1840          | 0.7384    | 0.7561 | 0.7471 | 0.9444   |
| 0.1376        | 3.0   | 582  | 0.1931          | 0.7438    | 0.7618 | 0.7527 | 0.9442   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
