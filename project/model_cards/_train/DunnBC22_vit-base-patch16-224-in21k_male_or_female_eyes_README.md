---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
- f1
- recall
- precision
model-index:
- name: vit-base-patch16-224-in21k_male_or_female_eyes
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9726681127982646
    - name: F1
      type: f1
      value: 0.9741273100616017
    - name: Recall
      type: recall
      value: 0.9665851670741646
    - name: Precision
      type: precision
      value: 0.9817880794701986
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-patch16-224-in21k_male_or_female_eyes

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0810
- Accuracy: 0.9727
- F1: 0.9741
- Recall: 0.9666
- Precision: 0.9818

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Recall | Precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:------:|:---------:|
| 0.1998        | 1.0   | 577  | 0.2365          | 0.9072   | 0.9196 | 0.9976 | 0.8530    |
| 0.0846        | 2.0   | 1154 | 0.0810          | 0.9727   | 0.9741 | 0.9666 | 0.9818    |
| 0.0309        | 3.0   | 1731 | 0.0852          | 0.9809   | 0.9821 | 0.9837 | 0.9805    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.8.0
- Tokenizers 0.12.1
