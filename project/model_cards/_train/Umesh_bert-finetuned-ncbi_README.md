---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- ncbi_disease
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-ncbi
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: ncbi_disease
      type: ncbi_disease
      config: ncbi_disease
      split: train
      args: ncbi_disease
    metrics:
    - name: Precision
      type: precision
      value: 0.7807118254879449
    - name: Recall
      type: recall
      value: 0.8640406607369758
    - name: F1
      type: f1
      value: 0.8202653799758745
    - name: Accuracy
      type: accuracy
      value: 0.9831009585459978
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ncbi

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the ncbi_disease dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0679
- Precision: 0.7807
- Recall: 0.8640
- F1: 0.8203
- Accuracy: 0.9831

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1146        | 1.0   | 680  | 0.0686          | 0.7450    | 0.8056 | 0.7741 | 0.9805   |
| 0.0458        | 2.0   | 1360 | 0.0612          | 0.7646    | 0.8628 | 0.8107 | 0.9815   |
| 0.0161        | 3.0   | 2040 | 0.0679          | 0.7807    | 0.8640 | 0.8203 | 0.9831   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
