---
library_name: keras
tags:
- image-classification
---

## Model Description

### Keras Implementation of Classification using Attention-based Deep Multiple Instance Learning (MIL)

This repo contains the trained model of [Classification using Attention-based Deep Multiple Instance Learning (MIL)](https://keras.io/examples/vision/attention_mil_classification/).

The full credit goes to: [Mohamad Jaber](https://www.linkedin.com/in/mohamadjaber1/)

## Intended uses & limitations
- The trained model can be used to classify a bag of image instances (the bag of image instances can be generated from an original image) with the motivation of knowing which patterns in the original image is actually causing it to belong to that class.

## Training and evaluation data
- Original MNIST train & test dataset were loaded from tensorflow datasets and the images were randomly chosen to create different bags of instance with number of instances per bag is 3
- Number 8 is selected to be the Positive class (i.e. the bag that contains image of 8 belongs to Positive class and others are Negative class)

## Training procedure
### Training hyperparameter 
The following hyperparameters were used during training:
- optimizer: 'adam'
- loss: 'sparse_categorical_crossentropy'
- epochs: 50
- batch_size: 8

## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>