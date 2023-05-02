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
- name: vit-base-patch16-224-in21k_Bart_or_Homer
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
      value: 0.9863013698630136
    - name: F1
      type: f1
      value: 0.9841269841269841
    - name: Recall
      type: recall
      value: 1.0
    - name: Precision
      type: precision
      value: 0.96875
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-patch16-224-in21k_Bart_or_Homer

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0636
- Accuracy: 0.9863
- F1: 0.9841
- Recall: 1.0
- Precision: 0.9688

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
| 0.6996        | 1.0   | 13   | 0.1327          | 0.9726   | 0.9688 | 1.0    | 0.9394    |
| 0.6996        | 2.0   | 26   | 0.0636          | 0.9863   | 0.9841 | 1.0    | 0.9688    |
| 0.6996        | 3.0   | 39   | 0.1420          | 0.9452   | 0.9394 | 1.0    | 0.8857    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
