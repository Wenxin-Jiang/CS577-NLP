---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: finetuned_sentence_itr0_2e-05_all_27_02_2022-19_05_42
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_sentence_itr0_2e-05_all_27_02_2022-19_05_42

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4917
- Accuracy: 0.8231
- F1: 0.8833

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
| No log        | 1.0   | 195  | 0.3883          | 0.8146   | 0.8833 |
| No log        | 2.0   | 390  | 0.3607          | 0.8390   | 0.8964 |
| 0.4085        | 3.0   | 585  | 0.3812          | 0.8488   | 0.9042 |
| 0.4085        | 4.0   | 780  | 0.3977          | 0.8549   | 0.9077 |
| 0.4085        | 5.0   | 975  | 0.4233          | 0.8573   | 0.9092 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
