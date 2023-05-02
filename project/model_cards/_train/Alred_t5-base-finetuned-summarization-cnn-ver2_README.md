---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: t5-base-finetuned-summarization-cnn-ver2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-finetuned-summarization-cnn-ver2

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7601
- Bertscore-mean-precision: 0.8926
- Bertscore-mean-recall: 0.8628
- Bertscore-mean-f1: 0.8772
- Bertscore-median-precision: 0.8906
- Bertscore-median-recall: 0.8600
- Bertscore-median-f1: 0.8751

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bertscore-mean-precision | Bertscore-mean-recall | Bertscore-mean-f1 | Bertscore-median-precision | Bertscore-median-recall | Bertscore-median-f1 |
|:-------------:|:-----:|:-----:|:---------------:|:------------------------:|:---------------------:|:-----------------:|:--------------------------:|:-----------------------:|:-------------------:|
| 1.4581        | 1.0   | 5742  | 1.6800          | 0.8904                   | 0.8615                | 0.8755            | 0.8887                     | 0.8597                  | 0.8737              |
| 1.2356        | 2.0   | 11484 | 1.7274          | 0.8924                   | 0.8626                | 0.8771            | 0.8911                     | 0.8607                  | 0.8753              |
| 1.1073        | 3.0   | 17226 | 1.7601          | 0.8926                   | 0.8628                | 0.8772            | 0.8906                     | 0.8600                  | 0.8751              |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
