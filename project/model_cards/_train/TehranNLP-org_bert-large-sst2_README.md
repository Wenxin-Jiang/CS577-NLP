---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- sst2
metrics:
- accuracy
model-index:
- name: '42'
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: SST2
      type: glue
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9254587155963303
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 42

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the SST2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3109
- Accuracy: 0.9255

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- distributed_type: not_parallel
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| No log        | 1.0   | 2105  | 0.2167          | 0.9232   |
| 0.2049        | 2.0   | 4210  | 0.2375          | 0.9278   |
| 0.123         | 3.0   | 6315  | 0.2636          | 0.9243   |
| 0.0839        | 4.0   | 8420  | 0.2865          | 0.9243   |
| 0.058         | 5.0   | 10525 | 0.3109          | 0.9255   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu113
- Datasets 2.7.1
- Tokenizers 0.11.6
