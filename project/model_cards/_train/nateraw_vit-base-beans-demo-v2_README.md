---
license: apache-2.0
tags:
- image-classification
- other-image-classification
- generated_from_trainer
datasets:
- beans
metrics:
- accuracy
model-index:
- name: vit-base-beans-demo-v2
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: beans
      type: beans
      args: default
    metrics:
      - name: Accuracy
        type: accuracy
        value: 1.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-beans-demo-v2

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the beans dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0099
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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0705        | 1.54  | 100  | 0.0562          | 0.9925   |
| 0.0123        | 3.08  | 200  | 0.0124          | 1.0      |
| 0.008         | 4.62  | 300  | 0.0099          | 1.0      |


### Framework versions

- Transformers 4.10.0.dev0
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
