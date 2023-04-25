---
library_name: keras
tags:
- image-classification
- Architecture
---

# Tensorflow Keras implementation of : [Image classification with ConvMixer](https://keras.io/examples/vision/convmixer/)

The full credit goes to: [Sayak Paul](https://twitter.com/RisingSayak)

## Short description:

ConvMixer is a simple model based on the ideas of representing an image as patches( used in ViT) and separating the mixing of Spatial and channel dimensions (used in MLP-Mixer). Unlike ViT and MLP-Mixer, they use only standard Convolution operations. The full paper is a submission to ICLR 22 and can be found [here](https://openreview.net/pdf?id=TVHS5Y4dNvM)

## Model and Dataset used

The Dataset used here is CIFAR-10. The model is called ConvMixer-256/8 where 256 is the hidden dimension (the dimension of patches) and 8 is the depth(number of repetitions of ConvMix layers)

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
After 10 Epocs, the test accuracy of the model is 83.57%

 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>