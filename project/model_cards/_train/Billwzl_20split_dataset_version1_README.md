---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: 20split_dataset_version1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 20split_dataset_version1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1942

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
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 2.7475        | 1.0   | 11851  | 2.5194          |
| 2.5528        | 2.0   | 23702  | 2.4191          |
| 2.4649        | 3.0   | 35553  | 2.3646          |
| 2.4038        | 4.0   | 47404  | 2.3289          |
| 2.3632        | 5.0   | 59255  | 2.2922          |
| 2.3273        | 6.0   | 71106  | 2.2739          |
| 2.2964        | 7.0   | 82957  | 2.2494          |
| 2.2732        | 8.0   | 94808  | 2.2217          |
| 2.2526        | 9.0   | 106659 | 2.2149          |
| 2.2369        | 10.0  | 118510 | 2.2029          |
| 2.222         | 11.0  | 130361 | 2.2020          |
| 2.2135        | 12.0  | 142212 | 2.1942          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
