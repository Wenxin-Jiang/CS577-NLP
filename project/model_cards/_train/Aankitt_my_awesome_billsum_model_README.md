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
      value: 0.1966
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_awesome_billsum_model

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the billsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3829
- Rouge1: 0.1966
- Rouge2: 0.0969
- Rougel: 0.1655
- Rougelsum: 0.1657
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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| No log        | 1.0   | 248  | 2.5380          | 0.1441 | 0.0519 | 0.1188 | 0.1189    | 19.0    |
| No log        | 2.0   | 496  | 2.4335          | 0.1939 | 0.0933 | 0.162  | 0.1622    | 19.0    |
| 2.8683        | 3.0   | 744  | 2.3940          | 0.1974 | 0.0974 | 0.1665 | 0.1666    | 19.0    |
| 2.8683        | 4.0   | 992  | 2.3829          | 0.1966 | 0.0969 | 0.1655 | 0.1657    | 19.0    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
