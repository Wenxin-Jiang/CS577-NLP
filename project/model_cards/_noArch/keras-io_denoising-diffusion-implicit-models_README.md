---
library_name: keras
tags:
- generative
- denoising
- diffusion
- ddim
- ddpm
- unconditional-image-generation
---

This model was created for the [Keras code example](https://keras.io/examples/generative/ddim/) on [denoising diffusion implicit models (DDIM)](https://arxiv.org/abs/2010.02502).

## Model description

The model uses a [U-Net](https://arxiv.org/abs/1505.04597) with identical input and output dimensions. It progressively downsamples and upsamples its input image, adding skip connections between layers having the same resolution. The architecture is a simplified version of the architecture of [DDPM](https://arxiv.org/abs/2006.11239). It consists of convolutional residual blocks and lacks attention layers. The network takes two inputs, the noisy images and the variances of their noise components, which it encodes using [sinusoidal embeddings](https://arxiv.org/abs/1706.03762).

## Intended uses & limitations

The model is intended for educational purposes, as a simple example of denoising diffusion generative models. It has modest compute requirements with reasonable natural image generation performance.

## Training and evaluation data

The model is trained on the [Oxford Flowers 102](https://www.tensorflow.org/datasets/catalog/oxford_flowers102) dataset for generating images, which is a diverse natural dataset containing around 8,000 images of flowers. Since the official splits are imbalanced (most of the images are contained in the test splite), new random splits were created (80% train, 20% validation) for training the model. Center crops were used for preprocessing.

## Training procedure

The model is trained to denoise noisy images, and can generate images by iteratively denoising pure Gaussian noise. 

For more details check out the [Keras code example](https://keras.io/examples/generative/ddim/), or the companion [code repository](https://github.com/beresandras/clear-diffusion-keras), with additional features..

## Training hyperparameters

| Hyperparameters | Value |
| :-- | :-- |
| num epochs | 80 |
| dataset repetitions per epoch| 5 |
| image resolution | 64 |
| min signal rate | 0.02 |
| max signal rate | 0.95 |
| embedding dimensions | 32 |
| embedding max frequency | 1000.0 |
| block widths | 32, 64, 96, 128 |
| block depth | 2 |
| batch size | 64 |
| exponential moving average | 0.999 |
| optimizer | [AdamW](https://arxiv.org/abs/1711.05101) |
| learning rate | 1e-3 |
| weight decay | 1e-4 |

 ## Model plot

<details>
<summary>View model plot</summary>

![network architecture residual unet](./model.png)

</details>