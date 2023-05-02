---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: bart-base-finetuned-summarization-cnn-ver3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-finetuned-summarization-cnn-ver3

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9827
- Bertscore-mean-precision: 0.8811
- Bertscore-mean-recall: 0.8554
- Bertscore-mean-f1: 0.8679
- Bertscore-median-precision: 0.8809
- Bertscore-median-recall: 0.8545
- Bertscore-median-f1: 0.8669

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bertscore-mean-precision | Bertscore-mean-recall | Bertscore-mean-f1 | Bertscore-median-precision | Bertscore-median-recall | Bertscore-median-f1 |
|:-------------:|:-----:|:----:|:---------------:|:------------------------:|:---------------------:|:-----------------:|:--------------------------:|:-----------------------:|:-------------------:|
| 3.632         | 1.0   | 5742 | 2.9827          | 0.8811                   | 0.8554                | 0.8679            | 0.8809                     | 0.8545                  | 0.8669              |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
