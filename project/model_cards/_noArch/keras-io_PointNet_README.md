---
license: apache-2.0
library_name: keras
tags:
- image-classification
- image-segmentation
---

## Model Description
### Keras Implementation of Point cloud classification with PointNet

This repo contains the trained model of [Point cloud classification with PointNet](https://keras.io/examples/vision/pointnet/).

The full credit goes to: [David Griffiths](https://dgriffiths3.github.io/)

## Intended uses & limitations
- As stated in the paper, PointNet is 3D perception model, applying deep learning to point clouds for object classification and scene semantic segmentation. 
- PointNet takes raw point cloud data as input, which is typically collected from either a lidar or radar sensor.

## Training and evaluation data
- The dataset used for training is ModelNet10, the smaller 10 class version of the ModelNet40 dataset.

## Training procedure
### Training hyperparameter 
The following hyperparameters were used during training:
- optimizer: 'adam'
- loss: 'sparse_categorical_crossentropy'
- epochs: 20
- batch_size: 32
- learning_rate: 0.001

## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>