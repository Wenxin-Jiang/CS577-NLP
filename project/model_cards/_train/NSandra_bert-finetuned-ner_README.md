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
- name: bert-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5658
- Precision: 1.0
- Recall: 1.0
- F1: 1.0
- Accuracy: 1.0

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1  | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:---:|:--------:|
| No log        | 1.0   | 1    | 2.8381          | 1.0       | 1.0    | 1.0 | 1.0      |
| No log        | 2.0   | 2    | 2.6555          | 1.0       | 1.0    | 1.0 | 1.0      |
| No log        | 3.0   | 3    | 2.5658          | 1.0       | 1.0    | 1.0 | 1.0      |


### Framework versions

- Transformers 4.27.4
- Pytorch 2.0.0+cu118
- Datasets 2.11.0
- Tokenizers 0.13.3
