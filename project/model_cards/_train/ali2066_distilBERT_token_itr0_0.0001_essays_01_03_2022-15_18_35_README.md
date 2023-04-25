---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: distilBERT_token_itr0_0.0001_essays_01_03_2022-15_18_35
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilBERT_token_itr0_0.0001_essays_01_03_2022-15_18_35

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1832
- Precision: 0.6138
- Recall: 0.7169
- F1: 0.6613
- Accuracy: 0.9332

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 11   | 0.2740          | 0.4554    | 0.5460 | 0.4966 | 0.8943   |
| No log        | 2.0   | 22   | 0.2189          | 0.5470    | 0.6558 | 0.5965 | 0.9193   |
| No log        | 3.0   | 33   | 0.2039          | 0.5256    | 0.6706 | 0.5893 | 0.9198   |
| No log        | 4.0   | 44   | 0.2097          | 0.5401    | 0.6795 | 0.6018 | 0.9237   |
| No log        | 5.0   | 55   | 0.2255          | 0.6117    | 0.6825 | 0.6452 | 0.9223   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
