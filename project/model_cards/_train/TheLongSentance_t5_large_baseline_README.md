---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model_index:
- name: t5_large_baseline
  results:
  - task:
      name: Summarization
      type: summarization
    metric:
      name: Rouge1
      type: rouge
      value: 99.8958
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5_large_baseline

This model is a fine-tuned version of [t5-large](https://huggingface.co/t5-large) on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0010
- Rouge1: 99.8958
- Rouge2: 99.8696
- Rougel: 99.8958
- Rougelsum: 99.8958
- Gen Len: 46.715

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 0.9852        | 0.33  | 50   | 0.1098          | 55.1421 | 49.8248 | 54.4294 | 54.7377   | 19.0    |
| 0.1186        | 0.67  | 100  | 0.0176          | 58.0994 | 54.8973 | 57.7383 | 57.9538   | 19.0    |
| 0.0417        | 1.0   | 150  | 0.0057          | 58.3685 | 55.7353 | 58.279  | 58.2729   | 19.0    |
| 0.0225        | 1.33  | 200  | 0.0029          | 58.8981 | 56.2457 | 58.8202 | 58.7906   | 19.0    |
| 0.0131        | 1.67  | 250  | 0.0024          | 58.8439 | 56.2535 | 58.7557 | 58.7218   | 19.0    |
| 0.0112        | 2.0   | 300  | 0.0013          | 58.9538 | 56.4749 | 58.9322 | 58.8817   | 19.0    |
| 0.0077        | 2.33  | 350  | 0.0013          | 58.9538 | 56.4749 | 58.9322 | 58.8817   | 19.0    |
| 0.0043        | 2.67  | 400  | 0.0010          | 59.0124 | 56.5806 | 58.9867 | 58.9342   | 19.0    |
| 0.0052        | 3.0   | 450  | 0.0010          | 59.0402 | 56.6982 | 59.0385 | 58.986    | 19.0    |


### Framework versions

- Transformers 4.10.0.dev0
- Pytorch 1.9.0+cu111
- Datasets 1.11.0
- Tokenizers 0.10.3
