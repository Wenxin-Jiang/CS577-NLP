---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one100v6_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_100v6_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one100v6_wikigold_split
      type: tagged_one100v6_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.244097995545657
    - name: Recall
      type: recall
      value: 0.13908629441624365
    - name: F1
      type: f1
      value: 0.17720291026677445
    - name: Accuracy
      type: accuracy
      value: 0.8258844149255108
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_100v6_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one100v6_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5346
- Precision: 0.2441
- Recall: 0.1391
- F1: 0.1772
- Accuracy: 0.8259

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
| No log        | 1.0   | 47   | 0.5840          | 0.1614    | 0.0454 | 0.0709 | 0.8044   |
| No log        | 2.0   | 94   | 0.5226          | 0.2489    | 0.1312 | 0.1718 | 0.8256   |
| No log        | 3.0   | 141  | 0.5346          | 0.2441    | 0.1391 | 0.1772 | 0.8259   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
