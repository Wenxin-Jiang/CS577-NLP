---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- beans
metrics:
- accuracy
widget:
  - src: >-
      https://huggingface.co/platzi/platzi-vit-base-beans/resolve/main/healthy.jpeg
    example_title: Healthy
  - src: >-
      https://huggingface.co/platzi/platzi-vit-base-beans/resolve/main/bean_rust.jpeg
    example_title: Bean Rust
model-index:
- name: vit-model-juan-bula
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: beans
      type: beans
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 1.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-model-juan-bula

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the beans dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0077
- Accuracy: 1.0

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0067        | 3.85  | 500  | 0.0077          | 1.0      |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cpu
- Datasets 2.7.1
- Tokenizers 0.13.2
