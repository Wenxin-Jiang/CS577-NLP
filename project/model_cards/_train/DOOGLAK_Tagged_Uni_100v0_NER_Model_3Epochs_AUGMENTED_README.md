---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni100v0_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_100v0_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni100v0_wikigold_split
      type: tagged_uni100v0_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.1801752464403067
    - name: Recall
      type: recall
      value: 0.08303886925795052
    - name: F1
      type: f1
      value: 0.11368348306841741
    - name: Accuracy
      type: accuracy
      value: 0.8143372512510183
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_100v0_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni100v0_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4601
- Precision: 0.1802
- Recall: 0.0830
- F1: 0.1137
- Accuracy: 0.8143

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
| No log        | 1.0   | 33   | 0.5687          | 0.0882    | 0.0015 | 0.0030 | 0.7791   |
| No log        | 2.0   | 66   | 0.5410          | 0.1319    | 0.0270 | 0.0448 | 0.7946   |
| No log        | 3.0   | 99   | 0.4601          | 0.1802    | 0.0830 | 0.1137 | 0.8143   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
