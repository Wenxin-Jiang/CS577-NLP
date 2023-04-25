---
license: apache-2.0
tags:
- pytorch
- diffusers
- unconditional-image-generation
---

# Denoising Diffusion Probabilistic Models (DDPM)

**Paper**: [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)

**Authors**: Jonathan Ho, Ajay Jain, Pieter Abbeel

**Abstract**:

*We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN.*

## Inference

**DDPM** models can use *discrete noise schedulers* such as:

- [scheduling_ddpm](https://github.com/huggingface/diffusers/blob/main/src/diffusers/schedulers/scheduling_ddpm.py)
- [scheduling_ddim](https://github.com/huggingface/diffusers/blob/main/src/diffusers/schedulers/scheduling_ddim.py)
- [scheduling_pndm](https://github.com/huggingface/diffusers/blob/main/src/diffusers/schedulers/scheduling_pndm.py)

for inference. Note that while the *ddpm* scheduler yields the highest quality, it also takes the longest.
For a good trade-off between quality and inference speed you might want to consider the *ddim* or *pndm* schedulers instead.

See the following code:

```python
# !pip install diffusers
from diffusers import DDPMPipeline, DDIMPipeline, PNDMPipeline

model_id = "google/ddpm-celebahq-256"

# load model and scheduler
ddpm = DDPMPipeline.from_pretrained(model_id)  # you can replace DDPMPipeline with DDIMPipeline or PNDMPipeline for faster inference

# run pipeline in inference (sample random noise and denoise)
image = ddpm()["sample"]


# save image
image[0].save("ddpm_generated_image.png")
```

For more in-detail information, please have a look at the [official inference example](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/diffusers_intro.ipynb)

## Training

If you want to train your own model, please have a look at the [official training example](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/training_example.ipynb)

## Samples
1. ![sample_1](https://huggingface.co/google/ddpm-celebahq-256/resolve/main/images/generated_image_0.png)
2. ![sample_2](https://huggingface.co/google/ddpm-celebahq-256/resolve/main/images/generated_image_1.png)
3. ![sample_3](https://huggingface.co/google/ddpm-celebahq-256/resolve/main/images/generated_image_2.png)
4. ![sample_4](https://huggingface.co/google/ddpm-celebahq-256/resolve/main/images/generated_image_3.png)