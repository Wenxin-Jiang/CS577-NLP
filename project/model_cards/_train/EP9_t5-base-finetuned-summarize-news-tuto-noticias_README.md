---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-base-finetuned-summarize-news-tuto-noticias
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-finetuned-summarize-news-tuto-noticias

This model is a fine-tuned version of [mrm8488/t5-base-finetuned-summarize-news](https://huggingface.co/mrm8488/t5-base-finetuned-summarize-news) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1414
- Rouge1: 0.3108
- Rouge2: 0.2066
- Rougel: 0.3003
- Rougelsum: 0.3004

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 1.3374        | 1.0   | 6034 | 1.1414          | 0.3108 | 0.2066 | 0.3003 | 0.3004    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
