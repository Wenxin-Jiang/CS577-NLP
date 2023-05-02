---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- consumer-finance-complaints
metrics:
- accuracy
- f1
- recall
- precision
model-index:
- name: distilroberta-base-wandb-week-3-complaints-classifier-512
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: consumer-finance-complaints
      type: consumer-finance-complaints
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8038326283064064
    - name: F1
      type: f1
      value: 0.791857014338201
    - name: Recall
      type: recall
      value: 0.8038326283064064
    - name: Precision
      type: precision
      value: 0.7922430702228043
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilroberta-base-wandb-week-3-complaints-classifier-512

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the consumer-finance-complaints dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6004
- Accuracy: 0.8038
- F1: 0.7919
- Recall: 0.8038
- Precision: 0.7922

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.7835312622444155e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 512
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Recall | Precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:------:|:---------:|
| 0.7559        | 0.61  | 1500 | 0.7307          | 0.7733   | 0.7411 | 0.7733 | 0.7286    |
| 0.6361        | 1.22  | 3000 | 0.6559          | 0.7846   | 0.7699 | 0.7846 | 0.7718    |
| 0.5774        | 1.83  | 4500 | 0.6004          | 0.8038   | 0.7919 | 0.8038 | 0.7922    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1
