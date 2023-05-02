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
- name: model_from_berturk_1401
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_from_berturk_1401

This model is a fine-tuned version of [dbmdz/bert-base-turkish-cased](https://huggingface.co/dbmdz/bert-base-turkish-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2702
- Precision: 0.8979
- Recall: 0.8911
- F1: 0.8945
- Accuracy: 0.9254

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
| No log        | 1.0   | 244  | 0.4037          | 0.8571    | 0.8504 | 0.8537 | 0.8950   |
| No log        | 2.0   | 488  | 0.3194          | 0.8798    | 0.8741 | 0.8769 | 0.9126   |
| 0.6153        | 3.0   | 732  | 0.2787          | 0.8954    | 0.8862 | 0.8908 | 0.9230   |
| 0.6153        | 4.0   | 976  | 0.2702          | 0.8979    | 0.8911 | 0.8945 | 0.9254   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
