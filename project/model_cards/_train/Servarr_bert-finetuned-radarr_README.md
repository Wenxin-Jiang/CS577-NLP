---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- movie_releases
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-radarr
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: movie_releases
      type: movie_releases
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.9555421444377389
    - name: Recall
      type: recall
      value: 0.9638798701298701
    - name: F1
      type: f1
      value: 0.9596928982725529
    - name: Accuracy
      type: accuracy
      value: 0.9817602584524263
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-radarr

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the movie_releases dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0731
- Precision: 0.9555
- Recall: 0.9639
- F1: 0.9597
- Accuracy: 0.9818

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
| 0.0431        | 1.0   | 1191 | 0.1403          | 0.9436    | 0.9574 | 0.9504 | 0.9626   |
| 0.0236        | 2.0   | 2382 | 0.0881          | 0.9485    | 0.9560 | 0.9522 | 0.9694   |
| 0.0138        | 3.0   | 3573 | 0.0731          | 0.9555    | 0.9639 | 0.9597 | 0.9818   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
