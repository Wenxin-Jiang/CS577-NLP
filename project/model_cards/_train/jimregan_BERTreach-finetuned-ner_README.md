---
license: apache-2.0
language: ga
tags:
- generated_from_trainer
- irish
datasets:
- wikiann
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: BERTreach-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      args: ga
    metrics:
    - name: Precision
      type: precision
      value: 0.5200517464424321
    - name: Recall
      type: recall
      value: 0.5667293233082706
    - name: F1
      type: f1
      value: 0.5423881268270744
    - name: Accuracy
      type: accuracy
      value: 0.8365605828220859
widget:
- text: "Saolaíodh Pádraic Ó Conaire i nGaillimh sa bhliain 1882."
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERTreach-finetuned-ner

This model is a fine-tuned version of [jimregan/BERTreach](https://huggingface.co/jimregan/BERTreach) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4944
- Precision: 0.5201
- Recall: 0.5667
- F1: 0.5424
- Accuracy: 0.8366

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 63   | 0.7249          | 0.3645    | 0.3905 | 0.3770 | 0.7584   |
| No log        | 2.0   | 126  | 0.5850          | 0.4529    | 0.4948 | 0.4729 | 0.8072   |
| No log        | 3.0   | 189  | 0.5192          | 0.4949    | 0.5456 | 0.5190 | 0.8288   |
| No log        | 4.0   | 252  | 0.5042          | 0.5208    | 0.5592 | 0.5393 | 0.8348   |
| No log        | 5.0   | 315  | 0.4944          | 0.5201    | 0.5667 | 0.5424 | 0.8366   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
