---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: t5-small-finetuned-summarization-cnn-ver2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-summarization-cnn-ver2

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0084
- Bertscore-mean-precision: 0.8859
- Bertscore-mean-recall: 0.8592
- Bertscore-mean-f1: 0.8721
- Bertscore-median-precision: 0.8855
- Bertscore-median-recall: 0.8578
- Bertscore-median-f1: 0.8718

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bertscore-mean-precision | Bertscore-mean-recall | Bertscore-mean-f1 | Bertscore-median-precision | Bertscore-median-recall | Bertscore-median-f1 |
|:-------------:|:-----:|:----:|:---------------:|:------------------------:|:---------------------:|:-----------------:|:--------------------------:|:-----------------------:|:-------------------:|
| 2.0422        | 1.0   | 718  | 2.0139          | 0.8853                   | 0.8589                | 0.8717            | 0.8857                     | 0.8564                  | 0.8715              |
| 1.9481        | 2.0   | 1436 | 2.0085          | 0.8863                   | 0.8591                | 0.8723            | 0.8858                     | 0.8577                  | 0.8718              |
| 1.9231        | 3.0   | 2154 | 2.0084          | 0.8859                   | 0.8592                | 0.8721            | 0.8855                     | 0.8578                  | 0.8718              |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
