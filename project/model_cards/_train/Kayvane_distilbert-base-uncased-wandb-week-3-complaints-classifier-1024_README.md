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
- name: distilbert-base-uncased-wandb-week-3-complaints-classifier-1024
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
      value: 0.8166760103970236
    - name: F1
      type: f1
      value: 0.8089132637288794
    - name: Recall
      type: recall
      value: 0.8166760103970236
    - name: Precision
      type: precision
      value: 0.810259366582512
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-wandb-week-3-complaints-classifier-1024

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the consumer-finance-complaints dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5664
- Accuracy: 0.8167
- F1: 0.8089
- Recall: 0.8167
- Precision: 0.8103

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2.9291066722689668e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1024
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Recall | Precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:------:|:---------:|
| 0.7592        | 0.61  | 1500 | 0.6981          | 0.7776   | 0.7495 | 0.7776 | 0.7610    |
| 0.5859        | 1.22  | 3000 | 0.6082          | 0.8085   | 0.7990 | 0.8085 | 0.8005    |
| 0.5228        | 1.83  | 4500 | 0.5664          | 0.8167   | 0.8089 | 0.8167 | 0.8103    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1
