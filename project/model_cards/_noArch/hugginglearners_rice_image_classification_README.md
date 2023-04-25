---
tags:
- fastai
- image-classification
---
## Model description
This repo contains the trained model for rice image classification

Full credits go to [Vu Minh Chien](https://www.linkedin.com/in/vumichien/)

Motivation: Rice, which is among the most widely produced grain products worldwide, has many genetic varieties. These varieties are separated from each other due to some of their features. These usually feature such as texture, shape, and color. With these features that distinguish rice varieties, it is possible to classify and evaluate the quality of seeds. 

## Intended uses & limitations
In this repo, Arborio, Basmati, Ipsala, Jasmine, and Karacadag, which are five different varieties of rice often grown in Turkey, were used. A total of 75,000-grain images, 15,000 from each of these varieties, are included in the dataset.

## Training and evaluation data
### Training hyperparameters

The following hyperparameters were used during training:

| Hyperparameters | Value |
| :-- | :-- |
| name | Adam |
| learning_rate | 3e-4 |
| freeze_epochs| 3 |
| unfreeze_epochs| 10|
| training_precision | float16 |

