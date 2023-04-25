---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- animal
widget:
- text: a photo of shbrcky dog in the water
---

# DreamBooth model for the shbrcky concept trained by peterj on the peterj/shibaricky dataset.

This is a Stable Diffusion model fine-tuned on the shbrcky concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of shbrcky dog**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `dog` images for the animal theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('peterj/shbrcky-dog')
image = pipeline().images[0]
image
```
