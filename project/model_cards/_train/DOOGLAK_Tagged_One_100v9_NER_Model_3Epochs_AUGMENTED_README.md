---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one100v9_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_100v9_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one100v9_wikigold_split
      type: tagged_one100v9_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.3040441176470588
    - name: Recall
      type: recall
      value: 0.21319927816447537
    - name: F1
      type: f1
      value: 0.2506440369752993
    - name: Accuracy
      type: accuracy
      value: 0.8538912172644546
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_100v9_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one100v9_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4255
- Precision: 0.3040
- Recall: 0.2132
- F1: 0.2506
- Accuracy: 0.8539

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
| No log        | 1.0   | 40   | 0.5167          | 0.1936    | 0.0376 | 0.0630 | 0.8004   |
| No log        | 2.0   | 80   | 0.4406          | 0.2405    | 0.1441 | 0.1802 | 0.8385   |
| No log        | 3.0   | 120  | 0.4255          | 0.3040    | 0.2132 | 0.2506 | 0.8539   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
