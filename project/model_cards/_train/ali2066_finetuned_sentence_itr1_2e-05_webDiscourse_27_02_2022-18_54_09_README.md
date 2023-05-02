---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: finetuned_sentence_itr1_2e-05_webDiscourse_27_02_2022-18_54_09
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr1_2e-05_webDiscourse_27_02_2022-18_54_09

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6049
- Accuracy: 0.6926
- F1: 0.4160

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
| No log        | 1.0   | 48   | 0.5835          | 0.71     | 0.0333 |
| No log        | 2.0   | 96   | 0.5718          | 0.715    | 0.3871 |
| No log        | 3.0   | 144  | 0.5731          | 0.715    | 0.4    |
| No log        | 4.0   | 192  | 0.6009          | 0.705    | 0.3516 |
| No log        | 5.0   | 240  | 0.6122          | 0.7      | 0.4000 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
