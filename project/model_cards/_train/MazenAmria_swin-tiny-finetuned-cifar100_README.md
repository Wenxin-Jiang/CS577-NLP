---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cifar100
metrics:
- accuracy
model-index:
- name: swin-tiny-finetuned-cifar100
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: cifar100
      type: cifar100
      args: cifar100
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8735
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swin-tiny-finetuned-cifar100

This model is a fine-tuned version of [microsoft/swin-tiny-patch4-window7-224](https://huggingface.co/microsoft/swin-tiny-patch4-window7-224) on the cifar100 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4223
- Accuracy: 0.8735

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
- num_epochs: 20 (with early stopping)

### Training results

| Training Loss | Epoch | Step | Accuracy | Validation Loss |
|:-------------:|:-----:|:----:|:--------:|:---------------:|
| 0.6439        | 1.0   | 781  | 0.8138   | 0.6126          |
| 0.6222        | 2.0   | 1562 | 0.8393   | 0.5094          |
| 0.2912        | 3.0   | 2343 | 0.861    | 0.4452          |
| 0.2234        | 4.0   | 3124 | 0.8679   | 0.4330          |
| 0.121         | 5.0   | 3905 | 0.8735   | 0.4223          |
| 0.2589        | 6.0   | 4686 | 0.8622   | 0.4775          |
| 0.1419        | 7.0   | 5467 | 0.8642   | 0.4900          |
| 0.1513        | 8.0   | 6248 | 0.8667   | 0.4956          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
