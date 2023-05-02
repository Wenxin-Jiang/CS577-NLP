---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-uncased-finetuned-emotion
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: emotion
      type: emotion
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9385
    - name: F1
      type: f1
      value: 0.9383492808338979
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-emotion

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1495
- Accuracy: 0.9385
- F1: 0.9383

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.1739        | 1.0   | 250  | 0.1827          | 0.931    | 0.9302 |
| 0.1176        | 2.0   | 500  | 0.1567          | 0.9325   | 0.9326 |
| 0.0994        | 3.0   | 750  | 0.1555          | 0.9385   | 0.9389 |
| 0.08          | 4.0   | 1000 | 0.1496          | 0.9445   | 0.9443 |
| 0.0654        | 5.0   | 1250 | 0.1495          | 0.9385   | 0.9383 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.18.0
- Tokenizers 0.10.3
