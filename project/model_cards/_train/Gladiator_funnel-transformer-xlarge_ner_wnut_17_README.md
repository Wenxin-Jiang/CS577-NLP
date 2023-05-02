---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wnut_17
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: funnel-transformer-xlarge_ner_wnut_17
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wnut_17
      type: wnut_17
      args: wnut_17
    metrics:
    - name: Precision
      type: precision
      value: 0.7205240174672489
    - name: Recall
      type: recall
      value: 0.5921052631578947
    - name: F1
      type: f1
      value: 0.650032829940906
    - name: Accuracy
      type: accuracy
      value: 0.9619810541038846
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# funnel-transformer-xlarge_ner_wnut_17

This model is a fine-tuned version of [funnel-transformer/xlarge](https://huggingface.co/funnel-transformer/xlarge) on the wnut_17 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2453
- Precision: 0.7205
- Recall: 0.5921
- F1: 0.6500
- Accuracy: 0.9620

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
| No log        | 1.0   | 213  | 0.2331          | 0.6897    | 0.4067 | 0.5117 | 0.9462   |
| No log        | 2.0   | 426  | 0.2056          | 0.7097    | 0.5526 | 0.6214 | 0.9587   |
| 0.1454        | 3.0   | 639  | 0.2379          | 0.7102    | 0.5658 | 0.6298 | 0.9600   |
| 0.1454        | 4.0   | 852  | 0.2397          | 0.7141    | 0.5885 | 0.6452 | 0.9620   |
| 0.0319        | 5.0   | 1065 | 0.2453          | 0.7205    | 0.5921 | 0.6500 | 0.9620   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
