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
- name: correct_BERT_token_itr0_0.0001_all_01_03_2022-15_52_19
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# correct_BERT_token_itr0_0.0001_all_01_03_2022-15_52_19

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2711
- Precision: 0.3373
- Recall: 0.5670
- F1: 0.4230
- Accuracy: 0.8943

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
| No log        | 1.0   | 30   | 0.3783          | 0.1833    | 0.3975 | 0.2509 | 0.8413   |
| No log        | 2.0   | 60   | 0.3021          | 0.3280    | 0.4820 | 0.3904 | 0.8876   |
| No log        | 3.0   | 90   | 0.3196          | 0.3504    | 0.5036 | 0.4133 | 0.8918   |
| No log        | 4.0   | 120  | 0.3645          | 0.3434    | 0.5306 | 0.4170 | 0.8759   |
| No log        | 5.0   | 150  | 0.4027          | 0.3217    | 0.5486 | 0.4056 | 0.8797   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
