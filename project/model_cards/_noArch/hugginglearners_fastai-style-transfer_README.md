---
tags:
- fastai
- pytorch
- image-to-image
---
## Model description
This repo contains the trained model for Style transfer using vgg16 as the backbone.

Full credits go to [Nhu Hoang](https://www.linkedin.com/in/nhu-hoang/)

Motivation: Style transfer is an interesting task with an amazing outcome. 

## Training and evaluation data
### Training hyperparameters

The following hyperparameters were used during training:

| Hyperparameters | Value |
| :-- | :-- |
| name | Adam |
| learning_rate | 3e-5 |
| training_precision | float16 |