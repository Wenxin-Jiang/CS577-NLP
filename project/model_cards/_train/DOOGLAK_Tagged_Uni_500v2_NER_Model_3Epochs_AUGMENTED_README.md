---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni500v2_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_500v2_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni500v2_wikigold_split
      type: tagged_uni500v2_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7018014564967421
    - name: Recall
      type: recall
      value: 0.6811755952380952
    - name: F1
      type: f1
      value: 0.6913347177647726
    - name: Accuracy
      type: accuracy
      value: 0.926232333678042
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_500v2_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni500v2_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2645
- Precision: 0.7018
- Recall: 0.6812
- F1: 0.6913
- Accuracy: 0.9262

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
| No log        | 1.0   | 171  | 0.2364          | 0.6168    | 0.5804 | 0.5980 | 0.9178   |
| No log        | 2.0   | 342  | 0.2626          | 0.6815    | 0.6417 | 0.6610 | 0.9210   |
| 0.1121        | 3.0   | 513  | 0.2645          | 0.7018    | 0.6812 | 0.6913 | 0.9262   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
