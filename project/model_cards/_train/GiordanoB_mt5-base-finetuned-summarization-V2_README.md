---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-finetuned-summarization-V2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-finetuned-summarization-V2

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 8.3409
- Rouge1: 6.1259
- Rouge2: 1.4637
- Rougel: 5.3192
- Rougelsum: 5.7739
- Gen Len: 9.9286

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

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| No log        | 1.0   | 15   | 10.0266         | 6.7528 | 2.8064 | 5.9938 | 6.4352    | 10.0    |
| No log        | 2.0   | 30   | 8.4159          | 6.1259 | 1.4637 | 5.3192 | 5.7739    | 10.0714 |
| No log        | 3.0   | 45   | 8.3409          | 6.1259 | 1.4637 | 5.3192 | 5.7739    | 9.9286  |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
