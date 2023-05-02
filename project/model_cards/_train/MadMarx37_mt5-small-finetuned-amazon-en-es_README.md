---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-amazon-en-es
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-amazon-en-es

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0294
- Rouge1: 16.4909
- Rouge2: 7.9422
- Rougel: 16.3139
- Rougelsum: 16.3615

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
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| 6.5928        | 1.0   | 1209 | 3.3005          | 14.6517 | 6.5194 | 14.3474 | 14.2801   |
| 3.9024        | 2.0   | 2418 | 3.1399          | 16.744  | 8.6706 | 16.0952 | 16.1512   |
| 3.5806        | 3.0   | 3627 | 3.0869          | 18.0041 | 9.2385 | 17.718  | 17.6889   |
| 3.4201        | 4.0   | 4836 | 3.0590          | 17.5844 | 8.972  | 17.1709 | 17.2169   |
| 3.3202        | 5.0   | 6045 | 3.0598          | 17.5762 | 8.6036 | 17.3677 | 17.3708   |
| 3.2436        | 6.0   | 7254 | 3.0409          | 16.7641 | 8.19   | 16.6109 | 16.5899   |
| 3.2079        | 7.0   | 8463 | 3.0332          | 16.6917 | 8.1747 | 16.4958 | 16.527    |
| 3.1801        | 8.0   | 9672 | 3.0294          | 16.4909 | 7.9422 | 16.3139 | 16.3615   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
