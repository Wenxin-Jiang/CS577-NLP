---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- klue
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: koelectra-base-v3-discriminator-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: klue
      type: klue
      args: ner
    metrics:
    - name: Precision
      type: precision
      value: 0.6665182546749777
    - name: Recall
      type: recall
      value: 0.7350073648032546
    - name: F1
      type: f1
      value: 0.6990893625537877
    - name: Accuracy
      type: accuracy
      value: 0.9395764497172635
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# koelectra-base-v3-discriminator-finetuned-ner

This model is a fine-tuned version of [monologg/koelectra-base-v3-discriminator](https://huggingface.co/monologg/koelectra-base-v3-discriminator) on the klue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1957
- Precision: 0.6665
- Recall: 0.7350
- F1: 0.6991
- Accuracy: 0.9396

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
- train_batch_size: 48
- eval_batch_size: 48
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 438  | 0.2588          | 0.5701    | 0.6655 | 0.6141 | 0.9212   |
| 0.4333        | 2.0   | 876  | 0.2060          | 0.6671    | 0.7134 | 0.6895 | 0.9373   |
| 0.1944        | 3.0   | 1314 | 0.1957          | 0.6665    | 0.7350 | 0.6991 | 0.9396   |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.12.0+cu102
- Datasets 1.14.0
- Tokenizers 0.10.3
