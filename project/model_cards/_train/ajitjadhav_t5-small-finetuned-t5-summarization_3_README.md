---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
metrics:
- rouge
model-index:
- name: t5-small-finetuned-t5-summarization_3
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
      value: 24.4517
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-t5-summarization_3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8102
- Rouge1: 24.4517
- Rouge2: 11.7161
- Rougel: 20.205
- Rougelsum: 23.053
- Gen Len: 18.9999

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.0073        | 1.0   | 17945 | 1.8144          | 24.4341 | 11.7155 | 20.1969 | 23.0364   | 18.9999 |
| 1.9855        | 2.0   | 35890 | 1.8102          | 24.4517 | 11.7161 | 20.205  | 23.053    | 18.9999 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
