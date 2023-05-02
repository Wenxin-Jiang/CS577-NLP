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
- name: distilbert-base-uncased-wandb-week-3-complaints-classifier-256
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
      value: 0.8234544620559604
    - name: F1
      type: f1
      value: 0.8176243580045963
    - name: Recall
      type: recall
      value: 0.8234544620559604
    - name: Precision
      type: precision
      value: 0.8171438106054644
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-wandb-week-3-complaints-classifier-256

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the consumer-finance-complaints dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5453
- Accuracy: 0.8235
- F1: 0.8176
- Recall: 0.8235
- Precision: 0.8171

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.097565552226687e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 256
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Recall | Precision |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:------:|:---------:|
| 0.6691        | 0.61  | 1500 | 0.6475          | 0.7962   | 0.7818 | 0.7962 | 0.7875    |
| 0.5361        | 1.22  | 3000 | 0.5794          | 0.8161   | 0.8080 | 0.8161 | 0.8112    |
| 0.4659        | 1.83  | 4500 | 0.5453          | 0.8235   | 0.8176 | 0.8235 | 0.8171    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1
