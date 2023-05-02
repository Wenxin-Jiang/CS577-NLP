---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- f1
model-index:
- name: finetuned-bert-mrpc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      config: mrpc
      split: train
      args: mrpc
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8504901960784313
    - name: F1
      type: f1
      value: 0.8960817717206134
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-bert-mrpc

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4478
- Accuracy: 0.8505
- F1: 0.8961

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
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.5323        | 1.0   | 230  | 0.3748          | 0.8480   | 0.8916 |
| 0.2969        | 2.0   | 460  | 0.3628          | 0.8603   | 0.9005 |
| 0.1535        | 3.0   | 690  | 0.4478          | 0.8505   | 0.8961 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
