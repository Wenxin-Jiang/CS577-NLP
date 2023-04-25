---
tags:
- computer-vision
- image-segmentation
license:
- cc0-1.0
library_name: keras
---

## Multiclass semantic segmentation using DeepLabV3+
This repo contains the model and the notebook [to this Keras example on Multiclass semantic segmentation using DeepLabV3+](https://keras.io/examples/vision/deeplabv3_plus/).

Full credits to: [Soumik Rakshit](http://github.com/soumik12345)

The model is trained for demonstrative purposes and does not guarantee the best results in production. For better results, follow & optimize the [Keras example]((https://keras.io/examples/vision/deeplabv3_plus/) as per your need.

## Background Information 
Semantic segmentation, with the goal to assign semantic labels to every pixel in an image, is an essential computer vision task. In this example, we implement the DeepLabV3+ model for multi-class semantic segmentation, a fully-convolutional architecture that performs well on semantic segmentation benchmarks.   

## Training Data
The model is trained on a subset (10,000 images) of [Crowd Instance-level Human Parsing Dataset](https://arxiv.org/abs/1811.12596). The Crowd Instance-level Human Parsing (CIHP) dataset has 38,280 diverse human images. Each image in CIHP is labeled with pixel-wise annotations for 20 categories, as well as instance-level identification. This dataset can be used for the "human part segmentation" task.

## Model
The model uses ResNet50 pretrained on ImageNet as the backbone model.

References:   
1. [Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation](https://arxiv.org/pdf/1802.02611.pdf)   
2. [Rethinking Atrous Convolution for Semantic Image Segmentation](https://arxiv.org/abs/1706.05587)   
3. [DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs](https://arxiv.org/abs/1606.00915)