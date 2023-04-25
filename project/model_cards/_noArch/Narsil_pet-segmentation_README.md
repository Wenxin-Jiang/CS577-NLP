---
tags:
- image-segmentation
- generic
library_name: generic
pipeline_tag: image-segmentation
dataset:
- oxfort-iit pets
license: apache-2.0
---
## Keras semantic segmentation models on the 🤗Hub! 🐶 🐕 🐩 

Image classification task tells us about a class assigned to an image, and object detection task creates a boundary box on an object in an image. But what if we want to know about the shape of the image? Segmentation models helps us segment images and reveal their shapes. It has many variants. You can host your Keras segmentation models on the Hub.
Semantic segmentation models classify pixels, meaning, they assign a class (can be cat or dog) to each pixel. The output of a model looks like following.
![Raw Output](./raw_output.jpg)
We need to get the best prediction for every pixel.
![Mask](./mask.jpg)
This is still not readable. We have to convert this into different binary masks for each class and convert to a readable format by converting each mask into base64. We will return a list of dicts, and for each dictionary, we have the label itself, the base64 code and a score (semantic segmentation models don't return a score, so we have to return 1.0 for this case). You can find the full implementation in ```pipeline.py```.
![Binary Mask](./binary_mask.jpg)
Now that you know the expected output by the model, you can host your Keras segmentation models (and other semantic segmentation models) in the similar fashion. Try it yourself and host your segmentation models!
![Segmented Cat](./hircin_the_cat.png)