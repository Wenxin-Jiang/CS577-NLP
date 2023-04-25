---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- food
widget:
- text: a robot made of pbchoc dessert
---

# DreamBooth model for the pbchoc concept trained by jnick on the jnick/chocolate-peanut-butter-bars dataset.

This is a Stable Diffusion model fine-tuned on the pbchoc concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of pbchoc dessert**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description

This is a Stable Diffusion model fine-tuned on images of peanut butter chocolate bars for the food theme.

![Examples](BarsCollage.png)

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('jnick/peanut-butter-chocolate-bars')
image = pipeline().images[0]
image
```
