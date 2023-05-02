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
- name: vit-base-patch16-224-in21k_dog_vs_cat_image_classification
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
      value: 0.99
    - name: F1
      type: f1
      value: 0.9897161661867544
    - name: Recall
      type: recall
      value: 0.9909390444810544
    - name: Precision
      type: precision
      value: 0.9884963023829088
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-patch16-224-in21k_dog_vs_cat_image_classification

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0404
- Accuracy: 0.99
- F1: 0.9897
- Recall: 0.9909
- Precision: 0.9885

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
| 0.0896        | 1.0   | 1250 | 0.0590          | 0.979    | 0.9783 | 0.9728 | 0.9838    |
| 0.0253        | 2.0   | 2500 | 0.0543          | 0.9842   | 0.9837 | 0.9802 | 0.9871    |
| 0.0066        | 3.0   | 3750 | 0.0404          | 0.99     | 0.9897 | 0.9909 | 0.9885    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.8.0
- Tokenizers 0.12.1
