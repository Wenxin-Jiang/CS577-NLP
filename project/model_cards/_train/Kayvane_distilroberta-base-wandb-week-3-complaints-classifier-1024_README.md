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
- name: distilroberta-base-wandb-week-3-complaints-classifier-1024
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
      value: 0.8279904184292339
    - name: F1
      type: f1
      value: 0.8236604095677945
    - name: Recall
      type: recall
      value: 0.8279904184292339
    - name: Precision
      type: precision
      value: 0.8235526237070518
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilroberta-base-wandb-week-3-complaints-classifier-1024

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the consumer-finance-complaints dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5351
- Accuracy: 0.8280
- F1: 0.8237
- Recall: 0.8280
- Precision: 0.8236

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 9.027176214786854e-05
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
| 0.7756        | 0.61  | 1500 | 0.7411          | 0.7647   | 0.7375 | 0.7647 | 0.7606    |
| 0.5804        | 1.22  | 3000 | 0.6140          | 0.8088   | 0.8052 | 0.8088 | 0.8077    |
| 0.5008        | 1.83  | 4500 | 0.5351          | 0.8280   | 0.8237 | 0.8280 | 0.8236    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu102
- Datasets 2.3.2
- Tokenizers 0.12.1
