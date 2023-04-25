---
library_name: keras
tags:
- data-augmentation
- image-classification
---

# Tensorflow Keras implementation of : [CutMix data augmentation for image classification](https://keras.io/examples/vision/cutmix/)

The full credit goes to: [Sayan Nath](https://twitter.com/sayannath2350)

## The Data augmentation strategy

CutMix is a data Augmentation strategy where some portion of the training example is removed and pasted with the content from other images in the training set. The labels are also mixed based on the proportion of the pixels that were combined. The full paper is at [https://arxiv.org/pdf/1905.04899.pdf](https://arxiv.org/pdf/1905.04899.pdf) by Yun et. al., 2019.

# CutMix augmented examples from CIFAR-10

Here are a few examples of augmented images.
![Few examples](./cutMixEx.PNG)

## Model and Dataset used

The Data augmentation is applied to the CIFAR-10 Data set. The model used here is the Resnet-20 with Categorical Cross-Entropy loss.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': 0.001, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}
- training_precision: float32

 ## Training Metrics
After 20 Epocs, the accuracy of the model trained on the CutMix augmented data is 79.61%, while the accuracy of the model trained on the original data is 75.62%. I also found that the training on the original data was slightly faster.


 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>