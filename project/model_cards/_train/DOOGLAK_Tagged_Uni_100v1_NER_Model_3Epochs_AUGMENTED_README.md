---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni100v1_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_100v1_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni100v1_wikigold_split
      type: tagged_uni100v1_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.23641213737912636
    - name: Recall
      type: recall
      value: 0.18425155925155925
    - name: F1
      type: f1
      value: 0.20709799912370383
    - name: Accuracy
      type: accuracy
      value: 0.8493674748280798
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_100v1_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni100v1_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4031
- Precision: 0.2364
- Recall: 0.1843
- F1: 0.2071
- Accuracy: 0.8494

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
| No log        | 1.0   | 39   | 0.4906          | 0.1526    | 0.0580 | 0.0840 | 0.8187   |
| No log        | 2.0   | 78   | 0.4213          | 0.2321    | 0.1736 | 0.1986 | 0.8456   |
| No log        | 3.0   | 117  | 0.4031          | 0.2364    | 0.1843 | 0.2071 | 0.8494   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
