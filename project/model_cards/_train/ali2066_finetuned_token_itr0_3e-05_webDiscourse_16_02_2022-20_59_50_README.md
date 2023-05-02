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
- name: finetuned_token_itr0_3e-05_webDiscourse_16_02_2022-20_59_50
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_3e-05_webDiscourse_16_02_2022-20_59_50

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5450
- Precision: 0.0049
- Recall: 0.0146
- F1: 0.0074
- Accuracy: 0.7431

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
| No log        | 1.0   | 10   | 0.6830          | 0.0109    | 0.0323 | 0.0163 | 0.5685   |
| No log        | 2.0   | 20   | 0.7187          | 0.0256    | 0.0323 | 0.0286 | 0.5668   |
| No log        | 3.0   | 30   | 0.6839          | 0.0076    | 0.0484 | 0.0131 | 0.5848   |
| No log        | 4.0   | 40   | 0.6988          | 0.0092    | 0.0484 | 0.0155 | 0.5918   |
| No log        | 5.0   | 50   | 0.7055          | 0.0100    | 0.0484 | 0.0165 | 0.5946   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
