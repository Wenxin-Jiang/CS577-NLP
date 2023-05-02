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
- name: bert-base-uncased-finetuned-ner-kmeans
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-ner-kmeans

This model is a fine-tuned version of [ArBert/bert-base-uncased-finetuned-ner](https://huggingface.co/ArBert/bert-base-uncased-finetuned-ner) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1169
- Precision: 0.9084
- Recall: 0.9245
- F1: 0.9164
- Accuracy: 0.9792

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.036         | 1.0   | 1123 | 0.1010          | 0.9086    | 0.9117 | 0.9101 | 0.9779   |
| 0.0214        | 2.0   | 2246 | 0.1094          | 0.9033    | 0.9199 | 0.9115 | 0.9784   |
| 0.014         | 3.0   | 3369 | 0.1169          | 0.9084    | 0.9245 | 0.9164 | 0.9792   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
