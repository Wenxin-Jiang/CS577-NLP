---
tags:
- generated_from_trainer
model-index:
- name: t5-shakespearify-lite
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-shakespearify-lite

This model was trained from the t5 checkpoint on a custom dataset from [Shakescleare](https://www.litcharts.com/shakescleare/shakespeare-translations). This is a website shakespeare's works have been translated to modern english. This model idealizes style transforms as a translation process as we use the original english as a final translation. The dataset is available on [Kaggle](https://www.kaggle.com/datasets/garnavaurha/shakespearify).

## Model description

The model was trained for 5 epochs with a subset of the dataset. The subset was only about 10k examples long out of the over 50k examples in the raw dataset.

## Intended uses & limitations

This is a novelty project intended for playing around with. However, it has its limitations since it is translating english to english with some minor tweaks. These tweaks maybe changing sentence structure or minor word substitution. It works best unsurprisingly on story based excerpts like below.
```
translate: Why have you come to Mr. Smith with this crap?
```
 

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Tokenizers 0.12.1
