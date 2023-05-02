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
- name: BERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8223
- Accuracy: 0.82
- Precision: 0.84
- Recall: 0.9130
- F1: 0.8750

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
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.6778        | 1.0   | 50   | 0.6148          | 0.69     | 0.7794    | 0.7681 | 0.7737 |
| 0.5331        | 2.0   | 100  | 0.5578          | 0.8      | 0.8267    | 0.8986 | 0.8611 |
| 0.3768        | 3.0   | 150  | 0.5052          | 0.73     | 0.8889    | 0.6957 | 0.7805 |
| 0.2802        | 4.0   | 200  | 0.4998          | 0.86     | 0.8667    | 0.9420 | 0.9028 |
| 0.1869        | 5.0   | 250  | 0.5187          | 0.81     | 0.8906    | 0.8261 | 0.8571 |
| 0.1293        | 6.0   | 300  | 0.6516          | 0.85     | 0.8649    | 0.9275 | 0.8951 |
| 0.1165        | 7.0   | 350  | 0.6541          | 0.82     | 0.8806    | 0.8551 | 0.8676 |
| 0.0937        | 8.0   | 400  | 0.6855          | 0.84     | 0.8841    | 0.8841 | 0.8841 |
| 0.0791        | 9.0   | 450  | 0.7652          | 0.81     | 0.8472    | 0.8841 | 0.8652 |
| 0.0599        | 10.0  | 500  | 0.8223          | 0.82     | 0.84      | 0.9130 | 0.8750 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
