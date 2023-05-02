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
- name: bert-base-uncased_token_itr0_0.0001_TRAIN_all_TEST_null__second_train_set_NULL_False
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased_token_itr0_0.0001_TRAIN_all_TEST_null__second_train_set_NULL_False

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0650
- Precision: 0.9847
- Recall: 0.9864
- F1: 0.9856
- Accuracy: 0.9719

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
| No log        | 1.0   | 25   | 0.2530          | 0.9106    | 0.8321 | 0.8696 | 0.7793   |
| No log        | 2.0   | 50   | 0.1882          | 0.9855    | 0.6891 | 0.8111 | 0.7116   |
| No log        | 3.0   | 75   | 0.1879          | 0.9467    | 0.7173 | 0.8162 | 0.7105   |
| No log        | 4.0   | 100  | 0.1987          | 0.9567    | 0.7108 | 0.8156 | 0.7120   |
| No log        | 5.0   | 125  | 0.1949          | 0.9511    | 0.7136 | 0.8154 | 0.7105   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
