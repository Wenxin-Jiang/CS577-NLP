---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: roberta-base_edos_b
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base_edos_b

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3797
- Accuracy: 0.6337
- F1: 0.6259
- Precision: 0.6395
- Recall: 0.6155

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.9275        | 1.0   | 638  | 0.8373          | 0.6502   | 0.6579 | 0.6348    | 0.6989 |
| 0.5744        | 2.0   | 1276 | 1.1104          | 0.6337   | 0.6187 | 0.6332    | 0.6225 |
| 0.334         | 3.0   | 1914 | 1.3797          | 0.6337   | 0.6259 | 0.6395    | 0.6155 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
