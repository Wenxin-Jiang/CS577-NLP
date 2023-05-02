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
- name: distilbert-base-uncased-finetuned-mrpc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: mrpc
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8578431372549019
    - name: F1
      type: f1
      value: 0.9006849315068494
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-mrpc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5556
- Accuracy: 0.8578
- F1: 0.9007

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 230  | 0.3937          | 0.8113   | 0.8670 |
| No log        | 2.0   | 460  | 0.3660          | 0.8480   | 0.8967 |
| 0.4387        | 3.0   | 690  | 0.4298          | 0.8529   | 0.8973 |
| 0.4387        | 4.0   | 920  | 0.5573          | 0.8529   | 0.8990 |
| 0.1832        | 5.0   | 1150 | 0.5556          | 0.8578   | 0.9007 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
