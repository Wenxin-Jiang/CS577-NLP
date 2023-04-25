---
tags:
- image-segmentation
- generic
library_name: generic
dataset:
- oxfort-iit pets
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/cat-1.jpg
  example_title: Kedis
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/cat-2.jpg
  example_title: Cat in a Crate
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/cat-3.jpg
  example_title: Two Cats Chilling
license: cc0-1.0
---
## Keras semantic segmentation models on the 🤗Hub! 🐶 🐕 🐩 
Full credits go to [François Chollet](https://twitter.com/fchollet).

This repository contains the model from [this notebook on segmenting pets using U-net-like architecture](https://keras.io/examples/vision/oxford_pets_image_segmentation/). We've changed the inference part to enable segmentation widget on the Hub. (see ```pipeline.py```)

## Background Information 

Image classification task tells us about a class assigned to an image, and object detection task creates a boundary box on an object in an image. But what if we want to know about the shape of the image? Segmentation models helps us segment images and reveal their shapes. It has many variants, including, panoptic segmentation, instance segmentation and semantic segmentation.This post is on hosting your Keras semantic segmentation models on Hub.
Semantic segmentation models classify pixels, meaning, they assign a class (can be cat or dog) to each pixel. The output of a model looks like following.
![Raw Output](./raw_output.jpg)
We need to get the best prediction for every pixel.
![Mask](./mask.jpg)
This is still not readable. We have to convert this into different binary masks for each class and convert to a readable format by converting each mask into base64. We will return a list of dicts, and for each dictionary, we have the label itself, the base64 code and a score (semantic segmentation models don't return a score, so we have to return 1.0 for this case). You can find the full implementation in ```pipeline.py```.
![Binary Mask](./binary_mask.jpg)
Now that you know the expected output by the model, you can host your Keras segmentation models (and other semantic segmentation models) in the similar fashion. Try it yourself and host your segmentation models!
![Segmented Cat](./hircin_the_cat.png)