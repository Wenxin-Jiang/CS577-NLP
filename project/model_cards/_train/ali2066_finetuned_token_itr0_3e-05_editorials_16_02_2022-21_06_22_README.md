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
- name: finetuned_token_itr0_3e-05_editorials_16_02_2022-21_06_22
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_3e-05_editorials_16_02_2022-21_06_22

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1060
- Precision: 0.2003
- Recall: 0.1154
- F1: 0.1464
- Accuracy: 0.9712

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 15   | 0.0897          | 0.08      | 0.0110 | 0.0193 | 0.9801   |
| No log        | 2.0   | 30   | 0.0798          | 0.08      | 0.0110 | 0.0193 | 0.9801   |
| No log        | 3.0   | 45   | 0.0743          | 0.08      | 0.0110 | 0.0193 | 0.9801   |
| No log        | 4.0   | 60   | 0.0707          | 0.0741    | 0.0110 | 0.0191 | 0.9802   |
| No log        | 5.0   | 75   | 0.0696          | 0.2727    | 0.1648 | 0.2055 | 0.9805   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
