---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: t5-small-finetuned-summarization-cnn-ver3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-summarization-cnn-ver3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1072
- Bertscore-mean-precision: 0.8861
- Bertscore-mean-recall: 0.8592
- Bertscore-mean-f1: 0.8723
- Bertscore-median-precision: 0.8851
- Bertscore-median-recall: 0.8582
- Bertscore-median-f1: 0.8719

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bertscore-mean-precision | Bertscore-mean-recall | Bertscore-mean-f1 | Bertscore-median-precision | Bertscore-median-recall | Bertscore-median-f1 |
|:-------------:|:-----:|:----:|:---------------:|:------------------------:|:---------------------:|:-----------------:|:--------------------------:|:-----------------------:|:-------------------:|
| 2.0168        | 1.0   | 718  | 2.0528          | 0.8870                   | 0.8591                | 0.8727            | 0.8864                     | 0.8578                  | 0.8724              |
| 1.8387        | 2.0   | 1436 | 2.0610          | 0.8863                   | 0.8591                | 0.8723            | 0.8848                     | 0.8575                  | 0.8712              |
| 1.7302        | 3.0   | 2154 | 2.0659          | 0.8856                   | 0.8588                | 0.8719            | 0.8847                     | 0.8569                  | 0.8717              |
| 1.6459        | 4.0   | 2872 | 2.0931          | 0.8860                   | 0.8592                | 0.8722            | 0.8850                     | 0.8570                  | 0.8718              |
| 1.5907        | 5.0   | 3590 | 2.1072          | 0.8861                   | 0.8592                | 0.8723            | 0.8851                     | 0.8582                  | 0.8719              |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
