---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-base-finetuned-emo20q-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-finetuned-emo20q-classification

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3759
- Rouge1: 70.3125
- Rouge2: 0.0
- Rougel: 70.2083
- Rougelsum: 70.2083
- Gen Len: 2.0

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
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 280  | 0.3952          | 68.3333 | 0.0    | 68.2292 | 68.2812   | 2.0     |
| 0.7404        | 2.0   | 560  | 0.3774          | 70.1042 | 0.0    | 70.1042 | 70.1042   | 2.0     |
| 0.7404        | 3.0   | 840  | 0.3759          | 70.3125 | 0.0    | 70.2083 | 70.2083   | 2.0     |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
