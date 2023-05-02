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
- name: distilbert-base-uncased-wandb-week-3-complaints-classifier-512
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
      value: 0.6745323887671373
    - name: F1
      type: f1
      value: 0.6355967633316707
    - name: Recall
      type: recall
      value: 0.6745323887671373
    - name: Precision
      type: precision
      value: 0.6122130681567332
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-wandb-week-3-complaints-classifier-512

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the consumer-finance-complaints dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0839
- Accuracy: 0.6745
- F1: 0.6356
- Recall: 0.6745
- Precision: 0.6122

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0007879237562376572
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
| 1.2707        | 0.61  | 1500 | 1.3009          | 0.6381   | 0.5848 | 0.6381 | 0.5503    |
| 1.1348        | 1.22  | 3000 | 1.1510          | 0.6610   | 0.6178 | 0.6610 | 0.5909    |
| 1.0649        | 1.83  | 4500 | 1.0839          | 0.6745   | 0.6356 | 0.6745 | 0.6122    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1
