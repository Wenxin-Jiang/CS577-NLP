---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: pegasus-xsum-whole_summary_chatGPT_and_tweetsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-xsum-whole_summary_chatGPT_and_tweetsum

This model is a fine-tuned version of [google/pegasus-xsum](https://huggingface.co/google/pegasus-xsum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4139
- Rouge1: 27.4412
- Rouge2: 10.8393
- Rougel: 25.1988
- Rougelsum: 25.2193
- Gen Len: 14.3333

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 381  | 2.5524          | 26.025  | 9.5118  | 22.8243 | 22.8505   | 15.8095 |
| 2.9387        | 2.0   | 762  | 2.4394          | 29.4773 | 11.7365 | 27.6403 | 27.7766   | 15.4286 |
| 2.2822        | 3.0   | 1143 | 2.4139          | 27.4412 | 10.8393 | 25.1988 | 25.2193   | 14.3333 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.2
