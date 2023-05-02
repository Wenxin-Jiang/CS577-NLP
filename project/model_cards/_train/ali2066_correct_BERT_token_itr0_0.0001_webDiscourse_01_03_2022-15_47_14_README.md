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
- name: correct_BERT_token_itr0_0.0001_webDiscourse_01_03_2022-15_47_14
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# correct_BERT_token_itr0_0.0001_webDiscourse_01_03_2022-15_47_14

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6542
- Precision: 0.0092
- Recall: 0.0403
- F1: 0.0150
- Accuracy: 0.7291

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 10   | 0.5856          | 0.0012    | 0.0125 | 0.0022 | 0.6950   |
| No log        | 2.0   | 20   | 0.5933          | 0.0       | 0.0    | 0.0    | 0.7282   |
| No log        | 3.0   | 30   | 0.5729          | 0.0051    | 0.025  | 0.0085 | 0.7155   |
| No log        | 4.0   | 40   | 0.6178          | 0.0029    | 0.0125 | 0.0047 | 0.7143   |
| No log        | 5.0   | 50   | 0.6707          | 0.0110    | 0.0375 | 0.0170 | 0.7178   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
