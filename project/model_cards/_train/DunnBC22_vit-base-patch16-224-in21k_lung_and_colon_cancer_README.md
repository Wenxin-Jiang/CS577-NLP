---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vit-base-patch16-224-in21k_lung_and_colon_cancer
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
      value: 0.9994
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-patch16-224-in21k_lung_and_colon_cancer

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0016
- Accuracy: 0.9994
- Weighted f1: 0.9994
- Micro f1: 0.9994
- Macro f1: 0.9994
- Weighted recall: 0.9994
- Micro recall: 0.9994
- Macro recall: 0.9994
- Weighted precision: 0.9994
- Micro precision: 0.9994
- Macro precision: 0.9994

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Weighted f1 | Micro f1 | Macro f1 | Weighted recall | Micro recall | Macro recall | Weighted precision | Micro precision | Macro precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-----------:|:--------:|:--------:|:---------------:|:------------:|:------------:|:------------------:|:---------------:|:---------------:|
| 0.0574        | 1.0   | 1250 | 0.0410          | 0.9864   | 0.9864      | 0.9864   | 0.9865   | 0.9864          | 0.9864       | 0.9864       | 0.9872             | 0.9864          | 0.9875          |
| 0.0031        | 2.0   | 2500 | 0.0105          | 0.9972   | 0.9972      | 0.9972   | 0.9972   | 0.9972          | 0.9972       | 0.9973       | 0.9972             | 0.9972          | 0.9972          |
| 0.0007        | 3.0   | 3750 | 0.0016          | 0.9994   | 0.9994      | 0.9994   | 0.9994   | 0.9994          | 0.9994       | 0.9994       | 0.9994             | 0.9994          | 0.9994          |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.12.1
