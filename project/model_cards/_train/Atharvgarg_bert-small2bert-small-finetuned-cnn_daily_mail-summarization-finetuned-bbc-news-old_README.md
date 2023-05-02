---
license: apache-2.0
tags:
- summarisation
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bert-small2bert-small-finetuned-cnn_daily_mail-summarization-finetuned-bbc-news-old
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-small2bert-small-finetuned-cnn_daily_mail-summarization-finetuned-bbc-news-old

This model is a fine-tuned version of [mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization](https://huggingface.co/mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6733
- Rouge1: 60.9431
- Rouge2: 49.8688
- Rougel: 42.4663
- Rougelsum: 59.836

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
| 0.8246        | 1.0   | 223  | 0.6974          | 55.2742 | 41.9883 | 37.8584 | 53.7602   |
| 0.6396        | 2.0   | 446  | 0.6786          | 56.0006 | 43.1917 | 38.5125 | 54.4571   |
| 0.5582        | 3.0   | 669  | 0.6720          | 57.8912 | 45.7807 | 40.0807 | 56.4985   |
| 0.505         | 4.0   | 892  | 0.6659          | 59.6611 | 48.0095 | 41.752  | 58.5059   |
| 0.4611        | 5.0   | 1115 | 0.6706          | 59.7241 | 48.164  | 41.4523 | 58.5295   |
| 0.4254        | 6.0   | 1338 | 0.6711          | 59.8524 | 48.1821 | 41.2299 | 58.6072   |
| 0.3967        | 7.0   | 1561 | 0.6718          | 60.3009 | 49.0085 | 42.0306 | 59.0723   |
| 0.38          | 8.0   | 1784 | 0.6733          | 60.9431 | 49.8688 | 42.4663 | 59.836    |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
