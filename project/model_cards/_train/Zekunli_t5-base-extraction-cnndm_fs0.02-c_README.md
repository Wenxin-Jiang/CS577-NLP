---
tags:
- generated_from_trainer
metrics:
- recall
- precision
- f1
model-index:
- name: t5-base-extraction-cnndm_fs0.02-c
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-extraction-cnndm_fs0.02-c

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8400
- Recall: 35.4852
- Precision: 40.9499
- F1: 36.9238
- Gen Len: 19.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 32
- eval_batch_size: 32
- seed: 1799
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Recall  | Precision | F1      | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:---------:|:-------:|:-------:|
| 2.7966        | 1.14  | 200  | 2.0568          | 17.0907 | 45.1725   | 21.4724 | 12.7061 |
| 2.1271        | 2.29  | 400  | 1.8400          | 35.4852 | 40.9499   | 36.9238 | 19.0    |
| 1.9831        | 3.43  | 600  | 1.7756          | 35.0259 | 39.8685   | 36.1824 | 18.9962 |
| 1.9025        | 4.57  | 800  | 1.7365          | 34.9077 | 39.2092   | 35.8205 | 19.0    |
| 1.8564        | 5.71  | 1000 | 1.7075          | 33.8282 | 38.141    | 34.765  | 19.0    |
| 1.8164        | 6.86  | 1200 | 1.6898          | 34.6927 | 38.999    | 35.5568 | 19.0    |
| 1.7929        | 8.0   | 1400 | 1.6753          | 34.9922 | 39.2711   | 35.8318 | 19.0    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.10.0+cu111
- Datasets 2.8.0
- Tokenizers 0.13.2
