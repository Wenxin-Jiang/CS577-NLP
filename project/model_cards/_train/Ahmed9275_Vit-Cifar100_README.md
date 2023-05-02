---
license: apache-2.0
tags:
- image-classification
- generated_from_trainer
datasets:
- cifar100
metrics:
- accuracy
model-index:
- name: vit-base-beans-demo-v5
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: Cifar100
      type: cifar100
      args: cifar100
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8985
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-beans-demo-v5

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the Cifar100 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4420
- Accuracy: 0.8985

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
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 1.08          | 1.0   | 3125  | 0.6196          | 0.8262   |
| 0.3816        | 2.0   | 6250  | 0.5322          | 0.8555   |
| 0.1619        | 3.0   | 9375  | 0.4817          | 0.8765   |
| 0.0443        | 4.0   | 12500 | 0.4420          | 0.8985   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1
