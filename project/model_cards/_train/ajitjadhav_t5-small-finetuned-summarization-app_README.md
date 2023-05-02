---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
metrics:
- rouge
model-index:
- name: t5-small-finetuned-summarization-app
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      config: 3.0.0
      split: train
      args: 3.0.0
    metrics:
    - name: Rouge1
      type: rouge
      value: 24.5589
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-summarization-app

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6614
- Rouge1: 24.5589
- Rouge2: 11.8509
- Rougel: 20.3011
- Rougelsum: 23.1768
- Gen Len: 19.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 12
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.8267        | 1.0   | 23927 | 1.6689          | 24.4634 | 11.7413 | 20.2154 | 23.0875   | 18.9993 |
| 1.81          | 2.0   | 47854 | 1.6614          | 24.5589 | 11.8509 | 20.3011 | 23.1768   | 19.0    |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
