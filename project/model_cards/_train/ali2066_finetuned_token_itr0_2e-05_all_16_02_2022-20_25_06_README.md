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
- name: finetuned_token_itr0_2e-05_all_16_02_2022-20_25_06
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_2e-05_all_16_02_2022-20_25_06

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1778
- Precision: 0.3270
- Recall: 0.3348
- F1: 0.3309
- Accuracy: 0.9439

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 38   | 0.4023          | 0.1050    | 0.2331 | 0.1448 | 0.8121   |
| No log        | 2.0   | 76   | 0.3629          | 0.1856    | 0.3414 | 0.2405 | 0.8368   |
| No log        | 3.0   | 114  | 0.3329          | 0.1794    | 0.3594 | 0.2394 | 0.8504   |
| No log        | 4.0   | 152  | 0.3261          | 0.1786    | 0.3684 | 0.2405 | 0.8503   |
| No log        | 5.0   | 190  | 0.3244          | 0.1872    | 0.3684 | 0.2482 | 0.8534   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
