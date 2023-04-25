---
tags:
- computer-vision
- image-classification
license:
- cc0-1.0
library_name: keras
---

## Image Classification using MobileViT
This repo contains the model and the notebook [to this Keras example on MobileViT](https://keras.io/examples/vision/mobilevit/).

Full credits to: [Sayak Paul](https://twitter.com/RisingSayak)

## Background Information 
MobileViT architecture (Mehta et al.), combines the benefits of Transformers (Vaswani et al.) and convolutions. With Transformers, we can capture long-range dependencies that result in global representations. With convolutions, we can capture spatial relationships that model locality.

Besides combining the properties of Transformers and convolutions, the authors introduce MobileViT as a general-purpose mobile-friendly backbone for different image recognition tasks. Their findings suggest that, performance-wise, MobileViT is better than other models with the same or higher complexity (MobileNetV3, for example), while being efficient on mobile devices.  

## Training Data
The model is trained on a [tf_flowers dataset](https://www.tensorflow.org/datasets/catalog/tf_flowers)