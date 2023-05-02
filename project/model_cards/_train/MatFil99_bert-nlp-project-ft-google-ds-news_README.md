---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-nlp-project-ft-google-ds-news
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-nlp-project-ft-google-ds-news

This model is a fine-tuned version of [jestemleon/bert-nlp-project-google](https://huggingface.co/jestemleon/bert-nlp-project-google) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4440
- Accuracy: 0.8938
- F1: 0.8717

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.3989        | 0.37  | 120  | 0.3025          | 0.875    | 0.8444 |
| 0.3088        | 0.75  | 240  | 0.3063          | 0.8812   | 0.8577 |
| 0.2669        | 1.12  | 360  | 0.3307          | 0.9      | 0.8801 |
| 0.2058        | 1.5   | 480  | 0.3502          | 0.9      | 0.8769 |
| 0.1626        | 1.87  | 600  | 0.3725          | 0.8953   | 0.8719 |
| 0.1526        | 2.24  | 720  | 0.3813          | 0.8969   | 0.875  |
| 0.0992        | 2.62  | 840  | 0.4399          | 0.8953   | 0.8738 |
| 0.101         | 2.99  | 960  | 0.4440          | 0.8938   | 0.8717 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
