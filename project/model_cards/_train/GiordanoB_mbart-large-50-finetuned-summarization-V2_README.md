---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mbart-large-50-finetuned-summarization-V2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-50-finetuned-summarization-V2

This model is a fine-tuned version of [facebook/mbart-large-50](https://huggingface.co/facebook/mbart-large-50) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9183
- Rouge1: 50.0118
- Rouge2: 31.3168
- Rougel: 37.6392
- Rougelsum: 45.2287
- Gen Len: 102.3571

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len  |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:--------:|
| No log        | 1.0   | 15   | 2.0228          | 51.9711 | 32.5963 | 39.9154 | 48.3431   | 134.6429 |
| No log        | 2.0   | 30   | 1.9410          | 48.2977 | 30.5942 | 35.9761 | 43.7634   | 92.0714  |
| No log        | 3.0   | 45   | 1.9183          | 50.0118 | 31.3168 | 37.6392 | 45.2287   | 102.3571 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
