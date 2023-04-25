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
- name: distilBERT_token_itr0_0.0001_all_01_03_2022-15_22_12
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilBERT_token_itr0_0.0001_all_01_03_2022-15_22_12

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2811
- Precision: 0.3231
- Recall: 0.5151
- F1: 0.3971
- Accuracy: 0.8913

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
| No log        | 1.0   | 30   | 0.2881          | 0.2089    | 0.3621 | 0.2650 | 0.8715   |
| No log        | 2.0   | 60   | 0.2500          | 0.2619    | 0.3842 | 0.3115 | 0.8845   |
| No log        | 3.0   | 90   | 0.2571          | 0.2327    | 0.4338 | 0.3030 | 0.8809   |
| No log        | 4.0   | 120  | 0.2479          | 0.3051    | 0.4761 | 0.3719 | 0.8949   |
| No log        | 5.0   | 150  | 0.2783          | 0.3287    | 0.4761 | 0.3889 | 0.8936   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
