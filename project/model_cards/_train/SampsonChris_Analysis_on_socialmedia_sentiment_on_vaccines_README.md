---
tags:
- generated_from_trainer
model-index:
- name: Analysis_on_socialmedia_sentiment_on_vaccines
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Analysis_on_socialmedia_sentiment_on_vaccines

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.6998
- eval_accuracy: 0.713
- eval_runtime: 64.2098
- eval_samples_per_second: 31.148
- eval_steps_per_second: 3.893
- step: 0

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
- num_epochs: 1

### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
