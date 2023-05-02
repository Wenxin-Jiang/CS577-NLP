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
- name: roberta-large-finetuned-ADEs_model_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-finetuned-ADEs_model_2

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2580
- Precision: 0.5407
- Recall: 0.6311
- F1: 0.5824
- Accuracy: 0.8897

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.7461        | 1.0   | 640  | 0.3393          | 0.4247    | 0.5095 | 0.4633 | 0.8648   |
| 0.3632        | 2.0   | 1280 | 0.2822          | 0.4934    | 0.6035 | 0.5429 | 0.8819   |
| 0.3102        | 3.0   | 1920 | 0.2663          | 0.5218    | 0.6112 | 0.5630 | 0.8879   |
| 0.2806        | 4.0   | 2560 | 0.2604          | 0.5337    | 0.6311 | 0.5783 | 0.8890   |
| 0.2772        | 5.0   | 3200 | 0.2580          | 0.5407    | 0.6311 | 0.5824 | 0.8897   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
