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
- name: finetuned_token_itr0_0.0002_webDiscourse_16_02_2022-21_00_50
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_0.0002_webDiscourse_16_02_2022-21_00_50

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5530
- Precision: 0.0044
- Recall: 0.0182
- F1: 0.0071
- Accuracy: 0.7268

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 10   | 0.7051          | 0.0645    | 0.0323 | 0.0430 | 0.4465   |
| No log        | 2.0   | 20   | 0.6928          | 0.0476    | 0.0161 | 0.0241 | 0.5546   |
| No log        | 3.0   | 30   | 0.6875          | 0.0069    | 0.0484 | 0.0120 | 0.5533   |
| No log        | 4.0   | 40   | 0.6966          | 0.0064    | 0.0323 | 0.0107 | 0.5832   |
| No log        | 5.0   | 50   | 0.7093          | 0.0061    | 0.0323 | 0.0102 | 0.5742   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
