---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: Setfit-finetuned-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Setfit-finetuned-classifier

This model is a fine-tuned version of [Kuaaangwen/Setfit-few-shot-classifier](https://huggingface.co/Kuaaangwen/Setfit-few-shot-classifier) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3147
- Accuracy: 0.9854

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 69   | 2.6990          | 0.8832   |
| No log        | 2.0   | 138  | 2.3147          | 0.9854   |
| No log        | 3.0   | 207  | 2.0378          | 0.9489   |
| No log        | 4.0   | 276  | 1.8422          | 0.9635   |
| No log        | 5.0   | 345  | 1.6889          | 0.9781   |
| No log        | 6.0   | 414  | 1.5720          | 0.9708   |
| No log        | 7.0   | 483  | 1.4913          | 0.9781   |
| 2.0817        | 8.0   | 552  | 1.4335          | 0.9708   |
| 2.0817        | 9.0   | 621  | 1.3979          | 0.9781   |
| 2.0817        | 10.0  | 690  | 1.3872          | 0.9854   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
