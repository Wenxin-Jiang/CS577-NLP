---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: bert_base_uncased_itr0_0.0001_all_01_03_2022-14_08_15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert_base_uncased_itr0_0.0001_all_01_03_2022-14_08_15

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7632
- Accuracy: 0.8263
- F1: 0.8871
- Precision: 0.8551
- Recall: 0.9215

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 390  | 0.3986          | 0.8305   | 0.8903 | 0.8868    | 0.8938 |
| 0.4561        | 2.0   | 780  | 0.4018          | 0.8439   | 0.9009 | 0.8805    | 0.9223 |
| 0.3111        | 3.0   | 1170 | 0.4306          | 0.8354   | 0.8924 | 0.8974    | 0.8875 |
| 0.1739        | 4.0   | 1560 | 0.5499          | 0.8378   | 0.9002 | 0.8547    | 0.9509 |
| 0.1739        | 5.0   | 1950 | 0.6223          | 0.85     | 0.9052 | 0.8814    | 0.9303 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
