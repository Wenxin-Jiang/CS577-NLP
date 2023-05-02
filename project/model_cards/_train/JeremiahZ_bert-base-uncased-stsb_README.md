---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- spearmanr
model-index:
- name: bert-base-uncased-stsb
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
      value: 0.8843169724798454
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-stsb

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the GLUE STSB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5144
- Pearson: 0.8875
- Spearmanr: 0.8843
- Combined Score: 0.8859

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Pearson | Spearmanr | Combined Score |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:---------:|:--------------:|
| No log        | 1.0   | 180  | 0.5179          | 0.8806  | 0.8735    | 0.8771         |
| No log        | 2.0   | 360  | 0.5145          | 0.8850  | 0.8820    | 0.8835         |
| 0.7868        | 3.0   | 540  | 0.5144          | 0.8875  | 0.8843    | 0.8859         |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
