---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-base-devices-sum-ver1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-devices-sum-ver1

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0935
- Rouge1: 97.2294
- Rouge2: 80.1323
- Rougel: 97.245
- Rougelsum: 97.2763
- Gen Len: 4.9507

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 186  | 0.2461          | 91.9436 | 71.232  | 91.9417 | 91.9585   | 4.6644  |
| No log        | 2.0   | 372  | 0.1580          | 94.5247 | 76.1321 | 94.5044 | 94.5382   | 4.8953  |
| 0.488         | 3.0   | 558  | 0.1239          | 95.8673 | 78.1183 | 95.8862 | 95.8919   | 4.9102  |
| 0.488         | 4.0   | 744  | 0.1100          | 96.5746 | 78.9878 | 96.5848 | 96.5831   | 4.9102  |
| 0.488         | 5.0   | 930  | 0.1008          | 96.9074 | 79.5536 | 96.9143 | 96.9317   | 4.9291  |
| 0.1303        | 6.0   | 1116 | 0.0974          | 96.9274 | 79.6953 | 96.933  | 96.9473   | 4.9291  |
| 0.1303        | 7.0   | 1302 | 0.0969          | 96.8041 | 79.5073 | 96.817  | 96.8266   | 4.9271  |
| 0.1303        | 8.0   | 1488 | 0.0945          | 97.1496 | 79.9757 | 97.1529 | 97.1779   | 4.9534  |
| 0.089         | 9.0   | 1674 | 0.0944          | 97.253  | 80.1236 | 97.2619 | 97.2899   | 4.9595  |
| 0.089         | 10.0  | 1860 | 0.0935          | 97.2294 | 80.1323 | 97.245  | 97.2763   | 4.9507  |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
