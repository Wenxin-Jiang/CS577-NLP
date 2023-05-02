---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-Regression-Edmunds_Car_Reviews-Non_European_Imports
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-Regression-Edmunds_Car_Reviews-Non_European_Imports

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2240
- Mae: 0.3140
- Mse: 0.2240
- Rmse: 0.4733

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Mae    | Mse    | Rmse   |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|
| 0.6594        | 1.0   | 715  | 0.2436          | 0.3319 | 0.2436 | 0.4935 |
| 0.2324        | 2.0   | 1430 | 0.2274          | 0.3210 | 0.2274 | 0.4769 |
| 0.1975        | 3.0   | 2145 | 0.2303          | 0.3198 | 0.2303 | 0.4799 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.12.1
