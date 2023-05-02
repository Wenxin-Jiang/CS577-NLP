---
license: apache-2.0
tags:
- summarization_v1_m5
- generated_from_trainer
datasets:
- samsum
metrics:
- rouge
model-index:
- name: mt5-small-finetune-sumsum
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: samsum
      type: samsum
      args: samsum
    metrics:
    - name: Rouge1
      type: rouge
      value: 20.9651
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetune-sumsum

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the samsum dataset.
It achieves the following results on the evaluation set:
- Loss: 3.3263
- Rouge1: 20.9651
- Rouge2: 7.1527
- Rougel: 18.4396
- Rougelsum: 19.5209

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| 12.2648       | 1.0   | 125  | 4.3790          | 9.8078  | 1.7255 | 9.0852  | 9.4233    |
| 6.0853        | 2.0   | 250  | 3.4753          | 20.7185 | 6.502  | 18.079  | 19.2584   |
| 4.9838        | 3.0   | 375  | 3.3263          | 20.9651 | 7.1527 | 18.4396 | 19.5209   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.13.0
- Datasets 2.6.1
- Tokenizers 0.11.0
