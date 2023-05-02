---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article500v7_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_500v7_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article500v7_wikigold_split
      type: article500v7_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6722146739130435
    - name: Recall
      type: recall
      value: 0.7278411180581096
    - name: F1
      type: f1
      value: 0.6989228324209782
    - name: Accuracy
      type: accuracy
      value: 0.938498377390592
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_500v7_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article500v7_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1885
- Precision: 0.6722
- Recall: 0.7278
- F1: 0.6989
- Accuracy: 0.9385

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
| No log        | 1.0   | 60   | 0.2683          | 0.4958    | 0.5388 | 0.5164 | 0.9127   |
| No log        | 2.0   | 120  | 0.1973          | 0.6554    | 0.6896 | 0.6720 | 0.9343   |
| No log        | 3.0   | 180  | 0.1885          | 0.6722    | 0.7278 | 0.6989 | 0.9385   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
