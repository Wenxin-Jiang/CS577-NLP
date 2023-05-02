---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-finetuned-fin
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-fin

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3931
- Accuracy: 0.8873
- F1: 0.8902

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
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.6478        | 1.0   | 134  | 0.4118          | 0.8293   | 0.8309 |
| 0.3304        | 2.0   | 268  | 0.3315          | 0.8653   | 0.8694 |
| 0.2221        | 3.0   | 402  | 0.3229          | 0.8756   | 0.8781 |
| 0.1752        | 4.0   | 536  | 0.3192          | 0.8891   | 0.8921 |
| 0.1457        | 5.0   | 670  | 0.3700          | 0.8840   | 0.8880 |
| 0.1315        | 6.0   | 804  | 0.3774          | 0.8854   | 0.8882 |
| 0.1172        | 7.0   | 938  | 0.3883          | 0.8849   | 0.8877 |
| 0.112         | 8.0   | 1072 | 0.3931          | 0.8873   | 0.8902 |


### Framework versions

- Transformers 4.26.0
- Pytorch 1.13.1+cu116
- Datasets 2.9.0
- Tokenizers 0.13.2
