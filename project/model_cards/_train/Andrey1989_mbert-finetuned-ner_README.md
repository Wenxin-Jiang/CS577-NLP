---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikiann
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: mbert-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      args: lv
    metrics:
    - name: Precision
      type: precision
      value: 0.9304986338797814
    - name: Recall
      type: recall
      value: 0.9375430144528561
    - name: F1
      type: f1
      value: 0.9340075419952005
    - name: Accuracy
      type: accuracy
      value: 0.9699674740348558
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbert-finetuned-ner

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1264
- Precision: 0.9305
- Recall: 0.9375
- F1: 0.9340
- Accuracy: 0.9700

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.301         | 1.0   | 625  | 0.1756          | 0.8843    | 0.9067 | 0.8953 | 0.9500   |
| 0.1259        | 2.0   | 1250 | 0.1248          | 0.9285    | 0.9335 | 0.9310 | 0.9688   |
| 0.0895        | 3.0   | 1875 | 0.1264          | 0.9305    | 0.9375 | 0.9340 | 0.9700   |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
