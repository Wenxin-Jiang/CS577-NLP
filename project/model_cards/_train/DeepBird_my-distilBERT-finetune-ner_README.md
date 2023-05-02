---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
model-index:
- name: my-distilBERT-finetune-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9376994122586062
    - name: Recall
      type: recall
      value: 0.9397509256142713
    - name: F1
      type: f1
      value: 0.9387240480793477
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my-distilBERT-finetune-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0563
- Precision: 0.9377
- Recall: 0.9398
- F1: 0.9387

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
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|
| No log        | 1.0   | 439  | 0.0547          | 0.9251    | 0.9291 | 0.9271 |
| 0.1451        | 2.0   | 878  | 0.0531          | 0.9315    | 0.9386 | 0.9350 |
| 0.0326        | 3.0   | 1317 | 0.0563          | 0.9377    | 0.9398 | 0.9387 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
