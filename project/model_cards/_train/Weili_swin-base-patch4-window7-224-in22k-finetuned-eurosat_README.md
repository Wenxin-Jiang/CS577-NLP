---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: swin-base-patch4-window7-224-in22k-finetuned-eurosat
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
      value: 0.9844444444444445
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swin-base-patch4-window7-224-in22k-finetuned-eurosat

This model is a fine-tuned version of [microsoft/swin-base-patch4-window7-224-in22k](https://huggingface.co/microsoft/swin-base-patch4-window7-224-in22k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0434
- Accuracy: 0.9844

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
| 0.2023        | 1.0   | 190  | 0.0598          | 0.9789   |
| 0.1286        | 2.0   | 380  | 0.0434          | 0.9844   |
| 0.0859        | 3.0   | 570  | 0.0334          | 0.9844   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
