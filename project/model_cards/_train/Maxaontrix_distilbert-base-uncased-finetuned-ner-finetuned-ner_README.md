---
tags:
- generated_from_trainer
datasets:
- skript
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-ner-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: skript
      type: skript
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.058091286307053944
    - name: Recall
      type: recall
      value: 0.04498714652956298
    - name: F1
      type: f1
      value: 0.05070626584570808
    - name: Accuracy
      type: accuracy
      value: 0.7974446689319497
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner-finetuned-ner

This model was trained from scratch on the skript dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6713
- Precision: 0.0581
- Recall: 0.0450
- F1: 0.0507
- Accuracy: 0.7974

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
| No log        | 1.0   | 44   | 0.8207          | 0.0       | 0.0    | 0.0    | 0.7748   |
| No log        | 2.0   | 88   | 0.7113          | 0.0405    | 0.0231 | 0.0294 | 0.7889   |
| No log        | 3.0   | 132  | 0.6713          | 0.0581    | 0.0450 | 0.0507 | 0.7974   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
