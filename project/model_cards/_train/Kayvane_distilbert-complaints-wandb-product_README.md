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
- name: distilbert-complaints-wandb-product
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
      value: 0.8690996641956535
    - name: F1
      type: f1
      value: 0.8645310918904254
    - name: Recall
      type: recall
      value: 0.8690996641956535
    - name: Precision
      type: precision
      value: 0.8629318199420283
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-complaints-wandb-product

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the consumer-finance-complaints dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4431
- Accuracy: 0.8691
- F1: 0.8645
- Recall: 0.8691
- Precision: 0.8629

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     | Recall | Precision |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|:------:|:---------:|
| 0.562         | 0.51  | 2000  | 0.5107          | 0.8452   | 0.8346 | 0.8452 | 0.8252    |
| 0.4548        | 1.01  | 4000  | 0.4628          | 0.8565   | 0.8481 | 0.8565 | 0.8466    |
| 0.3439        | 1.52  | 6000  | 0.4519          | 0.8605   | 0.8544 | 0.8605 | 0.8545    |
| 0.2626        | 2.03  | 8000  | 0.4412          | 0.8678   | 0.8618 | 0.8678 | 0.8626    |
| 0.2717        | 2.53  | 10000 | 0.4431          | 0.8691   | 0.8645 | 0.8691 | 0.8629    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
