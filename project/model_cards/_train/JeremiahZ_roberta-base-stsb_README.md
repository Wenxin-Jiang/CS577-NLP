---
language:
- en
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- spearmanr
model-index:
- name: roberta-base-stsb
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE STSB
      type: glue
      args: stsb
    metrics:
    - name: Spearmanr
      type: spearmanr
      value: 0.907904999413384
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-stsb

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE STSB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4155
- Pearson: 0.9101
- Spearmanr: 0.9079
- Combined Score: 0.9090

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Pearson | Spearmanr | Combined Score |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:---------:|:--------------:|
| No log        | 1.0   | 360  | 0.6202          | 0.8787  | 0.8813    | 0.8800         |
| 1.6425        | 2.0   | 720  | 0.4864          | 0.9008  | 0.8992    | 0.9000         |
| 0.3629        | 3.0   | 1080 | 0.4201          | 0.9043  | 0.9016    | 0.9030         |
| 0.3629        | 4.0   | 1440 | 0.4686          | 0.9052  | 0.9003    | 0.9027         |
| 0.2212        | 5.0   | 1800 | 0.4622          | 0.9061  | 0.9031    | 0.9046         |
| 0.1556        | 6.0   | 2160 | 0.3952          | 0.9086  | 0.9065    | 0.9075         |
| 0.1162        | 7.0   | 2520 | 0.4271          | 0.9081  | 0.9070    | 0.9075         |
| 0.1162        | 8.0   | 2880 | 0.4169          | 0.9094  | 0.9075    | 0.9085         |
| 0.0887        | 9.0   | 3240 | 0.4383          | 0.9091  | 0.9074    | 0.9083         |
| 0.0717        | 10.0  | 3600 | 0.4155          | 0.9101  | 0.9079    | 0.9090         |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
