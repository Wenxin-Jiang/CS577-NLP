---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: distilbert-legal-chunk
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-legal-chunk

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0699
- Precision: 0.8994
- Recall: 0.8721
- Macro F1: 0.8855
- Micro F1: 0.8855
- Accuracy: 0.9789
- Marker F1: 0.9804
- Marker Precision: 0.9687
- Marker Recall: 0.9925
- Reference F1: 0.9791
- Reference Precision: 0.9804
- Reference Recall: 0.9778
- Term F1: 0.8670
- Term Precision: 0.8844
- Term Recall: 0.8502

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | Macro F1 | Micro F1 | Accuracy | Marker F1 | Marker Precision | Marker Recall | Reference F1 | Reference Precision | Reference Recall | Term F1 | Term Precision | Term Recall |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:--------:|:--------:|:--------:|:---------:|:----------------:|:-------------:|:------------:|:-------------------:|:----------------:|:-------:|:--------------:|:-----------:|
| 0.0857        | 1.0   | 3125  | 0.0966          | 0.8374    | 0.7889 | 0.8124   | 0.8124   | 0.9676   | 0.6143    | 0.5874           | 0.6437        | 0.9628       | 0.9423              | 0.9842           | 0.8291  | 0.8656         | 0.7955      |
| 0.058         | 2.0   | 6250  | 0.0606          | 0.8869    | 0.9146 | 0.9006   | 0.9006   | 0.9814   | 0.9405    | 0.9126           | 0.9702        | 0.9689       | 0.9511              | 0.9873           | 0.8923  | 0.8805         | 0.9045      |
| 0.0415        | 3.0   | 9375  | 0.0642          | 0.9077    | 0.9131 | 0.9104   | 0.9104   | 0.9823   | 0.9524    | 0.9262           | 0.9801        | 0.9742       | 0.9614              | 0.9873           | 0.9021  | 0.9026         | 0.9016      |
| 0.0283        | 4.0   | 12500 | 0.0646          | 0.9066    | 0.9089 | 0.9077   | 0.9077   | 0.9819   | 0.9564    | 0.9326           | 0.9815        | 0.9712       | 0.9555              | 0.9873           | 0.8986  | 0.9008         | 0.8965      |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
