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
- text: dog eating food momos
---

# DreamBooth model for the food concept trained by Someman on the Someman/momo dataset.

This is a Stable Diffusion model fine-tuned on the food concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of food momos**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `momos` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Someman/food-momos')
image = pipeline().images[0]
image
```
