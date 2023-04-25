---
language : en
tags     : image-classification
license  : mit
dataset  : cifar10
metrics  : accuracy (https://hf.co/metrics/accuracy)
---

## Model description

**Upside down detector**: Model to detect if images are upside down

* Picked a dataset of natural images - cifar10
* Synthetically turned some of images upside down. Created a training and test set.
* Trained it to classify image orientation ie if the image is upside down or not.

## Intended uses & limitations
Intended to showcase skill set of being able to train a simple CNN classifier.

## How to use
n/a

## Limitations and bias
Trained on a relatively small dataset, hence it's hard to derive conclusions. 

## Training data
cifar10

## Training procedure
Trained using Keras with Nadam classifier with ReduceLROnPlateau which halves the learning rate when the validation loss doesn't improve for 5 iterations

## Evaluation results
The classifier was able to achieve 90% validation accuracy