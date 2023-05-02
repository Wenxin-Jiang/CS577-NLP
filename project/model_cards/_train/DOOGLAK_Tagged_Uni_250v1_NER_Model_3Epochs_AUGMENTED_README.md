---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni250v1_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_250v1_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni250v1_wikigold_split
      type: tagged_uni250v1_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.5971956660293181
    - name: Recall
      type: recall
      value: 0.5290796160361377
    - name: F1
      type: f1
      value: 0.5610778443113772
    - name: Accuracy
      type: accuracy
      value: 0.906793008840565
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_250v1_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni250v1_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3057
- Precision: 0.5972
- Recall: 0.5291
- F1: 0.5611
- Accuracy: 0.9068

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
| No log        | 1.0   | 87   | 0.3972          | 0.2749    | 0.2081 | 0.2369 | 0.8625   |
| No log        | 2.0   | 174  | 0.2895          | 0.5545    | 0.5054 | 0.5288 | 0.9059   |
| No log        | 3.0   | 261  | 0.3057          | 0.5972    | 0.5291 | 0.5611 | 0.9068   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6