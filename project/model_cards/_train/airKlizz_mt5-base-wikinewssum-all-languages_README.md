---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-wikinewssum-all-languages
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-wikinewssum-all-languages

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2454
- Rouge1: 8.3826
- Rouge2: 3.5524
- Rougel: 6.8656
- Rougelsum: 7.8362

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

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|
| No log        | 1.0   | 3467  | 2.4034          | 8.0363 | 3.2484 | 6.5409 | 7.477     |
| No log        | 2.0   | 6934  | 2.3276          | 8.1054 | 3.2905 | 6.5765 | 7.5687    |
| No log        | 3.0   | 10401 | 2.2976          | 8.169  | 3.4272 | 6.6597 | 7.6435    |
| No log        | 4.0   | 13868 | 2.2795          | 8.2941 | 3.5353 | 6.7881 | 7.7664    |
| 2.8057        | 5.0   | 17335 | 2.2621          | 8.3302 | 3.5599 | 6.8238 | 7.7928    |
| 2.8057        | 6.0   | 20802 | 2.2547          | 8.3818 | 3.5886 | 6.8672 | 7.844     |
| 2.8057        | 7.0   | 24269 | 2.2472          | 8.3809 | 3.5696 | 6.8575 | 7.8327    |
| 2.8057        | 8.0   | 27736 | 2.2454          | 8.3826 | 3.5524 | 6.8656 | 7.8362    |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.1
- Datasets 1.16.1
- Tokenizers 0.10.3
