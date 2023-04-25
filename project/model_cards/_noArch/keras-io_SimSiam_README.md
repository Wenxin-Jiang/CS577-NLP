---
tags: 
- computer-vision
- image-classification

library_name: keras
---

## Model description

This repo contains the trained model Self-supervised contrastive learning with SimSiam on CIFAR-10 Dataset.
Keras link: https://keras.io/examples/vision/simsiam/

Full credits to https://twitter.com/RisingSayak

## Intended uses & limitations
The trained model can be used as a learned representation for downstream tasks like image classification.


## Training and evaluation data

The dataset we are using here is called CIFAR-100. The CIFAR-10 dataset consists of 60000 32x32 color images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

Two particular augmentation transforms that seem to matter the most are: 
- Random resized crops
- Color distortions

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

| name | learning_rate | decay | momentum | nesterov | training_precision |
|----|-------------|-----|--------|--------|------------------|
|SGD|{'class_name': 'CosineDecay', 'config': {'initial_learning_rate': 0.03, 'decay_steps': 3900, 'alpha': 0.0, 'name': None}}|0.0|0.8999999761581421|False|float32|

 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>