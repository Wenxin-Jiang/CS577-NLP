---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: 8Agos
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 8Agos

This model is a fine-tuned version of [xlm-roberta-large-finetuned-conll03-english](https://huggingface.co/xlm-roberta-large-finetuned-conll03-english) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1416
- Precision: 0.7659
- Recall: 0.7986
- F1: 0.7819
- Accuracy: 0.9640

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
| No log        | 1.0   | 176  | 0.1571          | 0.7362    | 0.7788 | 0.7569 | 0.9593   |
| No log        | 2.0   | 352  | 0.1416          | 0.7529    | 0.7831 | 0.7677 | 0.9624   |
| 0.1109        | 3.0   | 528  | 0.1416          | 0.7659    | 0.7986 | 0.7819 | 0.9640   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
