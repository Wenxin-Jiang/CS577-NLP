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
- name: bert-finetuned-propaganda-18
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-propaganda-18

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6542
- Precision: 0.0924
- Recall: 0.0470
- F1: 0.0623
- Accuracy: 0.8836

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
| 0.6679        | 1.0   | 670  | 0.7379          | 0.125     | 0.0035 | 0.0069 | 0.8868   |
| 0.548         | 2.0   | 1340 | 0.5916          | 0.0845    | 0.0435 | 0.0574 | 0.8831   |
| 0.3781        | 3.0   | 2010 | 0.6542          | 0.0924    | 0.0470 | 0.0623 | 0.8836   |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
