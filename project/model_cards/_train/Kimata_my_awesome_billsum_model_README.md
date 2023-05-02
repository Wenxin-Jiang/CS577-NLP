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
      value: 0.1362
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_awesome_billsum_model

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the billsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5474
- Rouge1: 0.1362
- Rouge2: 0.0419
- Rougel: 0.1111
- Rougelsum: 0.1112
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
| No log        | 1.0   | 62   | 2.8519          | 0.1206 | 0.0274 | 0.0991 | 0.0992    | 19.0    |
| No log        | 2.0   | 124  | 2.6323          | 0.1315 | 0.0377 | 0.1066 | 0.1067    | 19.0    |
| No log        | 3.0   | 186  | 2.5643          | 0.1371 | 0.043  | 0.1117 | 0.1118    | 19.0    |
| No log        | 4.0   | 248  | 2.5474          | 0.1362 | 0.0419 | 0.1111 | 0.1112    | 19.0    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
