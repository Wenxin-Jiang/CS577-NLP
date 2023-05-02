---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: bart-base-finetuned-summarization-cnn-ver1.2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-finetuned-summarization-cnn-ver1.2

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2476
- Bertscore-mean-precision: 0.8904
- Bertscore-mean-recall: 0.8611
- Bertscore-mean-f1: 0.8753
- Bertscore-median-precision: 0.8891
- Bertscore-median-recall: 0.8600
- Bertscore-median-f1: 0.8741

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bertscore-mean-precision | Bertscore-mean-recall | Bertscore-mean-f1 | Bertscore-median-precision | Bertscore-median-recall | Bertscore-median-f1 |
|:-------------:|:-----:|:-----:|:---------------:|:------------------------:|:---------------------:|:-----------------:|:--------------------------:|:-----------------------:|:-------------------:|
| 2.3305        | 1.0   | 5742  | 2.2125          | 0.8845                   | 0.8587                | 0.8713            | 0.8840                     | 0.8577                  | 0.8706              |
| 1.7751        | 2.0   | 11484 | 2.2028          | 0.8910                   | 0.8616                | 0.8759            | 0.8903                     | 0.8603                  | 0.8744              |
| 1.4564        | 3.0   | 17226 | 2.2476          | 0.8904                   | 0.8611                | 0.8753            | 0.8891                     | 0.8600                  | 0.8741              |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
