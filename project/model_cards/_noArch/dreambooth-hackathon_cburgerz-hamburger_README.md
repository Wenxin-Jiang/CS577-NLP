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
- text: a photo of cburgerz hamburger in a car
---

# DreamBooth model for cburgerz trained by lewtun on the `lewtun/hamburgers` dataset.

This your the Stable Diffusion model fine-tuned the cburgerz concept taught to Stable Diffusion with DreamBooth.
It can be used by modifying the `instance_prompt`: **a photo of cburgerz hamburger**

This model was created as part of the DreamBooth Hackathon. Visit the organisation page for instructions on how to take part!

## Description

Describe your model and concept here.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('dreambooth-hackathon/cburgerz-hamburger')
image = pipeline().images[0]
image
```
