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
- name: distilbert-base-uncased-finetuned-ner-invoiceSenderName1912
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner-invoiceSenderName1912

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4109
- Precision: 0.0
- Recall: 0.0
- F1: 0.0
- Accuracy: 0.9669

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
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1  | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:---:|:--------:|
| No log        | 1.0   | 1    | 0.6428          | 0.0       | 0.0    | 0.0 | 0.7603   |
| No log        | 2.0   | 2    | 0.5174          | 0.0       | 0.0    | 0.0 | 0.9421   |
| No log        | 3.0   | 3    | 0.4444          | 0.0       | 0.0    | 0.0 | 0.9669   |
| No log        | 4.0   | 4    | 0.4109          | 0.0       | 0.0    | 0.0 | 0.9669   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0
- Datasets 2.3.2
- Tokenizers 0.10.3
