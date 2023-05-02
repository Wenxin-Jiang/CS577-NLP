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
- name: model_6012023
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_6012023

This model is a fine-tuned version of [Buseak/my_pos_model](https://huggingface.co/Buseak/my_pos_model) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2391
- Precision: 0.9109
- Recall: 0.9042
- F1: 0.9076
- Accuracy: 0.9348

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 244  | 0.3030          | 0.8906    | 0.8845 | 0.8875 | 0.9202   |
| No log        | 2.0   | 488  | 0.2526          | 0.9051    | 0.8977 | 0.9014 | 0.9306   |
| 0.4278        | 3.0   | 732  | 0.2391          | 0.9109    | 0.9042 | 0.9076 | 0.9348   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
