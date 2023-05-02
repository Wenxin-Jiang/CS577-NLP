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
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9192622045504749
    - name: Recall
      type: recall
      value: 0.9310884886452623
    - name: F1
      type: f1
      value: 0.9251375534930251
    - name: Accuracy
      type: accuracy
      value: 0.9823820039080496
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0626
- Precision: 0.9193
- Recall: 0.9311
- F1: 0.9251
- Accuracy: 0.9824

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2393        | 1.0   | 878  | 0.0732          | 0.9052    | 0.9207 | 0.9129 | 0.9801   |
| 0.0569        | 2.0   | 1756 | 0.0626          | 0.9193    | 0.9311 | 0.9251 | 0.9824   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.0
- Tokenizers 0.10.3
