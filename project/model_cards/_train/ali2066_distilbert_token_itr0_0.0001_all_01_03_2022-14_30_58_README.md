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
- name: distilbert_token_itr0_0.0001_all_01_03_2022-14_30_58
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert_token_itr0_0.0001_all_01_03_2022-14_30_58

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2572
- Precision: 0.3363
- Recall: 0.5110
- F1: 0.4057
- Accuracy: 0.8931

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
| No log        | 1.0   | 30   | 0.3976          | 0.1405    | 0.3058 | 0.1925 | 0.7921   |
| No log        | 2.0   | 60   | 0.3511          | 0.2360    | 0.4038 | 0.2979 | 0.8260   |
| No log        | 3.0   | 90   | 0.3595          | 0.1863    | 0.3827 | 0.2506 | 0.8211   |
| No log        | 4.0   | 120  | 0.3591          | 0.2144    | 0.4288 | 0.2859 | 0.8299   |
| No log        | 5.0   | 150  | 0.3605          | 0.1989    | 0.4212 | 0.2702 | 0.8343   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
