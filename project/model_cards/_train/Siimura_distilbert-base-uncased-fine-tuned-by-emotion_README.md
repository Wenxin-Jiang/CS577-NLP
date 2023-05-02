---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- f1
- accuracy
model-index:
- name: distilbert-base-uncased-fine-tuned-by-emotion
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: emotion
      type: emotion
      config: default
      split: train
      args: default
    metrics:
    - name: F1
      type: f1
      value: 0.9345054748683583
    - name: Accuracy
      type: accuracy
      value: 0.9345
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-fine-tuned-by-emotion

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1678
- F1: 0.9345
- Accuracy: 0.9345

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:--------:|
| 0.4805        | 1.0   | 1000 | 0.2051          | 0.9250 | 0.9245   |
| 0.1541        | 2.0   | 2000 | 0.1678          | 0.9345 | 0.9345   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.13.0.dev20220824
- Datasets 2.4.0
- Tokenizers 0.12.1
