---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: ner_kaggle_class_prediction_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ner_kaggle_class_prediction_model

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0191
- Precision: 0.9850
- Recall: 0.9830
- F1: 0.9840
- Accuracy: 0.9950

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1304        | 1.0   | 806  | 0.0202          | 0.9823    | 0.9794 | 0.9808 | 0.9940   |
| 0.0142        | 2.0   | 1612 | 0.0178          | 0.9819    | 0.9826 | 0.9823 | 0.9945   |
| 0.0081        | 3.0   | 2418 | 0.0191          | 0.9850    | 0.9830 | 0.9840 | 0.9950   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
