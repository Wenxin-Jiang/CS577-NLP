---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wnut_17
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: my_awesome_wnut_model
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wnut_17
      type: wnut_17
      config: wnut_17
      split: train
      args: wnut_17
    metrics:
    - name: Precision
      type: precision
      value: 0.5675675675675675
    - name: Recall
      type: recall
      value: 0.2919369786839666
    - name: F1
      type: f1
      value: 0.3855569155446756
    - name: Accuracy
      type: accuracy
      value: 0.9411739557949639
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_awesome_wnut_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the wnut_17 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2777
- Precision: 0.5676
- Recall: 0.2919
- F1: 0.3856
- Accuracy: 0.9412

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 213  | 0.2872          | 0.4563    | 0.2373 | 0.3122 | 0.9377   |
| No log        | 2.0   | 426  | 0.2777          | 0.5676    | 0.2919 | 0.3856 | 0.9412   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
