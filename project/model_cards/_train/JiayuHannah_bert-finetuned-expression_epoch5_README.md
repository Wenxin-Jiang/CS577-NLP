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
- name: bert-finetuned-expression_epoch5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-expression_epoch5

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5897
- Precision: 0.5835
- Recall: 0.5688
- F1: 0.5760
- Accuracy: 0.8344

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 218  | 0.5185          | 0.5076    | 0.5034 | 0.5055 | 0.8207   |
| No log        | 2.0   | 436  | 0.4972          | 0.4948    | 0.5638 | 0.5271 | 0.8177   |
| 0.5193        | 3.0   | 654  | 0.5128          | 0.5838    | 0.5554 | 0.5692 | 0.8390   |
| 0.5193        | 4.0   | 872  | 0.5665          | 0.5612    | 0.6074 | 0.5834 | 0.8224   |
| 0.2063        | 5.0   | 1090 | 0.5897          | 0.5835    | 0.5688 | 0.5760 | 0.8344   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
