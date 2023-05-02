---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-wikinewssum-english-1000
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-wikinewssum-english-1000

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4724
- Rouge1: 7.7389
- Rouge2: 3.1606
- Rougel: 6.3317
- Rougelsum: 7.2487

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
| No log        | 1.0   | 125  | 2.6981          | 7.1504 | 2.6253 | 5.8261 | 6.7427    |
| No log        | 2.0   | 250  | 2.5597          | 7.4666 | 2.9362 | 6.0965 | 6.9699    |
| No log        | 3.0   | 375  | 2.5145          | 7.4599 | 2.9449 | 6.0941 | 6.9734    |
| No log        | 4.0   | 500  | 2.4904          | 7.5063 | 2.975  | 6.137  | 7.0027    |
| No log        | 5.0   | 625  | 2.4904          | 7.6027 | 3.0582 | 6.2161 | 7.0832    |
| No log        | 6.0   | 750  | 2.4801          | 7.7601 | 3.1916 | 6.3689 | 7.2686    |
| No log        | 7.0   | 875  | 2.4737          | 7.7162 | 3.1332 | 6.3113 | 7.2283    |
| No log        | 8.0   | 1000 | 2.4724          | 7.7389 | 3.1606 | 6.3317 | 7.2487    |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
