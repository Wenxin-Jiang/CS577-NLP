---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-distilled-multi_teacher_avg_logit_twitter_sentiment_07_alpha0.8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-distilled-multi_teacher_avg_logit_twitter_sentiment_07_alpha0.8

This model is a fine-tuned version of [ArafatBHossain/distilbert-base-uncased-twitter_eval_sentiment_data](https://huggingface.co/ArafatBHossain/distilbert-base-uncased-twitter_eval_sentiment_data) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3250
- Accuracy: 0.671

## Model description

More information needed

## Intended uses & limitations

More information needed

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
- num_epochs: 7
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.4044        | 1.0   | 1875  | 0.3820          | 0.6655   |
| 0.2636        | 2.0   | 3750  | 0.3914          | 0.668    |
| 0.206         | 3.0   | 5625  | 0.3595          | 0.6655   |
| 0.1694        | 4.0   | 7500  | 0.3548          | 0.6725   |
| 0.1437        | 5.0   | 9375  | 0.3360          | 0.6725   |
| 0.1272        | 6.0   | 11250 | 0.3259          | 0.6755   |
| 0.1167        | 7.0   | 13125 | 0.3250          | 0.671    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
