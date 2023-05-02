---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bert2bert_shared-spanish-finetuned-summarization-intento2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert2bert_shared-spanish-finetuned-summarization-intento2

This model is a fine-tuned version of [mrm8488/bert2bert_shared-spanish-finetuned-summarization](https://huggingface.co/mrm8488/bert2bert_shared-spanish-finetuned-summarization) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 7.9693
- Rouge1: 1.8257
- Rouge2: 0.0
- Rougel: 1.6832
- Rougelsum: 1.6866
- Gen Len: 10.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| 7.9999        | 1.0   | 6180  | 7.9915          | 1.5443 | 0.0    | 1.4357 | 1.4377    | 10.0    |
| 7.9469        | 2.0   | 12360 | 7.9693          | 1.8257 | 0.0    | 1.6832 | 1.6866    | 10.0    |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
