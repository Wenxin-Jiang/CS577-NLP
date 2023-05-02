---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: swin-small-patch4-window7-224-finetuned-eurosat
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
      value: 0.9956803455723542
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swin-small-patch4-window7-224-finetuned-eurosat

This model is a fine-tuned version of [microsoft/swin-small-patch4-window7-224](https://huggingface.co/microsoft/swin-small-patch4-window7-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0102
- Accuracy: 0.9957

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0225        | 0.98  | 32   | 0.0102          | 0.9957   |
| 0.0378        | 1.98  | 64   | 0.0102          | 0.9957   |
| 0.041         | 2.98  | 96   | 0.0102          | 0.9957   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.13.0+cpu
- Datasets 2.6.1
- Tokenizers 0.13.1
