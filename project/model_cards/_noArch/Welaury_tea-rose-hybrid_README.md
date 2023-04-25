---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- science
widget:
- text: a photo of tea rose hybrid bud
---

# DreamBooth model for the tea rose hybrid bud concept trained by Welaury on the Welaury/hybrid_rose dataset.

This is a Stable Diffusion model fine-tuned on the tea rose hybrid bud concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of tea rose hybrid bud**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on tea rose hybrid images for the science theme.


## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('Welaury/tea-rose-hybrid')
image = pipeline().images[0]
image
```
