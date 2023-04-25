---
tags:
- transformers
- swin-transformers
- Keras
- image-classification
dataset:
- CIFAR-100
license: cc0-1.0
---
## Image classification with Swin Transformers on the 🤗Hub! 

Author: [Kelvin Idanwekhai](https://twitter.com/KelvinIdan).

[Paper](https://arxiv.org/abs/2103.14030) | [Keras Tutorial](https://keras.io/examples/vision/swin_transformers/)

Excerpt from the Tutorial:

Swin Transformer (Shifted Window Transformer) can serve as a general-purpose backbone for computer vision. Swin Transformer is a hierarchical Transformer whose representations are computed with shifted windows. The shifted window scheme brings greater efficiency by limiting self-attention computation to non-overlapping local windows while also allowing for cross-window connections. This architecture has the flexibility to model information at various scales and has a linear computational complexity with respect to image size. 

## About The dataset

The dataset we are using here is called [CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html). The CIFAR-10 dataset consists of 60000 32x32 color images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class. 

