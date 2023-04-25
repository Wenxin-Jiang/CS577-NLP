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
- text: A photo of cmexsks drink with ice cream on top
---

# DreamBooth model for the cmexsks concept trained by shahp7575 on the shahp7575/chemex dataset.

This is a Stable Diffusion model fine-tuned on the cmexsks concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of cmexsks drink**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `drink` images for the food theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('shahp7575/chemex-coffee')
image = pipeline().images[0]
image
```
