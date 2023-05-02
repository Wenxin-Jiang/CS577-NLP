---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-Regression-Edmunds_Car_Reviews-European_Made
  results: []
---
# distilbert-base-uncased-Regression-Edmunds_Car_Reviews

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1999
- Mse: 0.1999
- Rmse: 0.4471
- Mae: 0.2824

## Model description

More information needed

## Intended uses & limitations

I used this to improve my skillset. I thank all of authors of the different technologies and dataset(s) for 
their contributions that have this possible. I am not too worried about getting credit for my part, but make 
sure to properly cite the authors of the different technologies and dataset(s) as they 
absolutely deserve credit for their contributions.

## Training and evaluation data

Dataset Source: https://www.kaggle.com/datasets/ankkur13/edmundsconsumer-car-ratings-and-reviews

I only used car manufacturers headquartered in Europe that are not luxury brands. 
Additionally, I removed manufacturers with limited reviews.

## Training procedure

The script for this project will be uploaded to my GitHub profile soon. Once it is, I will make sure to add the link here.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Mse    | Rmse   | Mae    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|
| 1.4892        | 1.0   | 236  | 0.2587          | 0.2587 | 0.5086 | 0.3120 |
| 0.2384        | 2.0   | 472  | 0.2359          | 0.2359 | 0.4857 | 0.2994 |
| 0.188         | 3.0   | 708  | 0.2304          | 0.2304 | 0.4800 | 0.2948 |
| 0.1558        | 4.0   | 944  | 0.2443          | 0.2443 | 0.4942 | 0.2981 |
| 0.133         | 5.0   | 1180 | 0.2410          | 0.2410 | 0.4909 | 0.2983 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.12.1
