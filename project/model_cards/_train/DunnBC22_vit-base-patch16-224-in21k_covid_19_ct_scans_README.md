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
- name: vit-base-patch16-224-in21k_covid_19_ct_scans
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
      value: 0.94
    - name: F1
      type: f1
      value: 0.9379310344827586
    - name: Recall
      type: recall
      value: 0.8947368421052632
    - name: Precision
      type: precision
      value: 0.9855072463768116
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-patch16-224-in21k_covid_19_ct_scans

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1727
- Accuracy: 0.94
- F1: 0.9379
- Recall: 0.8947
- Precision: 0.9855

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
| 0.6742        | 1.0   | 38   | 0.4309          | 0.9      | 0.8993 | 0.8816 | 0.9178    |
| 0.6742        | 2.0   | 76   | 0.3739          | 0.8467   | 0.8686 | 1.0    | 0.7677    |
| 0.6742        | 3.0   | 114  | 0.1727          | 0.94     | 0.9379 | 0.8947 | 0.9855    |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.12.1
