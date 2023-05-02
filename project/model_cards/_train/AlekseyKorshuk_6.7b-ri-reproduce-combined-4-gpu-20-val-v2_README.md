---
license: other
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: 6.7b-ri-reproduce-combined-4-gpu-20-val-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 6.7b-ri-reproduce-combined-4-gpu-20-val-v2

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.9434
- Accuracy: 0.0329
- Perplexity: 51.5916

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 9e-07
- train_batch_size: 1
- eval_batch_size: 8
- seed: 100
- distributed_type: multi-GPU
- num_devices: 4
- total_train_batch_size: 4
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant
- num_epochs: 15.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Perplexity |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:----------:|
| 2.5731        | 1.0   | 79   | 2.6113          | 0.0317   | 13.6171    |
| 2.206         | 2.0   | 158  | 2.4805          | 0.0328   | 11.9469    |
| 1.9105        | 3.0   | 237  | 2.4512          | 0.0333   | 11.6019    |
| 1.6301        | 4.0   | 316  | 2.5078          | 0.0345   | 12.2780    |
| 1.3733        | 5.0   | 395  | 2.6816          | 0.0342   | 14.6090    |
| 1.1337        | 6.0   | 474  | 3.0078          | 0.0330   | 20.2431    |
| 0.9619        | 7.0   | 553  | 3.1777          | 0.0330   | 23.9923    |
| 0.798         | 8.0   | 632  | 3.2559          | 0.0330   | 25.9419    |
| 0.6653        | 9.0   | 711  | 3.4277          | 0.0331   | 30.8068    |
| 0.552         | 10.0  | 790  | 3.5566          | 0.0333   | 35.0453    |
| 0.4568        | 11.0  | 869  | 3.7324          | 0.0324   | 41.7802    |
| 0.3756        | 12.0  | 948  | 3.8184          | 0.0328   | 45.5295    |
| 0.3119        | 13.0  | 1027 | 3.8477          | 0.0331   | 46.8831    |
| 0.2448        | 14.0  | 1106 | 3.9062          | 0.0329   | 49.7122    |
| 0.1986        | 15.0  | 1185 | 3.9434          | 0.0329   | 51.5916    |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
