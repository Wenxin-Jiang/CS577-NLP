---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- precision
- recall
- accuracy
- f1
model-index:
- name: distilbert-base-uncased-finetuned-sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      config: sst2
      split: train
      args: sst2
    metrics:
    - name: Precision
      type: precision
      value: 0.9038031319910514
    - name: Recall
      type: recall
      value: 0.9099099099099099
    - name: Accuracy
      type: accuracy
      value: 0.9048165137614679
    - name: F1
      type: f1
      value: 0.9068462401795736
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-sst2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5776
- Precision: 0.9038
- Recall: 0.9099
- Accuracy: 0.9048
- F1: 0.9068

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

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:--------:|:------:|
| 0.0237        | 1.0   | 4210  | 0.6639          | 0.8685    | 0.9369 | 0.8956   | 0.9014 |
| 0.0247        | 2.0   | 8420  | 0.5776          | 0.9038    | 0.9099 | 0.9048   | 0.9068 |
| 0.0304        | 3.0   | 12630 | 0.6533          | 0.8839    | 0.9257 | 0.9002   | 0.9043 |
| 0.0281        | 4.0   | 16840 | 0.6654          | 0.8877    | 0.9257 | 0.9025   | 0.9063 |
| 0.0095        | 5.0   | 21050 | 0.7832          | 0.8710    | 0.9279 | 0.8933   | 0.8986 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
