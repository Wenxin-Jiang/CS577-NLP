---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- wildcard
widget:
- text: vasyalozhkin style, painting of a dog flying in the sky
---

# DreamBooth model for the vasyalozhkin concept trained by neuronaut on the neuronaut/vasyalozhkin2 dataset.

This is a Stable Diffusion model v1.5 fine-tuned on Vasya Lozhkin paintings with DreamBooth. Used 8000 steps. It can be used by modifying the instance_prompt: **vasyalozhkin style** or **vasyalozhkin**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `style` images for the wildcard theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('neuronaut/vasyalozhkin2-style')
image = pipeline().images[0]
image
```
