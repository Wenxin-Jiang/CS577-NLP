---
license: apache-2.0
tags:
- summarisation
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bert-small2bert-small-finetuned-cnn_daily_mail-summarization-finetuned-bbc-news-extracted-sumy
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-small2bert-small-finetuned-cnn_daily_mail-summarization-finetuned-bbc-news-extracted-sumy

This model is a fine-tuned version of [mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization](https://huggingface.co/mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3228
- Rouge1: 56.5706
- Rouge2: 43.0906
- Rougel: 47.9957
- Rougelsum: 53.417

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
| 0.3226        | 1.0   | 223  | 0.3225          | 55.7639 | 41.9414 | 46.9804 | 52.5639   |
| 0.262         | 2.0   | 446  | 0.3198          | 55.7522 | 42.0929 | 46.8388 | 52.6659   |
| 0.2153        | 3.0   | 669  | 0.3195          | 55.7091 | 42.2111 | 47.2641 | 52.5765   |
| 0.1805        | 4.0   | 892  | 0.3164          | 55.8115 | 42.5536 | 47.3529 | 52.7672   |
| 0.1527        | 5.0   | 1115 | 0.3203          | 56.8658 | 43.4238 | 48.2268 | 53.8136   |
| 0.14          | 6.0   | 1338 | 0.3234          | 55.7138 | 41.8562 | 46.8362 | 52.5201   |
| 0.1252        | 7.0   | 1561 | 0.3228          | 56.5706 | 43.0906 | 47.9957 | 53.417    |
| 0.1229        | 8.0   | 1784 | 0.3228          | 56.5706 | 43.0906 | 47.9957 | 53.417    |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
