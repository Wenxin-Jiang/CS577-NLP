---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-base-cased-twitter_sentiment
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-twitter_sentiment

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6907
- Accuracy: 0.7132

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.8901        | 1.0   | 1387  | 0.8592          | 0.6249   |
| 0.8085        | 2.0   | 2774  | 0.7600          | 0.6822   |
| 0.7336        | 3.0   | 4161  | 0.7170          | 0.6915   |
| 0.6938        | 4.0   | 5548  | 0.7018          | 0.7016   |
| 0.6738        | 5.0   | 6935  | 0.6926          | 0.7067   |
| 0.6496        | 6.0   | 8322  | 0.6910          | 0.7088   |
| 0.6599        | 7.0   | 9709  | 0.6902          | 0.7088   |
| 0.631         | 8.0   | 11096 | 0.6910          | 0.7095   |
| 0.6327        | 9.0   | 12483 | 0.6925          | 0.7146   |
| 0.6305        | 10.0  | 13870 | 0.6907          | 0.7132   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
