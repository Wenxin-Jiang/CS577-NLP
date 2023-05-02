---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: bert-base-uncased-sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE SST2
      type: glue
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9323394495412844
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-sst2

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the GLUE SST2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2478
- Accuracy: 0.9323

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.1668        | 1.0   | 2105 | 0.2513          | 0.9174   |
| 0.1119        | 2.0   | 4210 | 0.2478          | 0.9323   |
| 0.0699        | 3.0   | 6315 | 0.2764          | 0.9266   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
