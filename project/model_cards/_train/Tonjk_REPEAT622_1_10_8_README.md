---
tags:
- generated_from_trainer
model-index:
- name: REPEAT622_1_10_8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# REPEAT622_1_10_8

This model is a fine-tuned version of [airesearch/wangchanberta-base-att-spm-uncased](https://huggingface.co/airesearch/wangchanberta-base-att-spm-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1449

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
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.3564        | 1.0   | 9531  | 0.6554          |
| 0.1645        | 2.0   | 19062 | 0.9331          |
| 0.1333        | 3.0   | 28593 | 1.1128          |
| 0.1148        | 4.0   | 38124 | 1.2805          |
| 0.1035        | 5.0   | 47655 | 1.9552          |
| 0.0875        | 6.0   | 57186 | 2.5004          |
| 0.0767        | 7.0   | 66717 | 2.9955          |
| 0.0684        | 8.0   | 76248 | 2.7516          |
| 0.0616        | 9.0   | 85779 | 2.9578          |
| 0.0572        | 10.0  | 95310 | 3.1449          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.13.1+cu116
- Datasets 1.17.0
- Tokenizers 0.10.3
