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
- name: finetuned_token_2e-05_16_02_2022-14_30_32
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_2e-05_16_02_2022-14_30_32

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1722
- Precision: 0.3378
- Recall: 0.3615
- F1: 0.3492
- Accuracy: 0.9448

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 38   | 0.3781          | 0.1512    | 0.2671 | 0.1931 | 0.8216   |
| No log        | 2.0   | 76   | 0.3020          | 0.1748    | 0.2938 | 0.2192 | 0.8551   |
| No log        | 3.0   | 114  | 0.2723          | 0.1938    | 0.3339 | 0.2452 | 0.8663   |
| No log        | 4.0   | 152  | 0.2574          | 0.2119    | 0.3506 | 0.2642 | 0.8727   |
| No log        | 5.0   | 190  | 0.2521          | 0.2121    | 0.3623 | 0.2676 | 0.8756   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
