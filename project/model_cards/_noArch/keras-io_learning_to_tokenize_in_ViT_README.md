---
library_name: keras
tags:
- image-classification
- Architecture
---

# Tensorflow Keras implementation of : [Learning to tokenize in Vision Transformers](https://keras.io/examples/vision/token_learner/)

The full credit goes to: [Aritra Roy Gosthipaty](https://twitter.com/ariG23498), [Sayak Paul](https://twitter.com/RisingSayak)

## Short description:

ViT and other Transformer based architectures break down images into patches. As we increase the resolution of the images, the number of patches increases as well. To tackle this, Ryoo et al. introduced a new module called TokenLearner which can help reduce the number of patches used. The full paper can be found [here](https://openreview.net/forum?id=z-l1kpDXs88)

## Model and Dataset used

The Dataset used here is CIFAR-10. The model used here is a mini ViT model with the TokenLearner module.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

| Hyperparameters | Value |
| :-- | :-- |
| name | AdamW |
| learning_rate | 0.0010000000474974513 |
| decay | 0.0 |
| beta_1 | 0.8999999761581421 |
| beta_2 | 0.9990000128746033 |
| epsilon | 1e-07 |
| amsgrad | False |
| weight_decay | 9.999999747378752e-05 |
| exclude_from_weight_decay | None |
| training_precision | float32 |

## Training Metrics
After 20 Epocs, the test accuracy of the model is 55.9% and the Top 5 test accuracy is 95.06%

 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>