---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- indonlu
metrics:
- accuracy
- f1
model-index:
- name: indobert-distilled-optimized-for-classification
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: indonlu
      type: indonlu
      args: smsa
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9023809523809524
    - name: F1
      type: f1
      value: 0.9020516403647337
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indobert-distilled-optimized-for-classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the indonlu dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5991
- Accuracy: 0.9024
- F1: 0.9021

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.262995179171344e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 33
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 1.2938        | 1.0   | 688  | 0.8433          | 0.8484   | 0.8513 |
| 0.711         | 2.0   | 1376 | 0.6408          | 0.8881   | 0.8878 |
| 0.4416        | 3.0   | 2064 | 0.7964          | 0.8794   | 0.8793 |
| 0.2907        | 4.0   | 2752 | 0.7559          | 0.8897   | 0.8900 |
| 0.2065        | 5.0   | 3440 | 0.6892          | 0.8968   | 0.8974 |
| 0.1574        | 6.0   | 4128 | 0.6881          | 0.8913   | 0.8906 |
| 0.1131        | 7.0   | 4816 | 0.6224          | 0.8984   | 0.8982 |
| 0.0865        | 8.0   | 5504 | 0.6312          | 0.8976   | 0.8970 |
| 0.0678        | 9.0   | 6192 | 0.6187          | 0.8992   | 0.8989 |
| 0.0526        | 10.0  | 6880 | 0.5991          | 0.9024   | 0.9021 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
