---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: model_from_berturk_1401_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_from_berturk_1401_v2

This model is a fine-tuned version of [Buseak/model_from_berturk_1401](https://huggingface.co/Buseak/model_from_berturk_1401) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1542
- Precision: 0.9414
- Recall: 0.9356
- F1: 0.9385
- Accuracy: 0.9569

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
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 244  | 0.2277          | 0.9129    | 0.9058 | 0.9094 | 0.9362   |
| No log        | 2.0   | 488  | 0.1855          | 0.9275    | 0.9204 | 0.9240 | 0.9472   |
| 0.2477        | 3.0   | 732  | 0.1602          | 0.9403    | 0.9315 | 0.9359 | 0.9554   |
| 0.2477        | 4.0   | 976  | 0.1542          | 0.9414    | 0.9356 | 0.9385 | 0.9569   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
