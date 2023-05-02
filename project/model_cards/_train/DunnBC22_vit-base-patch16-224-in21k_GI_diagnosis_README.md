---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vit-base-patch16-224-in21k_GI_diagnosis
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
      value: 0.9375
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-patch16-224-in21k_GI_diagnosis

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2538
- Accuracy: 0.9375
- Weighted f1: 0.9365
- Micro f1: 0.9375
- Macro f1: 0.9365
- Weighted recall: 0.9375
- Micro recall: 0.9375
- Macro recall: 0.9375
- Weighted precision: 0.9455
- Micro precision: 0.9375
- Macro precision: 0.9455

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
| 1.3805        | 1.0   | 200  | 0.5006          | 0.8638   | 0.8531      | 0.8638   | 0.8531   | 0.8638          | 0.8638       | 0.8638       | 0.9111             | 0.8638          | 0.9111          |
| 1.3805        | 2.0   | 400  | 0.2538          | 0.9375   | 0.9365      | 0.9375   | 0.9365   | 0.9375          | 0.9375       | 0.9375       | 0.9455             | 0.9375          | 0.9455          |
| 0.0628        | 3.0   | 600  | 0.5797          | 0.8812   | 0.8740      | 0.8812   | 0.8740   | 0.8812          | 0.8812       | 0.8813       | 0.9157             | 0.8812          | 0.9157          |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.12.1
