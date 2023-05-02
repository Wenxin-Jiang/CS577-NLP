---
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-bert-base-uncased-mc-weight0-epoch15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-bert-base-uncased-mc-weight0-epoch15

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.3651
- Cls loss: 2.9223
- Lm loss: 4.3649
- Cls Accuracy: 0.0248
- Cls F1: 0.0057
- Cls Precision: 0.0061
- Cls Recall: 0.0248
- Perplexity: 78.64

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
| 4.8711        | 1.0   | 3470  | 4.5156          | 2.9252   | 4.5155  | 0.0213       | 0.0047 | 0.0042        | 0.0213     | 91.42      |
| 4.483         | 2.0   | 6940  | 4.4193          | 2.9248   | 4.4191  | 0.0219       | 0.0048 | 0.0042        | 0.0219     | 83.02      |
| 4.3345        | 3.0   | 10410 | 4.3684          | 2.9244   | 4.3682  | 0.0219       | 0.0048 | 0.0042        | 0.0219     | 78.91      |
| 4.2266        | 4.0   | 13880 | 4.3445          | 2.9241   | 4.3443  | 0.0225       | 0.0049 | 0.0043        | 0.0225     | 77.04      |
| 4.1388        | 5.0   | 17350 | 4.3260          | 2.9237   | 4.3258  | 0.0231       | 0.0050 | 0.0044        | 0.0231     | 75.63      |
| 4.0644        | 6.0   | 20820 | 4.3299          | 2.9234   | 4.3297  | 0.0231       | 0.0050 | 0.0044        | 0.0231     | 75.92      |
| 3.999         | 7.0   | 24290 | 4.3278          | 2.9232   | 4.3276  | 0.0231       | 0.0059 | 0.0061        | 0.0231     | 75.76      |
| 3.9426        | 8.0   | 27760 | 4.3269          | 2.9230   | 4.3267  | 0.0231       | 0.0059 | 0.0061        | 0.0231     | 75.70      |
| 3.8929        | 9.0   | 31230 | 4.3324          | 2.9228   | 4.3322  | 0.0248       | 0.0061 | 0.0062        | 0.0248     | 76.11      |
| 3.8488        | 10.0  | 34700 | 4.3382          | 2.9227   | 4.3380  | 0.0248       | 0.0061 | 0.0064        | 0.0248     | 76.55      |
| 3.8116        | 11.0  | 38170 | 4.3461          | 2.9225   | 4.3459  | 0.0242       | 0.0057 | 0.0061        | 0.0242     | 77.16      |
| 3.7791        | 12.0  | 41640 | 4.3537          | 2.9224   | 4.3535  | 0.0248       | 0.0057 | 0.0061        | 0.0248     | 77.75      |
| 3.7532        | 13.0  | 45110 | 4.3593          | 2.9223   | 4.3591  | 0.0248       | 0.0057 | 0.0061        | 0.0248     | 78.19      |
| 3.7321        | 14.0  | 48580 | 4.3588          | 2.9223   | 4.3586  | 0.0248       | 0.0057 | 0.0061        | 0.0248     | 78.15      |
| 3.7182        | 15.0  | 52050 | 4.3651          | 2.9223   | 4.3649  | 0.0248       | 0.0057 | 0.0061        | 0.0248     | 78.64      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1