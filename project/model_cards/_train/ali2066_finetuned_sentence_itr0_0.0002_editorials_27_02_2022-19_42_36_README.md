---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: finetuned_sentence_itr0_0.0002_editorials_27_02_2022-19_42_36
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr0_0.0002_editorials_27_02_2022-19_42_36

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0926
- Accuracy: 0.9772
- F1: 0.9883

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 104  | 0.0539          | 0.9885   | 0.9942 |
| No log        | 2.0   | 208  | 0.0282          | 0.9885   | 0.9942 |
| No log        | 3.0   | 312  | 0.0317          | 0.9914   | 0.9956 |
| No log        | 4.0   | 416  | 0.0462          | 0.9885   | 0.9942 |
| 0.0409        | 5.0   | 520  | 0.0517          | 0.9885   | 0.9942 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
