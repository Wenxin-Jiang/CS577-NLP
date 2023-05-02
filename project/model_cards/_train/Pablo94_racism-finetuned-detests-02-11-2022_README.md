---
license: cc
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: racism-finetuned-detests-02-11-2022
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# racism-finetuned-detests-02-11-2022

This model is a fine-tuned version of [davidmasip/racism](https://huggingface.co/davidmasip/racism) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8819
- F1: 0.6199

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.3032        | 0.64  | 25   | 0.3482          | 0.6434 |
| 0.1132        | 1.28  | 50   | 0.3707          | 0.6218 |
| 0.1253        | 1.92  | 75   | 0.4004          | 0.6286 |
| 0.0064        | 2.56  | 100  | 0.6223          | 0.6254 |
| 0.0007        | 3.21  | 125  | 0.7347          | 0.6032 |
| 0.0006        | 3.85  | 150  | 0.7705          | 0.6312 |
| 0.0004        | 4.49  | 175  | 0.7988          | 0.6304 |
| 0.0003        | 5.13  | 200  | 0.8206          | 0.6255 |
| 0.0003        | 5.77  | 225  | 0.8371          | 0.6097 |
| 0.0003        | 6.41  | 250  | 0.8503          | 0.6148 |
| 0.0003        | 7.05  | 275  | 0.8610          | 0.6148 |
| 0.0002        | 7.69  | 300  | 0.8693          | 0.6199 |
| 0.0002        | 8.33  | 325  | 0.8755          | 0.6199 |
| 0.0002        | 8.97  | 350  | 0.8797          | 0.6199 |
| 0.0002        | 9.62  | 375  | 0.8819          | 0.6199 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
