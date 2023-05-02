---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pawsx
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-multilingual-cased-finetuned-similarite
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: pawsx
      type: pawsx
      args: fr
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7995
    - name: F1
      type: f1
      value: 0.7994565743967147
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-multilingual-cased-finetuned-similarite

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on the pawsx dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4781
- Accuracy: 0.7995
- F1: 0.7995

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.5343        | 1.0   | 772  | 0.4879          | 0.7705   | 0.7714 |
| 0.3523        | 2.0   | 1544 | 0.4781          | 0.7995   | 0.7995 |


### Framework versions

- Transformers 4.19.3
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
