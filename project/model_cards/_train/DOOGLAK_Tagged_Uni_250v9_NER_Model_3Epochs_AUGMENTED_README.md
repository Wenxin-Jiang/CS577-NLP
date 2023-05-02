---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni250v9_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_250v9_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni250v9_wikigold_split
      type: tagged_uni250v9_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.587685364281109
    - name: Recall
      type: recall
      value: 0.526270207852194
    - name: F1
      type: f1
      value: 0.5552848004873592
    - name: Accuracy
      type: accuracy
      value: 0.9092797783933518
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_250v9_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni250v9_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2786
- Precision: 0.5877
- Recall: 0.5263
- F1: 0.5553
- Accuracy: 0.9093

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
| No log        | 1.0   | 88   | 0.3533          | 0.3574    | 0.2156 | 0.2690 | 0.8658   |
| No log        | 2.0   | 176  | 0.2946          | 0.5370    | 0.4529 | 0.4914 | 0.8999   |
| No log        | 3.0   | 264  | 0.2786          | 0.5877    | 0.5263 | 0.5553 | 0.9093   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
