---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: xlm-roberta-base-fa-base-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-fa-base-ner

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2856
- Precision: 0.5353
- Recall: 0.5704
- F1: 0.5523
- Accuracy: 0.9168

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.673         | 1.0   | 511  | 0.4067          | 0.4767    | 0.3981 | 0.4339 | 0.8956   |
| 0.3673        | 2.0   | 1022 | 0.3279          | 0.4611    | 0.5138 | 0.4860 | 0.9031   |
| 0.2998        | 3.0   | 1533 | 0.2977          | 0.5265    | 0.4976 | 0.5116 | 0.9132   |
| 0.2616        | 4.0   | 2044 | 0.2860          | 0.5365    | 0.5477 | 0.5420 | 0.9151   |
| 0.2394        | 5.0   | 2555 | 0.2856          | 0.5353    | 0.5704 | 0.5523 | 0.9168   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
