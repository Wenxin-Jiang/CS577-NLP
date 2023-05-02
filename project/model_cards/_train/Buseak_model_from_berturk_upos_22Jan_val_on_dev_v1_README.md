---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: model_from_berturk_upos_22Jan_val_on_dev_v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model_from_berturk_upos_22Jan_val_on_dev_v1

This model is a fine-tuned version of [dbmdz/bert-base-turkish-cased](https://huggingface.co/dbmdz/bert-base-turkish-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4600
- Precision: 0.8894
- Recall: 0.8931
- F1: 0.8913
- Accuracy: 0.9217

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 170  | 0.3259          | 0.8864    | 0.8851 | 0.8857 | 0.9170   |
| No log        | 2.0   | 340  | 0.2976          | 0.8991    | 0.9005 | 0.8998 | 0.9271   |
| 0.3859        | 3.0   | 510  | 0.2988          | 0.8970    | 0.8981 | 0.8976 | 0.9257   |
| 0.3859        | 4.0   | 680  | 0.3131          | 0.8977    | 0.8984 | 0.8981 | 0.9267   |
| 0.3859        | 5.0   | 850  | 0.3291          | 0.8943    | 0.8974 | 0.8958 | 0.9246   |
| 0.1338        | 6.0   | 1020 | 0.3298          | 0.8974    | 0.8984 | 0.8979 | 0.9253   |
| 0.1338        | 7.0   | 1190 | 0.3538          | 0.8908    | 0.8950 | 0.8929 | 0.9222   |
| 0.1338        | 8.0   | 1360 | 0.3879          | 0.8903    | 0.8921 | 0.8912 | 0.9220   |
| 0.0798        | 9.0   | 1530 | 0.3852          | 0.8929    | 0.8933 | 0.8931 | 0.9228   |
| 0.0798        | 10.0  | 1700 | 0.4111          | 0.8873    | 0.8896 | 0.8884 | 0.9196   |
| 0.0798        | 11.0  | 1870 | 0.4254          | 0.8928    | 0.8940 | 0.8934 | 0.9231   |
| 0.0507        | 12.0  | 2040 | 0.4476          | 0.8911    | 0.8930 | 0.8921 | 0.9224   |
| 0.0507        | 13.0  | 2210 | 0.4478          | 0.8900    | 0.8926 | 0.8913 | 0.9220   |
| 0.0507        | 14.0  | 2380 | 0.4563          | 0.8896    | 0.8931 | 0.8914 | 0.9217   |
| 0.0357        | 15.0  | 2550 | 0.4600          | 0.8894    | 0.8931 | 0.8913 | 0.9217   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
