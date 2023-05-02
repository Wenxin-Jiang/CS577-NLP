---
license: apache-2.0
tags:
- summarisation
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bert-small2bert-small-finetuned-cnn_daily_mail-summarization-finetuned-bbc-news-Sumy
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-small2bert-small-finetuned-cnn_daily_mail-summarization-finetuned-bbc-news-Sumy

This model is a fine-tuned version of [mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization](https://huggingface.co/mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5583
- Rouge1: 55.2899
- Rouge2: 43.2426
- Rougel: 38.5056
- Rougelsum: 53.8807

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 1.7407        | 1.0   | 223  | 1.5900          | 51.3058 | 38.3952 | 35.7343 | 49.7129   |
| 1.4813        | 2.0   | 446  | 1.5500          | 53.8089 | 41.2455 | 37.3864 | 52.3387   |
| 1.3517        | 3.0   | 669  | 1.5429          | 53.4914 | 40.907  | 37.1428 | 52.0338   |
| 1.2432        | 4.0   | 892  | 1.5472          | 54.1139 | 41.3589 | 37.6392 | 52.711    |
| 1.1748        | 5.0   | 1115 | 1.5426          | 55.3482 | 43.312  | 38.0625 | 54.0424   |
| 1.1108        | 6.0   | 1338 | 1.5529          | 55.4752 | 43.3561 | 38.5813 | 54.1141   |
| 1.0745        | 7.0   | 1561 | 1.5539          | 55.705  | 43.6772 | 38.7629 | 54.3892   |
| 1.0428        | 8.0   | 1784 | 1.5583          | 55.2899 | 43.2426 | 38.5056 | 53.8807   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
