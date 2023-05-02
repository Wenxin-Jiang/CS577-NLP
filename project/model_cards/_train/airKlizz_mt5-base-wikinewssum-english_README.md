---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-wikinewssum-english
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-wikinewssum-english

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3040
- Rouge1: 8.9565
- Rouge2: 3.6563
- Rougel: 7.1346
- Rougelsum: 8.3802

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| No log        | 1.0   | 1010 | 2.4360          | 8.7287 | 3.5817 | 7.0093 | 8.1879    |
| No log        | 2.0   | 2020 | 2.3922          | 8.7227 | 3.5385 | 6.96   | 8.1887    |
| No log        | 3.0   | 3030 | 2.3422          | 8.8565 | 3.5772 | 7.0203 | 8.2957    |
| No log        | 4.0   | 4040 | 2.3288          | 8.89   | 3.645  | 7.0602 | 8.3314    |
| 3.1253        | 5.0   | 5050 | 2.3209          | 8.868  | 3.6109 | 7.0537 | 8.299     |
| 3.1253        | 6.0   | 6060 | 2.3127          | 8.9488 | 3.6615 | 7.1044 | 8.3785    |
| 3.1253        | 7.0   | 7070 | 2.3056          | 8.9366 | 3.6507 | 7.1338 | 8.3615    |
| 3.1253        | 8.0   | 8080 | 2.3040          | 8.9565 | 3.6563 | 7.1346 | 8.3802    |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
