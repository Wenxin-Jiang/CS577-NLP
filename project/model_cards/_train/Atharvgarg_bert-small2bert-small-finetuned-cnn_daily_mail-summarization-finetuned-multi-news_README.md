---
license: apache-2.0
tags:
- summarisation
- generated_from_trainer
datasets:
- multi_news
metrics:
- rouge
model-index:
- name: bert-small2bert-small-finetuned-cnn_daily_mail-summarization-finetuned-multi-news
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: multi_news
      type: multi_news
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 38.9616
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-small2bert-small-finetuned-cnn_daily_mail-summarization-finetuned-multi-news

This model is a fine-tuned version of [mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization](https://huggingface.co/mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization) on the multi_news dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0185
- Rouge1: 38.9616
- Rouge2: 14.1539
- Rougel: 21.1788
- Rougelsum: 35.314

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 3.3679        | 1.0   | 11243 | 3.1314          | 38.4459 | 13.7777 | 20.8772 | 34.8321   |
| 3.1115        | 2.0   | 22486 | 3.0589          | 38.7419 | 13.9355 | 20.9911 | 35.0988   |
| 2.9826        | 3.0   | 33729 | 3.0311          | 38.7345 | 14.0365 | 21.0571 | 35.1604   |
| 2.8986        | 4.0   | 44972 | 3.0185          | 38.9616 | 14.1539 | 21.1788 | 35.314    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
