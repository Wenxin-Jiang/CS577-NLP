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
- name: twitter_RoBERTa_token_itr0_1e-05_all_01_03_2022-14_37_35
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter_RoBERTa_token_itr0_1e-05_all_01_03_2022-14_37_35

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3190
- Precision: 0.1194
- Recall: 0.2563
- F1: 0.1629
- Accuracy: 0.8546

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 30   | 0.4963          | 0.0223    | 0.0562 | 0.0319 | 0.7461   |
| No log        | 2.0   | 60   | 0.4089          | 0.0617    | 0.1359 | 0.0849 | 0.8093   |
| No log        | 3.0   | 90   | 0.3919          | 0.1053    | 0.2101 | 0.1403 | 0.8219   |
| No log        | 4.0   | 120  | 0.3787          | 0.1202    | 0.2482 | 0.1619 | 0.8270   |
| No log        | 5.0   | 150  | 0.3745          | 0.1171    | 0.2391 | 0.1572 | 0.8311   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
