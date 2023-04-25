---
tags:
- fastai
- image-classification
---
## Model description
This repo contains the trained model for grapevine leaves image classification

Full credits go to [Vu Minh Chien](https://www.linkedin.com/in/vumichien/)

Motivation: The main product of grapevines is grapes that are consumed fresh or processed. In addition, grapevine leaves are harvested once a year as a by-product. The species of grapevine leaves are important in terms of price and taste. In this repo, deep learning-based classification is conducted by using images of grapevine leaves

## Intended uses & limitations
Images of 500 vine leaves belonging to 5 species were taken with a special self-illuminating system. Later, this number was increased to 2500 with data augmentation methods

## Training and evaluation data
### Training hyperparameters

The following hyperparameters were used during training:

| Hyperparameters | Value |
| :-- | :-- |
| name | Adam |
| learning_rate | e-3 |
| freeze_epochs| 3 |
| unfreeze_epochs| 10|
| training_precision | float16 |

