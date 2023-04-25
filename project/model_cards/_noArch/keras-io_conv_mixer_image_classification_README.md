---
library_name: keras
tags:
- image-classification
- computer-vision
- convmixer
- cifar10
---

## Model description

### Image classification with ConvMixer

[Keras Example Link](https://keras.io/examples/vision/convmixer/)

In the [Patches Are All You Need paper](https://arxiv.org/abs/2201.09792), the authors extend the idea of using patches to train an all-convolutional network and demonstrate competitive results. Their architecture namely ConvMixer uses recipes from the recent isotrophic architectures like ViT, MLP-Mixer (Tolstikhin et al.), such as using the same depth and resolution across different layers in the network, residual connections, and so on.

ConvMixer is very similar to the MLP-Mixer, model with the following key differences: Instead of using fully-connected layers, it uses standard convolution layers. Instead of LayerNorm (which is typical for ViTs and MLP-Mixers), it uses BatchNorm.

Full Credits to <a href = "https://twitter.com/RisingSayak" target='_blank'> Sayak Paul </a> for this work.


## Intended uses & limitations

More information needed

## Training and evaluation data

Trained and evaluated on [CIFAR-10](https://keras.io/api/datasets/cifar10/) dataset.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

| name | learning_rate | decay | beta_1 | beta_2 | epsilon | amsgrad | weight_decay | exclude_from_weight_decay | training_precision |
|----|-------------|-----|------|------|-------|-------|------------|-------------------------|------------------|
|AdamW|0.0010000000474974513|0.0|0.8999999761581421|0.9990000128746033|1e-07|False|9.999999747378752e-05|None|float32|

 ## Training Metrics
Model history needed
 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>