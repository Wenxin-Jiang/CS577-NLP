---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- billsum
metrics:
- rouge
model-index:
- name: my_awesome_billsum_model
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: billsum
      type: billsum
      config: default
      split: ca_test
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 0.1327
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_awesome_billsum_model

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the billsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7576
- Rouge1: 0.1327
- Rouge2: 0.0444
- Rougel: 0.1111
- Rougelsum: 0.1111
- Gen Len: 19.0

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
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| No log        | 1.0   | 62   | 3.0485          | 0.1269 | 0.0387 | 0.1064 | 0.1065    | 19.0    |
| No log        | 2.0   | 124  | 2.8371          | 0.1322 | 0.0468 | 0.1114 | 0.1114    | 19.0    |
| No log        | 3.0   | 186  | 2.7747          | 0.1335 | 0.0464 | 0.1124 | 0.1123    | 19.0    |
| No log        | 4.0   | 248  | 2.7576          | 0.1327 | 0.0444 | 0.1111 | 0.1111    | 19.0    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu117
- Datasets 2.8.0
- Tokenizers 0.13.2
