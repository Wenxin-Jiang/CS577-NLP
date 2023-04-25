---
library_name: keras
tags:
- image-classification
- vision
---

# Compact Convolutional Transformers

Based on the _Compact Convolutional Transformers_ example on [keras.io](https://keras.io/examples/vision/cct/) created by [Sayak Paul](https://twitter.com/RisingSayak).

## Model description

As discussed in the [Vision Transformers (ViT)](https://arxiv.org/abs/2010.11929) paper, a Transformer-based architecture for vision typically requires a larger dataset than usual, as well as a longer pre-training schedule. ImageNet-1k (which has about a million images) is considered to fall under the medium-sized data regime with respect to ViTs. This is primarily because, unlike CNNs, ViTs (or a typical Transformer-based architecture) do not have well-informed inductive biases (such as convolutions for processing images). This begs the question: can't we combine the benefits of convolution and the benefits of Transformers in a single network architecture? These benefits include parameter-efficiency, and self-attention to process long-range and global dependencies (interactions between different regions in an image).

In [Escaping the Big Data Paradigm with Compact Transformers](https://arxiv.org/abs/2104.05704), Hassani et al. present an approach for doing exactly this. They proposed the Compact Convolutional Transformer (CCT) architecture. 

## Intended uses & limitations

- In the original paper, the authors use _AutoAugment_ to induce stronger regularization. In this example, the standard geometric augmentations (like random cropping and flipping) are used.
- The CCT model was trained for 30 epochs. Its plot in the 'Training Metrics' tab shows no signs of overfitting. This means that this network can be trained for longer (perhaps with a bit more regularization) and better performance may be obtained. This performance can further be improved by additional recipes like cosine decay learning rate schedule, other data augmentation techniques like AutoAugment, MixUp or Cutmix.

## Training and evaluation data

The model is trained using the [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html).

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

| name | learning_rate | decay | beta_1 | beta_2 | epsilon | amsgrad | weight_decay | exclude_from_weight_decay | training_precision |
|----|-------------|-----|------|------|-------|-------|------------|-------------------------|------------------|
|AdamW|0.0010000000474974513|0.0|0.8999999761581421|0.9990000128746033|1e-07|False|9.999999747378752e-05|None|float32|

 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>

<center>
Model reproduced by <a href="https://github.com/EdAbati" target="_blank">Edoardo Abati</a>
</center>