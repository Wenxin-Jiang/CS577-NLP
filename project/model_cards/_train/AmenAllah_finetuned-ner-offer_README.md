---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- data_set
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: finetuned-ner-offer
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: data_set
      type: data_set
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.2254335260115607
    - name: Recall
      type: recall
      value: 0.24528301886792453
    - name: F1
      type: f1
      value: 0.23493975903614459
    - name: Accuracy
      type: accuracy
      value: 0.9209345919528688
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-ner-offer

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the data_set dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3242
- Precision: 0.2254
- Recall: 0.2453
- F1: 0.2349
- Accuracy: 0.9209

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 100  | 0.3344          | 0.2162    | 0.2013 | 0.2085 | 0.9217   |
| No log        | 2.0   | 200  | 0.3167          | 0.1804    | 0.2201 | 0.1983 | 0.9204   |
| No log        | 3.0   | 300  | 0.3242          | 0.2254    | 0.2453 | 0.2349 | 0.9209   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
