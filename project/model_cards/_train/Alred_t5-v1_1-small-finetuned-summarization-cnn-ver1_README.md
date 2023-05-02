---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: t5-v1_1-small-finetuned-summarization-cnn-ver1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-v1_1-small-finetuned-summarization-cnn-ver1

This model is a fine-tuned version of [google/t5-v1_1-small](https://huggingface.co/google/t5-v1_1-small) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7467
- Bertscore-mean-precision: 0.8764
- Bertscore-mean-recall: 0.8519
- Bertscore-mean-f1: 0.8639
- Bertscore-median-precision: 0.8746
- Bertscore-median-recall: 0.8518
- Bertscore-median-f1: 0.8632

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bertscore-mean-precision | Bertscore-mean-recall | Bertscore-mean-f1 | Bertscore-median-precision | Bertscore-median-recall | Bertscore-median-f1 |
|:-------------:|:-----:|:----:|:---------------:|:------------------------:|:---------------------:|:-----------------:|:--------------------------:|:-----------------------:|:-------------------:|
| 4.6845        | 1.0   | 718  | 2.9003          | 0.8698                   | 0.8456                | 0.8574            | 0.8693                     | 0.8445                  | 0.8570              |
| 3.7925        | 2.0   | 1436 | 2.7654          | 0.8765                   | 0.8519                | 0.8639            | 0.8745                     | 0.8512                  | 0.8629              |
| 3.6332        | 3.0   | 2154 | 2.7467          | 0.8764                   | 0.8519                | 0.8639            | 0.8746                     | 0.8518                  | 0.8632              |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
