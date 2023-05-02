---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cifar100
metrics:
- accuracy
model-index:
- name: swin-base-finetuned-cifar100
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: cifar100
      type: cifar100
      config: cifar100
      split: train
      args: cifar100
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9201
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swin-base-finetuned-cifar100

This model is a fine-tuned version of [microsoft/swin-base-patch4-window7-224](https://huggingface.co/microsoft/swin-base-patch4-window7-224) on the cifar100 dataset.
It achieves the following results on the evaluation set:
- Accuracy: 0.9201
- Loss: 0.3670

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Accuracy | Validation Loss |
|:-------------:|:-----:|:----:|:--------:|:---------------:|
| 0.3536        | 1.0   | 781  | 0.9052   | 0.3141          |
| 0.3254        | 2.0   | 1562 | 0.9117   | 0.2991          |
| 0.0936        | 3.0   | 2343 | 0.9138   | 0.3322          |
| 0.1054        | 4.0   | 3124 | 0.9158   | 0.3483          |
| 0.0269        | 5.0   | 3905 | 0.9201   | 0.3670          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
