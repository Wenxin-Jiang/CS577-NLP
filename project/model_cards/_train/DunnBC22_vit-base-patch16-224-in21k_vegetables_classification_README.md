---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vit-base-patch16-224-in21k_vegetables_clf
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
      value: 1.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-patch16-224-in21k_vegetables_clf

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0014
- Accuracy: 1.0
- Weighted f1: 1.0
- Micro f1: 1.0
- Macro f1: 1.0
- Weighted recall: 1.0
- Micro recall: 1.0
- Macro recall: 1.0
- Weighted precision: 1.0
- Micro precision: 1.0
- Macro precision: 1.0

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
| 0.2079        | 1.0   | 938  | 0.0193          | 0.996    | 0.9960      | 0.996    | 0.9960   | 0.996           | 0.996        | 0.9960       | 0.9960             | 0.996           | 0.9960          |
| 0.0154        | 2.0   | 1876 | 0.0068          | 0.9987   | 0.9987      | 0.9987   | 0.9987   | 0.9987          | 0.9987       | 0.9987       | 0.9987             | 0.9987          | 0.9987          |
| 0.0018        | 3.0   | 2814 | 0.0014          | 1.0      | 1.0         | 1.0      | 1.0      | 1.0             | 1.0          | 1.0          | 1.0                | 1.0             | 1.0             |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.8.0
- Tokenizers 0.12.1
