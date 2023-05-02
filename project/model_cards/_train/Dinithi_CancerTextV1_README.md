---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: CancerTextV1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CancerTextV1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5476
- Accuracy: 0.8683
- Precision: 0.8558
- Recall: 0.8870
- F1: 0.8711

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.3268        | 1.0   | 600  | 0.3939          | 0.8475   | 0.8268    | 0.8804 | 0.8528 |
| 0.3132        | 2.0   | 1200 | 0.3510          | 0.8475   | 0.8509    | 0.8439 | 0.8474 |
| 0.2595        | 3.0   | 1800 | 0.3631          | 0.8617   | 0.8505    | 0.8787 | 0.8644 |
| 0.2256        | 4.0   | 2400 | 0.4303          | 0.8625   | 0.8507    | 0.8804 | 0.8653 |
| 0.1944        | 5.0   | 3000 | 0.4551          | 0.8642   | 0.8592    | 0.8721 | 0.8656 |
| 0.1734        | 6.0   | 3600 | 0.4673          | 0.86     | 0.8434    | 0.8854 | 0.8639 |
| 0.1446        | 7.0   | 4200 | 0.4960          | 0.87     | 0.8562    | 0.8904 | 0.8730 |
| 0.1371        | 8.0   | 4800 | 0.5162          | 0.8708   | 0.8646    | 0.8804 | 0.8724 |
| 0.123         | 9.0   | 5400 | 0.5396          | 0.8642   | 0.8604    | 0.8704 | 0.8654 |
| 0.1174        | 10.0  | 6000 | 0.5476          | 0.8683   | 0.8558    | 0.8870 | 0.8711 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
