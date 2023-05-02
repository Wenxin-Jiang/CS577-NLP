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
- name: bert-large-uncased_ner_conll2003
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
      value: 0.9424197037776668
    - name: Recall
      type: recall
      value: 0.9530461124200605
    - name: F1
      type: f1
      value: 0.947703121077734
    - name: Accuracy
      type: accuracy
      value: 0.9897784354191815
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-large-uncased_ner_conll2003

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0516
- Precision: 0.9424
- Recall: 0.9530
- F1: 0.9477
- Accuracy: 0.9898

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
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1605        | 1.0   | 878  | 0.0533          | 0.9252    | 0.9329 | 0.9290 | 0.9864   |
| 0.032         | 2.0   | 1756 | 0.0433          | 0.9320    | 0.9475 | 0.9397 | 0.9887   |
| 0.0125        | 3.0   | 2634 | 0.0454          | 0.9424    | 0.9524 | 0.9474 | 0.9897   |
| 0.006         | 4.0   | 3512 | 0.0507          | 0.9417    | 0.9519 | 0.9468 | 0.9896   |
| 0.0036        | 5.0   | 4390 | 0.0516          | 0.9424    | 0.9530 | 0.9477 | 0.9898   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
