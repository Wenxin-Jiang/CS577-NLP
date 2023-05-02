---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-Regression-Edmunds_Car_Reviews-American_Made
  results: []
---

# distilbert-base-uncased-Regression-Edmunds_Car_Reviews-American_Made

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2486
- Mae: 0.3469
- Mse: 0.2486
- Rmse: 0.4986

## Model description

More information needed

## Intended uses & limitations

I used this to improve my skillset. I thank all of authors of the different technologies and dataset(s) for 
their contributions that have this possible. I am not too worried about getting credit for my part, but 
make sure to properly cite the authors of the different technologies and dataset(s) as they absolutely 
deserve credit for their contributions.

## Training and evaluation data

Dataset Source: https://www.kaggle.com/datasets/ankkur13/edmundsconsumer-car-ratings-and-reviews

I only used car manufacturers headquartered in America that are not luxury brands. 
Additionally, I removed manufacturers with limited reviews.

## Training procedure

The script for this project will be uploaded to my GitHub profile soon. 
Once it is, I will make sure to add the link here.

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
| 0.6385        | 1.0   | 777  | 0.2743          | 0.3633 | 0.2743 | 0.5237 |
| 0.2551        | 2.0   | 1554 | 0.2588          | 0.3536 | 0.2588 | 0.5088 |
| 0.2161        | 3.0   | 2331 | 0.2568          | 0.3508 | 0.2568 | 0.5068 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.12.1
