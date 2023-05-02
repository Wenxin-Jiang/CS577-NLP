---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- food101
metrics:
- accuracy
model-index:
- name: swin-finetuned-food101
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: food101
      type: food101
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9220198019801981
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swin-finetuned-food101

This model is a fine-tuned version of [microsoft/swin-base-patch4-window7-224](https://huggingface.co/microsoft/swin-base-patch4-window7-224) on the food101 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4401
- Accuracy: 0.9220

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.0579        | 1.0   | 1183  | 0.4190          | 0.9102   |
| 0.0129        | 2.0   | 2366  | 0.4179          | 0.9155   |
| 0.0076        | 3.0   | 3549  | 0.4219          | 0.9198   |
| 0.0197        | 4.0   | 4732  | 0.4487          | 0.9160   |
| 0.0104        | 5.0   | 5915  | 0.4414          | 0.9210   |
| 0.0007        | 6.0   | 7098  | 0.4401          | 0.9220   |
| 0.0021        | 7.0   | 8281  | 0.4401          | 0.9220   |
| 0.0015        | 8.0   | 9464  | 0.4401          | 0.9220   |
| 0.0056        | 9.0   | 10647 | 0.4401          | 0.9220   |
| 0.0019        | 10.0  | 11830 | 0.4401          | 0.9220   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
