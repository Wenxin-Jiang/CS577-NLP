---
license: apache-2.0
tags:
- summarisation
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bert-small2bert-small-finetuned-cnn_daily_mail-summarization-finetuned-bbc-news
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-small2bert-small-finetuned-cnn_daily_mail-summarization-finetuned-bbc-news

This model is a fine-tuned version of [mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization](https://huggingface.co/mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6835
- Rouge1: 58.9345
- Rouge2: 47.1037
- Rougel: 40.9839
- Rougelsum: 57.6981

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
| 0.8246        | 1.0   | 223  | 0.7050          | 55.7882 | 42.9793 | 38.4511 | 54.3125   |
| 0.6414        | 2.0   | 446  | 0.6834          | 55.149  | 42.664  | 38.3864 | 53.7712   |
| 0.5603        | 3.0   | 669  | 0.6815          | 56.9756 | 44.8057 | 39.1377 | 55.5815   |
| 0.5079        | 4.0   | 892  | 0.6749          | 57.7397 | 45.6267 | 40.0509 | 56.3886   |
| 0.4622        | 5.0   | 1115 | 0.6781          | 58.07   | 45.9102 | 40.2704 | 56.7008   |
| 0.4263        | 6.0   | 1338 | 0.6798          | 58.1215 | 45.976  | 40.256  | 56.8203   |
| 0.399         | 7.0   | 1561 | 0.6798          | 58.5486 | 46.6901 | 40.8045 | 57.2947   |
| 0.3815        | 8.0   | 1784 | 0.6835          | 58.9345 | 47.1037 | 40.9839 | 57.6981   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
