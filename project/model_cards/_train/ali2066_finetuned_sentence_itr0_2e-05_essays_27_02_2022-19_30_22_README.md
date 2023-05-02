---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: finetuned_sentence_itr0_2e-05_essays_27_02_2022-19_30_22
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr0_2e-05_essays_27_02_2022-19_30_22

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3455
- Accuracy: 0.8609
- F1: 0.9156

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 81   | 0.4468          | 0.8235   | 0.8929 |
| No log        | 2.0   | 162  | 0.4497          | 0.8382   | 0.9    |
| No log        | 3.0   | 243  | 0.4861          | 0.8309   | 0.8940 |
| No log        | 4.0   | 324  | 0.5087          | 0.8235   | 0.8879 |
| No log        | 5.0   | 405  | 0.5228          | 0.8199   | 0.8858 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
