---
library_name: keras
tags:
- image-classification
- computer-vision
- consistency-regularization
- cifar10
---

## Model description

### Consistency training with supervision

[Keras Example Link](https://keras.io/examples/vision/consistency_training/)

In this example, we have trained an image classification model enforcing a sense of consistency inside it by doing the following:

- Train a standard image classification model.
- Train an equal or larger model on a noisy version of the dataset (augmented using RandAugment).
- To do this, we will first obtain predictions of the previous model on the clean images of the dataset.
- We will then use these predictions and train the second model to match these predictions on the noisy variant of the same images. This is identical to the workflow of Knowledge Distillation but since the student model is equal or larger in size this process is also referred to as Self-Training.

This overall training workflow finds its roots in works like FixMatch, Unsupervised Data Augmentation for Consistency Training, and Noisy Student Training. Since this training process encourages a model yield consistent predictions for clean as well as noisy images, it's often referred to as consistency training or training with consistency regularization. Although the example focuses on using consistency training to enhance the robustness of models to common corruptions this example can also serve a template for performing weakly supervised learning.

Full Credits to <a href = "https://twitter.com/RisingSayak" target='_blank'> Sayak Paul </a> for this work.

This repo contains only the <b>Student Model</b> of this training example.

<b>Teacher Model </b>Repo can be find at this <a href = "" target='_blank'> Link </a>.

## Intended uses & limitations

More information needed

## Training and evaluation data

Trained and evaluated on [CIFAR-10](https://keras.io/api/datasets/cifar10/) dataset.


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

| name | optimizer | average_period | start_averaging | training_precision |
|----|---------|--------------|---------------|------------------|
|SWA|{'class_name': 'Adam', 'config': {'name': 'Adam', 'learning_rate': 3.9063e-06, 'decay': 0.5, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False}}|10|0|float32|

 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>