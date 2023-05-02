---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: vit-base-patch16-224-in21k_car_or_motorcycle
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
      value: 0.99375
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-patch16-224-in21k_car_or_motorcycle

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0301
- Accuracy: 0.9938
- Weighted f1: 0.9939
- Weighted recall: 0.9927
- Weighted precision: 0.9951

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Weighted f1 | Weighted recall | Weighted precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:-----------:|:---------------:|:------------------:|
| 0.6908        | 1.0   | 200  | 0.0372          | 0.99     | 0.9902      | 0.9902          | 0.9902             |
| 0.6908        | 2.0   | 400  | 0.0301          | 0.9938   | 0.9939      | 0.9927          | 0.9951             |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.12.1
