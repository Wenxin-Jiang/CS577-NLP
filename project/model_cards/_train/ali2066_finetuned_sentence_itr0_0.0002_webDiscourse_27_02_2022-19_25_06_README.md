---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: finetuned_sentence_itr0_0.0002_webDiscourse_27_02_2022-19_25_06
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr0_0.0002_webDiscourse_27_02_2022-19_25_06

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5777
- Accuracy: 0.6794
- F1: 0.5010

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
| No log        | 1.0   | 48   | 0.6059          | 0.63     | 0.4932 |
| No log        | 2.0   | 96   | 0.6327          | 0.705    | 0.5630 |
| No log        | 3.0   | 144  | 0.7003          | 0.695    | 0.5197 |
| No log        | 4.0   | 192  | 0.9368          | 0.69     | 0.4655 |
| No log        | 5.0   | 240  | 1.1935          | 0.685    | 0.4425 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
