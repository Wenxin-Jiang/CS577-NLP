---
tags:
- image-classification
- timm
- generated_from_trainer
datasets:
- beans
metrics:
- accuracy
model_index:
- name: timm-resnet18-beans-test-2
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: beans
      type: beans
      args: default
    metric:
      name: Accuracy
      type: accuracy
      value: 0.5789473684210527
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# timm-resnet18-beans-test-2

This model is a fine-tuned version of [resnet18](https://huggingface.co/resnet18) on the beans dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3225
- Accuracy: 0.5789

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2601        | 0.02  | 5    | 2.8349          | 0.5113   |
| 1.8184        | 0.04  | 10   | 1.3225          | 0.5789   |


### Framework versions

- Transformers 4.9.1
- Pytorch 1.9.0
- Datasets 1.11.1.dev0
- Tokenizers 0.10.3
