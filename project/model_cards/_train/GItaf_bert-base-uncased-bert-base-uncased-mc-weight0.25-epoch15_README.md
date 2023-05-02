---
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-bert-base-uncased-mc-weight0.25-epoch15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-bert-base-uncased-mc-weight0.25-epoch15

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.1343
- Cls loss: 3.0991
- Lm loss: 4.3588
- Cls Accuracy: 0.6092
- Cls F1: 0.6066
- Cls Precision: 0.6082
- Cls Recall: 0.6092
- Perplexity: 78.17

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 5.3372        | 1.0   | 3470  | 4.9249          | 1.5682   | 4.5325  | 0.5712       | 0.5567 | 0.5751        | 0.5712     | 92.99      |
| 4.8287        | 2.0   | 6940  | 4.7830          | 1.3889   | 4.4355  | 0.6231       | 0.6169 | 0.6448        | 0.6231     | 84.39      |
| 4.6295        | 3.0   | 10410 | 4.7585          | 1.4752   | 4.3894  | 0.6248       | 0.6160 | 0.6340        | 0.6248     | 80.59      |
| 4.4704        | 4.0   | 13880 | 4.7707          | 1.6098   | 4.3678  | 0.6121       | 0.6079 | 0.6156        | 0.6121     | 78.87      |
| 4.3364        | 5.0   | 17350 | 4.8008          | 1.8102   | 4.3478  | 0.6086       | 0.6068 | 0.6105        | 0.6086     | 77.31      |
| 4.2245        | 6.0   | 20820 | 4.8353          | 1.9486   | 4.3477  | 0.6121       | 0.6075 | 0.6131        | 0.6121     | 77.30      |
| 4.1289        | 7.0   | 24290 | 4.8883          | 2.1912   | 4.3400  | 0.6110       | 0.6076 | 0.6182        | 0.6110     | 76.71      |
| 4.0485        | 8.0   | 27760 | 4.9394          | 2.4203   | 4.3337  | 0.5914       | 0.5862 | 0.6016        | 0.5914     | 76.23      |
| 3.9826        | 9.0   | 31230 | 5.0026          | 2.6664   | 4.3354  | 0.6006       | 0.5936 | 0.6035        | 0.6006     | 76.35      |
| 3.9277        | 10.0  | 34700 | 4.9902          | 2.5992   | 4.3398  | 0.6035       | 0.6032 | 0.6088        | 0.6035     | 76.69      |
| 3.8794        | 11.0  | 38170 | 5.0698          | 2.9006   | 4.3441  | 0.6156       | 0.6127 | 0.6213        | 0.6156     | 77.02      |
| 3.8428        | 12.0  | 41640 | 5.0956          | 2.9795   | 4.3501  | 0.6127       | 0.6110 | 0.6184        | 0.6127     | 77.49      |
| 3.8129        | 13.0  | 45110 | 5.1223          | 3.0646   | 4.3555  | 0.6138       | 0.6099 | 0.6172        | 0.6138     | 77.91      |
| 3.7891        | 14.0  | 48580 | 5.1242          | 3.0809   | 4.3534  | 0.6058       | 0.6045 | 0.6071        | 0.6058     | 77.74      |
| 3.7744        | 15.0  | 52050 | 5.1343          | 3.0991   | 4.3588  | 0.6092       | 0.6066 | 0.6082        | 0.6092     | 78.17      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1