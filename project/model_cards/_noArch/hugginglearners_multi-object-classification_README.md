---
tags:
- fastai
- image-classification
---
## Model description
This repo contains the trained model for Multi-object classification

Full credits go to [Nhu Hoang](https://www.linkedin.com/in/nhu-hoang/)

Motivation: Classifying multiple objects is a challenging task without using an object detection algorithm. This model was trained on resnet34 backbone and achieved a good accuracy.

## Training and evaluation data
### Training hyperparameters

The following hyperparameters were used during training:

| Hyperparameters | Value |
| :-- | :-- |
| name | Adam |
| learning_rate | 3e-3 |
| training_precision | float16 |
