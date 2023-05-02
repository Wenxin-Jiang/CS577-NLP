---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2734
- Precision: 0.0
- Recall: 0.0
- F1: 0.0
- Accuracy: 0.9388

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1  | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:---:|:--------:|
| No log        | 1.0   | 34   | 0.3396          | 0.0       | 0.0    | 0.0 | 0.9388   |
| No log        | 2.0   | 68   | 0.3204          | 0.0       | 0.0    | 0.0 | 0.9388   |
| No log        | 3.0   | 102  | 0.2837          | 0.0       | 0.0    | 0.0 | 0.9388   |
| No log        | 4.0   | 136  | 0.2751          | 0.0       | 0.0    | 0.0 | 0.9388   |
| No log        | 5.0   | 170  | 0.2734          | 0.0       | 0.0    | 0.0 | 0.9388   |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.13.1+cu116
- Datasets 2.10.0
- Tokenizers 0.13.2
