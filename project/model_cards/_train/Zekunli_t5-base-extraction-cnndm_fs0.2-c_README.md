---
tags:
- generated_from_trainer
metrics:
- recall
- precision
- f1
model-index:
- name: t5-base-extraction-cnndm_fs0.2-c
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-extraction-cnndm_fs0.2-c

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7632
- Recall: 35.3211
- Precision: 44.7184
- F1: 37.9638
- Gen Len: 18.9772

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
| 2.869         | 0.11  | 200  | 2.1451          | 5.0936  | 24.6632   | 7.5994  | 18.7768 |
| 2.1528        | 0.23  | 400  | 1.8487          | 34.4362 | 43.9397   | 36.9118 | 18.9848 |
| 1.9838        | 0.34  | 600  | 1.7632          | 35.3211 | 44.7184   | 37.9638 | 18.9772 |
| 1.9177        | 0.46  | 800  | 1.7159          | 35.2238 | 43.6081   | 37.5322 | 18.9939 |
| 1.866         | 0.57  | 1000 | 1.6831          | 34.9749 | 43.3927   | 37.2946 | 18.9924 |
| 1.8292        | 0.69  | 1200 | 1.6564          | 35.1338 | 43.3687   | 37.3903 | 18.9954 |
| 1.8132        | 0.8   | 1400 | 1.6331          | 35.1356 | 43.4627   | 37.3786 | 18.9954 |
| 1.7891        | 0.92  | 1600 | 1.6194          | 35.3715 | 44.0317   | 37.7205 | 18.9855 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.10.0+cu111
- Datasets 2.8.0
- Tokenizers 0.13.2
