---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: fine-tune-bert-chinese-sent-analysis-movies-sample-new
  results: []
---

# fine-tune-bert-chinese-sent-analysis-movies-sample-new

This model is a fine-tuned version of [bert-base-chinese](https://huggingface.co/bert-base-chinese) on the 14190 samples of the [Douban Movies Short Comments](https://www.kaggle.com/datasets/utmhikari/doubanmovieshortcomments) from [Kaggle](https://www.kaggle.com).

[Douban.com](https://en.wikipedia.org/wiki/Douban#:~:text=Douban.com%20(Chinese%3A%20%E8%B1%86%E7%93%A3,and%20activities%20in%20Chinese%20cities.) (Chinese: 豆瓣; pinyin: Dòubàn), launched on 6 March 2005, is a Chinese social networking service website that allows registered users to record information and create content related to film, books, music, recent events, and activities in Chinese cities.

It achieves the following results on the evaluation set of 6082 samples:
- Loss: 0.5694
- Accuracy: 0.7328
- F1: 0.6534

## Model description

Label_0 - negative, Label_1 - positive

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

The dataset has 1-5 values for 'Stars'. But, to reduce the number of labels, 1,2,3 stars were assigned a negative label (0) and 4,5 were assigned a positive label(1).

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results



### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1
