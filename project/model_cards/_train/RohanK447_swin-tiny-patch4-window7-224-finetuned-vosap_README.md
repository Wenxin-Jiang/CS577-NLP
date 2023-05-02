---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: swin-tiny-patch4-window7-224-finetuned-vosap
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
      value: 0.75
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swin-tiny-patch4-window7-224-finetuned-vosap

This model is a fine-tuned version of [microsoft/swin-tiny-patch4-window7-224](https://huggingface.co/microsoft/swin-tiny-patch4-window7-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4894
- Accuracy: 0.75

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 1    | 0.4894          | 0.75     |
| No log        | 2.0   | 2    | 0.5365          | 0.5      |
| No log        | 3.0   | 3    | 0.6957          | 0.5      |
| No log        | 4.0   | 4    | 0.6781          | 0.5      |
| No log        | 5.0   | 5    | 0.5617          | 0.5      |
| No log        | 6.0   | 6    | 0.4461          | 0.75     |
| No log        | 7.0   | 7    | 0.3368          | 0.75     |
| No log        | 8.0   | 8    | 0.3289          | 0.75     |
| No log        | 9.0   | 9    | 0.3642          | 0.75     |
| 0.0539        | 10.0  | 10   | 0.4334          | 0.75     |
| 0.0539        | 11.0  | 11   | 0.5582          | 0.5      |
| 0.0539        | 12.0  | 12   | 0.6676          | 0.5      |
| 0.0539        | 13.0  | 13   | 0.7586          | 0.5      |
| 0.0539        | 14.0  | 14   | 0.7937          | 0.5      |
| 0.0539        | 15.0  | 15   | 0.7986          | 0.5      |
| 0.0539        | 16.0  | 16   | 0.7619          | 0.5      |
| 0.0539        | 17.0  | 17   | 0.7134          | 0.5      |
| 0.0539        | 18.0  | 18   | 0.6725          | 0.5      |
| 0.0539        | 19.0  | 19   | 0.6390          | 0.5      |
| 0.0297        | 20.0  | 20   | 0.6222          | 0.5      |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
