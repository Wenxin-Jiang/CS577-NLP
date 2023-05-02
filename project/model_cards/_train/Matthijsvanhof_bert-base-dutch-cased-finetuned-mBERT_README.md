---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-base-dutch-cased-finetuned-mBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-dutch-cased-finetuned-mBERT

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0898
- Precision: 0.7255
- Recall: 0.7255
- F1: 0.7255
- Accuracy: 0.9758

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1603        | 1.0   | 533  | 0.0928          | 0.6896    | 0.6962 | 0.6929 | 0.9742   |
| 0.0832        | 2.0   | 1066 | 0.0898          | 0.7255    | 0.7255 | 0.7255 | 0.9758   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Tokenizers 0.10.3
