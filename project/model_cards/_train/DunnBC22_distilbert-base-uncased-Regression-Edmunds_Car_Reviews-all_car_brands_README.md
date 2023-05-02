---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-Regression-Edmunds_Car_Reviews-all_car_brands
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-Regression-Edmunds_Car_Reviews-all_car_brands

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2232
- Mse: 0.2232
- Rmse: 0.4724
- Mae: 0.3150

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.5e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Mse    | Rmse   | Mae    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|
| 0.3936        | 1.0   | 2592 | 0.2282          | 0.2282 | 0.4777 | 0.3158 |
| 0.2163        | 2.0   | 5184 | 0.2160          | 0.2160 | 0.4647 | 0.3106 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
